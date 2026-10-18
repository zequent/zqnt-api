import datetime

from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from zqnt_api.generated.zqnt.common.v3 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SimulationStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SIMULATION_STATUS_UNSPECIFIED: _ClassVar[SimulationStatus]
    SIMULATION_STATUS_PENDING: _ClassVar[SimulationStatus]
    SIMULATION_STATUS_RUNNING: _ClassVar[SimulationStatus]
    SIMULATION_STATUS_PAUSED: _ClassVar[SimulationStatus]
    SIMULATION_STATUS_SUCCEEDED: _ClassVar[SimulationStatus]
    SIMULATION_STATUS_FAILED: _ClassVar[SimulationStatus]
    SIMULATION_STATUS_CANCELLED: _ClassVar[SimulationStatus]
    SIMULATION_STATUS_TIMED_OUT: _ClassVar[SimulationStatus]
    SIMULATION_STATUS_CANCELLING: _ClassVar[SimulationStatus]

class NodeOutcome(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NODE_OUTCOME_UNSPECIFIED: _ClassVar[NodeOutcome]
    NODE_OUTCOME_SUCCESS: _ClassVar[NodeOutcome]
    NODE_OUTCOME_FAILURE: _ClassVar[NodeOutcome]
    NODE_OUTCOME_TIMEOUT: _ClassVar[NodeOutcome]

class ApprovalAnswer(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    APPROVAL_ANSWER_UNSPECIFIED: _ClassVar[ApprovalAnswer]
    APPROVAL_ANSWER_APPROVE: _ClassVar[ApprovalAnswer]
    APPROVAL_ANSWER_REJECT: _ClassVar[ApprovalAnswer]
    APPROVAL_ANSWER_NO_ANSWER: _ClassVar[ApprovalAnswer]

class AssetType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ASSET_TYPE_UNSPECIFIED: _ClassVar[AssetType]
    ASSET_TYPE_AIRCRAFT: _ClassVar[AssetType]
    ASSET_TYPE_DOCK: _ClassVar[AssetType]
    ASSET_TYPE_SENSOR: _ClassVar[AssetType]
    ASSET_TYPE_CAMERA: _ClassVar[AssetType]
    ASSET_TYPE_OTHER: _ClassVar[AssetType]
    ASSET_TYPE_JAMMER: _ClassVar[AssetType]

class NodeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NODE_TYPE_UNSPECIFIED: _ClassVar[NodeType]
    NODE_TYPE_COMMAND: _ClassVar[NodeType]
    NODE_TYPE_SKILL: _ClassVar[NodeType]
    NODE_TYPE_CONDITION: _ClassVar[NodeType]
    NODE_TYPE_PARALLEL_GATEWAY: _ClassVar[NodeType]
    NODE_TYPE_JOIN_GATEWAY: _ClassVar[NodeType]
    NODE_TYPE_WAIT: _ClassVar[NodeType]
    NODE_TYPE_EVENT_WAIT: _ClassVar[NodeType]
    NODE_TYPE_HUMAN_APPROVAL: _ClassVar[NodeType]
    NODE_TYPE_END: _ClassVar[NodeType]
    NODE_TYPE_AI: _ClassVar[NodeType]

class NodeStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NODE_STATUS_UNSPECIFIED: _ClassVar[NodeStatus]
    NODE_STATUS_PENDING: _ClassVar[NodeStatus]
    NODE_STATUS_RUNNING: _ClassVar[NodeStatus]
    NODE_STATUS_SUCCEEDED: _ClassVar[NodeStatus]
    NODE_STATUS_FAILED: _ClassVar[NodeStatus]
    NODE_STATUS_SKIPPED: _ClassVar[NodeStatus]
    NODE_STATUS_CANCELLED: _ClassVar[NodeStatus]
    NODE_STATUS_TIMED_OUT: _ClassVar[NodeStatus]
    NODE_STATUS_WAITING: _ClassVar[NodeStatus]
    NODE_STATUS_PAUSED: _ClassVar[NodeStatus]

class EdgeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EDGE_TYPE_UNSPECIFIED: _ClassVar[EdgeType]
    EDGE_TYPE_NORMAL: _ClassVar[EdgeType]
    EDGE_TYPE_SUCCESS: _ClassVar[EdgeType]
    EDGE_TYPE_FAILURE: _ClassVar[EdgeType]
    EDGE_TYPE_TIMEOUT: _ClassVar[EdgeType]
    EDGE_TYPE_COMPENSATION: _ClassVar[EdgeType]
SIMULATION_STATUS_UNSPECIFIED: SimulationStatus
SIMULATION_STATUS_PENDING: SimulationStatus
SIMULATION_STATUS_RUNNING: SimulationStatus
SIMULATION_STATUS_PAUSED: SimulationStatus
SIMULATION_STATUS_SUCCEEDED: SimulationStatus
SIMULATION_STATUS_FAILED: SimulationStatus
SIMULATION_STATUS_CANCELLED: SimulationStatus
SIMULATION_STATUS_TIMED_OUT: SimulationStatus
SIMULATION_STATUS_CANCELLING: SimulationStatus
NODE_OUTCOME_UNSPECIFIED: NodeOutcome
NODE_OUTCOME_SUCCESS: NodeOutcome
NODE_OUTCOME_FAILURE: NodeOutcome
NODE_OUTCOME_TIMEOUT: NodeOutcome
APPROVAL_ANSWER_UNSPECIFIED: ApprovalAnswer
APPROVAL_ANSWER_APPROVE: ApprovalAnswer
APPROVAL_ANSWER_REJECT: ApprovalAnswer
APPROVAL_ANSWER_NO_ANSWER: ApprovalAnswer
ASSET_TYPE_UNSPECIFIED: AssetType
ASSET_TYPE_AIRCRAFT: AssetType
ASSET_TYPE_DOCK: AssetType
ASSET_TYPE_SENSOR: AssetType
ASSET_TYPE_CAMERA: AssetType
ASSET_TYPE_OTHER: AssetType
ASSET_TYPE_JAMMER: AssetType
NODE_TYPE_UNSPECIFIED: NodeType
NODE_TYPE_COMMAND: NodeType
NODE_TYPE_SKILL: NodeType
NODE_TYPE_CONDITION: NodeType
NODE_TYPE_PARALLEL_GATEWAY: NodeType
NODE_TYPE_JOIN_GATEWAY: NodeType
NODE_TYPE_WAIT: NodeType
NODE_TYPE_EVENT_WAIT: NodeType
NODE_TYPE_HUMAN_APPROVAL: NodeType
NODE_TYPE_END: NodeType
NODE_TYPE_AI: NodeType
NODE_STATUS_UNSPECIFIED: NodeStatus
NODE_STATUS_PENDING: NodeStatus
NODE_STATUS_RUNNING: NodeStatus
NODE_STATUS_SUCCEEDED: NodeStatus
NODE_STATUS_FAILED: NodeStatus
NODE_STATUS_SKIPPED: NodeStatus
NODE_STATUS_CANCELLED: NodeStatus
NODE_STATUS_TIMED_OUT: NodeStatus
NODE_STATUS_WAITING: NodeStatus
NODE_STATUS_PAUSED: NodeStatus
EDGE_TYPE_UNSPECIFIED: EdgeType
EDGE_TYPE_NORMAL: EdgeType
EDGE_TYPE_SUCCESS: EdgeType
EDGE_TYPE_FAILURE: EdgeType
EDGE_TYPE_TIMEOUT: EdgeType
EDGE_TYPE_COMPENSATION: EdgeType

class NodeScenario(_message.Message):
    __slots__ = ("node_id", "command_id", "outcome", "error_code", "error_message", "delay", "output", "approval")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    OUTCOME_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DELAY_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    APPROVAL_FIELD_NUMBER: _ClassVar[int]
    node_id: str
    command_id: str
    outcome: NodeOutcome
    error_code: str
    error_message: str
    delay: _duration_pb2.Duration
    output: _struct_pb2.Struct
    approval: ApprovalAnswer
    def __init__(self, node_id: _Optional[str] = ..., command_id: _Optional[str] = ..., outcome: _Optional[_Union[NodeOutcome, str]] = ..., error_code: _Optional[str] = ..., error_message: _Optional[str] = ..., delay: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., output: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., approval: _Optional[_Union[ApprovalAnswer, str]] = ...) -> None: ...

class VirtualAsset(_message.Message):
    __slots__ = ("sn", "copy_of_sn", "name", "type", "commands", "position", "battery_percent", "site_id", "online")
    SN_FIELD_NUMBER: _ClassVar[int]
    COPY_OF_SN_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    COMMANDS_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    BATTERY_PERCENT_FIELD_NUMBER: _ClassVar[int]
    SITE_ID_FIELD_NUMBER: _ClassVar[int]
    ONLINE_FIELD_NUMBER: _ClassVar[int]
    sn: str
    copy_of_sn: str
    name: str
    type: AssetType
    commands: _containers.RepeatedScalarFieldContainer[str]
    position: _common_pb2.GeoPoint
    battery_percent: float
    site_id: str
    online: bool
    def __init__(self, sn: _Optional[str] = ..., copy_of_sn: _Optional[str] = ..., name: _Optional[str] = ..., type: _Optional[_Union[AssetType, str]] = ..., commands: _Optional[_Iterable[str]] = ..., position: _Optional[_Union[_common_pb2.GeoPoint, _Mapping]] = ..., battery_percent: _Optional[float] = ..., site_id: _Optional[str] = ..., online: _Optional[bool] = ...) -> None: ...

class StartSimulationRequest(_message.Message):
    __slots__ = ("context", "application_id", "application_version", "skill_id", "inputs", "site_id", "real_time", "command_duration", "approvals", "nodes", "fleet")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_VERSION_FIELD_NUMBER: _ClassVar[int]
    SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    SITE_ID_FIELD_NUMBER: _ClassVar[int]
    REAL_TIME_FIELD_NUMBER: _ClassVar[int]
    COMMAND_DURATION_FIELD_NUMBER: _ClassVar[int]
    APPROVALS_FIELD_NUMBER: _ClassVar[int]
    NODES_FIELD_NUMBER: _ClassVar[int]
    FLEET_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    application_id: str
    application_version: str
    skill_id: str
    inputs: _struct_pb2.Struct
    site_id: str
    real_time: bool
    command_duration: _duration_pb2.Duration
    approvals: ApprovalAnswer
    nodes: _containers.RepeatedCompositeFieldContainer[NodeScenario]
    fleet: _containers.RepeatedCompositeFieldContainer[VirtualAsset]
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., application_id: _Optional[str] = ..., application_version: _Optional[str] = ..., skill_id: _Optional[str] = ..., inputs: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., site_id: _Optional[str] = ..., real_time: _Optional[bool] = ..., command_duration: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., approvals: _Optional[_Union[ApprovalAnswer, str]] = ..., nodes: _Optional[_Iterable[_Union[NodeScenario, _Mapping]]] = ..., fleet: _Optional[_Iterable[_Union[VirtualAsset, _Mapping]]] = ...) -> None: ...

class StartSimulationResponse(_message.Message):
    __slots__ = ("execution_id", "status")
    EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    execution_id: str
    status: SimulationStatus
    def __init__(self, execution_id: _Optional[str] = ..., status: _Optional[_Union[SimulationStatus, str]] = ...) -> None: ...

class GetSimulationTraceRequest(_message.Message):
    __slots__ = ("context", "execution_id")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    execution_id: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., execution_id: _Optional[str] = ...) -> None: ...

