import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from . import mission_autonomy_types_pb2 as _mission_autonomy_types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GeoPointProtoDTO(_message.Message):
    __slots__ = ("latitude", "longitude", "altitude")
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    latitude: float
    longitude: float
    altitude: float
    def __init__(self, latitude: _Optional[float] = ..., longitude: _Optional[float] = ..., altitude: _Optional[float] = ...) -> None: ...

class GeoAreaProtoDTO(_message.Message):
    __slots__ = ("type", "vertices", "center", "radius_meters", "geo_json")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VERTICES_FIELD_NUMBER: _ClassVar[int]
    CENTER_FIELD_NUMBER: _ClassVar[int]
    RADIUS_METERS_FIELD_NUMBER: _ClassVar[int]
    GEO_JSON_FIELD_NUMBER: _ClassVar[int]
    type: _mission_autonomy_types_pb2.GeoAreaType
    vertices: _containers.RepeatedCompositeFieldContainer[GeoPointProtoDTO]
    center: GeoPointProtoDTO
    radius_meters: float
    geo_json: str
    def __init__(self, type: _Optional[_Union[_mission_autonomy_types_pb2.GeoAreaType, str]] = ..., vertices: _Optional[_Iterable[_Union[GeoPointProtoDTO, _Mapping]]] = ..., center: _Optional[_Union[GeoPointProtoDTO, _Mapping]] = ..., radius_meters: _Optional[float] = ..., geo_json: _Optional[str] = ...) -> None: ...

class MissionZoneProtoDTO(_message.Message):
    __slots__ = ("id", "name", "type", "enforcement_type", "area", "active", "priority", "config", "organization_id", "theatre_id", "min_altitude_meters", "max_altitude_meters", "created_at", "modified_at", "modified_from")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ENFORCEMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    AREA_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    THEATRE_ID_FIELD_NUMBER: _ClassVar[int]
    MIN_ALTITUDE_METERS_FIELD_NUMBER: _ClassVar[int]
    MAX_ALTITUDE_METERS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_FROM_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    type: _mission_autonomy_types_pb2.MissionZoneType
    enforcement_type: _mission_autonomy_types_pb2.ZoneEnforcementType
    area: GeoAreaProtoDTO
    active: bool
    priority: int
    config: _mission_autonomy_types_pb2.DynamicConfigProto
    organization_id: str
    theatre_id: str
    min_altitude_meters: float
    max_altitude_meters: float
    created_at: _timestamp_pb2.Timestamp
    modified_at: _timestamp_pb2.Timestamp
    modified_from: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., type: _Optional[_Union[_mission_autonomy_types_pb2.MissionZoneType, str]] = ..., enforcement_type: _Optional[_Union[_mission_autonomy_types_pb2.ZoneEnforcementType, str]] = ..., area: _Optional[_Union[GeoAreaProtoDTO, _Mapping]] = ..., active: bool = ..., priority: _Optional[int] = ..., config: _Optional[_Union[_mission_autonomy_types_pb2.DynamicConfigProto, _Mapping]] = ..., organization_id: _Optional[str] = ..., theatre_id: _Optional[str] = ..., min_altitude_meters: _Optional[float] = ..., max_altitude_meters: _Optional[float] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., modified_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., modified_from: _Optional[str] = ...) -> None: ...

class WorkflowStepProtoDTO(_message.Message):
    __slots__ = ("id", "name", "type", "status", "task_id", "depends_on_step_ids", "execution_order", "priority", "config")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    DEPENDS_ON_STEP_IDS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_ORDER_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    type: _mission_autonomy_types_pb2.WorkflowStepType
    status: _mission_autonomy_types_pb2.WorkflowStepStatus
    task_id: str
    depends_on_step_ids: _containers.RepeatedScalarFieldContainer[str]
    execution_order: int
    priority: int
    config: _mission_autonomy_types_pb2.DynamicConfigProto
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., type: _Optional[_Union[_mission_autonomy_types_pb2.WorkflowStepType, str]] = ..., status: _Optional[_Union[_mission_autonomy_types_pb2.WorkflowStepStatus, str]] = ..., task_id: _Optional[str] = ..., depends_on_step_ids: _Optional[_Iterable[str]] = ..., execution_order: _Optional[int] = ..., priority: _Optional[int] = ..., config: _Optional[_Union[_mission_autonomy_types_pb2.DynamicConfigProto, _Mapping]] = ...) -> None: ...

