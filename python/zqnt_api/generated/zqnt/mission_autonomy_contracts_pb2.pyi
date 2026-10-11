import datetime

from . import common_pb2 as _common_pb2
from . import base_pb2 as _base_pb2
from . import asset_pb2 as _asset_pb2
from . import device_control_contracts_pb2 as _device_control_contracts_pb2
from . import detection_pb2 as _detection_pb2
from . import mission_autonomy_types_pb2 as _mission_autonomy_types_pb2
from . import mission_autonomy_dto_pb2 as _mission_autonomy_dto_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetMissionRequest(_message.Message):
    __slots__ = ("base", "mission_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    mission_id: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., mission_id: _Optional[str] = ...) -> None: ...

class CreateMissionRequest(_message.Message):
    __slots__ = ("base", "mission")
    BASE_FIELD_NUMBER: _ClassVar[int]
    MISSION_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    mission: _mission_autonomy_dto_pb2.MissionProtoDTO
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., mission: _Optional[_Union[_mission_autonomy_dto_pb2.MissionProtoDTO, _Mapping]] = ...) -> None: ...

class UpdateMissionRequest(_message.Message):
    __slots__ = ("base", "mission_id", "mission")
    BASE_FIELD_NUMBER: _ClassVar[int]
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    MISSION_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    mission_id: str
    mission: _mission_autonomy_dto_pb2.MissionProtoDTO
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., mission_id: _Optional[str] = ..., mission: _Optional[_Union[_mission_autonomy_dto_pb2.MissionProtoDTO, _Mapping]] = ...) -> None: ...

class DeleteMissionRequest(_message.Message):
    __slots__ = ("base", "mission_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    mission_id: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., mission_id: _Optional[str] = ...) -> None: ...

class UploadMissionNfzZonesRequest(_message.Message):
    __slots__ = ("base", "mission_id", "zones", "replace_existing")
    BASE_FIELD_NUMBER: _ClassVar[int]
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    ZONES_FIELD_NUMBER: _ClassVar[int]
    REPLACE_EXISTING_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    mission_id: str
    zones: _containers.RepeatedCompositeFieldContainer[_mission_autonomy_dto_pb2.MissionZoneProtoDTO]
    replace_existing: bool
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., mission_id: _Optional[str] = ..., zones: _Optional[_Iterable[_Union[_mission_autonomy_dto_pb2.MissionZoneProtoDTO, _Mapping]]] = ..., replace_existing: bool = ...) -> None: ...

class GetTaskRequest(_message.Message):
    __slots__ = ("base", "task_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    task_id: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., task_id: _Optional[str] = ...) -> None: ...

class GetTaskByFlightIdRequest(_message.Message):
    __slots__ = ("base", "flight_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    FLIGHT_ID_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    flight_id: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., flight_id: _Optional[str] = ...) -> None: ...

class CreateTaskRequest(_message.Message):
    __slots__ = ("base", "task")
    BASE_FIELD_NUMBER: _ClassVar[int]
    TASK_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    task: _mission_autonomy_dto_pb2.TaskProtoDTO
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., task: _Optional[_Union[_mission_autonomy_dto_pb2.TaskProtoDTO, _Mapping]] = ...) -> None: ...

class UpdateTaskRequest(_message.Message):
    __slots__ = ("base", "task_id", "task")
    BASE_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    task_id: str
    task: _mission_autonomy_dto_pb2.TaskProtoDTO
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., task_id: _Optional[str] = ..., task: _Optional[_Union[_mission_autonomy_dto_pb2.TaskProtoDTO, _Mapping]] = ...) -> None: ...

class DeleteTaskRequest(_message.Message):
    __slots__ = ("base", "task_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    task_id: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., task_id: _Optional[str] = ...) -> None: ...

class TaskLifecycleRequest(_message.Message):
    __slots__ = ("base", "task_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    task_id: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., task_id: _Optional[str] = ...) -> None: ...

class GetSchedulerRequest(_message.Message):
    __slots__ = ("base", "scheduler_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULER_ID_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    scheduler_id: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., scheduler_id: _Optional[str] = ...) -> None: ...

class ListSchedulersRequest(_message.Message):
    __slots__ = ("base",)
    BASE_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ...) -> None: ...

class CreateSchedulerRequest(_message.Message):
    __slots__ = ("base", "scheduler")
    BASE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULER_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    scheduler: _mission_autonomy_dto_pb2.SchedulerProtoDTO
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., scheduler: _Optional[_Union[_mission_autonomy_dto_pb2.SchedulerProtoDTO, _Mapping]] = ...) -> None: ...

class CreateSchedulersRequest(_message.Message):
    __slots__ = ("base", "schedulers")
    BASE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULERS_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    schedulers: _containers.RepeatedCompositeFieldContainer[_mission_autonomy_dto_pb2.SchedulerProtoDTO]
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., schedulers: _Optional[_Iterable[_Union[_mission_autonomy_dto_pb2.SchedulerProtoDTO, _Mapping]]] = ...) -> None: ...

class UpdateSchedulerRequest(_message.Message):
    __slots__ = ("base", "scheduler_id", "scheduler")
    BASE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULER_ID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULER_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    scheduler_id: str
    scheduler: _mission_autonomy_dto_pb2.SchedulerProtoDTO
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., scheduler_id: _Optional[str] = ..., scheduler: _Optional[_Union[_mission_autonomy_dto_pb2.SchedulerProtoDTO, _Mapping]] = ...) -> None: ...

