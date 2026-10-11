"""
v2 ``Telemetry`` and v3 ``TelemetrySample``, both ways.

The fields every asset shares are typed on the sample; every other v2 field is a ``details`` entry
under one of the keys below, enum values as their v2 name without the enum's prefix.
:func:`telemetry_fields` describes those keys for ``CapabilitySet.telemetry_fields``.

Toward v2 a sample is a dock's (``asset``) or an aircraft's (``sub_asset``) by the keys it carries;
keys of the other kind, and keys v2 has no field for, are dropped there. ``Telemetry.id`` and
``SubAssetTelemetryDetails.component_telemetry`` are not carried.

The keys and the v2 fields behind them are the same as ``com.zqnt.utils.telemetry.TelemetrySampleMapper``
in zqnt-utils-java and the ``telemetry`` package of zqnt-utils-golang.
"""

from __future__ import annotations

import math
import struct
import uuid
from dataclasses import dataclass
from enum import Enum

from google.protobuf.descriptor import (
    EnumDescriptor,
    EnumValueDescriptor,
    FieldDescriptor,
)
from google.protobuf.message import Message
from google.protobuf.struct_pb2 import Struct, Value
from google.protobuf.timestamp_pb2 import Timestamp

from .generated.zqnt.base_pb2 import RequestBase
from .generated.zqnt.capability.v3.capability_pb2 import (
    TelemetryField,
    TelemetryValueType,
)
from .generated.zqnt.common.v3.common_pb2 import AssetRef, GeoPoint
from .generated.zqnt.live_data_types_pb2 import ProduceTelemetryRequest, Telemetry
from .generated.zqnt.telemetry.v3.telemetry_pb2 import TelemetrySample

WIND_SPEED = "wind.speed"
WIND_DIRECTION = "wind.direction"

DOCK_ENVIRONMENT_TEMPERATURE = "dock.environment_temperature"
DOCK_INSIDE_TEMPERATURE = "dock.inside_temperature"
DOCK_HUMIDITY = "dock.humidity"
DOCK_MODE = "dock.mode"
DOCK_RAINFALL = "dock.rainfall"
DOCK_COVER_STATE = "dock.cover_state"
DOCK_DEBUG_MODE_OPEN = "dock.debug_mode_open"
DOCK_POSITION_VALID = "dock.position_valid"
DOCK_WORKING_VOLTAGE = "dock.working_voltage"
DOCK_WORKING_CURRENT = "dock.working_current"
DOCK_SUPPLY_VOLTAGE = "dock.supply_voltage"
DOCK_AIR_CONDITIONER_STATE = "dock.air_conditioner.state"
DOCK_AIR_CONDITIONER_SWITCH_TIME = "dock.air_conditioner.switch_time"
DOCK_MANUAL_CONTROL_STATE = "dock.manual_control.state"
DOCK_MANUAL_CONTROL_ACTIVE_SESSION = "dock.manual_control.active_session"
DOCK_DRONE_SN = "dock.drone.sn"
DOCK_DRONE_MODEL = "dock.drone.model"
DOCK_DRONE_PAIRED = "dock.drone.paired"
DOCK_DRONE_ONLINE = "dock.drone.online"
DOCK_DRONE_AT_HOME = "dock.drone.at_home"
DOCK_DRONE_CHARGING = "dock.drone.charging"
DOCK_GNSS_GPS_SATELLITES = "dock.gnss.gps_satellites"
DOCK_GNSS_RTK_SATELLITES = "dock.gnss.rtk_satellites"
DOCK_GNSS_QUALITY = "dock.gnss.quality"
NETWORK_TYPE = "network.type"
NETWORK_RATE = "network.rate"
NETWORK_QUALITY = "network.quality"
LINK_4G_FREQUENCY_BAND = "link.4g.frequency_band"
LINK_4G_GROUND_QUALITY = "link.4g.ground_quality"
LINK_4G_LINK_STATE = "link.4g.link_state"
LINK_4G_QUALITY = "link.4g.quality"
LINK_4G_AIRCRAFT_QUALITY = "link.4g.aircraft_quality"
LINK_DONGLE_COUNT = "link.dongle_count"
LINK_WORK_MODE = "link.work_mode"
LINK_SDR_FREQUENCY_BAND = "link.sdr.frequency_band"
LINK_SDR_LINK_STATE = "link.sdr.link_state"
LINK_SDR_QUALITY = "link.sdr.quality"
SDR_DOWN_QUALITY = "sdr.down_quality"
SDR_UP_QUALITY = "sdr.up_quality"
SDR_FREQUENCY_BAND = "sdr.frequency_band"

