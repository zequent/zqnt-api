import math

from google.protobuf.struct_pb2 import Struct
from google.protobuf.timestamp_pb2 import Timestamp

from zqnt_api.generated.zqnt.capability.v3.capability_pb2 import TelemetryValueType
from zqnt_api.generated.zqnt.common.v3.common_pb2 import AssetRef, GeoPoint
from zqnt_api.generated.zqnt.live_data_types_pb2 import (
    AssetTelemetryDetails,
    PayloadTelemetry,
    ProduceTelemetryRequest,
    SubAssetTelemetryDetails,
    Telemetry,
)
from zqnt_api.generated.zqnt.telemetry.v3.telemetry_pb2 import TelemetrySample
from zqnt_api.telemetry import (
    CAMERA_GIMBAL_PITCH,
    DOCK_AIR_CONDITIONER_STATE,
    DOCK_COVER_STATE,
    DOCK_DRONE_AT_HOME,
    DOCK_DRONE_CHARGING,
    DOCK_ENVIRONMENT_TEMPERATURE,
    DOCK_HUMIDITY,
    DOCK_MODE,
    DOCK_RAINFALL,
    DOCK_SUPPLY_VOLTAGE,
    DOCK_WORKING_VOLTAGE,
    DRONE_MODE,
    LINK_SDR_QUALITY,
    NETWORK_QUALITY,
    NETWORK_TYPE,
    PAYLOAD_OBSERVED_AT,
    WIND_SPEED,
    request_to_sample,
    telemetry_field,
    telemetry_fields,
    to_request,
    to_sample,
    to_telemetry,
)

AT = Timestamp(seconds=1_791_000_000, nanos=250_000_000)


def dock() -> Telemetry:
    return Telemetry(
        id="sample-1",
        timestamp=AT,
        sn="DOCK-1",
        latitude=52.5200,
        longitude=13.4050,
        absolute_altitude=34.5,
        relative_altitude=0,
        wind_speed=3.2,
        heading=181.5,
        asset=AssetTelemetryDetails(
            environment_temp=21.3,
            inside_temp=25.1,
            humidity=48,
            mode="ASSET_MODE_WORKING",
            rainfall="RAINFALL_LIGHT",
            sub_asset_information=AssetTelemetryDetails.AssetSubAssetInformation(
                sn="AIRCRAFT-1", model="M3TD", paired=True, online=False
            ),
            sub_asset_at_home=True,
            sub_asset_charging=True,
            sub_asset_percentage=87,
            debug_mode_open=False,
            has_active_manual_control_session=False,
            cover_state="COVER_STATE_CLOSED",
            working_voltage=24_000,
            working_current=1_250,
            supply_voltage=230_400,
            position_valid=True,
            network_information=AssetTelemetryDetails.AssetNetworkInformation(
                type="NETWORK_TYPE_4_G",
                rate=512.5,
                quality="NETWORK_STATE_QUALITY_GOOD",
            ),
            air_conditioner=AssetTelemetryDetails.AssetAirConditioner(
                state="AIR_CONDITIONER_COOL", switch_time=30
            ),
            manual_control_state="MANUAL_CONTROL_STATE_DISCONNECTED",
            position_state=AssetTelemetryDetails.PositionState(
                gps_number=12, rtk_number=20, quality=5
            ),
            wireless_link=AssetTelemetryDetails.AssetWirelessLinkInformation(
                fourth_generation_freq_band=1.8,
                fourth_generation_gnd_quality=4,
                fourth_generation_link_state=True,
                fourth_generation_quality=3,
                fourth_generation_uav_quality=2,
                dongle_number=1,
                link_workmode="SDR_AND_4G",
                sdr_freq_band=5.8,
                sdr_link_state=True,
                sdr_quality=5,
            ),
            sdr_state=AssetTelemetryDetails.AssetSdrState(
                down_quality=5, up_quality=4, frequency_band=2.4
            ),
        ),
    )


