from . import base_pb2 as _base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

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

class DetectionPosition(_message.Message):
    __slots__ = ("latitude", "longitude", "altitude", "range_m", "bearing_deg", "elevation_deg", "speed_mps", "heading_deg")
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    RANGE_M_FIELD_NUMBER: _ClassVar[int]
    BEARING_DEG_FIELD_NUMBER: _ClassVar[int]
    ELEVATION_DEG_FIELD_NUMBER: _ClassVar[int]
    SPEED_MPS_FIELD_NUMBER: _ClassVar[int]
    HEADING_DEG_FIELD_NUMBER: _ClassVar[int]
    latitude: float
    longitude: float
    altitude: float
    range_m: float
    bearing_deg: float
    elevation_deg: float
    speed_mps: float
    heading_deg: float
    def __init__(self, latitude: _Optional[float] = ..., longitude: _Optional[float] = ..., altitude: _Optional[float] = ..., range_m: _Optional[float] = ..., bearing_deg: _Optional[float] = ..., elevation_deg: _Optional[float] = ..., speed_mps: _Optional[float] = ..., heading_deg: _Optional[float] = ...) -> None: ...

class DetectionResult(_message.Message):
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
    position: DetectionPosition
    def __init__(self, object_id: _Optional[str] = ..., object_type: _Optional[str] = ..., confidence: _Optional[float] = ..., bounding_box: _Optional[_Union[BoundingBox, _Mapping]] = ..., position: _Optional[_Union[DetectionPosition, _Mapping]] = ...) -> None: ...

class DetectionBatch(_message.Message):
    __slots__ = ("base", "detections", "stream_url")
    BASE_FIELD_NUMBER: _ClassVar[int]
    DETECTIONS_FIELD_NUMBER: _ClassVar[int]
    STREAM_URL_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    detections: _containers.RepeatedCompositeFieldContainer[DetectionResult]
    stream_url: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., detections: _Optional[_Iterable[_Union[DetectionResult, _Mapping]]] = ..., stream_url: _Optional[str] = ...) -> None: ...

class DetectionControlRequest(_message.Message):
    __slots__ = ("command", "asset_sn", "sub_asset_sn", "task_id", "stream_url", "gimbal_tracking_enabled")
    class DetectionControlCommand(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        REMOTE_CONTROL_COMMAND_DETECTION_START: _ClassVar[DetectionControlRequest.DetectionControlCommand]
        REMOTE_CONTROL_COMMAND_DETECTION_STOP: _ClassVar[DetectionControlRequest.DetectionControlCommand]
    REMOTE_CONTROL_COMMAND_DETECTION_START: DetectionControlRequest.DetectionControlCommand
    REMOTE_CONTROL_COMMAND_DETECTION_STOP: DetectionControlRequest.DetectionControlCommand
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    ASSET_SN_FIELD_NUMBER: _ClassVar[int]
    SUB_ASSET_SN_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    STREAM_URL_FIELD_NUMBER: _ClassVar[int]
    GIMBAL_TRACKING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    command: DetectionControlRequest.DetectionControlCommand
    asset_sn: str
    sub_asset_sn: str
    task_id: str
    stream_url: str
    gimbal_tracking_enabled: bool
    def __init__(self, command: _Optional[_Union[DetectionControlRequest.DetectionControlCommand, str]] = ..., asset_sn: _Optional[str] = ..., sub_asset_sn: _Optional[str] = ..., task_id: _Optional[str] = ..., stream_url: _Optional[str] = ..., gimbal_tracking_enabled: bool = ...) -> None: ...

class DetectionStreamRequest(_message.Message):
    __slots__ = ("base", "stream_url")
    BASE_FIELD_NUMBER: _ClassVar[int]
    STREAM_URL_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    stream_url: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., stream_url: _Optional[str] = ...) -> None: ...