DRONE_MODE = "drone.mode"
DRONE_GEAR = "drone.gear"
DRONE_HEIGHT_LIMIT = "drone.height_limit"
DRONE_HOME_DISTANCE = "drone.home_distance"
DRONE_TOTAL_FLIGHT_DISTANCE = "drone.total_flight_distance"
DRONE_TOTAL_FLIGHT_TIME = "drone.total_flight_time"
DRONE_COUNTRY = "drone.country"
DRONE_BATTERY_REMAINING_TIME = "drone.battery.remaining_time"
DRONE_BATTERY_RETURN_TO_HOME_POWER = "drone.battery.return_to_home_power"
PAYLOAD_ID = "payload.id"
PAYLOAD_NAME = "payload.name"
PAYLOAD_OBSERVED_AT = "payload.observed_at"
CAMERA_CURRENT_LENS = "camera.current_lens"
CAMERA_GIMBAL_PITCH = "camera.gimbal_pitch"
CAMERA_GIMBAL_YAW = "camera.gimbal_yaw"
CAMERA_GIMBAL_ROLL = "camera.gimbal_roll"
CAMERA_ZOOM_FACTOR = "camera.zoom_factor"
RANGE_FINDER_TARGET_LATITUDE = "range_finder.target_latitude"
RANGE_FINDER_TARGET_LONGITUDE = "range_finder.target_longitude"
RANGE_FINDER_TARGET_DISTANCE = "range_finder.target_distance"
RANGE_FINDER_TARGET_ALTITUDE = "range_finder.target_altitude"
SENSOR_TARGET_TEMPERATURE = "sensor.target_temperature"


class _Source(Enum):
    NONE = 0
    ASSET = 1
    SUB_ASSET = 2


@dataclass(frozen=True)
class _Detail:
    key: str
    path: tuple[FieldDescriptor, ...]
    source: _Source
    unit: str
    description: str


def _is_repeated(field: FieldDescriptor) -> bool:
    if hasattr(type(field), "is_repeated"):
        return field.is_repeated
    return field.label == FieldDescriptor.LABEL_REPEATED


def _detail(key: str, v2_path: str, unit: str, description: str) -> _Detail:
    path = []
    message = Telemetry.DESCRIPTOR
    for name in v2_path.split("."):
        field = message.fields_by_name.get(name) if message is not None else None
        if field is None or _is_repeated(field):
            raise ValueError(f"No singular field {name} on the path {v2_path}")
        path.append(field)
        message = field.message_type
    source = {"asset": _Source.ASSET, "sub_asset": _Source.SUB_ASSET}.get(
        path[0].name, _Source.NONE
    )
    return _Detail(key, tuple(path), source, unit, description)


