import datetime

from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from zqnt_api.generated.zqnt.common.v3 import common_pb2 as _common_pb2
from zqnt_api.generated.zqnt.edge.v3 import edge_adapter_service_pb2 as _edge_adapter_service_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SourceState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SOURCE_STATE_UNSPECIFIED: _ClassVar[SourceState]
    SOURCE_STATE_ONLINE: _ClassVar[SourceState]
    SOURCE_STATE_STALE: _ClassVar[SourceState]
    SOURCE_STATE_NO_DATA: _ClassVar[SourceState]

class AlertSeverity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ALERT_SEVERITY_UNSPECIFIED: _ClassVar[AlertSeverity]
    ALERT_SEVERITY_INFO: _ClassVar[AlertSeverity]
    ALERT_SEVERITY_WARNING: _ClassVar[AlertSeverity]
    ALERT_SEVERITY_CRITICAL: _ClassVar[AlertSeverity]
SOURCE_STATE_UNSPECIFIED: SourceState
SOURCE_STATE_ONLINE: SourceState
SOURCE_STATE_STALE: SourceState
SOURCE_STATE_NO_DATA: SourceState
ALERT_SEVERITY_UNSPECIFIED: AlertSeverity
ALERT_SEVERITY_INFO: AlertSeverity
ALERT_SEVERITY_WARNING: AlertSeverity
ALERT_SEVERITY_CRITICAL: AlertSeverity

