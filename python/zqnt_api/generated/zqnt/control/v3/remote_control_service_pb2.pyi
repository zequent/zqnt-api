from zqnt_api.generated.zqnt.capability.v3 import capability_pb2 as _capability_pb2
from zqnt_api.generated.zqnt.capability.v3 import command_pb2 as _command_pb2
from zqnt_api.generated.zqnt.common.v3 import common_pb2 as _common_pb2
from zqnt_api.generated.zqnt.edge.v3 import edge_adapter_service_pb2 as _edge_adapter_service_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
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
    __slots__ = ("context", "command", "reason", "no_fly_zone_override")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    NO_FLY_ZONE_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    command: _command_pb2.Command
    reason: str
    no_fly_zone_override: bool
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., command: _Optional[_Union[_command_pb2.Command, _Mapping]] = ..., reason: _Optional[str] = ..., no_fly_zone_override: bool = ...) -> None: ...

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

class WatchCommandEventsRequest(_message.Message):
    __slots__ = ("command_execution_id", "asset")
    COMMAND_EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    command_execution_id: str
    asset: _common_pb2.AssetRef
    def __init__(self, command_execution_id: _Optional[str] = ..., asset: _Optional[_Union[_common_pb2.AssetRef, _Mapping]] = ...) -> None: ...

class WatchCommandEventsResponse(_message.Message):
    __slots__ = ("event",)
    EVENT_FIELD_NUMBER: _ClassVar[int]
    event: _command_pb2.CommandEvent
    def __init__(self, event: _Optional[_Union[_command_pb2.CommandEvent, _Mapping]] = ...) -> None: ...

class StreamManualControlRequest(_message.Message):
    __slots__ = ("asset", "input")
    ASSET_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    asset: _common_pb2.AssetRef
    input: _edge_adapter_service_pb2.ManualControlInput
    def __init__(self, asset: _Optional[_Union[_common_pb2.AssetRef, _Mapping]] = ..., input: _Optional[_Union[_edge_adapter_service_pb2.ManualControlInput, _Mapping]] = ...) -> None: ...

class StreamManualControlResponse(_message.Message):
    __slots__ = ("accepted_inputs", "error")
    ACCEPTED_INPUTS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    accepted_inputs: int
    error: _common_pb2.Error
    def __init__(self, accepted_inputs: _Optional[int] = ..., error: _Optional[_Union[_common_pb2.Error, _Mapping]] = ...) -> None: ...