_DETAILS = (
    _detail(WIND_SPEED, "wind_speed", "m/s", "Wind speed"),
    _detail(
        DOCK_ENVIRONMENT_TEMPERATURE,
        "asset.environment_temp",
        "°C",
        "Temperature outside the dock",
    ),
    _detail(
        DOCK_INSIDE_TEMPERATURE,
        "asset.inside_temp",
        "°C",
        "Temperature inside the dock",
    ),
    _detail(DOCK_HUMIDITY, "asset.humidity", "%", "Relative humidity inside the dock"),
    _detail(DOCK_MODE, "asset.mode", "", "Operating mode of the dock"),
    _detail(DOCK_RAINFALL, "asset.rainfall", "", "Rainfall at the dock"),
    _detail(DOCK_COVER_STATE, "asset.cover_state", "", "State of the dock cover"),
    _detail(
        DOCK_DEBUG_MODE_OPEN,
        "asset.debug_mode_open",
        "",
        "Whether remote debugging is open",
    ),
    _detail(
        DOCK_POSITION_VALID,
        "asset.position_valid",
        "",
        "Whether the dock's position is calibrated",
    ),
    _detail(DOCK_WORKING_VOLTAGE, "asset.working_voltage", "mV", "Working voltage"),
    _detail(DOCK_WORKING_CURRENT, "asset.working_current", "mA", "Working current"),
    _detail(DOCK_SUPPLY_VOLTAGE, "asset.supply_voltage", "V", "Supply voltage"),
    _detail(
        DOCK_AIR_CONDITIONER_STATE,
        "asset.air_conditioner.state",
        "",
        "Air conditioner state",
    ),
    _detail(
        DOCK_AIR_CONDITIONER_SWITCH_TIME,
        "asset.air_conditioner.switch_time",
        "s",
        "Time until the air conditioner may switch mode again",
    ),
    _detail(
        DOCK_MANUAL_CONTROL_STATE,
        "asset.manual_control_state",
        "",
        "Manual control link state",
    ),
    _detail(
        DOCK_MANUAL_CONTROL_ACTIVE_SESSION,
        "asset.has_active_manual_control_session",
        "",
        "Whether a manual control session is active",
    ),
    _detail(
        DOCK_DRONE_SN,
        "asset.sub_asset_information.sn",
        "",
        "Serial of the docked aircraft",
    ),
    _detail(
        DOCK_DRONE_MODEL,
        "asset.sub_asset_information.model",
        "",
        "Model of the docked aircraft",
    ),
    _detail(
        DOCK_DRONE_PAIRED,
        "asset.sub_asset_information.paired",
        "",
        "Whether the aircraft is paired",
    ),
    _detail(
        DOCK_DRONE_ONLINE,
        "asset.sub_asset_information.online",
        "",
        "Whether the aircraft is online",
    ),
    _detail(
        DOCK_DRONE_AT_HOME,
        "asset.sub_asset_at_home",
        "",
        "Whether the aircraft is in the dock",
    ),
    _detail(
        DOCK_DRONE_CHARGING,
        "asset.sub_asset_charging",
        "",
        "Whether the aircraft is charging",
    ),
    _detail(
        DOCK_GNSS_GPS_SATELLITES,
        "asset.position_state.gps_number",
        "",
        "GPS satellites in view",
    ),
    _detail(
        DOCK_GNSS_RTK_SATELLITES,
        "asset.position_state.rtk_number",
        "",
        "RTK satellites in view",
    ),
    _detail(
        DOCK_GNSS_QUALITY,
        "asset.position_state.quality",
        "",
        "Positioning quality level",
    ),
    _detail(NETWORK_TYPE, "asset.network_information.type", "", "Uplink network type"),
    _detail(
        NETWORK_RATE, "asset.network_information.rate", "KB/s", "Uplink network rate"
    ),
    _detail(
        NETWORK_QUALITY,
        "asset.network_information.quality",
        "",
        "Uplink network quality",
    ),
    _detail(
        LINK_4G_FREQUENCY_BAND,
        "asset.wireless_link.fourth_generation_freq_band",
        "",
        "4G link frequency band",
    ),
    _detail(
        LINK_4G_GROUND_QUALITY,
        "asset.wireless_link.fourth_generation_gnd_quality",
        "",
        "4G link quality, ground side",
    ),
    _detail(
        LINK_4G_LINK_STATE,
        "asset.wireless_link.fourth_generation_link_state",
        "",
        "Whether the 4G link is up",
    ),
    _detail(
        LINK_4G_QUALITY,
        "asset.wireless_link.fourth_generation_quality",
        "",
        "4G link quality",
    ),
    _detail(
        LINK_4G_AIRCRAFT_QUALITY,
        "asset.wireless_link.fourth_generation_uav_quality",
        "",
        "4G link quality, aircraft side",
    ),
    _detail(
        LINK_DONGLE_COUNT, "asset.wireless_link.dongle_number", "", "4G dongles in use"
    ),
    _detail(
        LINK_WORK_MODE,
        "asset.wireless_link.link_workmode",
        "",
        "Wireless link work mode",
    ),
    _detail(
        LINK_SDR_FREQUENCY_BAND,
        "asset.wireless_link.sdr_freq_band",
        "GHz",
        "SDR link frequency band",
    ),
    _detail(
        LINK_SDR_LINK_STATE,
        "asset.wireless_link.sdr_link_state",
        "",
        "Whether the SDR link is up",
    ),
    _detail(
        LINK_SDR_QUALITY, "asset.wireless_link.sdr_quality", "", "SDR link quality"
    ),
    _detail(
        SDR_DOWN_QUALITY, "asset.sdr_state.down_quality", "", "SDR downlink quality"
    ),
    _detail(SDR_UP_QUALITY, "asset.sdr_state.up_quality", "", "SDR uplink quality"),
    _detail(
        SDR_FREQUENCY_BAND,
        "asset.sdr_state.frequency_band",
        "GHz",
        "SDR frequency band",
    ),
    _detail(WIND_DIRECTION, "sub_asset.wind_direction", "", "Wind direction"),
    _detail(DRONE_MODE, "sub_asset.mode", "", "Flight mode of the aircraft"),
    _detail(DRONE_GEAR, "sub_asset.gear", "", "Flight gear"),
    _detail(DRONE_HEIGHT_LIMIT, "sub_asset.height_limit", "m", "Height limit"),
    _detail(
        DRONE_HOME_DISTANCE,
        "sub_asset.home_distance",
        "m",
        "Distance to the home point",
    ),
    _detail(
        DRONE_TOTAL_FLIGHT_DISTANCE,
        "sub_asset.total_movement_distance",
        "m",
        "Total flight distance",
    ),
    _detail(
        DRONE_TOTAL_FLIGHT_TIME,
        "sub_asset.total_movement_time",
        "s",
        "Total flight time",
    ),
    _detail(DRONE_COUNTRY, "sub_asset.country", "", "Country the aircraft is in"),
    _detail(
        DRONE_BATTERY_REMAINING_TIME,
        "sub_asset.battery_information.remaining_time",
        "s",
        "Remaining flight time on the battery",
    ),
    _detail(
        DRONE_BATTERY_RETURN_TO_HOME_POWER,
        "sub_asset.battery_information.return_to_home_power",
        "",
        "Battery needed to return home",
    ),
    _detail(PAYLOAD_ID, "sub_asset.payload_telemetry.id", "", "Payload id"),
    _detail(PAYLOAD_NAME, "sub_asset.payload_telemetry.name", "", "Payload name"),
    _detail(
        PAYLOAD_OBSERVED_AT,
        "sub_asset.payload_telemetry.timestamp",
        "",
        "When the payload reported (RFC 3339)",
    ),
    _detail(
        CAMERA_CURRENT_LENS,
        "sub_asset.payload_telemetry.camera_data.current_lens",
        "",
        "Active camera lens",
    ),
    _detail(
        CAMERA_GIMBAL_PITCH,
        "sub_asset.payload_telemetry.camera_data.gimbal_pitch",
        "°",
        "Gimbal pitch",
    ),
    _detail(
        CAMERA_GIMBAL_YAW,
        "sub_asset.payload_telemetry.camera_data.gimbal_yaw",
        "°",
        "Gimbal yaw",
    ),
    _detail(
        CAMERA_GIMBAL_ROLL,
        "sub_asset.payload_telemetry.camera_data.gimbal_roll",
        "°",
        "Gimbal roll",
    ),
    _detail(
        CAMERA_ZOOM_FACTOR,
        "sub_asset.payload_telemetry.camera_data.zoom_factor",
        "",
        "Camera zoom factor",
    ),
    _detail(
        RANGE_FINDER_TARGET_LATITUDE,
        "sub_asset.payload_telemetry.range_finder_data.target_latitude",
        "°",
        "Latitude of the range finder's target",
    ),
    _detail(
        RANGE_FINDER_TARGET_LONGITUDE,
        "sub_asset.payload_telemetry.range_finder_data.target_longitude",
        "°",
        "Longitude of the range finder's target",
    ),
    _detail(
        RANGE_FINDER_TARGET_DISTANCE,
        "sub_asset.payload_telemetry.range_finder_data.target_distance",
        "m",
        "Distance to the range finder's target",
    ),
    _detail(
        RANGE_FINDER_TARGET_ALTITUDE,
        "sub_asset.payload_telemetry.range_finder_data.target_altitude",
        "m",
        "Altitude of the range finder's target",
    ),
    _detail(
        SENSOR_TARGET_TEMPERATURE,
        "sub_asset.payload_telemetry.sensor_data.target_temperature",
        "°C",
        "Temperature of the measured target",
    ),
)