class AutomationWorkflowProtoDTO(_message.Message):
    __slots__ = ("execution_strategy", "failure_strategy", "steps", "decision_engine_enabled", "workflow_config")
    EXECUTION_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    FAILURE_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    STEPS_FIELD_NUMBER: _ClassVar[int]
    DECISION_ENGINE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_CONFIG_FIELD_NUMBER: _ClassVar[int]
    execution_strategy: _mission_autonomy_types_pb2.ExecutionStrategy
    failure_strategy: _mission_autonomy_types_pb2.FailureStrategy
    steps: _containers.RepeatedCompositeFieldContainer[WorkflowStepProtoDTO]
    decision_engine_enabled: bool
    workflow_config: _mission_autonomy_types_pb2.DynamicConfigProto
    def __init__(self, execution_strategy: _Optional[_Union[_mission_autonomy_types_pb2.ExecutionStrategy, str]] = ..., failure_strategy: _Optional[_Union[_mission_autonomy_types_pb2.FailureStrategy, str]] = ..., steps: _Optional[_Iterable[_Union[WorkflowStepProtoDTO, _Mapping]]] = ..., decision_engine_enabled: bool = ..., workflow_config: _Optional[_Union[_mission_autonomy_types_pb2.DynamicConfigProto, _Mapping]] = ...) -> None: ...

class RetryPolicyProtoDTO(_message.Message):
    __slots__ = ("max_attempts", "retry_delay_seconds", "backoff_multiplier")
    MAX_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    RETRY_DELAY_SECONDS_FIELD_NUMBER: _ClassVar[int]
    BACKOFF_MULTIPLIER_FIELD_NUMBER: _ClassVar[int]
    max_attempts: int
    retry_delay_seconds: int
    backoff_multiplier: float
    def __init__(self, max_attempts: _Optional[int] = ..., retry_delay_seconds: _Optional[int] = ..., backoff_multiplier: _Optional[float] = ...) -> None: ...

class MissionProtoDTO(_message.Message):
    __slots__ = ("id", "name", "description", "tasks", "status", "type", "geo_json", "start_date", "end_date", "assigned_assets", "created_at", "modified_at", "updated_user", "mission_config", "external_id", "external_mission_type", "autonomy_config", "priority", "execution_order", "progress", "automation_workflow", "schedulers", "zones")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TASKS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    GEO_JSON_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_ASSETS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_USER_FIELD_NUMBER: _ClassVar[int]
    MISSION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_MISSION_TYPE_FIELD_NUMBER: _ClassVar[int]
    AUTONOMY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_ORDER_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    AUTOMATION_WORKFLOW_FIELD_NUMBER: _ClassVar[int]
    SCHEDULERS_FIELD_NUMBER: _ClassVar[int]
    ZONES_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    tasks: _containers.RepeatedCompositeFieldContainer[TaskProtoDTO]
    status: _mission_autonomy_types_pb2.MissionStatus
    type: _mission_autonomy_types_pb2.MissionType
    geo_json: str
    start_date: _timestamp_pb2.Timestamp
    end_date: _timestamp_pb2.Timestamp
    assigned_assets: _containers.RepeatedScalarFieldContainer[str]
    created_at: _timestamp_pb2.Timestamp
    modified_at: _timestamp_pb2.Timestamp
    updated_user: str
    mission_config: _mission_autonomy_types_pb2.DynamicConfigProto
    external_id: str
    external_mission_type: str
    autonomy_config: _mission_autonomy_types_pb2.AutonomyConfigProto
    priority: int
    execution_order: int
    progress: int
    automation_workflow: AutomationWorkflowProtoDTO
    schedulers: _containers.RepeatedCompositeFieldContainer[SchedulerProtoDTO]
    zones: _containers.RepeatedCompositeFieldContainer[MissionZoneProtoDTO]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., tasks: _Optional[_Iterable[_Union[TaskProtoDTO, _Mapping]]] = ..., status: _Optional[_Union[_mission_autonomy_types_pb2.MissionStatus, str]] = ..., type: _Optional[_Union[_mission_autonomy_types_pb2.MissionType, str]] = ..., geo_json: _Optional[str] = ..., start_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., end_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., assigned_assets: _Optional[_Iterable[str]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., modified_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_user: _Optional[str] = ..., mission_config: _Optional[_Union[_mission_autonomy_types_pb2.DynamicConfigProto, _Mapping]] = ..., external_id: _Optional[str] = ..., external_mission_type: _Optional[str] = ..., autonomy_config: _Optional[_Union[_mission_autonomy_types_pb2.AutonomyConfigProto, _Mapping]] = ..., priority: _Optional[int] = ..., execution_order: _Optional[int] = ..., progress: _Optional[int] = ..., automation_workflow: _Optional[_Union[AutomationWorkflowProtoDTO, _Mapping]] = ..., schedulers: _Optional[_Iterable[_Union[SchedulerProtoDTO, _Mapping]]] = ..., zones: _Optional[_Iterable[_Union[MissionZoneProtoDTO, _Mapping]]] = ...) -> None: ...

