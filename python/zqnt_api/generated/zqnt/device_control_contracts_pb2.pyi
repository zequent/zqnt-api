import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from . import base_pb2 as _base_pb2
from . import asset_pb2 as _asset_pb2
from . import detection_pb2 as _detection_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LiveDataServiceCommand(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LIVE_DATA_COMMAND_START_TELEMETRY_STREAM: _ClassVar[LiveDataServiceCommand]
    LIVE_DATA_COMMAND_GET_TELEMETRY_DATA: _ClassVar[LiveDataServiceCommand]
    LIVE_DATA_COMMAND_STOP_TELEMETRY_STREAM: _ClassVar[LiveDataServiceCommand]
    LIVE_DATA_COMMAND_START_LIVE_STREAM: _ClassVar[LiveDataServiceCommand]
    LIVE_DATA_COMMAND_STOP_LIVE_STREAM: _ClassVar[LiveDataServiceCommand]

class CapabilityState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CAPABILITY_STATE_UNSPECIFIED: _ClassVar[CapabilityState]
    CAPABILITY_STATE_AVAILABLE: _ClassVar[CapabilityState]
    CAPABILITY_STATE_TEMPORARILY_UNAVAILABLE: _ClassVar[CapabilityState]
    CAPABILITY_STATE_UNSUPPORTED: _ClassVar[CapabilityState]
    CAPABILITY_STATE_REQUIRES_AUTHORIZATION: _ClassVar[CapabilityState]

class CapabilitySnapshotState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CAPABILITY_SNAPSHOT_STATE_UNSPECIFIED: _ClassVar[CapabilitySnapshotState]
    CAPABILITY_SNAPSHOT_STATE_CURRENT: _ClassVar[CapabilitySnapshotState]
    CAPABILITY_SNAPSHOT_STATE_STALE: _ClassVar[CapabilitySnapshotState]
    CAPABILITY_SNAPSHOT_STATE_NO_DATA: _ClassVar[CapabilitySnapshotState]

class CapabilityTargetType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CAPABILITY_TARGET_TYPE_UNSPECIFIED: _ClassVar[CapabilityTargetType]
    CAPABILITY_TARGET_TYPE_ASSET: _ClassVar[CapabilityTargetType]
    CAPABILITY_TARGET_TYPE_SUB_ASSET: _ClassVar[CapabilityTargetType]
    CAPABILITY_TARGET_TYPE_PAYLOAD: _ClassVar[CapabilityTargetType]
    CAPABILITY_TARGET_TYPE_COMPONENT: _ClassVar[CapabilityTargetType]

class CapabilitySourceProto(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CAPABILITY_SOURCE_UNSPECIFIED: _ClassVar[CapabilitySourceProto]
    CAPABILITY_SOURCE_BUILT_IN: _ClassVar[CapabilitySourceProto]
    CAPABILITY_SOURCE_EDGE_ADAPTER: _ClassVar[CapabilitySourceProto]
    CAPABILITY_SOURCE_RUNTIME: _ClassVar[CapabilitySourceProto]
    CAPABILITY_SOURCE_USER: _ClassVar[CapabilitySourceProto]
    CAPABILITY_SOURCE_APPLICATION: _ClassVar[CapabilitySourceProto]
    CAPABILITY_SOURCE_INTEGRATION: _ClassVar[CapabilitySourceProto]
    CAPABILITY_SOURCE_AI_GENERATED: _ClassVar[CapabilitySourceProto]
LIVE_DATA_COMMAND_START_TELEMETRY_STREAM: LiveDataServiceCommand
LIVE_DATA_COMMAND_GET_TELEMETRY_DATA: LiveDataServiceCommand
LIVE_DATA_COMMAND_STOP_TELEMETRY_STREAM: LiveDataServiceCommand
LIVE_DATA_COMMAND_START_LIVE_STREAM: LiveDataServiceCommand
LIVE_DATA_COMMAND_STOP_LIVE_STREAM: LiveDataServiceCommand
CAPABILITY_STATE_UNSPECIFIED: CapabilityState
CAPABILITY_STATE_AVAILABLE: CapabilityState
CAPABILITY_STATE_TEMPORARILY_UNAVAILABLE: CapabilityState
CAPABILITY_STATE_UNSUPPORTED: CapabilityState
CAPABILITY_STATE_REQUIRES_AUTHORIZATION: CapabilityState
CAPABILITY_SNAPSHOT_STATE_UNSPECIFIED: CapabilitySnapshotState
CAPABILITY_SNAPSHOT_STATE_CURRENT: CapabilitySnapshotState
CAPABILITY_SNAPSHOT_STATE_STALE: CapabilitySnapshotState
CAPABILITY_SNAPSHOT_STATE_NO_DATA: CapabilitySnapshotState
CAPABILITY_TARGET_TYPE_UNSPECIFIED: CapabilityTargetType
CAPABILITY_TARGET_TYPE_ASSET: CapabilityTargetType
CAPABILITY_TARGET_TYPE_SUB_ASSET: CapabilityTargetType
CAPABILITY_TARGET_TYPE_PAYLOAD: CapabilityTargetType
CAPABILITY_TARGET_TYPE_COMPONENT: CapabilityTargetType
CAPABILITY_SOURCE_UNSPECIFIED: CapabilitySourceProto
CAPABILITY_SOURCE_BUILT_IN: CapabilitySourceProto
CAPABILITY_SOURCE_EDGE_ADAPTER: CapabilitySourceProto
CAPABILITY_SOURCE_RUNTIME: CapabilitySourceProto
CAPABILITY_SOURCE_USER: CapabilitySourceProto
CAPABILITY_SOURCE_APPLICATION: CapabilitySourceProto
CAPABILITY_SOURCE_INTEGRATION: CapabilitySourceProto
CAPABILITY_SOURCE_AI_GENERATED: CapabilitySourceProto

class CommandResponse(_message.Message):
    __slots__ = ("has_errors", "meta", "empty", "error", "progress", "live_stream_start_response")
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    EMPTY_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    LIVE_STREAM_START_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    has_errors: bool
    meta: _base_pb2.ResponseMeta
    empty: _empty_pb2.Empty
    error: _base_pb2.GlobalErrorMessage
    progress: _base_pb2.CommandProgress
    live_stream_start_response: LiveStreamStartResponse
    def __init__(self, has_errors: bool = ..., meta: _Optional[_Union[_base_pb2.ResponseMeta, _Mapping]] = ..., empty: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ..., progress: _Optional[_Union[_base_pb2.CommandProgress, _Mapping]] = ..., live_stream_start_response: _Optional[_Union[LiveStreamStartResponse, _Mapping]] = ...) -> None: ...

class CustomCommandRequest(_message.Message):
    __slots__ = ("base", "command_id", "params", "target")
    BASE_FIELD_NUMBER: _ClassVar[int]
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    command_id: str
    params: _struct_pb2.Struct
    target: CapabilityTarget
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., command_id: _Optional[str] = ..., params: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., target: _Optional[_Union[CapabilityTarget, _Mapping]] = ...) -> None: ...

class CustomCommandResponse(_message.Message):
    __slots__ = ("has_errors", "meta", "command_id", "result", "empty", "error", "progress")
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    EMPTY_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    has_errors: bool
    meta: _base_pb2.ResponseMeta
    command_id: str
    result: _struct_pb2.Struct
    empty: _empty_pb2.Empty
    error: _base_pb2.GlobalErrorMessage
    progress: _base_pb2.CommandProgress
    def __init__(self, has_errors: bool = ..., meta: _Optional[_Union[_base_pb2.ResponseMeta, _Mapping]] = ..., command_id: _Optional[str] = ..., result: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., empty: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ..., progress: _Optional[_Union[_base_pb2.CommandProgress, _Mapping]] = ...) -> None: ...

class CapabilityTarget(_message.Message):
    __slots__ = ("type", "target_ref")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TARGET_REF_FIELD_NUMBER: _ClassVar[int]
    type: CapabilityTargetType
    target_ref: str
    def __init__(self, type: _Optional[_Union[CapabilityTargetType, str]] = ..., target_ref: _Optional[str] = ...) -> None: ...

class CapabilityErrorProto(_message.Message):
    __slots__ = ("code", "description")
    CODE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    code: str
    description: str
    def __init__(self, code: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class CapabilityEventProto(_message.Message):
    __slots__ = ("name", "description", "payload_schema")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    payload_schema: _struct_pb2.Struct
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., payload_schema: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class CapabilityRequirementsProto(_message.Message):
    __slots__ = ("asset_types", "payloads", "runtime_features", "properties")
    ASSET_TYPES_FIELD_NUMBER: _ClassVar[int]
    PAYLOADS_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_FEATURES_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    asset_types: _containers.RepeatedScalarFieldContainer[str]
    payloads: _containers.RepeatedScalarFieldContainer[str]
    runtime_features: _containers.RepeatedScalarFieldContainer[str]
    properties: _struct_pb2.Struct
    def __init__(self, asset_types: _Optional[_Iterable[str]] = ..., payloads: _Optional[_Iterable[str]] = ..., runtime_features: _Optional[_Iterable[str]] = ..., properties: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class Capability(_message.Message):
    __slots__ = ("command_id", "display_name", "unavailable_reason", "metadata", "state", "constraints", "description", "input_schema", "output_schema", "target", "schema_version", "errors", "events", "requirements", "skill_id", "source", "provider")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    UNAVAILABLE_REASON_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    INPUT_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_VERSION_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    REQUIREMENTS_FIELD_NUMBER: _ClassVar[int]
    SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    command_id: str
    display_name: str
    unavailable_reason: str
    metadata: _containers.ScalarMap[str, str]
    state: CapabilityState
    constraints: _struct_pb2.Struct
    description: str
    input_schema: _struct_pb2.Struct
    output_schema: _struct_pb2.Struct
    target: CapabilityTarget
    schema_version: str
    errors: _containers.RepeatedCompositeFieldContainer[CapabilityErrorProto]
    events: _containers.RepeatedCompositeFieldContainer[CapabilityEventProto]
    requirements: CapabilityRequirementsProto
    skill_id: str
    source: CapabilitySourceProto
    provider: str
    def __init__(self, command_id: _Optional[str] = ..., display_name: _Optional[str] = ..., unavailable_reason: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., state: _Optional[_Union[CapabilityState, str]] = ..., constraints: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., description: _Optional[str] = ..., input_schema: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., output_schema: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., target: _Optional[_Union[CapabilityTarget, _Mapping]] = ..., schema_version: _Optional[str] = ..., errors: _Optional[_Iterable[_Union[CapabilityErrorProto, _Mapping]]] = ..., events: _Optional[_Iterable[_Union[CapabilityEventProto, _Mapping]]] = ..., requirements: _Optional[_Union[CapabilityRequirementsProto, _Mapping]] = ..., skill_id: _Optional[str] = ..., source: _Optional[_Union[CapabilitySourceProto, str]] = ..., provider: _Optional[str] = ...) -> None: ...

class AssetCapabilities(_message.Message):
    __slots__ = ("asset_sn", "asset_type", "capabilities", "timestamp", "valid_until", "revision", "snapshot_state")
    ASSET_SN_FIELD_NUMBER: _ClassVar[int]
    ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    VALID_UNTIL_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_STATE_FIELD_NUMBER: _ClassVar[int]
    asset_sn: str
    asset_type: str
    capabilities: _containers.RepeatedCompositeFieldContainer[Capability]
    timestamp: _timestamp_pb2.Timestamp
    valid_until: _timestamp_pb2.Timestamp
    revision: str
    snapshot_state: CapabilitySnapshotState
    def __init__(self, asset_sn: _Optional[str] = ..., asset_type: _Optional[str] = ..., capabilities: _Optional[_Iterable[_Union[Capability, _Mapping]]] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., valid_until: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., revision: _Optional[str] = ..., snapshot_state: _Optional[_Union[CapabilitySnapshotState, str]] = ...) -> None: ...

class AssetCapabilitiesRequest(_message.Message):
    __slots__ = ("sn", "asset_id", "base", "target")
    SN_FIELD_NUMBER: _ClassVar[int]
    ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    BASE_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    sn: str
    asset_id: str
    base: _base_pb2.RequestBase
    target: CapabilityTarget
    def __init__(self, sn: _Optional[str] = ..., asset_id: _Optional[str] = ..., base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., target: _Optional[_Union[CapabilityTarget, _Mapping]] = ...) -> None: ...

class DetectedPayload(_message.Message):
    __slots__ = ("payload_ref", "external_id", "serial_number", "slot_index", "kind", "vendor", "model", "firmware_version", "library_version", "state")
    PAYLOAD_REF_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    SLOT_INDEX_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    VENDOR_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    LIBRARY_VERSION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    payload_ref: str
    external_id: str
    serial_number: str
    slot_index: int
    kind: str
    vendor: str
    model: str
    firmware_version: str
    library_version: str
    state: _struct_pb2.Struct
    def __init__(self, payload_ref: _Optional[str] = ..., external_id: _Optional[str] = ..., serial_number: _Optional[str] = ..., slot_index: _Optional[int] = ..., kind: _Optional[str] = ..., vendor: _Optional[str] = ..., model: _Optional[str] = ..., firmware_version: _Optional[str] = ..., library_version: _Optional[str] = ..., state: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class ReportAssetRuntimeRequest(_message.Message):
    __slots__ = ("base", "asset_sn", "revision", "observed_at", "payloads", "capabilities")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ASSET_SN_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    OBSERVED_AT_FIELD_NUMBER: _ClassVar[int]
    PAYLOADS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    asset_sn: str
    revision: str
    observed_at: _timestamp_pb2.Timestamp
    payloads: _containers.RepeatedCompositeFieldContainer[DetectedPayload]
    capabilities: _containers.RepeatedCompositeFieldContainer[Capability]
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., asset_sn: _Optional[str] = ..., revision: _Optional[str] = ..., observed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., payloads: _Optional[_Iterable[_Union[DetectedPayload, _Mapping]]] = ..., capabilities: _Optional[_Iterable[_Union[Capability, _Mapping]]] = ...) -> None: ...

class ReportAssetRuntimeResponse(_message.Message):
    __slots__ = ("has_errors", "meta", "empty", "error", "accepted_revision")
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    EMPTY_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_REVISION_FIELD_NUMBER: _ClassVar[int]
    has_errors: bool
    meta: _base_pb2.ResponseMeta
    empty: _empty_pb2.Empty
    error: _base_pb2.GlobalErrorMessage
    accepted_revision: str
    def __init__(self, has_errors: bool = ..., meta: _Optional[_Union[_base_pb2.ResponseMeta, _Mapping]] = ..., empty: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ..., accepted_revision: _Optional[str] = ...) -> None: ...

class AssetCapabilitiesResponse(_message.Message):
    __slots__ = ("capabilities", "error")
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    capabilities: AssetCapabilities
    error: _base_pb2.GlobalErrorMessage
    def __init__(self, capabilities: _Optional[_Union[AssetCapabilities, _Mapping]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ...) -> None: ...

class GetAssetRuntimeRequest(_message.Message):
    __slots__ = ("base", "asset_sn", "asset_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ASSET_SN_FIELD_NUMBER: _ClassVar[int]
    ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    asset_sn: str
    asset_id: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., asset_sn: _Optional[str] = ..., asset_id: _Optional[str] = ...) -> None: ...

class AssetRuntimeSnapshot(_message.Message):
    __slots__ = ("asset_sn", "payloads", "capabilities", "revision", "snapshot_state", "observed_at", "valid_until")
    ASSET_SN_FIELD_NUMBER: _ClassVar[int]
    PAYLOADS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_STATE_FIELD_NUMBER: _ClassVar[int]
    OBSERVED_AT_FIELD_NUMBER: _ClassVar[int]
    VALID_UNTIL_FIELD_NUMBER: _ClassVar[int]
    asset_sn: str
    payloads: _containers.RepeatedCompositeFieldContainer[DetectedPayload]
    capabilities: _containers.RepeatedCompositeFieldContainer[Capability]
    revision: str
    snapshot_state: CapabilitySnapshotState
    observed_at: _timestamp_pb2.Timestamp
    valid_until: _timestamp_pb2.Timestamp
    def __init__(self, asset_sn: _Optional[str] = ..., payloads: _Optional[_Iterable[_Union[DetectedPayload, _Mapping]]] = ..., capabilities: _Optional[_Iterable[_Union[Capability, _Mapping]]] = ..., revision: _Optional[str] = ..., snapshot_state: _Optional[_Union[CapabilitySnapshotState, str]] = ..., observed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., valid_until: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class AssetRuntimeResponse(_message.Message):
    __slots__ = ("has_errors", "meta", "runtime", "error")
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    has_errors: bool
    meta: _base_pb2.ResponseMeta
    runtime: AssetRuntimeSnapshot
    error: _base_pb2.GlobalErrorMessage
    def __init__(self, has_errors: bool = ..., meta: _Optional[_Union[_base_pb2.ResponseMeta, _Mapping]] = ..., runtime: _Optional[_Union[AssetRuntimeSnapshot, _Mapping]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ...) -> None: ...

class GeoCoordinate(_message.Message):
    __slots__ = ("latitude", "longitude", "altitude")
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    latitude: float
    longitude: float
    altitude: float
    def __init__(self, latitude: _Optional[float] = ..., longitude: _Optional[float] = ..., altitude: _Optional[float] = ...) -> None: ...

class ReturnToHomeRequest(_message.Message):
    __slots__ = ("altitude",)
    ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    altitude: float
    def __init__(self, altitude: _Optional[float] = ...) -> None: ...

class ManualControlRequest(_message.Message):
    __slots__ = ("client_id", "user_id", "reason", "session_id")
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    user_id: str
    reason: str
    session_id: str
    def __init__(self, client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., reason: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class ManualControlInput(_message.Message):
    __slots__ = ("roll", "pitch", "yaw", "throttle", "gimbal_pitch")
    ROLL_FIELD_NUMBER: _ClassVar[int]
    PITCH_FIELD_NUMBER: _ClassVar[int]
    YAW_FIELD_NUMBER: _ClassVar[int]
    THROTTLE_FIELD_NUMBER: _ClassVar[int]
    GIMBAL_PITCH_FIELD_NUMBER: _ClassVar[int]
    roll: float
    pitch: float
    yaw: float
    throttle: float
    gimbal_pitch: float
    def __init__(self, roll: _Optional[float] = ..., pitch: _Optional[float] = ..., yaw: _Optional[float] = ..., throttle: _Optional[float] = ..., gimbal_pitch: _Optional[float] = ...) -> None: ...

class LiveStreamState(_message.Message):
    __slots__ = ("video_id", "stream_url", "is_live", "started_at", "asset_type")
    VIDEO_ID_FIELD_NUMBER: _ClassVar[int]
    STREAM_URL_FIELD_NUMBER: _ClassVar[int]
    IS_LIVE_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    video_id: str
    stream_url: str
    is_live: bool
    started_at: _timestamp_pb2.Timestamp
    asset_type: _asset_pb2.AssetTypeEnum
    def __init__(self, video_id: _Optional[str] = ..., stream_url: _Optional[str] = ..., is_live: bool = ..., started_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., asset_type: _Optional[_Union[_asset_pb2.AssetTypeEnum, str]] = ...) -> None: ...

class LiveStreamStartResponse(_message.Message):
    __slots__ = ("stream_url", "video_id")
    STREAM_URL_FIELD_NUMBER: _ClassVar[int]
    VIDEO_ID_FIELD_NUMBER: _ClassVar[int]
    stream_url: str
    video_id: str
    def __init__(self, stream_url: _Optional[str] = ..., video_id: _Optional[str] = ...) -> None: ...

class ChangeCameraLensRequest(_message.Message):
    __slots__ = ("lens",)
    LENS_FIELD_NUMBER: _ClassVar[int]
    lens: str
    def __init__(self, lens: _Optional[str] = ...) -> None: ...

class ChangeCameraZoomRequest(_message.Message):
    __slots__ = ("lens", "zoom")
    LENS_FIELD_NUMBER: _ClassVar[int]
    ZOOM_FIELD_NUMBER: _ClassVar[int]
    lens: str
    zoom: int
    def __init__(self, lens: _Optional[str] = ..., zoom: _Optional[int] = ...) -> None: ...

class ManualControlState(_message.Message):
    __slots__ = ("state", "sn", "asset_id", "active", "client_id", "user_id", "session_id")
    STATE_FIELD_NUMBER: _ClassVar[int]
    SN_FIELD_NUMBER: _ClassVar[int]
    ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    state: _asset_pb2.ManualControlStateEnum
    sn: str
    asset_id: str
    active: bool
    client_id: str
    user_id: str
    session_id: str
    def __init__(self, state: _Optional[_Union[_asset_pb2.ManualControlStateEnum, str]] = ..., sn: _Optional[str] = ..., asset_id: _Optional[str] = ..., active: bool = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class EmptyCommandRequest(_message.Message):
    __slots__ = ("base",)
    BASE_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ...) -> None: ...

class CoordinateCommandRequest(_message.Message):
    __slots__ = ("base", "coordinate", "no_fly_zone_override")
    BASE_FIELD_NUMBER: _ClassVar[int]
    COORDINATE_FIELD_NUMBER: _ClassVar[int]
    NO_FLY_ZONE_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    coordinate: GeoCoordinate
    no_fly_zone_override: bool
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., coordinate: _Optional[_Union[GeoCoordinate, _Mapping]] = ..., no_fly_zone_override: bool = ...) -> None: ...

class LookAtCommandRequest(_message.Message):
    __slots__ = ("base", "coordinate", "payload_index", "locked")
    BASE_FIELD_NUMBER: _ClassVar[int]
    COORDINATE_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_INDEX_FIELD_NUMBER: _ClassVar[int]
    LOCKED_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    coordinate: GeoCoordinate
    payload_index: str
    locked: bool
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., coordinate: _Optional[_Union[GeoCoordinate, _Mapping]] = ..., payload_index: _Optional[str] = ..., locked: bool = ...) -> None: ...

class ReturnToHomeCommandRequest(_message.Message):
    __slots__ = ("base", "request")
    BASE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    request: ReturnToHomeRequest
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., request: _Optional[_Union[ReturnToHomeRequest, _Mapping]] = ...) -> None: ...

class ManualControlCommandRequest(_message.Message):
    __slots__ = ("base", "request")
    BASE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    request: ManualControlRequest
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., request: _Optional[_Union[ManualControlRequest, _Mapping]] = ...) -> None: ...

class ManualControlInputCommandRequest(_message.Message):
    __slots__ = ("base", "request")
    BASE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    request: ManualControlInput
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., request: _Optional[_Union[ManualControlInput, _Mapping]] = ...) -> None: ...

class ToggleCommandRequest(_message.Message):
    __slots__ = ("base", "enabled")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    enabled: bool
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., enabled: bool = ...) -> None: ...

class SpotlightControlRequest(_message.Message):
    __slots__ = ("base", "light_switch")
    BASE_FIELD_NUMBER: _ClassVar[int]
    LIGHT_SWITCH_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    light_switch: bool
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., light_switch: bool = ...) -> None: ...