_NUMBER_TYPES = {
    FieldDescriptor.CPPTYPE_FLOAT,
    FieldDescriptor.CPPTYPE_DOUBLE,
    FieldDescriptor.CPPTYPE_INT32,
    FieldDescriptor.CPPTYPE_INT64,
    FieldDescriptor.CPPTYPE_UINT32,
    FieldDescriptor.CPPTYPE_UINT64,
}
_INTEGER_TYPES = _NUMBER_TYPES - {
    FieldDescriptor.CPPTYPE_FLOAT,
    FieldDescriptor.CPPTYPE_DOUBLE,
}


def _enum_prefix(enum: EnumDescriptor) -> str:
    """What every value name of an enum starts with, up to an underscore: ``COVER_STATE_``."""
    prefix = enum.values[0].name
    for value in enum.values:
        while not value.name.startswith(prefix):
            prefix = prefix[:-1]
    return prefix[: prefix.rfind("_") + 1]


def _enum_name(value: EnumValueDescriptor) -> str:
    return value.name[len(_enum_prefix(value.type)) :]


def _enum_value(enum: EnumDescriptor, name: str) -> EnumValueDescriptor | None:
    return enum.values_by_name.get(
        _enum_prefix(enum) + name
    ) or enum.values_by_name.get(name)


