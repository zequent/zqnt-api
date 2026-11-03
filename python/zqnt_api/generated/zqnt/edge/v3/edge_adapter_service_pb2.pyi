import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from zqnt_api.generated.zqnt.capability.v3 import capability_pb2 as _capability_pb2
from zqnt_api.generated.zqnt.capability.v3 import command_pb2 as _command_pb2
from zqnt_api.generated.zqnt.common.v3 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Identity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    IDENTITY_UNSPECIFIED: _ClassVar[Identity]
    IDENTITY_PENDING: _ClassVar[Identity]
    IDENTITY_UNKNOWN: _ClassVar[Identity]
    IDENTITY_ASSUMED_FRIEND: _ClassVar[Identity]
    IDENTITY_FRIEND: _ClassVar[Identity]
    IDENTITY_NEUTRAL: _ClassVar[Identity]
    IDENTITY_SUSPECT: _ClassVar[Identity]
    IDENTITY_HOSTILE: _ClassVar[Identity]

class IdentitySetBy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    IDENTITY_SET_BY_UNSPECIFIED: _ClassVar[IdentitySetBy]
    IDENTITY_SET_BY_PLATFORM: _ClassVar[IdentitySetBy]
    IDENTITY_SET_BY_OPERATOR: _ClassVar[IdentitySetBy]

class IdentitySourceKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    IDENTITY_SOURCE_KIND_UNSPECIFIED: _ClassVar[IdentitySourceKind]
    IDENTITY_SOURCE_KIND_POSITION: _ClassVar[IdentitySourceKind]
    IDENTITY_SOURCE_KIND_SENSOR: _ClassVar[IdentitySourceKind]
    IDENTITY_SOURCE_KIND_OPERATOR: _ClassVar[IdentitySourceKind]
    IDENTITY_SOURCE_KIND_TRACK: _ClassVar[IdentitySourceKind]
IDENTITY_UNSPECIFIED: Identity
IDENTITY_PENDING: Identity
IDENTITY_UNKNOWN: Identity
IDENTITY_ASSUMED_FRIEND: Identity
IDENTITY_FRIEND: Identity
IDENTITY_NEUTRAL: Identity
IDENTITY_SUSPECT: Identity
IDENTITY_HOSTILE: Identity
IDENTITY_SET_BY_UNSPECIFIED: IdentitySetBy
IDENTITY_SET_BY_PLATFORM: IdentitySetBy
IDENTITY_SET_BY_OPERATOR: IdentitySetBy
IDENTITY_SOURCE_KIND_UNSPECIFIED: IdentitySourceKind
IDENTITY_SOURCE_KIND_POSITION: IdentitySourceKind
IDENTITY_SOURCE_KIND_SENSOR: IdentitySourceKind
IDENTITY_SOURCE_KIND_OPERATOR: IdentitySourceKind
IDENTITY_SOURCE_KIND_TRACK: IdentitySourceKind

class GetCapabilitiesRequest(_message.Message):
    __slots__ = ("context", "asset", "target")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    asset: _common_pb2.AssetRef
    target: _capability_pb2.Target
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., asset: _Optional[_Union[_common_pb2.AssetRef, _Mapping]] = ..., target: _Optional[_Union[_capability_pb2.Target, _Mapping]] = ...) -> None: ...

class GetCapabilitiesResponse(_message.Message):
    __slots__ = ("capabilities",)
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    capabilities: _capability_pb2.CapabilitySet
    def __init__(self, capabilities: _Optional[_Union[_capability_pb2.CapabilitySet, _Mapping]] = ...) -> None: ...

class ExecuteCommandRequest(_message.Message):
    __slots__ = ("context", "command", "command_execution_id")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    COMMAND_EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    command: _command_pb2.Command
    command_execution_id: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., command: _Optional[_Union[_command_pb2.Command, _Mapping]] = ..., command_execution_id: _Optional[str] = ...) -> None: ...

class ExecuteCommandResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _command_pb2.CommandResult
    def __init__(self, result: _Optional[_Union[_command_pb2.CommandResult, _Mapping]] = ...) -> None: ...

class CancelCommandRequest(_message.Message):
    __slots__ = ("context", "command_execution_id", "reason")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    COMMAND_EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    command_execution_id: str
    reason: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., command_execution_id: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class CancelCommandResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _command_pb2.CommandResult
    def __init__(self, result: _Optional[_Union[_command_pb2.CommandResult, _Mapping]] = ...) -> None: ...

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

class StreamManualControlRequest(_message.Message):
    __slots__ = ("asset", "input", "sent_at")
    ASSET_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    SENT_AT_FIELD_NUMBER: _ClassVar[int]
    asset: _common_pb2.AssetRef
    input: ManualControlInput
    sent_at: _timestamp_pb2.Timestamp
    def __init__(self, asset: _Optional[_Union[_common_pb2.AssetRef, _Mapping]] = ..., input: _Optional[_Union[ManualControlInput, _Mapping]] = ..., sent_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class StreamManualControlResponse(_message.Message):
    __slots__ = ("accepted_inputs", "error")
    ACCEPTED_INPUTS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    accepted_inputs: int
    error: _common_pb2.Error
    def __init__(self, accepted_inputs: _Optional[int] = ..., error: _Optional[_Union[_common_pb2.Error, _Mapping]] = ...) -> None: ...

class StreamDetectionsRequest(_message.Message):
    __slots__ = ("asset", "stream_url")
    ASSET_FIELD_NUMBER: _ClassVar[int]
    STREAM_URL_FIELD_NUMBER: _ClassVar[int]
    asset: _common_pb2.AssetRef
    stream_url: str
    def __init__(self, asset: _Optional[_Union[_common_pb2.AssetRef, _Mapping]] = ..., stream_url: _Optional[str] = ...) -> None: ...

class BoundingBox(_message.Message):
    __slots__ = ("x", "y", "width", "height")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    width: float
    height: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ..., width: _Optional[float] = ..., height: _Optional[float] = ...) -> None: ...

