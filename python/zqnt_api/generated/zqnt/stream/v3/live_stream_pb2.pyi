import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from zqnt_api.generated.zqnt.common.v3 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LiveStream(_message.Message):
    __slots__ = ("asset", "path", "since", "viewers")
    ASSET_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    SINCE_FIELD_NUMBER: _ClassVar[int]
    VIEWERS_FIELD_NUMBER: _ClassVar[int]
    asset: _common_pb2.AssetRef
    path: str
    since: _timestamp_pb2.Timestamp
    viewers: int
    def __init__(self, asset: _Optional[_Union[_common_pb2.AssetRef, _Mapping]] = ..., path: _Optional[str] = ..., since: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., viewers: _Optional[int] = ...) -> None: ...

class ListLiveStreamsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListLiveStreamsResponse(_message.Message):
    __slots__ = ("streams",)
    STREAMS_FIELD_NUMBER: _ClassVar[int]
    streams: _containers.RepeatedCompositeFieldContainer[LiveStream]
    def __init__(self, streams: _Optional[_Iterable[_Union[LiveStream, _Mapping]]] = ...) -> None: ...