class TelemetrySample(_message.Message):
    __slots__ = ("asset", "observed_at", "position", "relative_altitude", "heading_degrees", "horizontal_speed", "vertical_speed", "battery_percent", "details")
    ASSET_FIELD_NUMBER: _ClassVar[int]
    OBSERVED_AT_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    HEADING_DEGREES_FIELD_NUMBER: _ClassVar[int]
    HORIZONTAL_SPEED_FIELD_NUMBER: _ClassVar[int]
    VERTICAL_SPEED_FIELD_NUMBER: _ClassVar[int]
    BATTERY_PERCENT_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    asset: _common_pb2.AssetRef
    observed_at: _timestamp_pb2.Timestamp
    position: _common_pb2.GeoPoint
    relative_altitude: float
    heading_degrees: float
    horizontal_speed: float
    vertical_speed: float
    battery_percent: float
    details: _struct_pb2.Struct
    def __init__(self, asset: _Optional[_Union[_common_pb2.AssetRef, _Mapping]] = ..., observed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., position: _Optional[_Union[_common_pb2.GeoPoint, _Mapping]] = ..., relative_altitude: _Optional[float] = ..., heading_degrees: _Optional[float] = ..., horizontal_speed: _Optional[float] = ..., vertical_speed: _Optional[float] = ..., battery_percent: _Optional[float] = ..., details: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class SourceStatus(_message.Message):
    __slots__ = ("asset", "state", "observed_at", "last_sample_at")
    ASSET_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    OBSERVED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_SAMPLE_AT_FIELD_NUMBER: _ClassVar[int]
    asset: _common_pb2.AssetRef
    state: SourceState
    observed_at: _timestamp_pb2.Timestamp
    last_sample_at: _timestamp_pb2.Timestamp
    def __init__(self, asset: _Optional[_Union[_common_pb2.AssetRef, _Mapping]] = ..., state: _Optional[_Union[SourceState, str]] = ..., observed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., last_sample_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class DetectionBatch(_message.Message):
    __slots__ = ("asset", "observed_at", "stream_url", "detections")
    ASSET_FIELD_NUMBER: _ClassVar[int]
    OBSERVED_AT_FIELD_NUMBER: _ClassVar[int]
    STREAM_URL_FIELD_NUMBER: _ClassVar[int]
    DETECTIONS_FIELD_NUMBER: _ClassVar[int]
    asset: _common_pb2.AssetRef
    observed_at: _timestamp_pb2.Timestamp
    stream_url: str
    detections: _containers.RepeatedCompositeFieldContainer[_edge_adapter_service_pb2.Detection]
    def __init__(self, asset: _Optional[_Union[_common_pb2.AssetRef, _Mapping]] = ..., observed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., stream_url: _Optional[str] = ..., detections: _Optional[_Iterable[_Union[_edge_adapter_service_pb2.Detection, _Mapping]]] = ...) -> None: ...

class Alert(_message.Message):
    __slots__ = ("asset", "occurred_at", "severity", "code", "message", "details")
    ASSET_FIELD_NUMBER: _ClassVar[int]
    OCCURRED_AT_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    asset: _common_pb2.AssetRef
    occurred_at: _timestamp_pb2.Timestamp
    severity: AlertSeverity
    code: str
    message: str
    details: _struct_pb2.Struct
    def __init__(self, asset: _Optional[_Union[_common_pb2.AssetRef, _Mapping]] = ..., occurred_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., severity: _Optional[_Union[AlertSeverity, str]] = ..., code: _Optional[str] = ..., message: _Optional[str] = ..., details: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class WatchTelemetryRequest(_message.Message):
    __slots__ = ("context", "assets", "min_interval")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ASSETS_FIELD_NUMBER: _ClassVar[int]
    MIN_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    assets: _containers.RepeatedCompositeFieldContainer[_common_pb2.AssetRef]
    min_interval: _duration_pb2.Duration
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., assets: _Optional[_Iterable[_Union[_common_pb2.AssetRef, _Mapping]]] = ..., min_interval: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class WatchTelemetryResponse(_message.Message):
    __slots__ = ("sample", "source_status", "heartbeat")
    SAMPLE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_STATUS_FIELD_NUMBER: _ClassVar[int]
    HEARTBEAT_FIELD_NUMBER: _ClassVar[int]
    sample: TelemetrySample
    source_status: SourceStatus
    heartbeat: _timestamp_pb2.Timestamp
    def __init__(self, sample: _Optional[_Union[TelemetrySample, _Mapping]] = ..., source_status: _Optional[_Union[SourceStatus, _Mapping]] = ..., heartbeat: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class WatchDetectionsRequest(_message.Message):
    __slots__ = ("context", "assets")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ASSETS_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    assets: _containers.RepeatedCompositeFieldContainer[_common_pb2.AssetRef]
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., assets: _Optional[_Iterable[_Union[_common_pb2.AssetRef, _Mapping]]] = ...) -> None: ...

class WatchDetectionsResponse(_message.Message):
    __slots__ = ("batch", "heartbeat")
    BATCH_FIELD_NUMBER: _ClassVar[int]
    HEARTBEAT_FIELD_NUMBER: _ClassVar[int]
    batch: DetectionBatch
    heartbeat: _timestamp_pb2.Timestamp
    def __init__(self, batch: _Optional[_Union[DetectionBatch, _Mapping]] = ..., heartbeat: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class WatchAlertsRequest(_message.Message):
    __slots__ = ("context", "assets", "min_severity")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ASSETS_FIELD_NUMBER: _ClassVar[int]
    MIN_SEVERITY_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    assets: _containers.RepeatedCompositeFieldContainer[_common_pb2.AssetRef]
    min_severity: AlertSeverity
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., assets: _Optional[_Iterable[_Union[_common_pb2.AssetRef, _Mapping]]] = ..., min_severity: _Optional[_Union[AlertSeverity, str]] = ...) -> None: ...

class WatchAlertsResponse(_message.Message):
    __slots__ = ("alert", "heartbeat")
    ALERT_FIELD_NUMBER: _ClassVar[int]
    HEARTBEAT_FIELD_NUMBER: _ClassVar[int]
    alert: Alert
    heartbeat: _timestamp_pb2.Timestamp
    def __init__(self, alert: _Optional[_Union[Alert, _Mapping]] = ..., heartbeat: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class PublishTelemetryRequest(_message.Message):
    __slots__ = ("sample",)
    SAMPLE_FIELD_NUMBER: _ClassVar[int]
    sample: TelemetrySample
    def __init__(self, sample: _Optional[_Union[TelemetrySample, _Mapping]] = ...) -> None: ...

class PublishTelemetryResponse(_message.Message):
    __slots__ = ("accepted", "rejected")
    ACCEPTED_FIELD_NUMBER: _ClassVar[int]
    REJECTED_FIELD_NUMBER: _ClassVar[int]
    accepted: int
    rejected: int
    def __init__(self, accepted: _Optional[int] = ..., rejected: _Optional[int] = ...) -> None: ...

class PublishDetectionsRequest(_message.Message):
    __slots__ = ("batch",)
    BATCH_FIELD_NUMBER: _ClassVar[int]
    batch: DetectionBatch
    def __init__(self, batch: _Optional[_Union[DetectionBatch, _Mapping]] = ...) -> None: ...

class PublishDetectionsResponse(_message.Message):
    __slots__ = ("accepted", "rejected")
    ACCEPTED_FIELD_NUMBER: _ClassVar[int]
    REJECTED_FIELD_NUMBER: _ClassVar[int]
    accepted: int
    rejected: int
    def __init__(self, accepted: _Optional[int] = ..., rejected: _Optional[int] = ...) -> None: ...

class PublishAlertsRequest(_message.Message):
    __slots__ = ("alert",)
    ALERT_FIELD_NUMBER: _ClassVar[int]
    alert: Alert
    def __init__(self, alert: _Optional[_Union[Alert, _Mapping]] = ...) -> None: ...

class PublishAlertsResponse(_message.Message):
    __slots__ = ("accepted", "rejected")
    ACCEPTED_FIELD_NUMBER: _ClassVar[int]
    REJECTED_FIELD_NUMBER: _ClassVar[int]
    accepted: int
    rejected: int
    def __init__(self, accepted: _Optional[int] = ..., rejected: _Optional[int] = ...) -> None: ...
