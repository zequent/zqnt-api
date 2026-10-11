import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ManualControlStateEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MANUAL_CONTROL_STATE_DISCONNECTED: _ClassVar[ManualControlStateEnum]
    MANUAL_CONTROL_STATE_CONNECTING: _ClassVar[ManualControlStateEnum]
    MANUAL_CONTROL_STATE_CONNECTED: _ClassVar[ManualControlStateEnum]

class RainfallEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RAINFALL_NO: _ClassVar[RainfallEnum]
    RAINFALL_LIGHT: _ClassVar[RainfallEnum]
    RAINFALL_MODERATE: _ClassVar[RainfallEnum]
    RAINFALL_HEAVY: _ClassVar[RainfallEnum]

class NetworkTypeEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NETWORK_TYPE_4_G: _ClassVar[NetworkTypeEnum]
    NETWORK_TYPE_ETHERNET: _ClassVar[NetworkTypeEnum]

class AssetCoverStateEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COVER_STATE_CLOSED: _ClassVar[AssetCoverStateEnum]
    COVER_STATE_OPENED: _ClassVar[AssetCoverStateEnum]
    COVER_STATE_HALF_OPEN: _ClassVar[AssetCoverStateEnum]
    COVER_STATE_ABNORMAL: _ClassVar[AssetCoverStateEnum]

class NetworkStateQualityEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NETWORK_STATE_QUALITY_NO_SIGNAL: _ClassVar[NetworkStateQualityEnum]
    NETWORK_STATE_QUALITY_BAD: _ClassVar[NetworkStateQualityEnum]
    NETWORK_STATE_QUALITY_POOR: _ClassVar[NetworkStateQualityEnum]
    NETWORK_STATE_QUALITY_FAIR: _ClassVar[NetworkStateQualityEnum]
    NETWORK_STATE_QUALITY_GOOD: _ClassVar[NetworkStateQualityEnum]
    NETWORK_STATE_QUALITY_EXCELLENT: _ClassVar[NetworkStateQualityEnum]

class AssetAirConditionerStateEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AIR_CONDITIONER_IDLE: _ClassVar[AssetAirConditionerStateEnum]
    AIR_CONDITIONER_COOL: _ClassVar[AssetAirConditionerStateEnum]
    AIR_CONDITIONER_HEAT: _ClassVar[AssetAirConditionerStateEnum]
    AIR_CONDITIONER_DEHUMIDIFICATION: _ClassVar[AssetAirConditionerStateEnum]
    AIR_CONDITIONER_COOLING_EXIT: _ClassVar[AssetAirConditionerStateEnum]
    AIR_CONDITIONER_HEATING_EXIT: _ClassVar[AssetAirConditionerStateEnum]
    AIR_CONDITIONER_DEHUMIDIFICATION_EXIT: _ClassVar[AssetAirConditionerStateEnum]
    AIR_CONDITIONER_COOLING_READY: _ClassVar[AssetAirConditionerStateEnum]
    AIR_CONDITIONER_HEATING_READY: _ClassVar[AssetAirConditionerStateEnum]
    AIR_CONDITIONER_DEHUMIDIFICATION_READY: _ClassVar[AssetAirConditionerStateEnum]
    AIR_CONDITIONER_PREPARING_FOR_AIR_COOLING: _ClassVar[AssetAirConditionerStateEnum]
    AIR_CONDITIONER_AIR_COOLING_IN_PROGRESS: _ClassVar[AssetAirConditionerStateEnum]
    AIR_CONDITIONER_AIR_COOLING_EXITING: _ClassVar[AssetAirConditionerStateEnum]
    AIR_CONDITIONER_PREPARING_FOR_DEFOGGER: _ClassVar[AssetAirConditionerStateEnum]
    AIR_CONDITIONER_DEFOGGER_IN_PROGRESS: _ClassVar[AssetAirConditionerStateEnum]
    AIR_CONDITIONER_DEFOGGER_EXITING: _ClassVar[AssetAirConditionerStateEnum]

class AssetMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ASSET_MODE_IDLE: _ClassVar[AssetMode]
    ASSET_MODE_DEBUGGING: _ClassVar[AssetMode]
    ASSET_MODE_REMOTE_DEBUGGING: _ClassVar[AssetMode]
    ASSET_MODE_UPGRADING: _ClassVar[AssetMode]
    ASSET_MODE_WORKING: _ClassVar[AssetMode]
    ASSET_MODE_TO_BE_CALIBRATED: _ClassVar[AssetMode]
    ASSET_MODE_OFFLINE: _ClassVar[AssetMode]

class SubAssetMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SUBASSET_MODE_IDLE: _ClassVar[SubAssetMode]
    SUBASSET_MODE_TAKEOFF_PREPARE: _ClassVar[SubAssetMode]
    SUBASSET_MODE_TAKEOFF_FINISHED: _ClassVar[SubAssetMode]
    SUBASSET_MODE_MANUAL: _ClassVar[SubAssetMode]
    SUBASSET_MODE_TAKEOFF_AUTO: _ClassVar[SubAssetMode]
    SUBASSET_MODE_WAYLINE: _ClassVar[SubAssetMode]
    SUBASSET_MODE_PANORAMIC_SHOT: _ClassVar[SubAssetMode]
    SUBASSET_MODE_ACTIVE_TRACK: _ClassVar[SubAssetMode]
    SUBASSET_MODE_ADS_B_AVOIDANCE: _ClassVar[SubAssetMode]
    SUBASSET_MODE_RETURN_AUTO: _ClassVar[SubAssetMode]
    SUBASSET_MODE_LANDING_AUTO: _ClassVar[SubAssetMode]
    SUBASSET_MODE_LANDING_FORCE: _ClassVar[SubAssetMode]
    SUBASSET_MODE_LANDING_THREE_PROPELLER: _ClassVar[SubAssetMode]
    SUBASSET_MODE_UPGRADING: _ClassVar[SubAssetMode]
    SUBASSET_MODE_DISCONNECTED: _ClassVar[SubAssetMode]
    SUBASSET_MODE_APAS: _ClassVar[SubAssetMode]
    SUBASSET_MODE_VIRTUAL_JOYSTICK: _ClassVar[SubAssetMode]
    SUBASSET_MODE_LIVE_FLIGHT_CONTROLS: _ClassVar[SubAssetMode]
    SUBASSET_MODE_AERIAL_RTK_FIXED: _ClassVar[SubAssetMode]
    SUBASSET_MODE_DOCK_SITE_EVALUATION: _ClassVar[SubAssetMode]
    SUBASSET_MODE_POI: _ClassVar[SubAssetMode]

class AssetTypeEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ASSET_TYPE_UNKNOWN: _ClassVar[AssetTypeEnum]
    ASSET_TYPE_AIRCRAFT: _ClassVar[AssetTypeEnum]
    ASSET_TYPE_DOCK: _ClassVar[AssetTypeEnum]
    ASSET_TYPE_SENSOR: _ClassVar[AssetTypeEnum]
    ASSET_TYPE_CAMERA: _ClassVar[AssetTypeEnum]
    ASSET_TYPE_OTHER: _ClassVar[AssetTypeEnum]
    ASSET_TYPE_JAMMER: _ClassVar[AssetTypeEnum]
    ASSET_TYPE_CYBER_ATTACK: _ClassVar[AssetTypeEnum]
    ASSET_TYPE_SAPIENT: _ClassVar[AssetTypeEnum]
    ASSET_TYPE_RNS: _ClassVar[AssetTypeEnum]