class TaskProtoDTO(_message.Message):
    __slots__ = ("id", "mission_id", "created_at", "modified_at", "modified_from", "name", "description", "task_type", "config", "status", "asset_id", "sn_number", "current_progress", "current_step", "break_reason", "external_command_type", "external_task_id", "task_config_template", "execution_order", "decision_engine_enabled", "autonomy_config", "priority", "timeout_seconds", "retry_policy", "waypoint_config", "detect_config", "area_mapping_config", "poi_config", "follow_config", "track_config", "dynamic_command_config")
    ID_FIELD_NUMBER: _ClassVar[int]
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_FROM_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TASK_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    SN_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CURRENT_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    CURRENT_STEP_FIELD_NUMBER: _ClassVar[int]
    BREAK_REASON_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_COMMAND_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_CONFIG_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_ORDER_FIELD_NUMBER: _ClassVar[int]
    DECISION_ENGINE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    AUTONOMY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_SECONDS_FIELD_NUMBER: _ClassVar[int]
    RETRY_POLICY_FIELD_NUMBER: _ClassVar[int]
    WAYPOINT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DETECT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    AREA_MAPPING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    POI_CONFIG_FIELD_NUMBER: _ClassVar[int]
    FOLLOW_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TRACK_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_COMMAND_CONFIG_FIELD_NUMBER: _ClassVar[int]
    id: str
    mission_id: str
    created_at: _timestamp_pb2.Timestamp
    modified_at: _timestamp_pb2.Timestamp
    modified_from: str
    name: str
    description: str
    task_type: _mission_autonomy_types_pb2.TaskTypeProto
    config: str
    status: _mission_autonomy_types_pb2.TaskStatus
    asset_id: str
    sn_number: str
    current_progress: int
    current_step: str
    break_reason: _mission_autonomy_types_pb2.FlighttaskBreakReasonEnumProto
    external_command_type: str
    external_task_id: str
    task_config_template: _mission_autonomy_types_pb2.DynamicConfigProto
    execution_order: int
    decision_engine_enabled: bool
    autonomy_config: _mission_autonomy_types_pb2.AutonomyConfigProto
    priority: int
    timeout_seconds: int
    retry_policy: RetryPolicyProtoDTO
    waypoint_config: _mission_autonomy_types_pb2.WaypointTaskConfigProto
    detect_config: _mission_autonomy_types_pb2.DetectTaskConfigProto
    area_mapping_config: _mission_autonomy_types_pb2.AreaMappingTaskConfigProto
    poi_config: _mission_autonomy_types_pb2.PoiTaskConfigProto
    follow_config: _mission_autonomy_types_pb2.FollowTaskConfigProto
    track_config: _mission_autonomy_types_pb2.TrackTaskConfigProto
    dynamic_command_config: _mission_autonomy_types_pb2.DynamicCommandTaskConfigProto
    def __init__(self, id: _Optional[str] = ..., mission_id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., modified_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., modified_from: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., task_type: _Optional[_Union[_mission_autonomy_types_pb2.TaskTypeProto, str]] = ..., config: _Optional[str] = ..., status: _Optional[_Union[_mission_autonomy_types_pb2.TaskStatus, str]] = ..., asset_id: _Optional[str] = ..., sn_number: _Optional[str] = ..., current_progress: _Optional[int] = ..., current_step: _Optional[str] = ..., break_reason: _Optional[_Union[_mission_autonomy_types_pb2.FlighttaskBreakReasonEnumProto, str]] = ..., external_command_type: _Optional[str] = ..., external_task_id: _Optional[str] = ..., task_config_template: _Optional[_Union[_mission_autonomy_types_pb2.DynamicConfigProto, _Mapping]] = ..., execution_order: _Optional[int] = ..., decision_engine_enabled: bool = ..., autonomy_config: _Optional[_Union[_mission_autonomy_types_pb2.AutonomyConfigProto, _Mapping]] = ..., priority: _Optional[int] = ..., timeout_seconds: _Optional[int] = ..., retry_policy: _Optional[_Union[RetryPolicyProtoDTO, _Mapping]] = ..., waypoint_config: _Optional[_Union[_mission_autonomy_types_pb2.WaypointTaskConfigProto, _Mapping]] = ..., detect_config: _Optional[_Union[_mission_autonomy_types_pb2.DetectTaskConfigProto, _Mapping]] = ..., area_mapping_config: _Optional[_Union[_mission_autonomy_types_pb2.AreaMappingTaskConfigProto, _Mapping]] = ..., poi_config: _Optional[_Union[_mission_autonomy_types_pb2.PoiTaskConfigProto, _Mapping]] = ..., follow_config: _Optional[_Union[_mission_autonomy_types_pb2.FollowTaskConfigProto, _Mapping]] = ..., track_config: _Optional[_Union[_mission_autonomy_types_pb2.TrackTaskConfigProto, _Mapping]] = ..., dynamic_command_config: _Optional[_Union[_mission_autonomy_types_pb2.DynamicCommandTaskConfigProto, _Mapping]] = ...) -> None: ...