class TaskCommandRequest(_message.Message):
    __slots__ = ("base", "task_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    task_id: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., task_id: _Optional[str] = ...) -> None: ...

class CloseCoverCommandRequest(_message.Message):
    __slots__ = ("base", "force")
    BASE_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    force: bool
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., force: bool = ...) -> None: ...

class BootSubAssetCommandRequest(_message.Message):
    __slots__ = ("base", "boot_up")
    BASE_FIELD_NUMBER: _ClassVar[int]
    BOOT_UP_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    boot_up: bool
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., boot_up: bool = ...) -> None: ...

class ChangeAcModeCommandRequest(_message.Message):
    __slots__ = ("base", "mode")
    BASE_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    mode: _asset_pb2.AssetAirConditionerStateEnum
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., mode: _Optional[_Union[_asset_pb2.AssetAirConditionerStateEnum, str]] = ...) -> None: ...

class ChangeCameraLensCommandRequest(_message.Message):
    __slots__ = ("base", "request")
    BASE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    request: ChangeCameraLensRequest
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., request: _Optional[_Union[ChangeCameraLensRequest, _Mapping]] = ...) -> None: ...

class ChangeCameraZoomCommandRequest(_message.Message):
    __slots__ = ("base", "request")
    BASE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    request: ChangeCameraZoomRequest
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., request: _Optional[_Union[ChangeCameraZoomRequest, _Mapping]] = ...) -> None: ...