class GetSimulationTraceResponse(_message.Message):
    __slots__ = ("trace",)
    TRACE_FIELD_NUMBER: _ClassVar[int]
    trace: SimulationTrace
    def __init__(self, trace: _Optional[_Union[SimulationTrace, _Mapping]] = ...) -> None: ...

class CancelSimulationRequest(_message.Message):
    __slots__ = ("context", "execution_id")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    execution_id: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., execution_id: _Optional[str] = ...) -> None: ...

class CancelSimulationResponse(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: SimulationStatus
    def __init__(self, status: _Optional[_Union[SimulationStatus, str]] = ...) -> None: ...

class TraceTransition(_message.Message):
    __slots__ = ("target_node_id", "edge_type", "reason")
    TARGET_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    EDGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    target_node_id: str
    edge_type: EdgeType
    reason: str
    def __init__(self, target_node_id: _Optional[str] = ..., edge_type: _Optional[_Union[EdgeType, str]] = ..., reason: _Optional[str] = ...) -> None: ...

class TraceStep(_message.Message):
    __slots__ = ("node_id", "name", "type", "command_id", "status", "attempt", "asset_sn", "dispatch_reason", "input", "output", "error", "warnings", "started_at", "completed_at", "offset", "duration", "next", "simulated_by")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_FIELD_NUMBER: _ClassVar[int]
    ASSET_SN_FIELD_NUMBER: _ClassVar[int]
    DISPATCH_REASON_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_AT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    NEXT_FIELD_NUMBER: _ClassVar[int]
    SIMULATED_BY_FIELD_NUMBER: _ClassVar[int]
    node_id: str
    name: str
    type: NodeType
    command_id: str
    status: NodeStatus
    attempt: int
    asset_sn: str
    dispatch_reason: str
    input: _struct_pb2.Struct
    output: _struct_pb2.Struct
    error: _common_pb2.Error
    warnings: _containers.RepeatedScalarFieldContainer[str]
    started_at: _timestamp_pb2.Timestamp
    completed_at: _timestamp_pb2.Timestamp
    offset: _duration_pb2.Duration
    duration: _duration_pb2.Duration
    next: _containers.RepeatedCompositeFieldContainer[TraceTransition]
    simulated_by: str
    def __init__(self, node_id: _Optional[str] = ..., name: _Optional[str] = ..., type: _Optional[_Union[NodeType, str]] = ..., command_id: _Optional[str] = ..., status: _Optional[_Union[NodeStatus, str]] = ..., attempt: _Optional[int] = ..., asset_sn: _Optional[str] = ..., dispatch_reason: _Optional[str] = ..., input: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., output: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., error: _Optional[_Union[_common_pb2.Error, _Mapping]] = ..., warnings: _Optional[_Iterable[str]] = ..., started_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., completed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., offset: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., duration: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., next: _Optional[_Iterable[_Union[TraceTransition, _Mapping]]] = ..., simulated_by: _Optional[str] = ...) -> None: ...

class SimulationTrace(_message.Message):
    __slots__ = ("execution_id", "status", "asset_sn", "fast_forward", "duration", "steps", "skipped_node_ids", "error", "output", "fleet")
    EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ASSET_SN_FIELD_NUMBER: _ClassVar[int]
    FAST_FORWARD_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    STEPS_FIELD_NUMBER: _ClassVar[int]
    SKIPPED_NODE_IDS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    FLEET_FIELD_NUMBER: _ClassVar[int]
    execution_id: str
    status: SimulationStatus
    asset_sn: str
    fast_forward: bool
    duration: _duration_pb2.Duration
    steps: _containers.RepeatedCompositeFieldContainer[TraceStep]
    skipped_node_ids: _containers.RepeatedScalarFieldContainer[str]
    error: _common_pb2.Error
    output: _struct_pb2.Struct
    fleet: _containers.RepeatedCompositeFieldContainer[VirtualAsset]
    def __init__(self, execution_id: _Optional[str] = ..., status: _Optional[_Union[SimulationStatus, str]] = ..., asset_sn: _Optional[str] = ..., fast_forward: _Optional[bool] = ..., duration: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., steps: _Optional[_Iterable[_Union[TraceStep, _Mapping]]] = ..., skipped_node_ids: _Optional[_Iterable[str]] = ..., error: _Optional[_Union[_common_pb2.Error, _Mapping]] = ..., output: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., fleet: _Optional[_Iterable[_Union[VirtualAsset, _Mapping]]] = ...) -> None: ...