def _describe(detail: _Detail) -> TelemetryField:
    leaf = detail.path[-1]
    field = TelemetryField(
        key=detail.key, unit=detail.unit, description=detail.description
    )
    if leaf.cpp_type in _NUMBER_TYPES:
        field.type = TelemetryValueType.TELEMETRY_VALUE_TYPE_NUMBER
    elif leaf.cpp_type == FieldDescriptor.CPPTYPE_BOOL:
        field.type = TelemetryValueType.TELEMETRY_VALUE_TYPE_BOOLEAN
    else:
        field.type = TelemetryValueType.TELEMETRY_VALUE_TYPE_STRING
        if leaf.cpp_type == FieldDescriptor.CPPTYPE_ENUM:
            field.allowed_values.extend(_enum_name(v) for v in leaf.enum_type.values)
    return field


_FIELDS = tuple(_describe(d) for d in _DETAILS)


def telemetry_fields() -> list[TelemetryField]:
    """The keys :func:`to_sample` writes into ``details``, for ``CapabilitySet.telemetry_fields``."""
    return [_copy(f) for f in _FIELDS]


def telemetry_field(key: str) -> TelemetryField | None:
    """One key's description, or ``None`` for a key this catalog does not know."""
    return next((_copy(f) for f in _FIELDS if f.key == key), None)


def _copy(field: TelemetryField) -> TelemetryField:
    copy = TelemetryField()
    copy.CopyFrom(field)
    return copy


def request_to_sample(request: ProduceTelemetryRequest) -> TelemetrySample | None:
    """The sample of a v2 frame, or ``None`` when the frame carries no telemetry."""
    if not request.HasField("data"):
        return None
    return to_sample(request.data, request.base.sn)


