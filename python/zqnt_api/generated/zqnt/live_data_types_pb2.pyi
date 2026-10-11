import datetime

from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from . import common_pb2 as _common_pb2
from . import base_pb2 as _base_pb2
from . import asset_pb2 as _asset_pb2
from . import device_control_contracts_pb2 as _device_control_contracts_pb2
from . import detection_pb2 as _detection_pb2
from . import mission_autonomy_types_pb2 as _mission_autonomy_types_pb2
from . import mission_autonomy_dto_pb2 as _mission_autonomy_dto_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TelemetrySourceState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TELEMETRY_SOURCE_STATE_UNSPECIFIED: _ClassVar[TelemetrySourceState]
    TELEMETRY_SOURCE_STATE_ONLINE: _ClassVar[TelemetrySourceState]
    TELEMETRY_SOURCE_STATE_STALE: _ClassVar[TelemetrySourceState]
    TELEMETRY_SOURCE_STATE_NO_DATA: _ClassVar[TelemetrySourceState]
TELEMETRY_SOURCE_STATE_UNSPECIFIED: TelemetrySourceState
TELEMETRY_SOURCE_STATE_ONLINE: TelemetrySourceState
TELEMETRY_SOURCE_STATE_STALE: TelemetrySourceState
TELEMETRY_SOURCE_STATE_NO_DATA: TelemetrySourceState

class LiveDataResponse(_message.Message):
    __slots__ = ("tid", "timestamp", "has_errors", "sn", "asset_id", "response_message", "telemetry", "empty", "error")
    TID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    SN_FIELD_NUMBER: _ClassVar[int]
    ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TELEMETRY_FIELD_NUMBER: _ClassVar[int]
    EMPTY_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    tid: str
    timestamp: _timestamp_pb2.Timestamp
    has_errors: bool
    sn: str
    asset_id: str
    response_message: str
    telemetry: Telemetry
    empty: _empty_pb2.Empty
    error: _base_pb2.GlobalErrorMessage
    def __init__(self, tid: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., has_errors: bool = ..., sn: _Optional[str] = ..., asset_id: _Optional[str] = ..., response_message: _Optional[str] = ..., telemetry: _Optional[_Union[Telemetry, _Mapping]] = ..., empty: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ...) -> None: ...

class StreamTelemetryRequest(_message.Message):
    __slots__ = ("base", "frequency_ms", "duration", "command")
    BASE_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_MS_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    frequency_ms: int
    duration: int
    command: _device_control_contracts_pb2.LiveDataServiceCommand
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., frequency_ms: _Optional[int] = ..., duration: _Optional[int] = ..., command: _Optional[_Union[_device_control_contracts_pb2.LiveDataServiceCommand, str]] = ...) -> None: ...

class ProduceTelemetryRequest(_message.Message):
    __slots__ = ("base", "data", "live_stream_state", "error")
    BASE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    LIVE_STREAM_STATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    data: Telemetry
    live_stream_state: _device_control_contracts_pb2.LiveStreamState
    error: _base_pb2.GlobalErrorMessage
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., data: _Optional[_Union[Telemetry, _Mapping]] = ..., live_stream_state: _Optional[_Union[_device_control_contracts_pb2.LiveStreamState, _Mapping]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ...) -> None: ...