def drone() -> Telemetry:
    return Telemetry(
        id="sample-2",
        timestamp=AT,
        sn="AIRCRAFT-1",
        latitude=52.5210,
        longitude=13.4070,
        absolute_altitude=110.2,
        relative_altitude=75.7,
        wind_speed=5.1,
        heading=-12.25,
        sub_asset=SubAssetTelemetryDetails(
            horizontal_speed=12.3,
            vertical_speed=-0.4,
            wind_direction="NORTH_EAST",
            gear=1,
            height_limit=120,
            home_distance=842.6,
            total_movement_distance=123_456.7,
            total_movement_time=98_765,
            mode="SUBASSET_MODE_WAYLINE",
            country="DE",
            battery_information=SubAssetTelemetryDetails.SubAssetBatteryInformation(
                percentage="64", remaining_time=1_320, return_to_home_power="22"
            ),
            payload_telemetry=PayloadTelemetry(
                id="payload-0",
                name="H20T",
                timestamp=AT,
                camera_data=PayloadTelemetry.CameraData(
                    current_lens="ir",
                    gimbal_pitch=-45.5,
                    gimbal_yaw=10,
                    zoom_factor=2,
                    gimbal_roll=0.1,
                ),
                range_finder_data=PayloadTelemetry.RangeFinderData(
                    target_latitude=52.53,
                    target_longitude=13.41,
                    target_distance=150.5,
                    target_altitude=30,
                ),
                sensor_data=PayloadTelemetry.SensorData(target_temperature=36.6),
            ),
        ),
    )


def without_id(telemetry: Telemetry) -> Telemetry:
    copy = Telemetry()
    copy.CopyFrom(telemetry)
    copy.ClearField("id")
    return copy


def test_a_dock_sample_survives_the_round_trip():
    assert to_telemetry(to_sample(dock())) == without_id(dock())


def test_a_drone_sample_survives_the_round_trip():
    assert to_telemetry(to_sample(drone())) == without_id(drone())


def test_the_shared_fields_are_typed():
    d = to_sample(dock())
    assert d.asset == AssetRef(sn="DOCK-1")
    assert d.observed_at == AT
    assert d.position == GeoPoint(latitude=52.52, longitude=13.405, altitude=34.5)
    assert d.heading_degrees == 181.5
    assert d.battery_percent == 87, (
        "a dock's battery is its aircraft's, as the console shows it"
    )
    assert not d.HasField("horizontal_speed")

    a = to_sample(drone())
    assert (
        a.relative_altitude,
        a.horizontal_speed,
        a.vertical_speed,
        a.battery_percent,
    ) == (75.7, 12.3, -0.4, 64)


def test_details_use_the_dotted_keys_and_enum_names_without_prefix():
    d = to_sample(dock()).details.fields
    assert d[DOCK_COVER_STATE].string_value == "CLOSED"
    assert d[DOCK_MODE].string_value == "WORKING"
    assert d[DOCK_AIR_CONDITIONER_STATE].string_value == "COOL"
    assert d[DOCK_RAINFALL].string_value == "LIGHT"
    assert d[NETWORK_TYPE].string_value == "4_G"
    assert d[NETWORK_QUALITY].string_value == "GOOD"
    assert d[DOCK_ENVIRONMENT_TEMPERATURE].number_value == 21.3
    assert d[LINK_SDR_QUALITY].number_value == 5
    assert d[DOCK_DRONE_AT_HOME].bool_value
    assert d[WIND_SPEED].number_value == 3.2

    a = to_sample(drone()).details.fields
    assert a[DRONE_MODE].string_value == "WAYLINE"
    assert a[CAMERA_GIMBAL_PITCH].number_value == -45.5
    assert a[PAYLOAD_OBSERVED_AT].string_value == "2026-10-03T04:00:00.250Z"