def to_sample(telemetry: Telemetry, fallback_sn: str = "") -> TelemetrySample:
    sn = telemetry.sn if telemetry.sn.strip() else fallback_sn
    sample = TelemetrySample(asset=AssetRef(sn=sn))
    if telemetry.HasField("timestamp"):
        sample.observed_at.CopyFrom(telemetry.timestamp)
    if (
        telemetry.HasField("latitude")
        and telemetry.HasField("longitude")
        and math.isfinite(telemetry.latitude)
        and math.isfinite(telemetry.longitude)
    ):
        position = GeoPoint(latitude=telemetry.latitude, longitude=telemetry.longitude)
        if telemetry.HasField("absolute_altitude"):
            position.altitude = _widen(telemetry.absolute_altitude)
        sample.position.CopyFrom(position)
    if telemetry.HasField("relative_altitude"):
        sample.relative_altitude = _widen(telemetry.relative_altitude)
    if telemetry.HasField("heading"):
        sample.heading_degrees = _widen(telemetry.heading)
    if telemetry.HasField("sub_asset"):
        aircraft = telemetry.sub_asset
        if aircraft.HasField("horizontal_speed"):
            sample.horizontal_speed = _widen(aircraft.horizontal_speed)
        if aircraft.HasField("vertical_speed"):
            sample.vertical_speed = _widen(aircraft.vertical_speed)
        if aircraft.battery_information.HasField("percentage"):
            percent = _parse_number(aircraft.battery_information.percentage)
            if percent is not None:
                sample.battery_percent = percent
    elif telemetry.HasField("asset") and telemetry.asset.HasField(
        "sub_asset_percentage"
    ):
        sample.battery_percent = _widen(telemetry.asset.sub_asset_percentage)
    details = Struct()
    for detail in _DETAILS:
        value = _read(telemetry, detail.path)
        if value is not None:
            details.fields[detail.key].CopyFrom(value)
    if details.fields:
        sample.details.CopyFrom(details)
    return sample


def to_request(sample: TelemetrySample) -> ProduceTelemetryRequest:
    """The v2 frame of a sample, as an adapter would have streamed it."""
    base = RequestBase(tid=str(uuid.uuid4()), sn=sample.asset.sn)
    base.timestamp.CopyFrom(sample.observed_at)
    if sample.asset.id.strip():
        base.asset_id = sample.asset.id
    data = to_telemetry(sample)
    data.id = str(uuid.uuid4())
    return ProduceTelemetryRequest(base=base, data=data)


def to_telemetry(sample: TelemetrySample) -> Telemetry:
    telemetry = Telemetry(sn=sample.asset.sn)
    if sample.HasField("observed_at"):
        telemetry.timestamp.CopyFrom(sample.observed_at)
    if sample.HasField("position"):
        telemetry.latitude = sample.position.latitude
        telemetry.longitude = sample.position.longitude
        if sample.position.HasField("altitude"):
            telemetry.absolute_altitude = sample.position.altitude
    if sample.HasField("relative_altitude"):
        telemetry.relative_altitude = sample.relative_altitude
    if sample.HasField("heading_degrees"):
        telemetry.heading = sample.heading_degrees

    values = sample.details.fields
    source = _source_of(sample, values)
    for detail in _DETAILS:
        if detail.key in values and detail.source in (_Source.NONE, source):
            _write(telemetry, detail.path, values[detail.key])
    if source is _Source.SUB_ASSET:
        aircraft = telemetry.sub_asset
        aircraft.SetInParent()
        if sample.HasField("horizontal_speed"):
            aircraft.horizontal_speed = sample.horizontal_speed
        if sample.HasField("vertical_speed"):
            aircraft.vertical_speed = sample.vertical_speed
        if sample.HasField("battery_percent"):
            aircraft.battery_information.percentage = _format_number(
                sample.battery_percent
            )
    elif source is _Source.ASSET and sample.HasField("battery_percent"):
        telemetry.asset.sub_asset_percentage = sample.battery_percent
    return telemetry


def _source_of(sample: TelemetrySample, values) -> _Source:
    """An aircraft's sample moves; a dock's or a single device's carries its own keys or only a battery."""
    if (
        sample.HasField("horizontal_speed")
        or sample.HasField("vertical_speed")
        or _carries(values, _Source.SUB_ASSET)
    ):
        return _Source.SUB_ASSET
    if _carries(values, _Source.ASSET) or sample.HasField("battery_percent"):
        return _Source.ASSET
    return _Source.NONE