class DetectionControlCommandRequest(_message.Message):
    __slots__ = ("base", "request")
    BASE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    request: _detection_pb2.DetectionControlRequest
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., request: _Optional[_Union[_detection_pb2.DetectionControlRequest, _Mapping]] = ...) -> None: ...

class LiveStreamStartCommandRequest(_message.Message):
    __slots__ = ("base", "request")
    BASE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    request: LiveStreamStartCommandPayload
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., request: _Optional[_Union[LiveStreamStartCommandPayload, _Mapping]] = ...) -> None: ...

class LiveStreamStopCommandRequest(_message.Message):
    __slots__ = ("base", "request")
    BASE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    request: LiveStreamStopCommandPayload
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., request: _Optional[_Union[LiveStreamStopCommandPayload, _Mapping]] = ...) -> None: ...

class LiveStreamStartCommandPayload(_message.Message):
    __slots__ = ("video_id", "stream_server", "stream_type", "asset_type")
    VIDEO_ID_FIELD_NUMBER: _ClassVar[int]
    STREAM_SERVER_FIELD_NUMBER: _ClassVar[int]
    STREAM_TYPE_FIELD_NUMBER: _ClassVar[int]
    ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    video_id: str
    stream_server: str
    stream_type: _asset_pb2.LiveStreamTypeEnum
    asset_type: _asset_pb2.AssetTypeEnum
    def __init__(self, video_id: _Optional[str] = ..., stream_server: _Optional[str] = ..., stream_type: _Optional[_Union[_asset_pb2.LiveStreamTypeEnum, str]] = ..., asset_type: _Optional[_Union[_asset_pb2.AssetTypeEnum, str]] = ...) -> None: ...

class LiveStreamStopCommandPayload(_message.Message):
    __slots__ = ("video_id",)
    VIDEO_ID_FIELD_NUMBER: _ClassVar[int]
    video_id: str
    def __init__(self, video_id: _Optional[str] = ...) -> None: ...

class RegisterAssetCommandRequest(_message.Message):
    __slots__ = ("base", "asset_dto")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ASSET_DTO_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    asset_dto: _asset_pb2.AssetProtoDTO
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., asset_dto: _Optional[_Union[_asset_pb2.AssetProtoDTO, _Mapping]] = ...) -> None: ...
