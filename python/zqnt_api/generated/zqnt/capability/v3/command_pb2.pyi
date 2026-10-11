import datetime

from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from zqnt_api.generated.zqnt.capability.v3 import capability_pb2 as _capability_pb2
from zqnt_api.generated.zqnt.common.v3 import common_pb2 as _common_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommandState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COMMAND_STATE_UNSPECIFIED: _ClassVar[CommandState]
    COMMAND_STATE_ACCEPTED: _ClassVar[CommandState]
    COMMAND_STATE_RUNNING: _ClassVar[CommandState]
    COMMAND_STATE_SUCCEEDED: _ClassVar[CommandState]
    COMMAND_STATE_FAILED: _ClassVar[CommandState]
    COMMAND_STATE_REJECTED: _ClassVar[CommandState]
    COMMAND_STATE_CANCELLED: _ClassVar[CommandState]
    COMMAND_STATE_TIMED_OUT: _ClassVar[CommandState]
COMMAND_STATE_UNSPECIFIED: CommandState
COMMAND_STATE_ACCEPTED: CommandState
COMMAND_STATE_RUNNING: CommandState
COMMAND_STATE_SUCCEEDED: CommandState
COMMAND_STATE_FAILED: CommandState
COMMAND_STATE_REJECTED: CommandState
COMMAND_STATE_CANCELLED: CommandState
COMMAND_STATE_TIMED_OUT: CommandState

class ExecutionRef(_message.Message):
    __slots__ = ("execution_id", "node_id")
    EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    execution_id: str
    node_id: str
    def __init__(self, execution_id: _Optional[str] = ..., node_id: _Optional[str] = ...) -> None: ...

class Command(_message.Message):
    __slots__ = ("asset", "command_id", "params", "target", "timeout", "execution")
    ASSET_FIELD_NUMBER: _ClassVar[int]
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    asset: _common_pb2.AssetRef
    command_id: str
    params: _struct_pb2.Struct
    target: _capability_pb2.Target
    timeout: _duration_pb2.Duration
    execution: ExecutionRef
    def __init__(self, asset: _Optional[_Union[_common_pb2.AssetRef, _Mapping]] = ..., command_id: _Optional[str] = ..., params: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., target: _Optional[_Union[_capability_pb2.Target, _Mapping]] = ..., timeout: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., execution: _Optional[_Union[ExecutionRef, _Mapping]] = ...) -> None: ...

class CommandResult(_message.Message):
    __slots__ = ("command_execution_id", "command_id", "state", "result", "error")
    COMMAND_EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    command_execution_id: str
    command_id: str
    state: CommandState
    result: _struct_pb2.Struct
    error: _common_pb2.Error
    def __init__(self, command_execution_id: _Optional[str] = ..., command_id: _Optional[str] = ..., state: _Optional[_Union[CommandState, str]] = ..., result: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., error: _Optional[_Union[_common_pb2.Error, _Mapping]] = ...) -> None: ...

class CommandEvent(_message.Message):
    __slots__ = ("command_execution_id", "command_id", "asset", "state", "progress", "remaining", "message", "result", "error", "occurred_at", "execution")
    COMMAND_EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    REMAINING_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    OCCURRED_AT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    command_execution_id: str
    command_id: str
    asset: _common_pb2.AssetRef
    state: CommandState
    progress: float
    remaining: _duration_pb2.Duration
    message: str
    result: _struct_pb2.Struct
    error: _common_pb2.Error
    occurred_at: _timestamp_pb2.Timestamp
    execution: ExecutionRef
    def __init__(self, command_execution_id: _Optional[str] = ..., command_id: _Optional[str] = ..., asset: _Optional[_Union[_common_pb2.AssetRef, _Mapping]] = ..., state: _Optional[_Union[CommandState, str]] = ..., progress: _Optional[float] = ..., remaining: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., message: _Optional[str] = ..., result: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., error: _Optional[_Union[_common_pb2.Error, _Mapping]] = ..., occurred_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., execution: _Optional[_Union[ExecutionRef, _Mapping]] = ...) -> None: ...
