import datetime

from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ErrorCategory(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ERROR_CATEGORY_UNSPECIFIED: _ClassVar[ErrorCategory]
    ERROR_CATEGORY_INVALID_ARGUMENT: _ClassVar[ErrorCategory]
    ERROR_CATEGORY_PERMISSION_DENIED: _ClassVar[ErrorCategory]
    ERROR_CATEGORY_PRECONDITION_FAILED: _ClassVar[ErrorCategory]
    ERROR_CATEGORY_ASSET: _ClassVar[ErrorCategory]
    ERROR_CATEGORY_SERVICE: _ClassVar[ErrorCategory]
    ERROR_CATEGORY_TIMEOUT: _ClassVar[ErrorCategory]
    ERROR_CATEGORY_NOT_FOUND: _ClassVar[ErrorCategory]
ERROR_CATEGORY_UNSPECIFIED: ErrorCategory
ERROR_CATEGORY_INVALID_ARGUMENT: ErrorCategory
ERROR_CATEGORY_PERMISSION_DENIED: ErrorCategory
ERROR_CATEGORY_PRECONDITION_FAILED: ErrorCategory
ERROR_CATEGORY_ASSET: ErrorCategory
ERROR_CATEGORY_SERVICE: ErrorCategory
ERROR_CATEGORY_TIMEOUT: ErrorCategory
ERROR_CATEGORY_NOT_FOUND: ErrorCategory

class AssetRef(_message.Message):
    __slots__ = ("sn", "id")
    SN_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    sn: str
    id: str
    def __init__(self, sn: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class RequestContext(_message.Message):
    __slots__ = ("request_id", "idempotency_key")
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    idempotency_key: str
    def __init__(self, request_id: _Optional[str] = ..., idempotency_key: _Optional[str] = ...) -> None: ...

class Error(_message.Message):
    __slots__ = ("category", "code", "message", "retryable", "details", "occurred_at")
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RETRYABLE_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    OCCURRED_AT_FIELD_NUMBER: _ClassVar[int]
    category: ErrorCategory
    code: str
    message: str
    retryable: bool
    details: _struct_pb2.Struct
    occurred_at: _timestamp_pb2.Timestamp
    def __init__(self, category: _Optional[_Union[ErrorCategory, str]] = ..., code: _Optional[str] = ..., message: _Optional[str] = ..., retryable: bool = ..., details: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., occurred_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class PageRequest(_message.Message):
    __slots__ = ("page_size", "page_token")
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str
    def __init__(self, page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class PageResponse(_message.Message):
    __slots__ = ("next_page_token", "total_size")
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    next_page_token: str
    total_size: int
    def __init__(self, next_page_token: _Optional[str] = ..., total_size: _Optional[int] = ...) -> None: ...

class GeoPoint(_message.Message):
    __slots__ = ("latitude", "longitude", "altitude")
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    latitude: float
    longitude: float
    altitude: float
    def __init__(self, latitude: _Optional[float] = ..., longitude: _Optional[float] = ..., altitude: _Optional[float] = ...) -> None: ...
