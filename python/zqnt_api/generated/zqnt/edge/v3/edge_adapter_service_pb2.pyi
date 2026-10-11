import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from zqnt_api.generated.zqnt.capability.v3 import capability_pb2 as _capability_pb2
from zqnt_api.generated.zqnt.capability.v3 import command_pb2 as _command_pb2
from zqnt_api.generated.zqnt.common.v3 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

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
    __slots__ = ("object_id", "object_type", "confidence", "bounding_box", "position")
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    BOUNDING_BOX_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    object_id: str
    object_type: str
    confidence: float
    bounding_box: BoundingBox
    position: _common_pb2.GeoPoint
    def __init__(self, object_id: _Optional[str] = ..., object_type: _Optional[str] = ..., confidence: _Optional[float] = ..., bounding_box: _Optional[_Union[BoundingBox, _Mapping]] = ..., position: _Optional[_Union[_common_pb2.GeoPoint, _Mapping]] = ...) -> None: ...

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