class SchedulerProtoDTO(_message.Message):
    __slots__ = ("id", "name", "cron_expression", "active", "type", "client_time_zone", "created_at", "modified_at", "asset_sn", "command_id", "application_id", "skill_id", "execution_parameters", "auto_start", "organization_id", "last_firing_at", "last_firing_outcome", "last_firing_reason", "last_execution_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CRON_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    ASSET_SN_FIELD_NUMBER: _ClassVar[int]
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    AUTO_START_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_FIRING_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_FIRING_OUTCOME_FIELD_NUMBER: _ClassVar[int]
    LAST_FIRING_REASON_FIELD_NUMBER: _ClassVar[int]
    LAST_EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    cron_expression: str
    active: bool
    type: _mission_autonomy_types_pb2.SchedulerType
    client_time_zone: str
    created_at: _timestamp_pb2.Timestamp
    modified_at: _timestamp_pb2.Timestamp
    asset_sn: str
    command_id: str
    application_id: str
    skill_id: str
    execution_parameters: _struct_pb2.Struct
    auto_start: bool
    organization_id: str
    last_firing_at: _timestamp_pb2.Timestamp
    last_firing_outcome: _mission_autonomy_types_pb2.SchedulerFiringOutcome
    last_firing_reason: str
    last_execution_id: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., cron_expression: _Optional[str] = ..., active: bool = ..., type: _Optional[_Union[_mission_autonomy_types_pb2.SchedulerType, str]] = ..., client_time_zone: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., modified_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., asset_sn: _Optional[str] = ..., command_id: _Optional[str] = ..., application_id: _Optional[str] = ..., skill_id: _Optional[str] = ..., execution_parameters: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., auto_start: bool = ..., organization_id: _Optional[str] = ..., last_firing_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., last_firing_outcome: _Optional[_Union[_mission_autonomy_types_pb2.SchedulerFiringOutcome, str]] = ..., last_firing_reason: _Optional[str] = ..., last_execution_id: _Optional[str] = ...) -> None: ...

class SchedulerProtoDTOList(_message.Message):
    __slots__ = ("scheduler_dto_list",)
    SCHEDULER_DTO_LIST_FIELD_NUMBER: _ClassVar[int]
    scheduler_dto_list: _containers.RepeatedCompositeFieldContainer[SchedulerProtoDTO]
    def __init__(self, scheduler_dto_list: _Optional[_Iterable[_Union[SchedulerProtoDTO, _Mapping]]] = ...) -> None: ...