class Detection(_message.Message):
    __slots__ = ("object_id", "object_type", "confidence", "bounding_box", "position", "range_meters", "bearing_degrees", "elevation_degrees", "speed", "heading_degrees", "identity", "identity_sources", "identity_set_by", "friendly_asset_sn", "identity_ambiguous", "track_id", "site_id")
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    BOUNDING_BOX_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    RANGE_METERS_FIELD_NUMBER: _ClassVar[int]
    BEARING_DEGREES_FIELD_NUMBER: _ClassVar[int]
    ELEVATION_DEGREES_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    HEADING_DEGREES_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_SOURCES_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_SET_BY_FIELD_NUMBER: _ClassVar[int]
    FRIENDLY_ASSET_SN_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_AMBIGUOUS_FIELD_NUMBER: _ClassVar[int]
    TRACK_ID_FIELD_NUMBER: _ClassVar[int]
    SITE_ID_FIELD_NUMBER: _ClassVar[int]
    object_id: str
    object_type: str
    confidence: float
    bounding_box: BoundingBox
    position: _common_pb2.GeoPoint
    range_meters: float
    bearing_degrees: float
    elevation_degrees: float
    speed: float
    heading_degrees: float
    identity: Identity
    identity_sources: _containers.RepeatedCompositeFieldContainer[IdentitySource]
    identity_set_by: IdentitySetBy
    friendly_asset_sn: str
    identity_ambiguous: bool
    track_id: str
    site_id: str
    def __init__(self, object_id: _Optional[str] = ..., object_type: _Optional[str] = ..., confidence: _Optional[float] = ..., bounding_box: _Optional[_Union[BoundingBox, _Mapping]] = ..., position: _Optional[_Union[_common_pb2.GeoPoint, _Mapping]] = ..., range_meters: _Optional[float] = ..., bearing_degrees: _Optional[float] = ..., elevation_degrees: _Optional[float] = ..., speed: _Optional[float] = ..., heading_degrees: _Optional[float] = ..., identity: _Optional[_Union[Identity, str]] = ..., identity_sources: _Optional[_Iterable[_Union[IdentitySource, _Mapping]]] = ..., identity_set_by: _Optional[_Union[IdentitySetBy, str]] = ..., friendly_asset_sn: _Optional[str] = ..., identity_ambiguous: _Optional[bool] = ..., track_id: _Optional[str] = ..., site_id: _Optional[str] = ...) -> None: ...

class IdentitySource(_message.Message):
    __slots__ = ("kind", "identity", "asset_sn", "distance_meters", "age_seconds", "confidence")
    KIND_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    ASSET_SN_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_METERS_FIELD_NUMBER: _ClassVar[int]
    AGE_SECONDS_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    kind: IdentitySourceKind
    identity: Identity
    asset_sn: str
    distance_meters: float
    age_seconds: float
    confidence: float
    def __init__(self, kind: _Optional[_Union[IdentitySourceKind, str]] = ..., identity: _Optional[_Union[Identity, str]] = ..., asset_sn: _Optional[str] = ..., distance_meters: _Optional[float] = ..., age_seconds: _Optional[float] = ..., confidence: _Optional[float] = ...) -> None: ...

class StreamDetectionsResponse(_message.Message):
    __slots__ = ("asset", "detections", "stream_url", "observed_at")
    ASSET_FIELD_NUMBER: _ClassVar[int]
    DETECTIONS_FIELD_NUMBER: _ClassVar[int]
    STREAM_URL_FIELD_NUMBER: _ClassVar[int]
    OBSERVED_AT_FIELD_NUMBER: _ClassVar[int]
    asset: _common_pb2.AssetRef
    detections: _containers.RepeatedCompositeFieldContainer[Detection]
    stream_url: str
    observed_at: _timestamp_pb2.Timestamp
    def __init__(self, asset: _Optional[_Union[_common_pb2.AssetRef, _Mapping]] = ..., detections: _Optional[_Iterable[_Union[Detection, _Mapping]]] = ..., stream_url: _Optional[str] = ..., observed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ReportCapabilitiesRequest(_message.Message):
    __slots__ = ("capabilities",)
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    capabilities: _capability_pb2.CapabilitySet
    def __init__(self, capabilities: _Optional[_Union[_capability_pb2.CapabilitySet, _Mapping]] = ...) -> None: ...

class ReportCapabilitiesResponse(_message.Message):
    __slots__ = ("accepted_revision",)
    ACCEPTED_REVISION_FIELD_NUMBER: _ClassVar[int]
    accepted_revision: str
    def __init__(self, accepted_revision: _Optional[str] = ...) -> None: ...

class PublishCommandEventRequest(_message.Message):
    __slots__ = ("event",)
    EVENT_FIELD_NUMBER: _ClassVar[int]
    event: _command_pb2.CommandEvent
    def __init__(self, event: _Optional[_Union[_command_pb2.CommandEvent, _Mapping]] = ...) -> None: ...

class PublishCommandEventResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