class RecordSchedulerFiringRequest(_message.Message):
    __slots__ = ("base", "scheduler_id", "fired_at", "outcome", "reason", "execution_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULER_ID_FIELD_NUMBER: _ClassVar[int]
    FIRED_AT_FIELD_NUMBER: _ClassVar[int]
    OUTCOME_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    scheduler_id: str
    fired_at: _timestamp_pb2.Timestamp
    outcome: _mission_autonomy_types_pb2.SchedulerFiringOutcome
    reason: str
    execution_id: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., scheduler_id: _Optional[str] = ..., fired_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., outcome: _Optional[_Union[_mission_autonomy_types_pb2.SchedulerFiringOutcome, str]] = ..., reason: _Optional[str] = ..., execution_id: _Optional[str] = ...) -> None: ...

class DeleteSchedulerRequest(_message.Message):
    __slots__ = ("base", "scheduler_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULER_ID_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    scheduler_id: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., scheduler_id: _Optional[str] = ...) -> None: ...

class DeleteSchedulersRequest(_message.Message):
    __slots__ = ("base", "scheduler_ids")
    BASE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULER_IDS_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    scheduler_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., scheduler_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class GetWaypointsByTaskIdRequest(_message.Message):
    __slots__ = ("base", "task_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    task_id: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., task_id: _Optional[str] = ...) -> None: ...

class WaypointsList(_message.Message):
    __slots__ = ("waypoints",)
    WAYPOINTS_FIELD_NUMBER: _ClassVar[int]
    waypoints: _containers.RepeatedCompositeFieldContainer[_mission_autonomy_types_pb2.WaypointProtoDTO]
    def __init__(self, waypoints: _Optional[_Iterable[_Union[_mission_autonomy_types_pb2.WaypointProtoDTO, _Mapping]]] = ...) -> None: ...

class MissionResponse(_message.Message):
    __slots__ = ("has_errors", "tid", "mission_id", "timestamp", "empty", "error", "progress", "mission")
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    TID_FIELD_NUMBER: _ClassVar[int]
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    EMPTY_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    MISSION_FIELD_NUMBER: _ClassVar[int]
    has_errors: bool
    tid: str
    mission_id: str
    timestamp: _timestamp_pb2.Timestamp
    empty: _empty_pb2.Empty
    error: _base_pb2.GlobalErrorMessage
    progress: _base_pb2.CommandProgress
    mission: _mission_autonomy_dto_pb2.MissionProtoDTO
    def __init__(self, has_errors: bool = ..., tid: _Optional[str] = ..., mission_id: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., empty: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ..., progress: _Optional[_Union[_base_pb2.CommandProgress, _Mapping]] = ..., mission: _Optional[_Union[_mission_autonomy_dto_pb2.MissionProtoDTO, _Mapping]] = ...) -> None: ...

class TaskResponse(_message.Message):
    __slots__ = ("has_errors", "tid", "task_id", "timestamp", "empty", "error", "progress", "task")
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    TID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    EMPTY_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    TASK_FIELD_NUMBER: _ClassVar[int]
    has_errors: bool
    tid: str
    task_id: str
    timestamp: _timestamp_pb2.Timestamp
    empty: _empty_pb2.Empty
    error: _base_pb2.GlobalErrorMessage
    progress: _base_pb2.CommandProgress
    task: _mission_autonomy_dto_pb2.TaskProtoDTO
    def __init__(self, has_errors: bool = ..., tid: _Optional[str] = ..., task_id: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., empty: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ..., progress: _Optional[_Union[_base_pb2.CommandProgress, _Mapping]] = ..., task: _Optional[_Union[_mission_autonomy_dto_pb2.TaskProtoDTO, _Mapping]] = ...) -> None: ...

class SchedulerResponse(_message.Message):
    __slots__ = ("has_errors", "tid", "scheduler_id", "timestamp", "empty", "error", "progress", "scheduler", "schedulers")
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    TID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULER_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    EMPTY_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    SCHEDULER_FIELD_NUMBER: _ClassVar[int]
    SCHEDULERS_FIELD_NUMBER: _ClassVar[int]
    has_errors: bool
    tid: str
    scheduler_id: str
    timestamp: _timestamp_pb2.Timestamp
    empty: _empty_pb2.Empty
    error: _base_pb2.GlobalErrorMessage
    progress: _base_pb2.CommandProgress
    scheduler: _mission_autonomy_dto_pb2.SchedulerProtoDTO
    schedulers: _mission_autonomy_dto_pb2.SchedulerProtoDTOList
    def __init__(self, has_errors: bool = ..., tid: _Optional[str] = ..., scheduler_id: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., empty: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ..., progress: _Optional[_Union[_base_pb2.CommandProgress, _Mapping]] = ..., scheduler: _Optional[_Union[_mission_autonomy_dto_pb2.SchedulerProtoDTO, _Mapping]] = ..., schedulers: _Optional[_Union[_mission_autonomy_dto_pb2.SchedulerProtoDTOList, _Mapping]] = ...) -> None: ...

class WaypointsResponse(_message.Message):
    __slots__ = ("has_errors", "tid", "task_id", "timestamp", "empty", "error", "waypoints")
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    TID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    EMPTY_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    WAYPOINTS_FIELD_NUMBER: _ClassVar[int]
    has_errors: bool
    tid: str
    task_id: str
    timestamp: _timestamp_pb2.Timestamp
    empty: _empty_pb2.Empty
    error: _base_pb2.GlobalErrorMessage
    waypoints: WaypointsList
    def __init__(self, has_errors: bool = ..., tid: _Optional[str] = ..., task_id: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., empty: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ..., waypoints: _Optional[_Union[WaypointsList, _Mapping]] = ...) -> None: ...