class LiveDataTelemetryResponse(_message.Message):
    __slots__ = ("tid", "timestamp", "has_errors", "sn", "asset_id", "data", "error", "live_stream_state", "stream_heartbeat", "source_status")
    TID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    SN_FIELD_NUMBER: _ClassVar[int]
    ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    LIVE_STREAM_STATE_FIELD_NUMBER: _ClassVar[int]
    STREAM_HEARTBEAT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_STATUS_FIELD_NUMBER: _ClassVar[int]
    tid: str
    timestamp: _timestamp_pb2.Timestamp
    has_errors: bool
    sn: str
    asset_id: str
    data: Telemetry
    error: _base_pb2.GlobalErrorMessage
    live_stream_state: _device_control_contracts_pb2.LiveStreamState
    stream_heartbeat: LiveDataStreamHeartbeat
    source_status: TelemetrySourceStatus
    def __init__(self, tid: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., has_errors: bool = ..., sn: _Optional[str] = ..., asset_id: _Optional[str] = ..., data: _Optional[_Union[Telemetry, _Mapping]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ..., live_stream_state: _Optional[_Union[_device_control_contracts_pb2.LiveStreamState, _Mapping]] = ..., stream_heartbeat: _Optional[_Union[LiveDataStreamHeartbeat, _Mapping]] = ..., source_status: _Optional[_Union[TelemetrySourceStatus, _Mapping]] = ...) -> None: ...

class LiveDataStreamHeartbeat(_message.Message):
    __slots__ = ("timestamp",)
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class TelemetrySourceStatus(_message.Message):
    __slots__ = ("sn", "state", "observed_at", "last_telemetry_at")
    SN_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    OBSERVED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_TELEMETRY_AT_FIELD_NUMBER: _ClassVar[int]
    sn: str
    state: TelemetrySourceState
    observed_at: _timestamp_pb2.Timestamp
    last_telemetry_at: _timestamp_pb2.Timestamp
    def __init__(self, sn: _Optional[str] = ..., state: _Optional[_Union[TelemetrySourceState, str]] = ..., observed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., last_telemetry_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class LiveDataDetectionResponse(_message.Message):
    __slots__ = ("tid", "timestamp", "has_errors", "sn", "asset_id", "detections", "error")
    TID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    SN_FIELD_NUMBER: _ClassVar[int]
    ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    DETECTIONS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    tid: str
    timestamp: _timestamp_pb2.Timestamp
    has_errors: bool
    sn: str
    asset_id: str
    detections: _detection_pb2.DetectionBatch
    error: _base_pb2.GlobalErrorMessage
    def __init__(self, tid: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., has_errors: bool = ..., sn: _Optional[str] = ..., asset_id: _Optional[str] = ..., detections: _Optional[_Union[_detection_pb2.DetectionBatch, _Mapping]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ...) -> None: ...

class Telemetry(_message.Message):
    __slots__ = ("id", "timestamp", "sn", "latitude", "longitude", "absolute_altitude", "relative_altitude", "wind_speed", "heading", "asset", "sub_asset")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    SN_FIELD_NUMBER: _ClassVar[int]
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    ABSOLUTE_ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    WIND_SPEED_FIELD_NUMBER: _ClassVar[int]
    HEADING_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    SUB_ASSET_FIELD_NUMBER: _ClassVar[int]
    id: str
    timestamp: _timestamp_pb2.Timestamp
    sn: str
    latitude: float
    longitude: float
    absolute_altitude: float
    relative_altitude: float
    wind_speed: float
    heading: float
    asset: AssetTelemetryDetails
    sub_asset: SubAssetTelemetryDetails
    def __init__(self, id: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., sn: _Optional[str] = ..., latitude: _Optional[float] = ..., longitude: _Optional[float] = ..., absolute_altitude: _Optional[float] = ..., relative_altitude: _Optional[float] = ..., wind_speed: _Optional[float] = ..., heading: _Optional[float] = ..., asset: _Optional[_Union[AssetTelemetryDetails, _Mapping]] = ..., sub_asset: _Optional[_Union[SubAssetTelemetryDetails, _Mapping]] = ...) -> None: ...

class AssetTelemetryDetails(_message.Message):
    __slots__ = ("environment_temp", "inside_temp", "humidity", "mode", "rainfall", "sub_asset_information", "sub_asset_at_home", "sub_asset_charging", "sub_asset_percentage", "debug_mode_open", "has_active_manual_control_session", "cover_state", "working_voltage", "working_current", "supply_voltage", "position_valid", "network_information", "air_conditioner", "manual_control_state", "position_state", "wireless_link", "sdr_state")
    class AssetSdrState(_message.Message):
        __slots__ = ("down_quality", "up_quality", "frequency_band")
        DOWN_QUALITY_FIELD_NUMBER: _ClassVar[int]
        UP_QUALITY_FIELD_NUMBER: _ClassVar[int]
        FREQUENCY_BAND_FIELD_NUMBER: _ClassVar[int]
        down_quality: int
        up_quality: int
        frequency_band: float
        def __init__(self, down_quality: _Optional[int] = ..., up_quality: _Optional[int] = ..., frequency_band: _Optional[float] = ...) -> None: ...
    class PositionState(_message.Message):
        __slots__ = ("gps_number", "rtk_number", "quality")
        GPS_NUMBER_FIELD_NUMBER: _ClassVar[int]
        RTK_NUMBER_FIELD_NUMBER: _ClassVar[int]
        QUALITY_FIELD_NUMBER: _ClassVar[int]
        gps_number: int
        rtk_number: int
        quality: int
        def __init__(self, gps_number: _Optional[int] = ..., rtk_number: _Optional[int] = ..., quality: _Optional[int] = ...) -> None: ...
    class AssetAirConditioner(_message.Message):
        __slots__ = ("state", "switch_time")
        STATE_FIELD_NUMBER: _ClassVar[int]
        SWITCH_TIME_FIELD_NUMBER: _ClassVar[int]
        state: _asset_pb2.AssetAirConditionerStateEnum
        switch_time: int
        def __init__(self, state: _Optional[_Union[_asset_pb2.AssetAirConditionerStateEnum, str]] = ..., switch_time: _Optional[int] = ...) -> None: ...
    class AssetNetworkInformation(_message.Message):
        __slots__ = ("type", "rate", "quality")
        TYPE_FIELD_NUMBER: _ClassVar[int]
        RATE_FIELD_NUMBER: _ClassVar[int]
        QUALITY_FIELD_NUMBER: _ClassVar[int]
        type: _asset_pb2.NetworkTypeEnum
        rate: float
        quality: _asset_pb2.NetworkStateQualityEnum
        def __init__(self, type: _Optional[_Union[_asset_pb2.NetworkTypeEnum, str]] = ..., rate: _Optional[float] = ..., quality: _Optional[_Union[_asset_pb2.NetworkStateQualityEnum, str]] = ...) -> None: ...
    class AssetWirelessLinkInformation(_message.Message):
        __slots__ = ("fourth_generation_freq_band", "fourth_generation_gnd_quality", "fourth_generation_link_state", "fourth_generation_quality", "fourth_generation_uav_quality", "dongle_number", "link_workmode", "sdr_freq_band", "sdr_link_state", "sdr_quality")
        FOURTH_GENERATION_FREQ_BAND_FIELD_NUMBER: _ClassVar[int]
        FOURTH_GENERATION_GND_QUALITY_FIELD_NUMBER: _ClassVar[int]
        FOURTH_GENERATION_LINK_STATE_FIELD_NUMBER: _ClassVar[int]
        FOURTH_GENERATION_QUALITY_FIELD_NUMBER: _ClassVar[int]
        FOURTH_GENERATION_UAV_QUALITY_FIELD_NUMBER: _ClassVar[int]
        DONGLE_NUMBER_FIELD_NUMBER: _ClassVar[int]
        LINK_WORKMODE_FIELD_NUMBER: _ClassVar[int]
        SDR_FREQ_BAND_FIELD_NUMBER: _ClassVar[int]
        SDR_LINK_STATE_FIELD_NUMBER: _ClassVar[int]
        SDR_QUALITY_FIELD_NUMBER: _ClassVar[int]
        fourth_generation_freq_band: float
        fourth_generation_gnd_quality: int
        fourth_generation_link_state: bool
        fourth_generation_quality: int
        fourth_generation_uav_quality: int
        dongle_number: int
        link_workmode: str
        sdr_freq_band: float
        sdr_link_state: bool
        sdr_quality: int
        def __init__(self, fourth_generation_freq_band: _Optional[float] = ..., fourth_generation_gnd_quality: _Optional[int] = ..., fourth_generation_link_state: bool = ..., fourth_generation_quality: _Optional[int] = ..., fourth_generation_uav_quality: _Optional[int] = ..., dongle_number: _Optional[int] = ..., link_workmode: _Optional[str] = ..., sdr_freq_band: _Optional[float] = ..., sdr_link_state: bool = ..., sdr_quality: _Optional[int] = ...) -> None: ...
    class AssetSubAssetInformation(_message.Message):
        __slots__ = ("sn", "model", "paired", "online")
        SN_FIELD_NUMBER: _ClassVar[int]
        MODEL_FIELD_NUMBER: _ClassVar[int]
        PAIRED_FIELD_NUMBER: _ClassVar[int]
        ONLINE_FIELD_NUMBER: _ClassVar[int]
        sn: str
        model: str
        paired: bool
        online: bool
        def __init__(self, sn: _Optional[str] = ..., model: _Optional[str] = ..., paired: bool = ..., online: bool = ...) -> None: ...
    ENVIRONMENT_TEMP_FIELD_NUMBER: _ClassVar[int]
    INSIDE_TEMP_FIELD_NUMBER: _ClassVar[int]
    HUMIDITY_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    RAINFALL_FIELD_NUMBER: _ClassVar[int]
    SUB_ASSET_INFORMATION_FIELD_NUMBER: _ClassVar[int]
    SUB_ASSET_AT_HOME_FIELD_NUMBER: _ClassVar[int]
    SUB_ASSET_CHARGING_FIELD_NUMBER: _ClassVar[int]
    SUB_ASSET_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    DEBUG_MODE_OPEN_FIELD_NUMBER: _ClassVar[int]
    HAS_ACTIVE_MANUAL_CONTROL_SESSION_FIELD_NUMBER: _ClassVar[int]
    COVER_STATE_FIELD_NUMBER: _ClassVar[int]
    WORKING_VOLTAGE_FIELD_NUMBER: _ClassVar[int]
    WORKING_CURRENT_FIELD_NUMBER: _ClassVar[int]
    SUPPLY_VOLTAGE_FIELD_NUMBER: _ClassVar[int]
    POSITION_VALID_FIELD_NUMBER: _ClassVar[int]
    NETWORK_INFORMATION_FIELD_NUMBER: _ClassVar[int]
    AIR_CONDITIONER_FIELD_NUMBER: _ClassVar[int]
    MANUAL_CONTROL_STATE_FIELD_NUMBER: _ClassVar[int]
    POSITION_STATE_FIELD_NUMBER: _ClassVar[int]
    WIRELESS_LINK_FIELD_NUMBER: _ClassVar[int]
    SDR_STATE_FIELD_NUMBER: _ClassVar[int]
    environment_temp: float
    inside_temp: float
    humidity: float
    mode: _asset_pb2.AssetMode
    rainfall: _asset_pb2.RainfallEnum
    sub_asset_information: AssetTelemetryDetails.AssetSubAssetInformation
    sub_asset_at_home: bool
    sub_asset_charging: bool
    sub_asset_percentage: float
    debug_mode_open: bool
    has_active_manual_control_session: bool
    cover_state: _asset_pb2.AssetCoverStateEnum
    working_voltage: int
    working_current: int
    supply_voltage: int
    position_valid: bool
    network_information: AssetTelemetryDetails.AssetNetworkInformation
    air_conditioner: AssetTelemetryDetails.AssetAirConditioner
    manual_control_state: _asset_pb2.ManualControlStateEnum
    position_state: AssetTelemetryDetails.PositionState
    wireless_link: AssetTelemetryDetails.AssetWirelessLinkInformation
    sdr_state: AssetTelemetryDetails.AssetSdrState
    def __init__(self, environment_temp: _Optional[float] = ..., inside_temp: _Optional[float] = ..., humidity: _Optional[float] = ..., mode: _Optional[_Union[_asset_pb2.AssetMode, str]] = ..., rainfall: _Optional[_Union[_asset_pb2.RainfallEnum, str]] = ..., sub_asset_information: _Optional[_Union[AssetTelemetryDetails.AssetSubAssetInformation, _Mapping]] = ..., sub_asset_at_home: bool = ..., sub_asset_charging: bool = ..., sub_asset_percentage: _Optional[float] = ..., debug_mode_open: bool = ..., has_active_manual_control_session: bool = ..., cover_state: _Optional[_Union[_asset_pb2.AssetCoverStateEnum, str]] = ..., working_voltage: _Optional[int] = ..., working_current: _Optional[int] = ..., supply_voltage: _Optional[int] = ..., position_valid: bool = ..., network_information: _Optional[_Union[AssetTelemetryDetails.AssetNetworkInformation, _Mapping]] = ..., air_conditioner: _Optional[_Union[AssetTelemetryDetails.AssetAirConditioner, _Mapping]] = ..., manual_control_state: _Optional[_Union[_asset_pb2.ManualControlStateEnum, str]] = ..., position_state: _Optional[_Union[AssetTelemetryDetails.PositionState, _Mapping]] = ..., wireless_link: _Optional[_Union[AssetTelemetryDetails.AssetWirelessLinkInformation, _Mapping]] = ..., sdr_state: _Optional[_Union[AssetTelemetryDetails.AssetSdrState, _Mapping]] = ...) -> None: ...

class SubAssetTelemetryDetails(_message.Message):
    __slots__ = ("horizontal_speed", "vertical_speed", "wind_direction", "gear", "payload_telemetry", "battery_information", "height_limit", "home_distance", "total_movement_distance", "total_movement_time", "mode", "country", "component_telemetry")
    class SubAssetBatteryInformation(_message.Message):
        __slots__ = ("percentage", "remaining_time", "return_to_home_power")
        PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
        REMAINING_TIME_FIELD_NUMBER: _ClassVar[int]
        RETURN_TO_HOME_POWER_FIELD_NUMBER: _ClassVar[int]
        percentage: str
        remaining_time: int
        return_to_home_power: str
        def __init__(self, percentage: _Optional[str] = ..., remaining_time: _Optional[int] = ..., return_to_home_power: _Optional[str] = ...) -> None: ...
    HORIZONTAL_SPEED_FIELD_NUMBER: _ClassVar[int]
    VERTICAL_SPEED_FIELD_NUMBER: _ClassVar[int]
    WIND_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    GEAR_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_TELEMETRY_FIELD_NUMBER: _ClassVar[int]
    BATTERY_INFORMATION_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_LIMIT_FIELD_NUMBER: _ClassVar[int]
    HOME_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_MOVEMENT_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_MOVEMENT_TIME_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_TELEMETRY_FIELD_NUMBER: _ClassVar[int]
    horizontal_speed: float
    vertical_speed: float
    wind_direction: str
    gear: int
    payload_telemetry: PayloadTelemetry
    battery_information: SubAssetTelemetryDetails.SubAssetBatteryInformation
    height_limit: int
    home_distance: float
    total_movement_distance: float
    total_movement_time: float
    mode: _asset_pb2.SubAssetMode
    country: str
    component_telemetry: _containers.RepeatedCompositeFieldContainer[ComponentTelemetry]
    def __init__(self, horizontal_speed: _Optional[float] = ..., vertical_speed: _Optional[float] = ..., wind_direction: _Optional[str] = ..., gear: _Optional[int] = ..., payload_telemetry: _Optional[_Union[PayloadTelemetry, _Mapping]] = ..., battery_information: _Optional[_Union[SubAssetTelemetryDetails.SubAssetBatteryInformation, _Mapping]] = ..., height_limit: _Optional[int] = ..., home_distance: _Optional[float] = ..., total_movement_distance: _Optional[float] = ..., total_movement_time: _Optional[float] = ..., mode: _Optional[_Union[_asset_pb2.SubAssetMode, str]] = ..., country: _Optional[str] = ..., component_telemetry: _Optional[_Iterable[_Union[ComponentTelemetry, _Mapping]]] = ...) -> None: ...

class ComponentTelemetry(_message.Message):
    __slots__ = ("component_id", "external_id", "kind", "timestamp", "camera_data", "range_finder_data", "sensor_data", "attributes")
    COMPONENT_ID_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    CAMERA_DATA_FIELD_NUMBER: _ClassVar[int]
    RANGE_FINDER_DATA_FIELD_NUMBER: _ClassVar[int]
    SENSOR_DATA_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    component_id: str
    external_id: str
    kind: str
    timestamp: _timestamp_pb2.Timestamp
    camera_data: PayloadTelemetry.CameraData
    range_finder_data: PayloadTelemetry.RangeFinderData
    sensor_data: PayloadTelemetry.SensorData
    attributes: _struct_pb2.Struct
    def __init__(self, component_id: _Optional[str] = ..., external_id: _Optional[str] = ..., kind: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., camera_data: _Optional[_Union[PayloadTelemetry.CameraData, _Mapping]] = ..., range_finder_data: _Optional[_Union[PayloadTelemetry.RangeFinderData, _Mapping]] = ..., sensor_data: _Optional[_Union[PayloadTelemetry.SensorData, _Mapping]] = ..., attributes: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class PayloadTelemetry(_message.Message):
    __slots__ = ("id", "timestamp", "camera_data", "range_finder_data", "sensor_data", "name")
    class CameraData(_message.Message):
        __slots__ = ("current_lens", "gimbal_pitch", "gimbal_yaw", "zoom_factor", "gimbal_roll")
        CURRENT_LENS_FIELD_NUMBER: _ClassVar[int]
        GIMBAL_PITCH_FIELD_NUMBER: _ClassVar[int]
        GIMBAL_YAW_FIELD_NUMBER: _ClassVar[int]
        ZOOM_FACTOR_FIELD_NUMBER: _ClassVar[int]
        GIMBAL_ROLL_FIELD_NUMBER: _ClassVar[int]
        current_lens: str
        gimbal_pitch: float
        gimbal_yaw: float
        zoom_factor: float
        gimbal_roll: float
        def __init__(self, current_lens: _Optional[str] = ..., gimbal_pitch: _Optional[float] = ..., gimbal_yaw: _Optional[float] = ..., zoom_factor: _Optional[float] = ..., gimbal_roll: _Optional[float] = ...) -> None: ...
    class RangeFinderData(_message.Message):
        __slots__ = ("target_latitude", "target_longitude", "target_distance", "target_altitude")
        TARGET_LATITUDE_FIELD_NUMBER: _ClassVar[int]
        TARGET_LONGITUDE_FIELD_NUMBER: _ClassVar[int]
        TARGET_DISTANCE_FIELD_NUMBER: _ClassVar[int]
        TARGET_ALTITUDE_FIELD_NUMBER: _ClassVar[int]
        target_latitude: float
        target_longitude: float
        target_distance: float
        target_altitude: float
        def __init__(self, target_latitude: _Optional[float] = ..., target_longitude: _Optional[float] = ..., target_distance: _Optional[float] = ..., target_altitude: _Optional[float] = ...) -> None: ...
    class SensorData(_message.Message):
        __slots__ = ("target_temperature",)
        TARGET_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
        target_temperature: float
        def __init__(self, target_temperature: _Optional[float] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    CAMERA_DATA_FIELD_NUMBER: _ClassVar[int]
    RANGE_FINDER_DATA_FIELD_NUMBER: _ClassVar[int]
    SENSOR_DATA_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    timestamp: _timestamp_pb2.Timestamp
    camera_data: PayloadTelemetry.CameraData
    range_finder_data: PayloadTelemetry.RangeFinderData
    sensor_data: PayloadTelemetry.SensorData
    name: str
    def __init__(self, id: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., camera_data: _Optional[_Union[PayloadTelemetry.CameraData, _Mapping]] = ..., range_finder_data: _Optional[_Union[PayloadTelemetry.RangeFinderData, _Mapping]] = ..., sensor_data: _Optional[_Union[PayloadTelemetry.SensorData, _Mapping]] = ..., name: _Optional[str] = ...) -> None: ...