class AssetVendor(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ASSET_VENDOR_DJI: _ClassVar[AssetVendor]
    ASSET_VENDOR_AUTEL: _ClassVar[AssetVendor]
    ASSET_VENDOR_ROS: _ClassVar[AssetVendor]
    ASSET_VENDOR_MAVLINK: _ClassVar[AssetVendor]
    ASSET_VENDOR_RTMP_RTSP: _ClassVar[AssetVendor]
    ASSET_VENDOR_SAPIENT: _ClassVar[AssetVendor]
    ASSET_VENDOR_BETAFLIGHT: _ClassVar[AssetVendor]
    ASSET_VENDOR_RNS: _ClassVar[AssetVendor]
    ASSET_VENDOR_ZQNT: _ClassVar[AssetVendor]
    ASSET_VENDOR_SIMULATOR: _ClassVar[AssetVendor]

class AssetConnection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MQTT: _ClassVar[AssetConnection]
    TCP: _ClassVar[AssetConnection]
    SERIAL: _ClassVar[AssetConnection]

class LiveStreamTypeEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LIVE_STREAM_TYPE_UNKNOWN: _ClassVar[LiveStreamTypeEnum]
    LIVE_STREAM_TYPE_RTMP: _ClassVar[LiveStreamTypeEnum]
    LIVE_STREAM_TYPE_RTSP: _ClassVar[LiveStreamTypeEnum]
    LIVE_STREAM_TYPE_WEBRTC: _ClassVar[LiveStreamTypeEnum]
MANUAL_CONTROL_STATE_DISCONNECTED: ManualControlStateEnum
MANUAL_CONTROL_STATE_CONNECTING: ManualControlStateEnum
MANUAL_CONTROL_STATE_CONNECTED: ManualControlStateEnum
RAINFALL_NO: RainfallEnum
RAINFALL_LIGHT: RainfallEnum
RAINFALL_MODERATE: RainfallEnum
RAINFALL_HEAVY: RainfallEnum
NETWORK_TYPE_4_G: NetworkTypeEnum
NETWORK_TYPE_ETHERNET: NetworkTypeEnum
COVER_STATE_CLOSED: AssetCoverStateEnum
COVER_STATE_OPENED: AssetCoverStateEnum
COVER_STATE_HALF_OPEN: AssetCoverStateEnum
COVER_STATE_ABNORMAL: AssetCoverStateEnum
NETWORK_STATE_QUALITY_NO_SIGNAL: NetworkStateQualityEnum
NETWORK_STATE_QUALITY_BAD: NetworkStateQualityEnum
NETWORK_STATE_QUALITY_POOR: NetworkStateQualityEnum
NETWORK_STATE_QUALITY_FAIR: NetworkStateQualityEnum
NETWORK_STATE_QUALITY_GOOD: NetworkStateQualityEnum
NETWORK_STATE_QUALITY_EXCELLENT: NetworkStateQualityEnum
AIR_CONDITIONER_IDLE: AssetAirConditionerStateEnum
AIR_CONDITIONER_COOL: AssetAirConditionerStateEnum
AIR_CONDITIONER_HEAT: AssetAirConditionerStateEnum
AIR_CONDITIONER_DEHUMIDIFICATION: AssetAirConditionerStateEnum
AIR_CONDITIONER_COOLING_EXIT: AssetAirConditionerStateEnum
AIR_CONDITIONER_HEATING_EXIT: AssetAirConditionerStateEnum
AIR_CONDITIONER_DEHUMIDIFICATION_EXIT: AssetAirConditionerStateEnum
AIR_CONDITIONER_COOLING_READY: AssetAirConditionerStateEnum
AIR_CONDITIONER_HEATING_READY: AssetAirConditionerStateEnum
AIR_CONDITIONER_DEHUMIDIFICATION_READY: AssetAirConditionerStateEnum
AIR_CONDITIONER_PREPARING_FOR_AIR_COOLING: AssetAirConditionerStateEnum
AIR_CONDITIONER_AIR_COOLING_IN_PROGRESS: AssetAirConditionerStateEnum
AIR_CONDITIONER_AIR_COOLING_EXITING: AssetAirConditionerStateEnum
AIR_CONDITIONER_PREPARING_FOR_DEFOGGER: AssetAirConditionerStateEnum
AIR_CONDITIONER_DEFOGGER_IN_PROGRESS: AssetAirConditionerStateEnum
AIR_CONDITIONER_DEFOGGER_EXITING: AssetAirConditionerStateEnum
ASSET_MODE_IDLE: AssetMode
ASSET_MODE_DEBUGGING: AssetMode
ASSET_MODE_REMOTE_DEBUGGING: AssetMode
ASSET_MODE_UPGRADING: AssetMode
ASSET_MODE_WORKING: AssetMode
ASSET_MODE_TO_BE_CALIBRATED: AssetMode
ASSET_MODE_OFFLINE: AssetMode
SUBASSET_MODE_IDLE: SubAssetMode
SUBASSET_MODE_TAKEOFF_PREPARE: SubAssetMode
SUBASSET_MODE_TAKEOFF_FINISHED: SubAssetMode
SUBASSET_MODE_MANUAL: SubAssetMode
SUBASSET_MODE_TAKEOFF_AUTO: SubAssetMode
SUBASSET_MODE_WAYLINE: SubAssetMode
SUBASSET_MODE_PANORAMIC_SHOT: SubAssetMode
SUBASSET_MODE_ACTIVE_TRACK: SubAssetMode
SUBASSET_MODE_ADS_B_AVOIDANCE: SubAssetMode
SUBASSET_MODE_RETURN_AUTO: SubAssetMode
SUBASSET_MODE_LANDING_AUTO: SubAssetMode
SUBASSET_MODE_LANDING_FORCE: SubAssetMode
SUBASSET_MODE_LANDING_THREE_PROPELLER: SubAssetMode
SUBASSET_MODE_UPGRADING: SubAssetMode
SUBASSET_MODE_DISCONNECTED: SubAssetMode
SUBASSET_MODE_APAS: SubAssetMode
SUBASSET_MODE_VIRTUAL_JOYSTICK: SubAssetMode
SUBASSET_MODE_LIVE_FLIGHT_CONTROLS: SubAssetMode
SUBASSET_MODE_AERIAL_RTK_FIXED: SubAssetMode
SUBASSET_MODE_DOCK_SITE_EVALUATION: SubAssetMode
SUBASSET_MODE_POI: SubAssetMode
ASSET_TYPE_UNKNOWN: AssetTypeEnum
ASSET_TYPE_AIRCRAFT: AssetTypeEnum
ASSET_TYPE_DOCK: AssetTypeEnum
ASSET_TYPE_SENSOR: AssetTypeEnum
ASSET_TYPE_CAMERA: AssetTypeEnum
ASSET_TYPE_OTHER: AssetTypeEnum
ASSET_TYPE_JAMMER: AssetTypeEnum
ASSET_TYPE_CYBER_ATTACK: AssetTypeEnum
ASSET_TYPE_SAPIENT: AssetTypeEnum
ASSET_TYPE_RNS: AssetTypeEnum
ASSET_VENDOR_DJI: AssetVendor
ASSET_VENDOR_AUTEL: AssetVendor
ASSET_VENDOR_ROS: AssetVendor
ASSET_VENDOR_MAVLINK: AssetVendor
ASSET_VENDOR_RTMP_RTSP: AssetVendor
ASSET_VENDOR_SAPIENT: AssetVendor
ASSET_VENDOR_BETAFLIGHT: AssetVendor
ASSET_VENDOR_RNS: AssetVendor
ASSET_VENDOR_ZQNT: AssetVendor
ASSET_VENDOR_SIMULATOR: AssetVendor
MQTT: AssetConnection
TCP: AssetConnection
SERIAL: AssetConnection
LIVE_STREAM_TYPE_UNKNOWN: LiveStreamTypeEnum
LIVE_STREAM_TYPE_RTMP: LiveStreamTypeEnum
LIVE_STREAM_TYPE_RTSP: LiveStreamTypeEnum
LIVE_STREAM_TYPE_WEBRTC: LiveStreamTypeEnum

class AssetProtoDTO(_message.Message):
    __slots__ = ("id", "sn", "name", "type", "vendor", "connection", "system_connection_string", "model", "external_device_type", "external_device_sub_type", "organization", "external_id", "payloads", "sub_assets", "created_at", "modified_at", "modified_from", "live_stream_push_url", "live_stream_pull_url", "theatre_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    SN_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VENDOR_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_CONNECTION_STRING_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_DEVICE_SUB_TYPE_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    PAYLOADS_FIELD_NUMBER: _ClassVar[int]
    SUB_ASSETS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_FROM_FIELD_NUMBER: _ClassVar[int]
    LIVE_STREAM_PUSH_URL_FIELD_NUMBER: _ClassVar[int]
    LIVE_STREAM_PULL_URL_FIELD_NUMBER: _ClassVar[int]
    THEATRE_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    sn: str
    name: str
    type: AssetTypeEnum
    vendor: AssetVendor
    connection: AssetConnection
    system_connection_string: str
    model: str
    external_device_type: str
    external_device_sub_type: str
    organization: str
    external_id: str
    payloads: _containers.RepeatedCompositeFieldContainer[AssetPayloadProtoDTO]
    sub_assets: _containers.RepeatedCompositeFieldContainer[SubAssetProtoDTO]
    created_at: _timestamp_pb2.Timestamp
    modified_at: _timestamp_pb2.Timestamp
    modified_from: str
    live_stream_push_url: str
    live_stream_pull_url: str
    theatre_id: str
    def __init__(self, id: _Optional[str] = ..., sn: _Optional[str] = ..., name: _Optional[str] = ..., type: _Optional[_Union[AssetTypeEnum, str]] = ..., vendor: _Optional[_Union[AssetVendor, str]] = ..., connection: _Optional[_Union[AssetConnection, str]] = ..., system_connection_string: _Optional[str] = ..., model: _Optional[str] = ..., external_device_type: _Optional[str] = ..., external_device_sub_type: _Optional[str] = ..., organization: _Optional[str] = ..., external_id: _Optional[str] = ..., payloads: _Optional[_Iterable[_Union[AssetPayloadProtoDTO, _Mapping]]] = ..., sub_assets: _Optional[_Iterable[_Union[SubAssetProtoDTO, _Mapping]]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., modified_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., modified_from: _Optional[str] = ..., live_stream_push_url: _Optional[str] = ..., live_stream_pull_url: _Optional[str] = ..., theatre_id: _Optional[str] = ...) -> None: ...

class AssetPropertyProtoDTO(_message.Message):
    __slots__ = ("key", "value", "description", "created_at", "modified_at")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: _struct_pb2.Value
    description: str
    created_at: _timestamp_pb2.Timestamp
    modified_at: _timestamp_pb2.Timestamp
    def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ..., description: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., modified_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SubAssetProtoDTO(_message.Message):
    __slots__ = ("id", "sn", "name", "type", "vendor", "connection", "system_connection_string", "model", "external_device_type", "external_device_sub_type", "external_id", "stream_url_predefined", "payloads", "created_at", "modified_at", "modified_from", "live_stream_push_url", "live_stream_pull_url")
    ID_FIELD_NUMBER: _ClassVar[int]
    SN_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VENDOR_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_CONNECTION_STRING_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_DEVICE_SUB_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    STREAM_URL_PREDEFINED_FIELD_NUMBER: _ClassVar[int]
    PAYLOADS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_FROM_FIELD_NUMBER: _ClassVar[int]
    LIVE_STREAM_PUSH_URL_FIELD_NUMBER: _ClassVar[int]
    LIVE_STREAM_PULL_URL_FIELD_NUMBER: _ClassVar[int]
    id: str
    sn: str
    name: str
    type: AssetTypeEnum
    vendor: AssetVendor
    connection: AssetConnection
    system_connection_string: str
    model: str
    external_device_type: str
    external_device_sub_type: str
    external_id: str
    stream_url_predefined: bool
    payloads: _containers.RepeatedCompositeFieldContainer[AssetPayloadProtoDTO]
    created_at: _timestamp_pb2.Timestamp
    modified_at: _timestamp_pb2.Timestamp
    modified_from: str
    live_stream_push_url: str
    live_stream_pull_url: str
    def __init__(self, id: _Optional[str] = ..., sn: _Optional[str] = ..., name: _Optional[str] = ..., type: _Optional[_Union[AssetTypeEnum, str]] = ..., vendor: _Optional[_Union[AssetVendor, str]] = ..., connection: _Optional[_Union[AssetConnection, str]] = ..., system_connection_string: _Optional[str] = ..., model: _Optional[str] = ..., external_device_type: _Optional[str] = ..., external_device_sub_type: _Optional[str] = ..., external_id: _Optional[str] = ..., stream_url_predefined: bool = ..., payloads: _Optional[_Iterable[_Union[AssetPayloadProtoDTO, _Mapping]]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., modified_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., modified_from: _Optional[str] = ..., live_stream_push_url: _Optional[str] = ..., live_stream_pull_url: _Optional[str] = ...) -> None: ...

class AssetPayloadProtoDTO(_message.Message):
    __slots__ = ("id", "external_id", "external_type", "slot_index", "name", "serial_number", "kind", "vendor", "model", "firmware_version", "library_version", "state_json", "active", "last_seen_at", "created_at", "modified_at", "modified_from", "payload_ref")
    ID_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_TYPE_FIELD_NUMBER: _ClassVar[int]
    SLOT_INDEX_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    VENDOR_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    LIBRARY_VERSION_FIELD_NUMBER: _ClassVar[int]
    STATE_JSON_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    LAST_SEEN_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_FROM_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_REF_FIELD_NUMBER: _ClassVar[int]
    id: str
    external_id: str
    external_type: str
    slot_index: int
    name: str
    serial_number: str
    kind: str
    vendor: str
    model: str
    firmware_version: str
    library_version: str
    state_json: str
    active: bool
    last_seen_at: _timestamp_pb2.Timestamp
    created_at: _timestamp_pb2.Timestamp
    modified_at: _timestamp_pb2.Timestamp
    modified_from: str
    payload_ref: str
    def __init__(self, id: _Optional[str] = ..., external_id: _Optional[str] = ..., external_type: _Optional[str] = ..., slot_index: _Optional[int] = ..., name: _Optional[str] = ..., serial_number: _Optional[str] = ..., kind: _Optional[str] = ..., vendor: _Optional[str] = ..., model: _Optional[str] = ..., firmware_version: _Optional[str] = ..., library_version: _Optional[str] = ..., state_json: _Optional[str] = ..., active: bool = ..., last_seen_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., modified_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., modified_from: _Optional[str] = ..., payload_ref: _Optional[str] = ...) -> None: ...

class OrganizationProtoDTO(_message.Message):
    __slots__ = ("id", "name", "description", "assets", "created_at", "modified_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ASSETS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    assets: _containers.RepeatedScalarFieldContainer[str]
    created_at: _timestamp_pb2.Timestamp
    modified_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., assets: _Optional[_Iterable[str]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., modified_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
