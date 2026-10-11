from google.protobuf import struct_pb2 as _struct_pb2
from . import device_control_contracts_pb2 as _device_control_contracts_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SchedulerFiringOutcome(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SCHEDULER_FIRING_OUTCOME_UNSPECIFIED: _ClassVar[SchedulerFiringOutcome]
    SCHEDULER_FIRING_OUTCOME_STARTED: _ClassVar[SchedulerFiringOutcome]
    SCHEDULER_FIRING_OUTCOME_SKIPPED: _ClassVar[SchedulerFiringOutcome]
    SCHEDULER_FIRING_OUTCOME_FAILED: _ClassVar[SchedulerFiringOutcome]

class SchedulerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SCHEDULER_TYPE_MISSION: _ClassVar[SchedulerType]
    SCHEDULER_TYPE_TASK: _ClassVar[SchedulerType]
    SCHEDULER_TYPE_SYSTEM_JOBS: _ClassVar[SchedulerType]
    SCHEDULER_TYPE_ORGANIZATION: _ClassVar[SchedulerType]
    SCHEDULER_TYPE_DATABASE: _ClassVar[SchedulerType]
    SCHEDULER_TYPE_CONNECTORS: _ClassVar[SchedulerType]

class GeoAreaType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GEO_AREA_TYPE_UNSPECIFIED: _ClassVar[GeoAreaType]
    GEO_AREA_TYPE_POLYGON: _ClassVar[GeoAreaType]
    GEO_AREA_TYPE_CIRCLE: _ClassVar[GeoAreaType]
    GEO_AREA_TYPE_GEO_JSON: _ClassVar[GeoAreaType]
    GEO_AREA_TYPE_BOUNDING_BOX: _ClassVar[GeoAreaType]

class MissionZoneType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MISSION_ZONE_TYPE_UNSPECIFIED: _ClassVar[MissionZoneType]
    MISSION_ZONE_TYPE_NO_FLY: _ClassVar[MissionZoneType]
    MISSION_ZONE_TYPE_KEEP_IN: _ClassVar[MissionZoneType]
    MISSION_ZONE_TYPE_TAKEOFF_LANDING: _ClassVar[MissionZoneType]
    MISSION_ZONE_TYPE_OBSERVATION: _ClassVar[MissionZoneType]
    MISSION_ZONE_TYPE_DANGER: _ClassVar[MissionZoneType]
    MISSION_ZONE_TYPE_PRIVACY: _ClassVar[MissionZoneType]
    MISSION_ZONE_TYPE_CUSTOM: _ClassVar[MissionZoneType]

class ZoneEnforcementType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ZONE_ENFORCEMENT_TYPE_UNSPECIFIED: _ClassVar[ZoneEnforcementType]
    ZONE_ENFORCEMENT_TYPE_ADVISORY: _ClassVar[ZoneEnforcementType]
    ZONE_ENFORCEMENT_TYPE_REQUIRE_APPROVAL: _ClassVar[ZoneEnforcementType]
    ZONE_ENFORCEMENT_TYPE_HARD_BLOCK: _ClassVar[ZoneEnforcementType]

class ExecutionStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EXECUTION_STRATEGY_UNSPECIFIED: _ClassVar[ExecutionStrategy]
    EXECUTION_STRATEGY_SEQUENTIAL: _ClassVar[ExecutionStrategy]
    EXECUTION_STRATEGY_PARALLEL: _ClassVar[ExecutionStrategy]
    EXECUTION_STRATEGY_CONDITIONAL: _ClassVar[ExecutionStrategy]
    EXECUTION_STRATEGY_PRIORITY: _ClassVar[ExecutionStrategy]

class FailureStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FAILURE_STRATEGY_UNSPECIFIED: _ClassVar[FailureStrategy]
    FAILURE_STRATEGY_STOP_MISSION: _ClassVar[FailureStrategy]
    FAILURE_STRATEGY_SKIP_TASK: _ClassVar[FailureStrategy]
    FAILURE_STRATEGY_RETRY_TASK: _ClassVar[FailureStrategy]
    FAILURE_STRATEGY_REQUIRE_HUMAN_APPROVAL: _ClassVar[FailureStrategy]
    FAILURE_STRATEGY_CUSTOM: _ClassVar[FailureStrategy]

class WorkflowStepType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WORKFLOW_STEP_TYPE_UNSPECIFIED: _ClassVar[WorkflowStepType]
    WORKFLOW_STEP_TYPE_TASK: _ClassVar[WorkflowStepType]
    WORKFLOW_STEP_TYPE_DECISION: _ClassVar[WorkflowStepType]
    WORKFLOW_STEP_TYPE_WAIT: _ClassVar[WorkflowStepType]
    WORKFLOW_STEP_TYPE_NOTIFICATION: _ClassVar[WorkflowStepType]
    WORKFLOW_STEP_TYPE_CUSTOM_COMMAND: _ClassVar[WorkflowStepType]
    WORKFLOW_STEP_TYPE_CUSTOM: _ClassVar[WorkflowStepType]

class WorkflowStepStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WORKFLOW_STEP_STATUS_UNSPECIFIED: _ClassVar[WorkflowStepStatus]
    WORKFLOW_STEP_STATUS_PENDING: _ClassVar[WorkflowStepStatus]
    WORKFLOW_STEP_STATUS_READY: _ClassVar[WorkflowStepStatus]
    WORKFLOW_STEP_STATUS_RUNNING: _ClassVar[WorkflowStepStatus]
    WORKFLOW_STEP_STATUS_BLOCKED: _ClassVar[WorkflowStepStatus]
    WORKFLOW_STEP_STATUS_COMPLETED: _ClassVar[WorkflowStepStatus]
    WORKFLOW_STEP_STATUS_SKIPPED: _ClassVar[WorkflowStepStatus]
    WORKFLOW_STEP_STATUS_ERROR: _ClassVar[WorkflowStepStatus]

class AutonomyMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AUTONOMY_MODE_UNSPECIFIED: _ClassVar[AutonomyMode]
    AUTONOMY_MODE_MANUAL_APPROVAL: _ClassVar[AutonomyMode]
    AUTONOMY_MODE_SUPERVISED: _ClassVar[AutonomyMode]
    AUTONOMY_MODE_AUTONOMOUS: _ClassVar[AutonomyMode]

class DecisionStrategyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DECISION_STRATEGY_TYPE_UNSPECIFIED: _ClassVar[DecisionStrategyType]
    DECISION_STRATEGY_TYPE_RULE_BASED: _ClassVar[DecisionStrategyType]
    DECISION_STRATEGY_TYPE_SCORE_BASED: _ClassVar[DecisionStrategyType]
    DECISION_STRATEGY_TYPE_POLICY_BASED: _ClassVar[DecisionStrategyType]
    DECISION_STRATEGY_TYPE_AI_ASSISTED: _ClassVar[DecisionStrategyType]
    DECISION_STRATEGY_TYPE_CUSTOM: _ClassVar[DecisionStrategyType]

class DecisionTriggerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DECISION_TRIGGER_TYPE_UNSPECIFIED: _ClassVar[DecisionTriggerType]
    DECISION_TRIGGER_TYPE_DETECTION: _ClassVar[DecisionTriggerType]
    DECISION_TRIGGER_TYPE_TELEMETRY: _ClassVar[DecisionTriggerType]
    DECISION_TRIGGER_TYPE_TASK_STATE: _ClassVar[DecisionTriggerType]
    DECISION_TRIGGER_TYPE_MISSION_STATE: _ClassVar[DecisionTriggerType]
    DECISION_TRIGGER_TYPE_SCHEDULE: _ClassVar[DecisionTriggerType]
    DECISION_TRIGGER_TYPE_MANUAL: _ClassVar[DecisionTriggerType]
    DECISION_TRIGGER_TYPE_EXTERNAL: _ClassVar[DecisionTriggerType]

class DecisionActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DECISION_ACTION_TYPE_UNSPECIFIED: _ClassVar[DecisionActionType]
    DECISION_ACTION_TYPE_START_TASK: _ClassVar[DecisionActionType]
    DECISION_ACTION_TYPE_STOP_TASK: _ClassVar[DecisionActionType]
    DECISION_ACTION_TYPE_PAUSE_TASK: _ClassVar[DecisionActionType]
    DECISION_ACTION_TYPE_RESUME_TASK: _ClassVar[DecisionActionType]
    DECISION_ACTION_TYPE_CREATE_TASK: _ClassVar[DecisionActionType]
    DECISION_ACTION_TYPE_ASSIGN_ASSET: _ClassVar[DecisionActionType]
    DECISION_ACTION_TYPE_CHANGE_TASK_CONFIG: _ClassVar[DecisionActionType]
    DECISION_ACTION_TYPE_CHANGE_MISSION_CONFIG: _ClassVar[DecisionActionType]
    DECISION_ACTION_TYPE_NOTIFY: _ClassVar[DecisionActionType]
    DECISION_ACTION_TYPE_CUSTOM_COMMAND: _ClassVar[DecisionActionType]
    DECISION_ACTION_TYPE_NO_ACTION: _ClassVar[DecisionActionType]
    DECISION_ACTION_TYPE_CUSTOM: _ClassVar[DecisionActionType]

class MissionAutonomyCommand(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COMMAND_UNSPECIFIED: _ClassVar[MissionAutonomyCommand]
    CREATE_MISSION: _ClassVar[MissionAutonomyCommand]
    UPDATE_MISSION: _ClassVar[MissionAutonomyCommand]
    DELETE_MISSION: _ClassVar[MissionAutonomyCommand]
    CREATE_TASK: _ClassVar[MissionAutonomyCommand]
    UPDATE_TASK: _ClassVar[MissionAutonomyCommand]
    DELETE_TASK: _ClassVar[MissionAutonomyCommand]
    GET_MISSION_BY_ID: _ClassVar[MissionAutonomyCommand]
    GET_ALL_MISSIONS: _ClassVar[MissionAutonomyCommand]
    GET_TASK_BY_FLIGHT_ID: _ClassVar[MissionAutonomyCommand]
    GET_ALL_TASKS_FOR_MISSION: _ClassVar[MissionAutonomyCommand]
    GET_ALL_TASKS_FOR_ASSET: _ClassVar[MissionAutonomyCommand]
    PREPARE_TASK: _ClassVar[MissionAutonomyCommand]
    START_TASK: _ClassVar[MissionAutonomyCommand]
    CANCEL_TASK: _ClassVar[MissionAutonomyCommand]
    UPLOAD_TASK_TO_STORAGE: _ClassVar[MissionAutonomyCommand]
    MISSION_EVENTS: _ClassVar[MissionAutonomyCommand]
    REGISTER_TASK_ON_ASSET: _ClassVar[MissionAutonomyCommand]
    PAUSE_TASK: _ClassVar[MissionAutonomyCommand]
    RESUME_TASK: _ClassVar[MissionAutonomyCommand]

class VehicleAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VEHICLE_ACTION_NONE: _ClassVar[VehicleAction]
    VEHICLE_ACTION_TAKEOFF: _ClassVar[VehicleAction]
    VEHICLE_ACTION_LAND: _ClassVar[VehicleAction]

class FlyToWaylineModeProto(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FTW_MODE_SAFELY: _ClassVar[FlyToWaylineModeProto]
    FTW_MODE_POINT_TO_POINT: _ClassVar[FlyToWaylineModeProto]

class WaylineFinishActionProto(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WF_ACTION_GO_HOME: _ClassVar[WaylineFinishActionProto]
    WF_ACTION_NO_ACTION: _ClassVar[WaylineFinishActionProto]
    WF_ACTION_AUTO_LANDING: _ClassVar[WaylineFinishActionProto]
    WF_ACTION_GOTO_FIRST_WAYPOINT: _ClassVar[WaylineFinishActionProto]
    WF_ACTION_STOP: _ClassVar[WaylineFinishActionProto]

class ExitWaylineWhenRcLostEnumProto(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EWWRL_CONTINUE: _ClassVar[ExitWaylineWhenRcLostEnumProto]
    EWWRL_EXECUTE_RC_LOST_ACTION: _ClassVar[ExitWaylineWhenRcLostEnumProto]

class RcLostActionEnumProto(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RC_LOST_ACTION_HOVER: _ClassVar[RcLostActionEnumProto]
    RC_LOST_ACTION_LAND: _ClassVar[RcLostActionEnumProto]
    RC_LOST_ACTION_RETURN_HOME: _ClassVar[RcLostActionEnumProto]

class WaylineTypeEnumProto(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WT_WAYPOINT: _ClassVar[WaylineTypeEnumProto]
    WT_MAPPING_2D: _ClassVar[WaylineTypeEnumProto]
    WT_MAPPING_3D: _ClassVar[WaylineTypeEnumProto]
    WT_MAPPING_STRIP: _ClassVar[WaylineTypeEnumProto]

class WaylineTurnModeProto(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WT_MODE_COORDINATE_TURN: _ClassVar[WaylineTurnModeProto]
    WT_MODE_TO_POINT_AND_STOP_WITH_DISCONTINUITY_CURVATURE: _ClassVar[WaylineTurnModeProto]
    WT_MODE_TO_POINT_AND_STOP_WITH_CONTINUITY_CURVATURE: _ClassVar[WaylineTurnModeProto]
    WT_MODE_TO_POINT_AND_PASS_WITH_CONTINUITY_CURVATURE: _ClassVar[WaylineTurnModeProto]

class WaylineGimbalPitchModeProto(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WGP_MODE_MANUAL: _ClassVar[WaylineGimbalPitchModeProto]
    WGP_MODE_POINT_SETTINGS: _ClassVar[WaylineGimbalPitchModeProto]
    WGP_MODE_LOOK_DOWN: _ClassVar[WaylineGimbalPitchModeProto]

class RthModeEnumProto(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RTH_MODE_OPTIMAL: _ClassVar[RthModeEnumProto]
    RTH_MODE_PRESET: _ClassVar[RthModeEnumProto]

class OutOfControlActionEnumProto(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OOC_RETURN_TO_HOME: _ClassVar[OutOfControlActionEnumProto]
    OOC_HOVERING: _ClassVar[OutOfControlActionEnumProto]
    OOC_LANDING: _ClassVar[OutOfControlActionEnumProto]

class WaylinePrecisionTypeEnumProto(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRECISION_GPS: _ClassVar[WaylinePrecisionTypeEnumProto]
    PRECISION_RTK: _ClassVar[WaylinePrecisionTypeEnumProto]

class FlighttaskBreakReasonEnumProto(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BREAK_REASON_NORMAL: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_NOT_ID: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_UNCOMMON_ERROR: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_ERROR_LOADING_FILE: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_ERROR_BREAKPOINT_FILE: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_INCORRECT_PARAMETER: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_PARSING_FILE_TIMEOUT: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_ALREADY_STARTED: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_UNABLE_TO_INTERRUPT_WAYLINE: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_NOT_STARTED: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_FLIGHT_MISSION_CONFLICT: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_UNABLE_TO_RESUME_WAYLINE: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_MAXIMUM_ALTITUDE_LIMIT: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_MAXIMUM_DISTANCE_LIMIT: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_TOO_LOW_HEIGHT: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_OBSTACLE_AVOIDANCE: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_POOR_RTK: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_BOUNDARY_OF_RESTRICTED_ZONE: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_GEO_ALTITUDE_LIMIT: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_TAKEOFF_REQUEST_FAILED: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_TAKEOFF_EXECUTION_FAILED: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_WAYLINE_MISSION_REQUEST_FAILED: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_RTK_FIXING_REQUEST_FAILED: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_RTK_FIXING_EXECUTION_FAILED: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_WEAK_GPS: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_ERROR_RC_MODE: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_HOME_POINT_NOT_REFRESHED: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_LOW_BATTERY: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_LOW_BATTERY_RTH: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_RC_DISCONNECTION: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_ON_THE_GROUND: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_ABNORMAL_VISUAL_STATUS: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_INVALID_ALTITUDE: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_CALCULATION_ERROR: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_STRONG_WINDS_RTH: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_USER_EXIT: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_USER_INTERRUPTION: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_USER_TRIGGERED_RTH: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_INCORRECT_START_INFORMATION: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_UNSUPPORTED_COORDINATE_SYSTEM: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_UNSUPPORTED_ALTITUDE_MODE: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_UNSUPPORTED_TRANSITIONAL_WAYLINE_MODE: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_UNSUPPORTED_YAW_MODE: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_UNSUPPORTED_YAW_DIRECTION_REVERSAL_MODE: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_UNSUPPORTED_WAYPOINT_TYPE: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_INVALID_COORDINATED_TURNING_TYPE: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_INVALID_GLOBAL_SPEED: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_WAYPOINT_NUMBER_ABNORMAL: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_INVALID_LATITUDE_AND_LONGITUDE: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_ABNORMAL_TURNING_INTERCEPT: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_INVALID_SEGMENT_MAXIMUM_SPEED: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_INVALID_TARGET_SPEED: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_INVALID_YAW_ANGLE: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_BREAKPOINT_INVALID_MISSION_ID: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_BREAKPOINT_INVALID_PROGRESS_INFORMATION: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_BREAKPOINT_ERROR_MISSION_STATE: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_BREAKPOINT_INVALID_INDEX_INFORMATION: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_BREAKPOINT_INCORRECT_LATITUDE_AND_LONGITUDE: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_BREAKPOINT_INVALID_YAW: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_BREAKPOINT_INCORRECT_FLAG_SETTING: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_WAYLINE_GENERATION_FAILED: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_WAYLINE_EXECUTION_FAILED: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_WAYLINE_OBSTACLE_SENSING: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_UNRECOGNIZED_ACTION_TYPE: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_DUPLICATE_ACTION_ID: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_ACTION_ID_NOT_65535: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_INVALID_NUMBER_OF_ACTION_GROUPS: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_ERROR_EFFECTIVE_RANGE: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_BREAKPOINT_INVALID_ACTION_INDEX: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_BREAKPOINT_TRIGGER_RUNNING_ABNORMAL: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_BREAKPOINT_DUPLICATE_ACTION_GROUP_ID: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_BREAKPOINT_DUPLICATE_ACTION_GROUP_POSITION: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_BREAKPOINT_INVALID_ACTION_GROUP_POSITION: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_BREAKPOINT_INVALID_ACTION_ID: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_BREAKPOINT_UNABLE_TO_INTERRUPT: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_INCORRECT_BREAKPOINT_INFORMATION: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_BREAKPOINT_UNRECOGNIZED_ACTION_TYPE: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_BREAKPOINT_UNRECOGNIZED_TRIGGER_TYPE: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_UNKNOWN_ERROR_1: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_UNKNOWN_ERROR_2: _ClassVar[FlighttaskBreakReasonEnumProto]

class TaskGoal(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TASK_UNDEFINED: _ClassVar[TaskGoal]
    TRACK: _ClassVar[TaskGoal]
    FOLLOW: _ClassVar[TaskGoal]
    SIMPLE: _ClassVar[TaskGoal]
    DETECT: _ClassVar[TaskGoal]

class TaskTypeProto(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TASK_TYPE_UNSPECIFIED: _ClassVar[TaskTypeProto]
    TASK_TYPE_DETECT: _ClassVar[TaskTypeProto]
    TASK_TYPE_AREA_MAPPING: _ClassVar[TaskTypeProto]
    TASK_TYPE_WAYPOINT: _ClassVar[TaskTypeProto]
    TASK_TYPE_POI: _ClassVar[TaskTypeProto]
    TASK_TYPE_FOLLOW: _ClassVar[TaskTypeProto]
    TASK_TYPE_TRACK: _ClassVar[TaskTypeProto]
    TASK_TYPE_COUNTER_DRONE: _ClassVar[TaskTypeProto]
    TASK_TYPE_TAKE_OFF: _ClassVar[TaskTypeProto]
    TASK_TYPE_GO_TO: _ClassVar[TaskTypeProto]
    TASK_TYPE_RETURN_TO_HOME: _ClassVar[TaskTypeProto]
    TASK_TYPE_ENTER_MANUAL_CONTROL: _ClassVar[TaskTypeProto]
    TASK_TYPE_EXIT_MANUAL_CONTROL: _ClassVar[TaskTypeProto]
    TASK_TYPE_LOOK_AT: _ClassVar[TaskTypeProto]
    TASK_TYPE_TAKE_PHOTO: _ClassVar[TaskTypeProto]
    TASK_TYPE_OPEN_COVER: _ClassVar[TaskTypeProto]
    TASK_TYPE_CLOSE_COVER: _ClassVar[TaskTypeProto]
    TASK_TYPE_START_CHARGING: _ClassVar[TaskTypeProto]
    TASK_TYPE_STOP_CHARGING: _ClassVar[TaskTypeProto]
    TASK_TYPE_REBOOT_ASSET: _ClassVar[TaskTypeProto]
    TASK_TYPE_BOOT_SUB_ASSET: _ClassVar[TaskTypeProto]
    TASK_TYPE_REMOTE_DEBUG: _ClassVar[TaskTypeProto]
    TASK_TYPE_CHANGE_AC_MODE: _ClassVar[TaskTypeProto]
    TASK_TYPE_CUSTOM_COMMAND: _ClassVar[TaskTypeProto]
    TASK_TYPE_EXTERNAL: _ClassVar[TaskTypeProto]

class TaskStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TASK_UNKNOWN: _ClassVar[TaskStatus]
    TASK_DRAFT: _ClassVar[TaskStatus]
    TASK_SCHEDULED: _ClassVar[TaskStatus]
    TASK_RUNNING: _ClassVar[TaskStatus]
    TASK_ERROR: _ClassVar[TaskStatus]
    TASK_COMPLETED: _ClassVar[TaskStatus]
    TASK_PREPARED: _ClassVar[TaskStatus]
    TASK_PAUSED: _ClassVar[TaskStatus]

class MissionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MISSION_TYPE_UNSPECIFIED: _ClassVar[MissionType]
    MISSION_TYPE_AREA_SCAN: _ClassVar[MissionType]
    MISSION_TYPE_POINT_INSPECTION: _ClassVar[MissionType]
    MISSION_TYPE_ROUTE_INSPECTION: _ClassVar[MissionType]
    MISSION_TYPE_PERIMETER_PATROL: _ClassVar[MissionType]
    MISSION_TYPE_ROUTE_PATROL: _ClassVar[MissionType]
    MISSION_TYPE_LIVE_OBSERVATION: _ClassVar[MissionType]
    MISSION_TYPE_TARGET_TRACKING: _ClassVar[MissionType]
    MISSION_TYPE_CROWD_MONITORING: _ClassVar[MissionType]
    MISSION_TYPE_THERMAL_SCAN: _ClassVar[MissionType]
    MISSION_TYPE_MULTISPECTRAL_SCAN: _ClassVar[MissionType]
    MISSION_TYPE_3D_MAPPING: _ClassVar[MissionType]
    MISSION_TYPE_PHOTOGRAMMETRY: _ClassVar[MissionType]
    MISSION_TYPE_DAMAGE_ASSESSMENT: _ClassVar[MissionType]
    MISSION_TYPE_SITUATIONAL_ASSESSMENT: _ClassVar[MissionType]
    MISSION_TYPE_SEARCH: _ClassVar[MissionType]
    MISSION_TYPE_PAYLOAD_DELIVERY: _ClassVar[MissionType]
    MISSION_TYPE_COMMUNICATION_RELAY: _ClassVar[MissionType]
    MISSION_TYPE_DATA_COLLECTION: _ClassVar[MissionType]
    MISSION_TYPE_SECURITY_SWEEP: _ClassVar[MissionType]
    MISSION_TYPE_HAZARD_DETECTION: _ClassVar[MissionType]
    MISSION_TYPE_GAS_DETECTION: _ClassVar[MissionType]
    MISSION_TYPE_RADIATION_DETECTION: _ClassVar[MissionType]
    MISSION_TYPE_CUSTOM: _ClassVar[MissionType]

class MissionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MISSION_STATUS_UNKNOWN: _ClassVar[MissionStatus]
    MISSION_STATUS_DRAFT: _ClassVar[MissionStatus]
    MISSION_STATUS_ACTIVE: _ClassVar[MissionStatus]
    MISSION_STATUS_INACTIVE: _ClassVar[MissionStatus]
    MISSION_STATUS_ERROR: _ClassVar[MissionStatus]
SCHEDULER_FIRING_OUTCOME_UNSPECIFIED: SchedulerFiringOutcome
SCHEDULER_FIRING_OUTCOME_STARTED: SchedulerFiringOutcome
SCHEDULER_FIRING_OUTCOME_SKIPPED: SchedulerFiringOutcome
SCHEDULER_FIRING_OUTCOME_FAILED: SchedulerFiringOutcome
SCHEDULER_TYPE_MISSION: SchedulerType
SCHEDULER_TYPE_TASK: SchedulerType
SCHEDULER_TYPE_SYSTEM_JOBS: SchedulerType
SCHEDULER_TYPE_ORGANIZATION: SchedulerType
SCHEDULER_TYPE_DATABASE: SchedulerType
SCHEDULER_TYPE_CONNECTORS: SchedulerType
GEO_AREA_TYPE_UNSPECIFIED: GeoAreaType
GEO_AREA_TYPE_POLYGON: GeoAreaType
GEO_AREA_TYPE_CIRCLE: GeoAreaType
GEO_AREA_TYPE_GEO_JSON: GeoAreaType
GEO_AREA_TYPE_BOUNDING_BOX: GeoAreaType
MISSION_ZONE_TYPE_UNSPECIFIED: MissionZoneType
MISSION_ZONE_TYPE_NO_FLY: MissionZoneType
MISSION_ZONE_TYPE_KEEP_IN: MissionZoneType
MISSION_ZONE_TYPE_TAKEOFF_LANDING: MissionZoneType
MISSION_ZONE_TYPE_OBSERVATION: MissionZoneType
MISSION_ZONE_TYPE_DANGER: MissionZoneType
MISSION_ZONE_TYPE_PRIVACY: MissionZoneType
MISSION_ZONE_TYPE_CUSTOM: MissionZoneType
ZONE_ENFORCEMENT_TYPE_UNSPECIFIED: ZoneEnforcementType
ZONE_ENFORCEMENT_TYPE_ADVISORY: ZoneEnforcementType
ZONE_ENFORCEMENT_TYPE_REQUIRE_APPROVAL: ZoneEnforcementType
ZONE_ENFORCEMENT_TYPE_HARD_BLOCK: ZoneEnforcementType
EXECUTION_STRATEGY_UNSPECIFIED: ExecutionStrategy
EXECUTION_STRATEGY_SEQUENTIAL: ExecutionStrategy
EXECUTION_STRATEGY_PARALLEL: ExecutionStrategy
EXECUTION_STRATEGY_CONDITIONAL: ExecutionStrategy
EXECUTION_STRATEGY_PRIORITY: ExecutionStrategy
FAILURE_STRATEGY_UNSPECIFIED: FailureStrategy
FAILURE_STRATEGY_STOP_MISSION: FailureStrategy
FAILURE_STRATEGY_SKIP_TASK: FailureStrategy
FAILURE_STRATEGY_RETRY_TASK: FailureStrategy
FAILURE_STRATEGY_REQUIRE_HUMAN_APPROVAL: FailureStrategy
FAILURE_STRATEGY_CUSTOM: FailureStrategy
WORKFLOW_STEP_TYPE_UNSPECIFIED: WorkflowStepType
WORKFLOW_STEP_TYPE_TASK: WorkflowStepType
WORKFLOW_STEP_TYPE_DECISION: WorkflowStepType
WORKFLOW_STEP_TYPE_WAIT: WorkflowStepType
WORKFLOW_STEP_TYPE_NOTIFICATION: WorkflowStepType
WORKFLOW_STEP_TYPE_CUSTOM_COMMAND: WorkflowStepType
WORKFLOW_STEP_TYPE_CUSTOM: WorkflowStepType
WORKFLOW_STEP_STATUS_UNSPECIFIED: WorkflowStepStatus
WORKFLOW_STEP_STATUS_PENDING: WorkflowStepStatus
WORKFLOW_STEP_STATUS_READY: WorkflowStepStatus
WORKFLOW_STEP_STATUS_RUNNING: WorkflowStepStatus
WORKFLOW_STEP_STATUS_BLOCKED: WorkflowStepStatus
WORKFLOW_STEP_STATUS_COMPLETED: WorkflowStepStatus
WORKFLOW_STEP_STATUS_SKIPPED: WorkflowStepStatus
WORKFLOW_STEP_STATUS_ERROR: WorkflowStepStatus
AUTONOMY_MODE_UNSPECIFIED: AutonomyMode
AUTONOMY_MODE_MANUAL_APPROVAL: AutonomyMode
AUTONOMY_MODE_SUPERVISED: AutonomyMode
AUTONOMY_MODE_AUTONOMOUS: AutonomyMode
DECISION_STRATEGY_TYPE_UNSPECIFIED: DecisionStrategyType
DECISION_STRATEGY_TYPE_RULE_BASED: DecisionStrategyType
DECISION_STRATEGY_TYPE_SCORE_BASED: DecisionStrategyType
DECISION_STRATEGY_TYPE_POLICY_BASED: DecisionStrategyType
DECISION_STRATEGY_TYPE_AI_ASSISTED: DecisionStrategyType
DECISION_STRATEGY_TYPE_CUSTOM: DecisionStrategyType
DECISION_TRIGGER_TYPE_UNSPECIFIED: DecisionTriggerType
DECISION_TRIGGER_TYPE_DETECTION: DecisionTriggerType
DECISION_TRIGGER_TYPE_TELEMETRY: DecisionTriggerType
DECISION_TRIGGER_TYPE_TASK_STATE: DecisionTriggerType
DECISION_TRIGGER_TYPE_MISSION_STATE: DecisionTriggerType
DECISION_TRIGGER_TYPE_SCHEDULE: DecisionTriggerType
DECISION_TRIGGER_TYPE_MANUAL: DecisionTriggerType
DECISION_TRIGGER_TYPE_EXTERNAL: DecisionTriggerType
DECISION_ACTION_TYPE_UNSPECIFIED: DecisionActionType
DECISION_ACTION_TYPE_START_TASK: DecisionActionType
DECISION_ACTION_TYPE_STOP_TASK: DecisionActionType
DECISION_ACTION_TYPE_PAUSE_TASK: DecisionActionType
DECISION_ACTION_TYPE_RESUME_TASK: DecisionActionType
DECISION_ACTION_TYPE_CREATE_TASK: DecisionActionType
DECISION_ACTION_TYPE_ASSIGN_ASSET: DecisionActionType
DECISION_ACTION_TYPE_CHANGE_TASK_CONFIG: DecisionActionType
DECISION_ACTION_TYPE_CHANGE_MISSION_CONFIG: DecisionActionType
DECISION_ACTION_TYPE_NOTIFY: DecisionActionType
DECISION_ACTION_TYPE_CUSTOM_COMMAND: DecisionActionType
DECISION_ACTION_TYPE_NO_ACTION: DecisionActionType
DECISION_ACTION_TYPE_CUSTOM: DecisionActionType
COMMAND_UNSPECIFIED: MissionAutonomyCommand
CREATE_MISSION: MissionAutonomyCommand
UPDATE_MISSION: MissionAutonomyCommand
DELETE_MISSION: MissionAutonomyCommand
CREATE_TASK: MissionAutonomyCommand
UPDATE_TASK: MissionAutonomyCommand
DELETE_TASK: MissionAutonomyCommand
GET_MISSION_BY_ID: MissionAutonomyCommand
GET_ALL_MISSIONS: MissionAutonomyCommand
GET_TASK_BY_FLIGHT_ID: MissionAutonomyCommand
GET_ALL_TASKS_FOR_MISSION: MissionAutonomyCommand
GET_ALL_TASKS_FOR_ASSET: MissionAutonomyCommand
PREPARE_TASK: MissionAutonomyCommand
START_TASK: MissionAutonomyCommand
CANCEL_TASK: MissionAutonomyCommand
UPLOAD_TASK_TO_STORAGE: MissionAutonomyCommand
MISSION_EVENTS: MissionAutonomyCommand
REGISTER_TASK_ON_ASSET: MissionAutonomyCommand
PAUSE_TASK: MissionAutonomyCommand
RESUME_TASK: MissionAutonomyCommand
VEHICLE_ACTION_NONE: VehicleAction
VEHICLE_ACTION_TAKEOFF: VehicleAction
VEHICLE_ACTION_LAND: VehicleAction
FTW_MODE_SAFELY: FlyToWaylineModeProto
FTW_MODE_POINT_TO_POINT: FlyToWaylineModeProto
WF_ACTION_GO_HOME: WaylineFinishActionProto
WF_ACTION_NO_ACTION: WaylineFinishActionProto
WF_ACTION_AUTO_LANDING: WaylineFinishActionProto
WF_ACTION_GOTO_FIRST_WAYPOINT: WaylineFinishActionProto
WF_ACTION_STOP: WaylineFinishActionProto
EWWRL_CONTINUE: ExitWaylineWhenRcLostEnumProto
EWWRL_EXECUTE_RC_LOST_ACTION: ExitWaylineWhenRcLostEnumProto
RC_LOST_ACTION_HOVER: RcLostActionEnumProto
RC_LOST_ACTION_LAND: RcLostActionEnumProto
RC_LOST_ACTION_RETURN_HOME: RcLostActionEnumProto
WT_WAYPOINT: WaylineTypeEnumProto
WT_MAPPING_2D: WaylineTypeEnumProto
WT_MAPPING_3D: WaylineTypeEnumProto
WT_MAPPING_STRIP: WaylineTypeEnumProto
WT_MODE_COORDINATE_TURN: WaylineTurnModeProto
WT_MODE_TO_POINT_AND_STOP_WITH_DISCONTINUITY_CURVATURE: WaylineTurnModeProto
WT_MODE_TO_POINT_AND_STOP_WITH_CONTINUITY_CURVATURE: WaylineTurnModeProto
WT_MODE_TO_POINT_AND_PASS_WITH_CONTINUITY_CURVATURE: WaylineTurnModeProto
WGP_MODE_MANUAL: WaylineGimbalPitchModeProto
WGP_MODE_POINT_SETTINGS: WaylineGimbalPitchModeProto
WGP_MODE_LOOK_DOWN: WaylineGimbalPitchModeProto
RTH_MODE_OPTIMAL: RthModeEnumProto
RTH_MODE_PRESET: RthModeEnumProto
OOC_RETURN_TO_HOME: OutOfControlActionEnumProto
OOC_HOVERING: OutOfControlActionEnumProto
OOC_LANDING: OutOfControlActionEnumProto
PRECISION_GPS: WaylinePrecisionTypeEnumProto
PRECISION_RTK: WaylinePrecisionTypeEnumProto
BREAK_REASON_NORMAL: FlighttaskBreakReasonEnumProto
BREAK_REASON_NOT_ID: FlighttaskBreakReasonEnumProto
BREAK_REASON_UNCOMMON_ERROR: FlighttaskBreakReasonEnumProto
BREAK_REASON_ERROR_LOADING_FILE: FlighttaskBreakReasonEnumProto
BREAK_REASON_ERROR_BREAKPOINT_FILE: FlighttaskBreakReasonEnumProto
BREAK_REASON_INCORRECT_PARAMETER: FlighttaskBreakReasonEnumProto
BREAK_REASON_PARSING_FILE_TIMEOUT: FlighttaskBreakReasonEnumProto
BREAK_REASON_ALREADY_STARTED: FlighttaskBreakReasonEnumProto
BREAK_REASON_UNABLE_TO_INTERRUPT_WAYLINE: FlighttaskBreakReasonEnumProto
BREAK_REASON_NOT_STARTED: FlighttaskBreakReasonEnumProto
BREAK_REASON_FLIGHT_MISSION_CONFLICT: FlighttaskBreakReasonEnumProto
BREAK_REASON_UNABLE_TO_RESUME_WAYLINE: FlighttaskBreakReasonEnumProto
BREAK_REASON_MAXIMUM_ALTITUDE_LIMIT: FlighttaskBreakReasonEnumProto
BREAK_REASON_MAXIMUM_DISTANCE_LIMIT: FlighttaskBreakReasonEnumProto
BREAK_REASON_TOO_LOW_HEIGHT: FlighttaskBreakReasonEnumProto
BREAK_REASON_OBSTACLE_AVOIDANCE: FlighttaskBreakReasonEnumProto
BREAK_REASON_POOR_RTK: FlighttaskBreakReasonEnumProto
BREAK_REASON_BOUNDARY_OF_RESTRICTED_ZONE: FlighttaskBreakReasonEnumProto
BREAK_REASON_GEO_ALTITUDE_LIMIT: FlighttaskBreakReasonEnumProto
BREAK_REASON_TAKEOFF_REQUEST_FAILED: FlighttaskBreakReasonEnumProto
BREAK_REASON_TAKEOFF_EXECUTION_FAILED: FlighttaskBreakReasonEnumProto
BREAK_REASON_WAYLINE_MISSION_REQUEST_FAILED: FlighttaskBreakReasonEnumProto
BREAK_REASON_RTK_FIXING_REQUEST_FAILED: FlighttaskBreakReasonEnumProto
BREAK_REASON_RTK_FIXING_EXECUTION_FAILED: FlighttaskBreakReasonEnumProto
BREAK_REASON_WEAK_GPS: FlighttaskBreakReasonEnumProto
BREAK_REASON_ERROR_RC_MODE: FlighttaskBreakReasonEnumProto
BREAK_REASON_HOME_POINT_NOT_REFRESHED: FlighttaskBreakReasonEnumProto
BREAK_REASON_LOW_BATTERY: FlighttaskBreakReasonEnumProto
BREAK_REASON_LOW_BATTERY_RTH: FlighttaskBreakReasonEnumProto
BREAK_REASON_RC_DISCONNECTION: FlighttaskBreakReasonEnumProto
BREAK_REASON_ON_THE_GROUND: FlighttaskBreakReasonEnumProto
BREAK_REASON_ABNORMAL_VISUAL_STATUS: FlighttaskBreakReasonEnumProto
BREAK_REASON_INVALID_ALTITUDE: FlighttaskBreakReasonEnumProto
BREAK_REASON_CALCULATION_ERROR: FlighttaskBreakReasonEnumProto
BREAK_REASON_STRONG_WINDS_RTH: FlighttaskBreakReasonEnumProto
BREAK_REASON_USER_EXIT: FlighttaskBreakReasonEnumProto
BREAK_REASON_USER_INTERRUPTION: FlighttaskBreakReasonEnumProto
BREAK_REASON_USER_TRIGGERED_RTH: FlighttaskBreakReasonEnumProto
BREAK_REASON_INCORRECT_START_INFORMATION: FlighttaskBreakReasonEnumProto
BREAK_REASON_UNSUPPORTED_COORDINATE_SYSTEM: FlighttaskBreakReasonEnumProto
BREAK_REASON_UNSUPPORTED_ALTITUDE_MODE: FlighttaskBreakReasonEnumProto
BREAK_REASON_UNSUPPORTED_TRANSITIONAL_WAYLINE_MODE: FlighttaskBreakReasonEnumProto
BREAK_REASON_UNSUPPORTED_YAW_MODE: FlighttaskBreakReasonEnumProto
BREAK_REASON_UNSUPPORTED_YAW_DIRECTION_REVERSAL_MODE: FlighttaskBreakReasonEnumProto
BREAK_REASON_UNSUPPORTED_WAYPOINT_TYPE: FlighttaskBreakReasonEnumProto
BREAK_REASON_INVALID_COORDINATED_TURNING_TYPE: FlighttaskBreakReasonEnumProto
BREAK_REASON_INVALID_GLOBAL_SPEED: FlighttaskBreakReasonEnumProto
BREAK_REASON_WAYPOINT_NUMBER_ABNORMAL: FlighttaskBreakReasonEnumProto
BREAK_REASON_INVALID_LATITUDE_AND_LONGITUDE: FlighttaskBreakReasonEnumProto
BREAK_REASON_ABNORMAL_TURNING_INTERCEPT: FlighttaskBreakReasonEnumProto
BREAK_REASON_INVALID_SEGMENT_MAXIMUM_SPEED: FlighttaskBreakReasonEnumProto
BREAK_REASON_INVALID_TARGET_SPEED: FlighttaskBreakReasonEnumProto
BREAK_REASON_INVALID_YAW_ANGLE: FlighttaskBreakReasonEnumProto
BREAK_REASON_BREAKPOINT_INVALID_MISSION_ID: FlighttaskBreakReasonEnumProto
BREAK_REASON_BREAKPOINT_INVALID_PROGRESS_INFORMATION: FlighttaskBreakReasonEnumProto
BREAK_REASON_BREAKPOINT_ERROR_MISSION_STATE: FlighttaskBreakReasonEnumProto
BREAK_REASON_BREAKPOINT_INVALID_INDEX_INFORMATION: FlighttaskBreakReasonEnumProto
BREAK_REASON_BREAKPOINT_INCORRECT_LATITUDE_AND_LONGITUDE: FlighttaskBreakReasonEnumProto
BREAK_REASON_BREAKPOINT_INVALID_YAW: FlighttaskBreakReasonEnumProto
BREAK_REASON_BREAKPOINT_INCORRECT_FLAG_SETTING: FlighttaskBreakReasonEnumProto
BREAK_REASON_WAYLINE_GENERATION_FAILED: FlighttaskBreakReasonEnumProto
BREAK_REASON_WAYLINE_EXECUTION_FAILED: FlighttaskBreakReasonEnumProto
BREAK_REASON_WAYLINE_OBSTACLE_SENSING: FlighttaskBreakReasonEnumProto
BREAK_REASON_UNRECOGNIZED_ACTION_TYPE: FlighttaskBreakReasonEnumProto
BREAK_REASON_DUPLICATE_ACTION_ID: FlighttaskBreakReasonEnumProto
BREAK_REASON_ACTION_ID_NOT_65535: FlighttaskBreakReasonEnumProto
BREAK_REASON_INVALID_NUMBER_OF_ACTION_GROUPS: FlighttaskBreakReasonEnumProto
BREAK_REASON_ERROR_EFFECTIVE_RANGE: FlighttaskBreakReasonEnumProto
BREAK_REASON_BREAKPOINT_INVALID_ACTION_INDEX: FlighttaskBreakReasonEnumProto
BREAK_REASON_BREAKPOINT_TRIGGER_RUNNING_ABNORMAL: FlighttaskBreakReasonEnumProto
BREAK_REASON_BREAKPOINT_DUPLICATE_ACTION_GROUP_ID: FlighttaskBreakReasonEnumProto
BREAK_REASON_BREAKPOINT_DUPLICATE_ACTION_GROUP_POSITION: FlighttaskBreakReasonEnumProto
BREAK_REASON_BREAKPOINT_INVALID_ACTION_GROUP_POSITION: FlighttaskBreakReasonEnumProto
BREAK_REASON_BREAKPOINT_INVALID_ACTION_ID: FlighttaskBreakReasonEnumProto
BREAK_REASON_BREAKPOINT_UNABLE_TO_INTERRUPT: FlighttaskBreakReasonEnumProto
BREAK_REASON_INCORRECT_BREAKPOINT_INFORMATION: FlighttaskBreakReasonEnumProto
BREAK_REASON_BREAKPOINT_UNRECOGNIZED_ACTION_TYPE: FlighttaskBreakReasonEnumProto
BREAK_REASON_BREAKPOINT_UNRECOGNIZED_TRIGGER_TYPE: FlighttaskBreakReasonEnumProto
BREAK_REASON_UNKNOWN_ERROR_1: FlighttaskBreakReasonEnumProto
BREAK_REASON_UNKNOWN_ERROR_2: FlighttaskBreakReasonEnumProto
TASK_UNDEFINED: TaskGoal
TRACK: TaskGoal
FOLLOW: TaskGoal
SIMPLE: TaskGoal
DETECT: TaskGoal
TASK_TYPE_UNSPECIFIED: TaskTypeProto
TASK_TYPE_DETECT: TaskTypeProto
TASK_TYPE_AREA_MAPPING: TaskTypeProto
TASK_TYPE_WAYPOINT: TaskTypeProto
TASK_TYPE_POI: TaskTypeProto
TASK_TYPE_FOLLOW: TaskTypeProto
TASK_TYPE_TRACK: TaskTypeProto
TASK_TYPE_COUNTER_DRONE: TaskTypeProto
TASK_TYPE_TAKE_OFF: TaskTypeProto
TASK_TYPE_GO_TO: TaskTypeProto
TASK_TYPE_RETURN_TO_HOME: TaskTypeProto
TASK_TYPE_ENTER_MANUAL_CONTROL: TaskTypeProto
TASK_TYPE_EXIT_MANUAL_CONTROL: TaskTypeProto
TASK_TYPE_LOOK_AT: TaskTypeProto
TASK_TYPE_TAKE_PHOTO: TaskTypeProto
TASK_TYPE_OPEN_COVER: TaskTypeProto
TASK_TYPE_CLOSE_COVER: TaskTypeProto
TASK_TYPE_START_CHARGING: TaskTypeProto
TASK_TYPE_STOP_CHARGING: TaskTypeProto
TASK_TYPE_REBOOT_ASSET: TaskTypeProto
TASK_TYPE_BOOT_SUB_ASSET: TaskTypeProto
TASK_TYPE_REMOTE_DEBUG: TaskTypeProto
TASK_TYPE_CHANGE_AC_MODE: TaskTypeProto
TASK_TYPE_CUSTOM_COMMAND: TaskTypeProto
TASK_TYPE_EXTERNAL: TaskTypeProto
TASK_UNKNOWN: TaskStatus
TASK_DRAFT: TaskStatus
TASK_SCHEDULED: TaskStatus
TASK_RUNNING: TaskStatus
TASK_ERROR: TaskStatus
TASK_COMPLETED: TaskStatus
TASK_PREPARED: TaskStatus
TASK_PAUSED: TaskStatus
MISSION_TYPE_UNSPECIFIED: MissionType
MISSION_TYPE_AREA_SCAN: MissionType
MISSION_TYPE_POINT_INSPECTION: MissionType
MISSION_TYPE_ROUTE_INSPECTION: MissionType
MISSION_TYPE_PERIMETER_PATROL: MissionType
MISSION_TYPE_ROUTE_PATROL: MissionType
MISSION_TYPE_LIVE_OBSERVATION: MissionType
MISSION_TYPE_TARGET_TRACKING: MissionType
MISSION_TYPE_CROWD_MONITORING: MissionType
MISSION_TYPE_THERMAL_SCAN: MissionType
MISSION_TYPE_MULTISPECTRAL_SCAN: MissionType
MISSION_TYPE_3D_MAPPING: MissionType
MISSION_TYPE_PHOTOGRAMMETRY: MissionType
MISSION_TYPE_DAMAGE_ASSESSMENT: MissionType
MISSION_TYPE_SITUATIONAL_ASSESSMENT: MissionType
MISSION_TYPE_SEARCH: MissionType
MISSION_TYPE_PAYLOAD_DELIVERY: MissionType
MISSION_TYPE_COMMUNICATION_RELAY: MissionType
MISSION_TYPE_DATA_COLLECTION: MissionType
MISSION_TYPE_SECURITY_SWEEP: MissionType
MISSION_TYPE_HAZARD_DETECTION: MissionType
MISSION_TYPE_GAS_DETECTION: MissionType
MISSION_TYPE_RADIATION_DETECTION: MissionType
MISSION_TYPE_CUSTOM: MissionType
MISSION_STATUS_UNKNOWN: MissionStatus
MISSION_STATUS_DRAFT: MissionStatus
MISSION_STATUS_ACTIVE: MissionStatus
MISSION_STATUS_INACTIVE: MissionStatus
MISSION_STATUS_ERROR: MissionStatus

class DynamicConfigProto(_message.Message):
    __slots__ = ("template_id", "template_version", "template_config", "overrides", "decision_config", "decision_engine_enabled")
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_VERSION_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    OVERRIDES_FIELD_NUMBER: _ClassVar[int]
    DECISION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DECISION_ENGINE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    template_id: str
    template_version: str
    template_config: _struct_pb2.Struct
    overrides: _struct_pb2.Struct
    decision_config: _struct_pb2.Struct
    decision_engine_enabled: bool
    def __init__(self, template_id: _Optional[str] = ..., template_version: _Optional[str] = ..., template_config: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., overrides: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., decision_config: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., decision_engine_enabled: bool = ...) -> None: ...

class DynamicCommandTaskConfigProto(_message.Message):
    __slots__ = ("command_id", "target", "params", "expected_schema_version")
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_SCHEMA_VERSION_FIELD_NUMBER: _ClassVar[int]
    command_id: str
    target: _device_control_contracts_pb2.CapabilityTarget
    params: _struct_pb2.Struct
    expected_schema_version: str
    def __init__(self, command_id: _Optional[str] = ..., target: _Optional[_Union[_device_control_contracts_pb2.CapabilityTarget, _Mapping]] = ..., params: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., expected_schema_version: _Optional[str] = ...) -> None: ...

class DecisionTriggerProto(_message.Message):
    __slots__ = ("type", "event_type", "params")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    type: DecisionTriggerType
    event_type: str
    params: _struct_pb2.Struct
    def __init__(self, type: _Optional[_Union[DecisionTriggerType, str]] = ..., event_type: _Optional[str] = ..., params: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class DecisionConditionProto(_message.Message):
    __slots__ = ("field_path", "operator", "value")
    FIELD_PATH_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    field_path: str
    operator: str
    value: _struct_pb2.Value
    def __init__(self, field_path: _Optional[str] = ..., operator: _Optional[str] = ..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...

class DecisionConstraintProto(_message.Message):
    __slots__ = ("name", "params", "violation_action")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    VIOLATION_ACTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    params: _struct_pb2.Struct
    violation_action: str
    def __init__(self, name: _Optional[str] = ..., params: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., violation_action: _Optional[str] = ...) -> None: ...

class DecisionActionProto(_message.Message):
    __slots__ = ("type", "target_ref", "params")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TARGET_REF_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    type: DecisionActionType
    target_ref: str
    params: _struct_pb2.Struct
    def __init__(self, type: _Optional[_Union[DecisionActionType, str]] = ..., target_ref: _Optional[str] = ..., params: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class DecisionRuleProto(_message.Message):
    __slots__ = ("id", "name", "enabled", "priority", "triggers", "conditions", "constraints", "actions")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    enabled: bool
    priority: int
    triggers: _containers.RepeatedCompositeFieldContainer[DecisionTriggerProto]
    conditions: _containers.RepeatedCompositeFieldContainer[DecisionConditionProto]
    constraints: _containers.RepeatedCompositeFieldContainer[DecisionConstraintProto]
    actions: _containers.RepeatedCompositeFieldContainer[DecisionActionProto]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., enabled: bool = ..., priority: _Optional[int] = ..., triggers: _Optional[_Iterable[_Union[DecisionTriggerProto, _Mapping]]] = ..., conditions: _Optional[_Iterable[_Union[DecisionConditionProto, _Mapping]]] = ..., constraints: _Optional[_Iterable[_Union[DecisionConstraintProto, _Mapping]]] = ..., actions: _Optional[_Iterable[_Union[DecisionActionProto, _Mapping]]] = ...) -> None: ...

class AutonomyConfigProto(_message.Message):
    __slots__ = ("enabled", "mode", "strategy_type", "dynamic_config", "decision_rules", "policy_scope", "policy_scope_target", "require_human_approval", "min_confidence", "fallback_action")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    STRATEGY_TYPE_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DECISION_RULES_FIELD_NUMBER: _ClassVar[int]
    POLICY_SCOPE_FIELD_NUMBER: _ClassVar[int]
    POLICY_SCOPE_TARGET_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_HUMAN_APPROVAL_FIELD_NUMBER: _ClassVar[int]
    MIN_CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    FALLBACK_ACTION_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    mode: AutonomyMode
    strategy_type: DecisionStrategyType
    dynamic_config: DynamicConfigProto
    decision_rules: _containers.RepeatedCompositeFieldContainer[DecisionRuleProto]
    policy_scope: str
    policy_scope_target: str
    require_human_approval: bool
    min_confidence: float
    fallback_action: str
    def __init__(self, enabled: bool = ..., mode: _Optional[_Union[AutonomyMode, str]] = ..., strategy_type: _Optional[_Union[DecisionStrategyType, str]] = ..., dynamic_config: _Optional[_Union[DynamicConfigProto, _Mapping]] = ..., decision_rules: _Optional[_Iterable[_Union[DecisionRuleProto, _Mapping]]] = ..., policy_scope: _Optional[str] = ..., policy_scope_target: _Optional[str] = ..., require_human_approval: bool = ..., min_confidence: _Optional[float] = ..., fallback_action: _Optional[str] = ...) -> None: ...

class WaypointProtoDTO(_message.Message):
    __slots__ = ("latitude", "longitude", "altitude", "speed", "fly_trough", "vehicle_action", "wp_order", "gimbal_pitch")
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    FLY_TROUGH_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_ACTION_FIELD_NUMBER: _ClassVar[int]
    WP_ORDER_FIELD_NUMBER: _ClassVar[int]
    GIMBAL_PITCH_FIELD_NUMBER: _ClassVar[int]
    latitude: float
    longitude: float
    altitude: float
    speed: float
    fly_trough: bool
    vehicle_action: VehicleAction
    wp_order: int
    gimbal_pitch: int
    def __init__(self, latitude: _Optional[float] = ..., longitude: _Optional[float] = ..., altitude: _Optional[float] = ..., speed: _Optional[float] = ..., fly_trough: bool = ..., vehicle_action: _Optional[_Union[VehicleAction, str]] = ..., wp_order: _Optional[int] = ..., gimbal_pitch: _Optional[int] = ...) -> None: ...

class WaypointTaskConfigProto(_message.Message):
    __slots__ = ("external_task_id", "waypoints", "fly_to_wayline_mode", "wayline_finish_action", "wayline_type", "wayline_turn_mode", "use_straight_line", "wayline_precision_type", "exit_wayline_when_rc_lost_enum", "rc_lost_action_enum", "out_of_control_action", "take_off_security_height", "rth_altitude", "rth_mode", "rth_speed", "global_speed", "global_transition_speed", "global_height", "gimbal_pitch_mode", "global_gimbal_pitch", "payload_imaging_type", "file_url", "file_md5", "flight_area_file_url", "flight_area_checksum")
    EXTERNAL_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    WAYPOINTS_FIELD_NUMBER: _ClassVar[int]
    FLY_TO_WAYLINE_MODE_FIELD_NUMBER: _ClassVar[int]
    WAYLINE_FINISH_ACTION_FIELD_NUMBER: _ClassVar[int]
    WAYLINE_TYPE_FIELD_NUMBER: _ClassVar[int]
    WAYLINE_TURN_MODE_FIELD_NUMBER: _ClassVar[int]
    USE_STRAIGHT_LINE_FIELD_NUMBER: _ClassVar[int]
    WAYLINE_PRECISION_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXIT_WAYLINE_WHEN_RC_LOST_ENUM_FIELD_NUMBER: _ClassVar[int]
    RC_LOST_ACTION_ENUM_FIELD_NUMBER: _ClassVar[int]
    OUT_OF_CONTROL_ACTION_FIELD_NUMBER: _ClassVar[int]
    TAKE_OFF_SECURITY_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    RTH_ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    RTH_MODE_FIELD_NUMBER: _ClassVar[int]
    RTH_SPEED_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_SPEED_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_TRANSITION_SPEED_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    GIMBAL_PITCH_MODE_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_GIMBAL_PITCH_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_IMAGING_TYPE_FIELD_NUMBER: _ClassVar[int]
    FILE_URL_FIELD_NUMBER: _ClassVar[int]
    FILE_MD5_FIELD_NUMBER: _ClassVar[int]
    FLIGHT_AREA_FILE_URL_FIELD_NUMBER: _ClassVar[int]
    FLIGHT_AREA_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    external_task_id: str
    waypoints: _containers.RepeatedCompositeFieldContainer[WaypointProtoDTO]
    fly_to_wayline_mode: FlyToWaylineModeProto
    wayline_finish_action: WaylineFinishActionProto
    wayline_type: WaylineTypeEnumProto
    wayline_turn_mode: WaylineTurnModeProto
    use_straight_line: bool
    wayline_precision_type: WaylinePrecisionTypeEnumProto
    exit_wayline_when_rc_lost_enum: ExitWaylineWhenRcLostEnumProto
    rc_lost_action_enum: RcLostActionEnumProto
    out_of_control_action: OutOfControlActionEnumProto
    take_off_security_height: float
    rth_altitude: int
    rth_mode: RthModeEnumProto
    rth_speed: float
    global_speed: float
    global_transition_speed: float
    global_height: float
    gimbal_pitch_mode: WaylineGimbalPitchModeProto
    global_gimbal_pitch: int
    payload_imaging_type: str
    file_url: str
    file_md5: str
    flight_area_file_url: str
    flight_area_checksum: str
    def __init__(self, external_task_id: _Optional[str] = ..., waypoints: _Optional[_Iterable[_Union[WaypointProtoDTO, _Mapping]]] = ..., fly_to_wayline_mode: _Optional[_Union[FlyToWaylineModeProto, str]] = ..., wayline_finish_action: _Optional[_Union[WaylineFinishActionProto, str]] = ..., wayline_type: _Optional[_Union[WaylineTypeEnumProto, str]] = ..., wayline_turn_mode: _Optional[_Union[WaylineTurnModeProto, str]] = ..., use_straight_line: bool = ..., wayline_precision_type: _Optional[_Union[WaylinePrecisionTypeEnumProto, str]] = ..., exit_wayline_when_rc_lost_enum: _Optional[_Union[ExitWaylineWhenRcLostEnumProto, str]] = ..., rc_lost_action_enum: _Optional[_Union[RcLostActionEnumProto, str]] = ..., out_of_control_action: _Optional[_Union[OutOfControlActionEnumProto, str]] = ..., take_off_security_height: _Optional[float] = ..., rth_altitude: _Optional[int] = ..., rth_mode: _Optional[_Union[RthModeEnumProto, str]] = ..., rth_speed: _Optional[float] = ..., global_speed: _Optional[float] = ..., global_transition_speed: _Optional[float] = ..., global_height: _Optional[float] = ..., gimbal_pitch_mode: _Optional[_Union[WaylineGimbalPitchModeProto, str]] = ..., global_gimbal_pitch: _Optional[int] = ..., payload_imaging_type: _Optional[str] = ..., file_url: _Optional[str] = ..., file_md5: _Optional[str] = ..., flight_area_file_url: _Optional[str] = ..., flight_area_checksum: _Optional[str] = ...) -> None: ...

class DetectTaskConfigProto(_message.Message):
    __slots__ = ("detection_targets", "detection_mode", "area_latitude", "area_longitude", "area_radius", "detection_altitude", "scan_pattern", "scan_speed", "thermal_detection", "visual_detection", "min_confidence", "max_detections", "auto_capture_on_detection", "investigate_detections", "investigation_distance", "investigation_duration", "gimbal_pitch", "enable_zoom", "zoom_level", "max_duration", "on_max_detections_action", "realtime_alerts", "ai_model_id", "detection_parameters")
    class DetectionParameterProto(_message.Message):
        __slots__ = ("name", "value", "description")
        NAME_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        name: str
        value: str
        description: str
        def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...
    DETECTION_TARGETS_FIELD_NUMBER: _ClassVar[int]
    DETECTION_MODE_FIELD_NUMBER: _ClassVar[int]
    AREA_LATITUDE_FIELD_NUMBER: _ClassVar[int]
    AREA_LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    AREA_RADIUS_FIELD_NUMBER: _ClassVar[int]
    DETECTION_ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    SCAN_PATTERN_FIELD_NUMBER: _ClassVar[int]
    SCAN_SPEED_FIELD_NUMBER: _ClassVar[int]
    THERMAL_DETECTION_FIELD_NUMBER: _ClassVar[int]
    VISUAL_DETECTION_FIELD_NUMBER: _ClassVar[int]
    MIN_CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    MAX_DETECTIONS_FIELD_NUMBER: _ClassVar[int]
    AUTO_CAPTURE_ON_DETECTION_FIELD_NUMBER: _ClassVar[int]
    INVESTIGATE_DETECTIONS_FIELD_NUMBER: _ClassVar[int]
    INVESTIGATION_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    INVESTIGATION_DURATION_FIELD_NUMBER: _ClassVar[int]
    GIMBAL_PITCH_FIELD_NUMBER: _ClassVar[int]
    ENABLE_ZOOM_FIELD_NUMBER: _ClassVar[int]
    ZOOM_LEVEL_FIELD_NUMBER: _ClassVar[int]
    MAX_DURATION_FIELD_NUMBER: _ClassVar[int]
    ON_MAX_DETECTIONS_ACTION_FIELD_NUMBER: _ClassVar[int]
    REALTIME_ALERTS_FIELD_NUMBER: _ClassVar[int]
    AI_MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    DETECTION_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    detection_targets: _containers.RepeatedScalarFieldContainer[str]
    detection_mode: str
    area_latitude: float
    area_longitude: float
    area_radius: float
    detection_altitude: float
    scan_pattern: str
    scan_speed: float
    thermal_detection: bool
    visual_detection: bool
    min_confidence: float
    max_detections: int
    auto_capture_on_detection: bool
    investigate_detections: bool
    investigation_distance: float
    investigation_duration: int
    gimbal_pitch: int
    enable_zoom: bool
    zoom_level: float
    max_duration: int
    on_max_detections_action: str
    realtime_alerts: bool
    ai_model_id: str
    detection_parameters: _containers.RepeatedCompositeFieldContainer[DetectTaskConfigProto.DetectionParameterProto]
    def __init__(self, detection_targets: _Optional[_Iterable[str]] = ..., detection_mode: _Optional[str] = ..., area_latitude: _Optional[float] = ..., area_longitude: _Optional[float] = ..., area_radius: _Optional[float] = ..., detection_altitude: _Optional[float] = ..., scan_pattern: _Optional[str] = ..., scan_speed: _Optional[float] = ..., thermal_detection: bool = ..., visual_detection: bool = ..., min_confidence: _Optional[float] = ..., max_detections: _Optional[int] = ..., auto_capture_on_detection: bool = ..., investigate_detections: bool = ..., investigation_distance: _Optional[float] = ..., investigation_duration: _Optional[int] = ..., gimbal_pitch: _Optional[int] = ..., enable_zoom: bool = ..., zoom_level: _Optional[float] = ..., max_duration: _Optional[int] = ..., on_max_detections_action: _Optional[str] = ..., realtime_alerts: bool = ..., ai_model_id: _Optional[str] = ..., detection_parameters: _Optional[_Iterable[_Union[DetectTaskConfigProto.DetectionParameterProto, _Mapping]]] = ...) -> None: ...

class AreaMappingTaskConfigProto(_message.Message):
    __slots__ = ("area_vertices", "survey_altitude", "flight_pattern", "front_overlap", "side_overlap", "speed", "gimbal_pitch", "camera_angle", "terrain_following", "ground_sampling_distance", "enable3_d_reconstruction")
    class AreaVertexProto(_message.Message):
        __slots__ = ("latitude", "longitude", "order")
        LATITUDE_FIELD_NUMBER: _ClassVar[int]
        LONGITUDE_FIELD_NUMBER: _ClassVar[int]
        ORDER_FIELD_NUMBER: _ClassVar[int]
        latitude: float
        longitude: float
        order: int
        def __init__(self, latitude: _Optional[float] = ..., longitude: _Optional[float] = ..., order: _Optional[int] = ...) -> None: ...
    AREA_VERTICES_FIELD_NUMBER: _ClassVar[int]
    SURVEY_ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    FLIGHT_PATTERN_FIELD_NUMBER: _ClassVar[int]
    FRONT_OVERLAP_FIELD_NUMBER: _ClassVar[int]
    SIDE_OVERLAP_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    GIMBAL_PITCH_FIELD_NUMBER: _ClassVar[int]
    CAMERA_ANGLE_FIELD_NUMBER: _ClassVar[int]
    TERRAIN_FOLLOWING_FIELD_NUMBER: _ClassVar[int]
    GROUND_SAMPLING_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    ENABLE3_D_RECONSTRUCTION_FIELD_NUMBER: _ClassVar[int]
    area_vertices: _containers.RepeatedCompositeFieldContainer[AreaMappingTaskConfigProto.AreaVertexProto]
    survey_altitude: float
    flight_pattern: str
    front_overlap: int
    side_overlap: int
    speed: float
    gimbal_pitch: int
    camera_angle: int
    terrain_following: bool
    ground_sampling_distance: float
    enable3_d_reconstruction: bool
    def __init__(self, area_vertices: _Optional[_Iterable[_Union[AreaMappingTaskConfigProto.AreaVertexProto, _Mapping]]] = ..., survey_altitude: _Optional[float] = ..., flight_pattern: _Optional[str] = ..., front_overlap: _Optional[int] = ..., side_overlap: _Optional[int] = ..., speed: _Optional[float] = ..., gimbal_pitch: _Optional[int] = ..., camera_angle: _Optional[int] = ..., terrain_following: bool = ..., ground_sampling_distance: _Optional[float] = ..., enable3_d_reconstruction: bool = ...) -> None: ...

class PoiTaskConfigProto(_message.Message):
    __slots__ = ("poi_latitude", "poi_longitude", "poi_altitude", "orbit_radius", "orbit_speed", "flight_altitude", "number_of_orbits", "orbit_direction", "start_angle", "end_angle", "capture_enabled", "capture_interval", "lock_camera_on_poi")
    POI_LATITUDE_FIELD_NUMBER: _ClassVar[int]
    POI_LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    POI_ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    ORBIT_RADIUS_FIELD_NUMBER: _ClassVar[int]
    ORBIT_SPEED_FIELD_NUMBER: _ClassVar[int]
    FLIGHT_ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    NUMBER_OF_ORBITS_FIELD_NUMBER: _ClassVar[int]
    ORBIT_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    START_ANGLE_FIELD_NUMBER: _ClassVar[int]
    END_ANGLE_FIELD_NUMBER: _ClassVar[int]
    CAPTURE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CAPTURE_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    LOCK_CAMERA_ON_POI_FIELD_NUMBER: _ClassVar[int]
    poi_latitude: float
    poi_longitude: float
    poi_altitude: float
    orbit_radius: float
    orbit_speed: float
    flight_altitude: float
    number_of_orbits: int
    orbit_direction: str
    start_angle: int
    end_angle: int
    capture_enabled: bool
    capture_interval: int
    lock_camera_on_poi: bool
    def __init__(self, poi_latitude: _Optional[float] = ..., poi_longitude: _Optional[float] = ..., poi_altitude: _Optional[float] = ..., orbit_radius: _Optional[float] = ..., orbit_speed: _Optional[float] = ..., flight_altitude: _Optional[float] = ..., number_of_orbits: _Optional[int] = ..., orbit_direction: _Optional[str] = ..., start_angle: _Optional[int] = ..., end_angle: _Optional[int] = ..., capture_enabled: bool = ..., capture_interval: _Optional[int] = ..., lock_camera_on_poi: bool = ...) -> None: ...

class FollowTaskConfigProto(_message.Message):
    __slots__ = ("target_type", "initial_latitude", "initial_longitude", "follow_distance", "relative_altitude", "max_speed", "follow_mode", "angle_offset", "obstacle_avoidance", "max_duration", "max_distance_from_start", "lost_target_action", "lost_target_timeout", "lock_camera_on_target", "gimbal_pitch_offset", "auto_capture", "capture_interval")
    TARGET_TYPE_FIELD_NUMBER: _ClassVar[int]
    INITIAL_LATITUDE_FIELD_NUMBER: _ClassVar[int]
    INITIAL_LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    FOLLOW_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    MAX_SPEED_FIELD_NUMBER: _ClassVar[int]
    FOLLOW_MODE_FIELD_NUMBER: _ClassVar[int]
    ANGLE_OFFSET_FIELD_NUMBER: _ClassVar[int]
    OBSTACLE_AVOIDANCE_FIELD_NUMBER: _ClassVar[int]
    MAX_DURATION_FIELD_NUMBER: _ClassVar[int]
    MAX_DISTANCE_FROM_START_FIELD_NUMBER: _ClassVar[int]
    LOST_TARGET_ACTION_FIELD_NUMBER: _ClassVar[int]
    LOST_TARGET_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    LOCK_CAMERA_ON_TARGET_FIELD_NUMBER: _ClassVar[int]
    GIMBAL_PITCH_OFFSET_FIELD_NUMBER: _ClassVar[int]
    AUTO_CAPTURE_FIELD_NUMBER: _ClassVar[int]
    CAPTURE_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    target_type: str
    initial_latitude: float
    initial_longitude: float
    follow_distance: float
    relative_altitude: float
    max_speed: float
    follow_mode: str
    angle_offset: int
    obstacle_avoidance: bool
    max_duration: int
    max_distance_from_start: float
    lost_target_action: str
    lost_target_timeout: int
    lock_camera_on_target: bool
    gimbal_pitch_offset: int
    auto_capture: bool
    capture_interval: int
    def __init__(self, target_type: _Optional[str] = ..., initial_latitude: _Optional[float] = ..., initial_longitude: _Optional[float] = ..., follow_distance: _Optional[float] = ..., relative_altitude: _Optional[float] = ..., max_speed: _Optional[float] = ..., follow_mode: _Optional[str] = ..., angle_offset: _Optional[int] = ..., obstacle_avoidance: bool = ..., max_duration: _Optional[int] = ..., max_distance_from_start: _Optional[float] = ..., lost_target_action: _Optional[str] = ..., lost_target_timeout: _Optional[int] = ..., lock_camera_on_target: bool = ..., gimbal_pitch_offset: _Optional[int] = ..., auto_capture: bool = ..., capture_interval: _Optional[int] = ...) -> None: ...

class TrackTaskConfigProto(_message.Message):
    __slots__ = ("target_type", "initial_latitude", "initial_longitude", "target_altitude", "tracking_mode", "max_movement_radius", "tracking_altitude", "gimbal_tracking", "auto_zoom", "zoom_level", "tracking_sensitivity", "max_duration", "lost_target_action", "lost_target_timeout", "search_pattern", "search_duration", "continuous_recording", "photo_capture", "capture_interval", "confidence_threshold")
    TARGET_TYPE_FIELD_NUMBER: _ClassVar[int]
    INITIAL_LATITUDE_FIELD_NUMBER: _ClassVar[int]
    INITIAL_LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    TARGET_ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    TRACKING_MODE_FIELD_NUMBER: _ClassVar[int]
    MAX_MOVEMENT_RADIUS_FIELD_NUMBER: _ClassVar[int]
    TRACKING_ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    GIMBAL_TRACKING_FIELD_NUMBER: _ClassVar[int]
    AUTO_ZOOM_FIELD_NUMBER: _ClassVar[int]
    ZOOM_LEVEL_FIELD_NUMBER: _ClassVar[int]
    TRACKING_SENSITIVITY_FIELD_NUMBER: _ClassVar[int]
    MAX_DURATION_FIELD_NUMBER: _ClassVar[int]
    LOST_TARGET_ACTION_FIELD_NUMBER: _ClassVar[int]
    LOST_TARGET_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    SEARCH_PATTERN_FIELD_NUMBER: _ClassVar[int]
    SEARCH_DURATION_FIELD_NUMBER: _ClassVar[int]
    CONTINUOUS_RECORDING_FIELD_NUMBER: _ClassVar[int]
    PHOTO_CAPTURE_FIELD_NUMBER: _ClassVar[int]
    CAPTURE_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    target_type: str
    initial_latitude: float
    initial_longitude: float
    target_altitude: float
    tracking_mode: str
    max_movement_radius: float
    tracking_altitude: float
    gimbal_tracking: bool
    auto_zoom: bool
    zoom_level: float
    tracking_sensitivity: str
    max_duration: int
    lost_target_action: str
    lost_target_timeout: int
    search_pattern: str
    search_duration: int
    continuous_recording: bool
    photo_capture: bool
    capture_interval: int
    confidence_threshold: float
    def __init__(self, target_type: _Optional[str] = ..., initial_latitude: _Optional[float] = ..., initial_longitude: _Optional[float] = ..., target_altitude: _Optional[float] = ..., tracking_mode: _Optional[str] = ..., max_movement_radius: _Optional[float] = ..., tracking_altitude: _Optional[float] = ..., gimbal_tracking: bool = ..., auto_zoom: bool = ..., zoom_level: _Optional[float] = ..., tracking_sensitivity: _Optional[str] = ..., max_duration: _Optional[int] = ..., lost_target_action: _Optional[str] = ..., lost_target_timeout: _Optional[int] = ..., search_pattern: _Optional[str] = ..., search_duration: _Optional[int] = ..., continuous_recording: bool = ..., photo_capture: bool = ..., capture_interval: _Optional[int] = ..., confidence_threshold: _Optional[float] = ...) -> None: ...