def test_every_detail_key_is_described_once_with_its_type():
    described = {f.key: f for f in telemetry_fields()}
    assert len(described) == len(telemetry_fields()) == 64, (
        "the same 64 keys as zqnt-utils-java"
    )
    for sample in (dock(), drone()):
        assert set(to_sample(sample).details.fields) <= set(described)

    cover = described[DOCK_COVER_STATE]
    assert cover.type == TelemetryValueType.TELEMETRY_VALUE_TYPE_STRING
    assert list(cover.allowed_values) == ["CLOSED", "OPENED", "HALF_OPEN", "ABNORMAL"]
    temperature = described[DOCK_ENVIRONMENT_TEMPERATURE]
    assert (temperature.type, temperature.unit) == (
        TelemetryValueType.TELEMETRY_VALUE_TYPE_NUMBER,
        "°C",
    )
    assert (
        described[DOCK_DRONE_CHARGING].type
        == TelemetryValueType.TELEMETRY_VALUE_TYPE_BOOLEAN
    )
    assert telemetry_field(DOCK_COVER_STATE) == cover
    assert telemetry_field("radar.mode") is None


def test_keys_v2_has_no_field_for_are_dropped_there_and_the_source_follows_the_keys():
    details = Struct()
    details.update(
        {
            "radar.mode": "SCAN",
            DOCK_COVER_STATE: "OPENED",
            DOCK_HUMIDITY: "not a number",
        }
    )
    sample = TelemetrySample(
        asset=AssetRef(sn="RADAR-1"),
        observed_at=AT,
        battery_percent=55.5,
        details=details,
    )

    telemetry = to_telemetry(sample)
    assert telemetry.HasField("asset")
    assert (
        telemetry.asset.cover_state
        == AssetTelemetryDetails()
        .DESCRIPTOR.fields_by_name["cover_state"]
        .enum_type.values_by_name["COVER_STATE_OPENED"]
        .number
    )
    assert not telemetry.asset.HasField("humidity"), (
        "a value of the wrong type is not guessed at"
    )
    assert telemetry.asset.sub_asset_percentage == 55.5

    sample.horizontal_speed = 4
    aircraft = to_telemetry(sample)
    assert aircraft.HasField("sub_asset"), (
        "a moving asset is an aircraft; the dock's keys are dropped"
    )
    assert aircraft.sub_asset.battery_information.percentage == "55.5"


def test_a_sample_becomes_the_frame_an_adapter_would_have_streamed():
    sample = to_sample(drone())
    sample.asset.CopyFrom(AssetRef(sn="AIRCRAFT-1", id="aircraft-1-id"))
    request = to_request(sample)
    assert request.base.sn == "AIRCRAFT-1"
    assert request.base.asset_id == "aircraft-1-id"
    assert request.base.timestamp == AT
    assert request.base.tid and request.data.id and request.base.tid != request.data.id
    back = request_to_sample(request)
    back.asset.CopyFrom(sample.asset)
    assert back == sample


def test_a_frame_without_coordinates_or_serial_still_maps():
    sample = to_sample(Telemetry(latitude=math.nan, longitude=math.nan), "FROM-BASE")
    assert not sample.HasField("position"), "omitted coordinates arrive as NaN"
    assert sample.asset.sn == "FROM-BASE"
    assert request_to_sample(ProduceTelemetryRequest()) is None


def test_the_supply_voltage_is_volts_in_v3_and_millivolts_in_v2():
    d = to_sample(dock()).details.fields
    assert d[DOCK_SUPPLY_VOLTAGE].number_value == 230.4
    assert d[DOCK_WORKING_VOLTAGE].number_value == 24_000
    assert telemetry_field(DOCK_SUPPLY_VOLTAGE).unit == "V"
    assert telemetry_field(DOCK_WORKING_VOLTAGE).unit == "mV"

    details = Struct()
    details.update({DOCK_SUPPLY_VOLTAGE: 16.204})
    sample = TelemetrySample(asset=AssetRef(sn="DRONE-1"), details=details)
    assert to_telemetry(sample).asset.supply_voltage == 16_204
