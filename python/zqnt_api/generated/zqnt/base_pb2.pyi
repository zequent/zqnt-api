import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ErrorCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ERROR_CODE_SYSTEM: _ClassVar[ErrorCode]
    ERROR_CODE_CLIENT: _ClassVar[ErrorCode]
    ERROR_CODE_SDK: _ClassVar[ErrorCode]
    ERROR_CODE_SERVICE: _ClassVar[ErrorCode]
    ERROR_CODE_ASSET: _ClassVar[ErrorCode]
ERROR_CODE_SYSTEM: ErrorCode
ERROR_CODE_CLIENT: ErrorCode
ERROR_CODE_SDK: ErrorCode
ERROR_CODE_SERVICE: ErrorCode
ERROR_CODE_ASSET: ErrorCode

class GlobalErrorMessage(_message.Message):
    __slots__ = ("timestamp", "error_message", "error_code")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    error_message: str
    error_code: ErrorCode
    def __init__(self, timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., error_message: _Optional[str] = ..., error_code: _Optional[_Union[ErrorCode, str]] = ...) -> None: ...

class RequestBase(_message.Message):
    __slots__ = ("tid", "sn", "timestamp", "asset_id", "external_id", "client_id", "user_id")
    TID_FIELD_NUMBER: _ClassVar[int]
    SN_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    tid: str
    sn: str
    timestamp: _timestamp_pb2.Timestamp
    asset_id: str
    external_id: str
    client_id: str
    user_id: str
    def __init__(self, tid: _Optional[str] = ..., sn: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., asset_id: _Optional[str] = ..., external_id: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class ResponseMeta(_message.Message):
    __slots__ = ("tid", "sn", "timestamp", "asset_id", "response_message", "external_id")
    TID_FIELD_NUMBER: _ClassVar[int]
    SN_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    tid: str
    sn: str
    timestamp: _timestamp_pb2.Timestamp
    asset_id: str
    response_message: str
    external_id: str
    def __init__(self, tid: _Optional[str] = ..., sn: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., asset_id: _Optional[str] = ..., response_message: _Optional[str] = ..., external_id: _Optional[str] = ...) -> None: ...

class CommandProgress(_message.Message):
    __slots__ = ("progress", "state", "left_time_in_seconds")
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    LEFT_TIME_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    progress: float
    state: str
    left_time_in_seconds: float
    def __init__(self, progress: _Optional[float] = ..., state: _Optional[str] = ..., left_time_in_seconds: _Optional[float] = ...) -> None: ...