def _carries(values, source: _Source) -> bool:
    return any(d.source is source and d.key in values for d in _DETAILS)


def _has(message: Message, field: FieldDescriptor) -> bool:
    if field.has_presence:
        return message.HasField(field.name)
    return getattr(message, field.name) != field.default_value


def _read(message: Message, path: tuple[FieldDescriptor, ...]) -> Value | None:
    current = message
    for step in path[:-1]:
        if not current.HasField(step.name):
            return None
        current = getattr(current, step.name)
    leaf = path[-1]
    if not _has(current, leaf):
        return None
    return _to_value(leaf, getattr(current, leaf.name))


def _write(root: Message, path: tuple[FieldDescriptor, ...], value: Value) -> None:
    leaf = path[-1]
    converted = _from_value(leaf, value)
    if converted is None:
        return
    current = root
    for step in path[:-1]:
        current = getattr(current, step.name)
    if leaf.cpp_type == FieldDescriptor.CPPTYPE_MESSAGE:
        getattr(current, leaf.name).CopyFrom(converted)
    else:
        setattr(current, leaf.name, converted)


def _to_value(field: FieldDescriptor, raw) -> Value | None:
    cpp = field.cpp_type
    if cpp == FieldDescriptor.CPPTYPE_FLOAT:
        return _number(_widen(raw))
    if cpp in _NUMBER_TYPES:
        return _number(float(raw))
    if cpp == FieldDescriptor.CPPTYPE_BOOL:
        return Value(bool_value=raw)
    if cpp == FieldDescriptor.CPPTYPE_STRING:
        return Value(string_value=raw)
    if cpp == FieldDescriptor.CPPTYPE_ENUM:
        value = field.enum_type.values_by_number.get(raw)
        return Value(string_value=_enum_name(value)) if value is not None else None
    if (
        cpp == FieldDescriptor.CPPTYPE_MESSAGE
        and field.message_type.full_name == Timestamp.DESCRIPTOR.full_name
    ):
        return Value(string_value=raw.ToJsonString())
    return None


def _from_value(field: FieldDescriptor, value: Value):
    kind = value.WhichOneof("kind")
    cpp = field.cpp_type
    if cpp in _INTEGER_TYPES:
        return math.floor(value.number_value + 0.5) if kind == "number_value" else None
    if cpp in _NUMBER_TYPES:
        return value.number_value if kind == "number_value" else None
    if cpp == FieldDescriptor.CPPTYPE_BOOL:
        return value.bool_value if kind == "bool_value" else None
    if cpp == FieldDescriptor.CPPTYPE_STRING:
        return value.string_value if kind == "string_value" else None
    if cpp == FieldDescriptor.CPPTYPE_ENUM:
        if kind != "string_value":
            return None
        enum_value = _enum_value(field.enum_type, value.string_value)
        return enum_value.number if enum_value is not None else None
    if (
        cpp == FieldDescriptor.CPPTYPE_MESSAGE
        and field.message_type.full_name == Timestamp.DESCRIPTOR.full_name
    ):
        if kind != "string_value":
            return None
        timestamp = Timestamp()
        try:
            timestamp.FromJsonString(value.string_value)
        except ValueError:
            return None
        return timestamp
    return None


def _number(value: float) -> Value | None:
    return Value(number_value=value) if math.isfinite(value) else None


def _widen(value: float) -> float:
    """A float32 as the decimal it was written as (0.1 is 0.1, not 0.10000000149011612)."""
    if not math.isfinite(value):
        return value
    single = struct.unpack("f", struct.pack("f", value))[0]
    for digits in range(1, 10):
        text = f"{single:.{digits}g}"
        if struct.unpack("f", struct.pack("f", float(text)))[0] == single:
            return float(text)
    return single


def _parse_number(text: str) -> float | None:
    try:
        value = float(text.strip())
    except ValueError:
        return None
    return value if math.isfinite(value) else None


def _format_number(value: float) -> str:
    if value == math.floor(value) and abs(value) < 1e15:
        return str(int(value))
    return repr(value)
