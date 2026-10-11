import datetime

from . import base_pb2 as _base_pb2
from . import capability_execution_types_pb2 as _capability_execution_types_pb2
from . import device_control_contracts_pb2 as _device_control_contracts_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from . import mission_autonomy_dto_pb2 as _mission_autonomy_dto_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ApplicationScopeProtoDTO(_message.Message):
    __slots__ = ("type", "target_id")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    type: _capability_execution_types_pb2.ApplicationScopeTypeProto
    target_id: str
    def __init__(self, type: _Optional[_Union[_capability_execution_types_pb2.ApplicationScopeTypeProto, str]] = ..., target_id: _Optional[str] = ...) -> None: ...

class ScopedExecutionConfigProtoDTO(_message.Message):
    __slots__ = ("id", "key", "value", "scope", "scope_target", "active", "revision", "description")
    ID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    SCOPE_TARGET_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    id: str
    key: str
    value: _struct_pb2.Value
    scope: _capability_execution_types_pb2.ExecutionConfigScopeTypeProto
    scope_target: str
    active: bool
    revision: str
    description: str
    def __init__(self, id: _Optional[str] = ..., key: _Optional[str] = ..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ..., scope: _Optional[_Union[_capability_execution_types_pb2.ExecutionConfigScopeTypeProto, str]] = ..., scope_target: _Optional[str] = ..., active: bool = ..., revision: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class ExecutionConfigContextProto(_message.Message):
    __slots__ = ("skill_id", "organization_id", "theatre_id", "asset_id", "asset_sn", "execution_overrides")
    SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    THEATRE_ID_FIELD_NUMBER: _ClassVar[int]
    ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    ASSET_SN_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_OVERRIDES_FIELD_NUMBER: _ClassVar[int]
    skill_id: str
    organization_id: str
    theatre_id: str
    asset_id: str
    asset_sn: str
    execution_overrides: _struct_pb2.Struct
    def __init__(self, skill_id: _Optional[str] = ..., organization_id: _Optional[str] = ..., theatre_id: _Optional[str] = ..., asset_id: _Optional[str] = ..., asset_sn: _Optional[str] = ..., execution_overrides: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class ResolvedExecutionConfigProtoDTO(_message.Message):
    __slots__ = ("values", "sources", "resolved_at")
    class SourcesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    VALUES_FIELD_NUMBER: _ClassVar[int]
    SOURCES_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_AT_FIELD_NUMBER: _ClassVar[int]
    values: _struct_pb2.Struct
    sources: _containers.ScalarMap[str, str]
    resolved_at: _timestamp_pb2.Timestamp
    def __init__(self, values: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., sources: _Optional[_Mapping[str, str]] = ..., resolved_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ExecutionComparisonProto(_message.Message):
    __slots__ = ("field_path", "operator", "expected_value")
    FIELD_PATH_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_VALUE_FIELD_NUMBER: _ClassVar[int]
    field_path: str
    operator: _capability_execution_types_pb2.ExecutionConditionOperatorProto
    expected_value: _struct_pb2.Value
    def __init__(self, field_path: _Optional[str] = ..., operator: _Optional[_Union[_capability_execution_types_pb2.ExecutionConditionOperatorProto, str]] = ..., expected_value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...

class ExecutionConditionGroupProto(_message.Message):
    __slots__ = ("operator", "conditions", "negate")
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    NEGATE_FIELD_NUMBER: _ClassVar[int]
    operator: _capability_execution_types_pb2.ExecutionConditionGroupOperatorProto
    conditions: _containers.RepeatedCompositeFieldContainer[ExecutionConditionProto]
    negate: bool
    def __init__(self, operator: _Optional[_Union[_capability_execution_types_pb2.ExecutionConditionGroupOperatorProto, str]] = ..., conditions: _Optional[_Iterable[_Union[ExecutionConditionProto, _Mapping]]] = ..., negate: bool = ...) -> None: ...

class ExecutionConditionProto(_message.Message):
    __slots__ = ("comparison", "group", "constant", "result_when_missing")
    COMPARISON_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    CONSTANT_FIELD_NUMBER: _ClassVar[int]
    RESULT_WHEN_MISSING_FIELD_NUMBER: _ClassVar[int]
    comparison: ExecutionComparisonProto
    group: ExecutionConditionGroupProto
    constant: bool
    result_when_missing: bool
    def __init__(self, comparison: _Optional[_Union[ExecutionComparisonProto, _Mapping]] = ..., group: _Optional[_Union[ExecutionConditionGroupProto, _Mapping]] = ..., constant: bool = ..., result_when_missing: bool = ...) -> None: ...

class CommandNodeConfigProto(_message.Message):
    __slots__ = ("command_id", "required_parameters", "parameter_defaults", "parameter_mapping", "command_schema_version")
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_DEFAULTS_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_MAPPING_FIELD_NUMBER: _ClassVar[int]
    COMMAND_SCHEMA_VERSION_FIELD_NUMBER: _ClassVar[int]
    command_id: str
    required_parameters: _containers.RepeatedScalarFieldContainer[str]
    parameter_defaults: _struct_pb2.Struct
    parameter_mapping: _struct_pb2.Struct
    command_schema_version: str
    def __init__(self, command_id: _Optional[str] = ..., required_parameters: _Optional[_Iterable[str]] = ..., parameter_defaults: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., parameter_mapping: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., command_schema_version: _Optional[str] = ...) -> None: ...

class SkillNodeConfigProto(_message.Message):
    __slots__ = ("skill_id", "parameter_mapping", "skill_version", "follow_latest")
    SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_MAPPING_FIELD_NUMBER: _ClassVar[int]
    SKILL_VERSION_FIELD_NUMBER: _ClassVar[int]
    FOLLOW_LATEST_FIELD_NUMBER: _ClassVar[int]
    skill_id: str
    parameter_mapping: _struct_pb2.Struct
    skill_version: str
    follow_latest: bool
    def __init__(self, skill_id: _Optional[str] = ..., parameter_mapping: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., skill_version: _Optional[str] = ..., follow_latest: bool = ...) -> None: ...

class GatewayNodeConfigProto(_message.Message):
    __slots__ = ("join_mode", "output_mapping")
    JOIN_MODE_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_MAPPING_FIELD_NUMBER: _ClassVar[int]
    join_mode: _capability_execution_types_pb2.ExecutionJoinModeProto
    output_mapping: _struct_pb2.Struct
    def __init__(self, join_mode: _Optional[_Union[_capability_execution_types_pb2.ExecutionJoinModeProto, str]] = ..., output_mapping: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class WaitNodeConfigProto(_message.Message):
    __slots__ = ("duration_seconds", "until")
    DURATION_SECONDS_FIELD_NUMBER: _ClassVar[int]
    UNTIL_FIELD_NUMBER: _ClassVar[int]
    duration_seconds: int
    until: _timestamp_pb2.Timestamp
    def __init__(self, duration_seconds: _Optional[int] = ..., until: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class EventWaitNodeConfigProto(_message.Message):
    __slots__ = ("event_type", "filter", "timeout_seconds")
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_SECONDS_FIELD_NUMBER: _ClassVar[int]
    event_type: str
    filter: ExecutionConditionProto
    timeout_seconds: int
    def __init__(self, event_type: _Optional[str] = ..., filter: _Optional[_Union[ExecutionConditionProto, _Mapping]] = ..., timeout_seconds: _Optional[int] = ...) -> None: ...

class HumanApprovalNodeConfigProto(_message.Message):
    __slots__ = ("approval_type", "approval_group", "timeout_seconds")
    APPROVAL_TYPE_FIELD_NUMBER: _ClassVar[int]
    APPROVAL_GROUP_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_SECONDS_FIELD_NUMBER: _ClassVar[int]
    approval_type: str
    approval_group: str
    timeout_seconds: int
    def __init__(self, approval_type: _Optional[str] = ..., approval_group: _Optional[str] = ..., timeout_seconds: _Optional[int] = ...) -> None: ...

class AiNodeConfigProto(_message.Message):
    __slots__ = ("prompt", "prompt_version", "model_id", "output_schema", "allowed_tool_categories", "max_cost_micro_eur")
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    PROMPT_VERSION_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_TOOL_CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    MAX_COST_MICRO_EUR_FIELD_NUMBER: _ClassVar[int]
    prompt: str
    prompt_version: str
    model_id: str
    output_schema: _struct_pb2.Struct
    allowed_tool_categories: _containers.RepeatedScalarFieldContainer[str]
    max_cost_micro_eur: int
    def __init__(self, prompt: _Optional[str] = ..., prompt_version: _Optional[str] = ..., model_id: _Optional[str] = ..., output_schema: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., allowed_tool_categories: _Optional[_Iterable[str]] = ..., max_cost_micro_eur: _Optional[int] = ...) -> None: ...

class ExecutionNodeProtoDTO(_message.Message):
    __slots__ = ("id", "name", "type", "command", "skill", "condition", "gateway", "wait", "event_wait", "human_approval", "ai", "timeout_seconds", "failure_strategy", "retry_policy", "enabled")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    SKILL_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_FIELD_NUMBER: _ClassVar[int]
    WAIT_FIELD_NUMBER: _ClassVar[int]
    EVENT_WAIT_FIELD_NUMBER: _ClassVar[int]
    HUMAN_APPROVAL_FIELD_NUMBER: _ClassVar[int]
    AI_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_SECONDS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    RETRY_POLICY_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    type: _capability_execution_types_pb2.ExecutionNodeTypeProto
    command: CommandNodeConfigProto
    skill: SkillNodeConfigProto
    condition: ExecutionConditionProto
    gateway: GatewayNodeConfigProto
    wait: WaitNodeConfigProto
    event_wait: EventWaitNodeConfigProto
    human_approval: HumanApprovalNodeConfigProto
    ai: AiNodeConfigProto
    timeout_seconds: int
    failure_strategy: _capability_execution_types_pb2.ExecutionFailureStrategyProto
    retry_policy: _mission_autonomy_dto_pb2.RetryPolicyProtoDTO
    enabled: bool
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., type: _Optional[_Union[_capability_execution_types_pb2.ExecutionNodeTypeProto, str]] = ..., command: _Optional[_Union[CommandNodeConfigProto, _Mapping]] = ..., skill: _Optional[_Union[SkillNodeConfigProto, _Mapping]] = ..., condition: _Optional[_Union[ExecutionConditionProto, _Mapping]] = ..., gateway: _Optional[_Union[GatewayNodeConfigProto, _Mapping]] = ..., wait: _Optional[_Union[WaitNodeConfigProto, _Mapping]] = ..., event_wait: _Optional[_Union[EventWaitNodeConfigProto, _Mapping]] = ..., human_approval: _Optional[_Union[HumanApprovalNodeConfigProto, _Mapping]] = ..., ai: _Optional[_Union[AiNodeConfigProto, _Mapping]] = ..., timeout_seconds: _Optional[int] = ..., failure_strategy: _Optional[_Union[_capability_execution_types_pb2.ExecutionFailureStrategyProto, str]] = ..., retry_policy: _Optional[_Union[_mission_autonomy_dto_pb2.RetryPolicyProtoDTO, _Mapping]] = ..., enabled: bool = ...) -> None: ...

class ExecutionEdgeProtoDTO(_message.Message):
    __slots__ = ("id", "source_node_id", "target_node_id", "type", "condition", "priority", "label")
    ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    id: str
    source_node_id: str
    target_node_id: str
    type: _capability_execution_types_pb2.ExecutionEdgeTypeProto
    condition: ExecutionConditionProto
    priority: int
    label: str
    def __init__(self, id: _Optional[str] = ..., source_node_id: _Optional[str] = ..., target_node_id: _Optional[str] = ..., type: _Optional[_Union[_capability_execution_types_pb2.ExecutionEdgeTypeProto, str]] = ..., condition: _Optional[_Union[ExecutionConditionProto, _Mapping]] = ..., priority: _Optional[int] = ..., label: _Optional[str] = ...) -> None: ...

class GraphNodeLayoutProtoDTO(_message.Message):
    __slots__ = ("node_id", "x", "y", "color", "collapsed", "editor_metadata")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    COLLAPSED_FIELD_NUMBER: _ClassVar[int]
    EDITOR_METADATA_FIELD_NUMBER: _ClassVar[int]
    node_id: str
    x: float
    y: float
    color: str
    collapsed: bool
    editor_metadata: _struct_pb2.Struct
    def __init__(self, node_id: _Optional[str] = ..., x: _Optional[float] = ..., y: _Optional[float] = ..., color: _Optional[str] = ..., collapsed: bool = ..., editor_metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class ExecutionGraphLayoutProtoDTO(_message.Message):
    __slots__ = ("nodes", "zoom", "viewport_x", "viewport_y")
    NODES_FIELD_NUMBER: _ClassVar[int]
    ZOOM_FIELD_NUMBER: _ClassVar[int]
    VIEWPORT_X_FIELD_NUMBER: _ClassVar[int]
    VIEWPORT_Y_FIELD_NUMBER: _ClassVar[int]
    nodes: _containers.RepeatedCompositeFieldContainer[GraphNodeLayoutProtoDTO]
    zoom: float
    viewport_x: float
    viewport_y: float
    def __init__(self, nodes: _Optional[_Iterable[_Union[GraphNodeLayoutProtoDTO, _Mapping]]] = ..., zoom: _Optional[float] = ..., viewport_x: _Optional[float] = ..., viewport_y: _Optional[float] = ...) -> None: ...

class ExecutionGraphProtoDTO(_message.Message):
    __slots__ = ("start_node_id", "nodes", "edges", "layout")
    START_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    NODES_FIELD_NUMBER: _ClassVar[int]
    EDGES_FIELD_NUMBER: _ClassVar[int]
    LAYOUT_FIELD_NUMBER: _ClassVar[int]
    start_node_id: str
    nodes: _containers.RepeatedCompositeFieldContainer[ExecutionNodeProtoDTO]
    edges: _containers.RepeatedCompositeFieldContainer[ExecutionEdgeProtoDTO]
    layout: ExecutionGraphLayoutProtoDTO
    def __init__(self, start_node_id: _Optional[str] = ..., nodes: _Optional[_Iterable[_Union[ExecutionNodeProtoDTO, _Mapping]]] = ..., edges: _Optional[_Iterable[_Union[ExecutionEdgeProtoDTO, _Mapping]]] = ..., layout: _Optional[_Union[ExecutionGraphLayoutProtoDTO, _Mapping]] = ...) -> None: ...

class SkillProtoDTO(_message.Message):
    __slots__ = ("id", "name", "description", "graph", "input_schema", "output_schema", "default_config", "enabled", "required_asset_capabilities", "output_mapping", "source_application_id", "source_version")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    GRAPH_FIELD_NUMBER: _ClassVar[int]
    INPUT_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_ASSET_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_MAPPING_FIELD_NUMBER: _ClassVar[int]
    SOURCE_APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_VERSION_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    graph: ExecutionGraphProtoDTO
    input_schema: _struct_pb2.Struct
    output_schema: _struct_pb2.Struct
    default_config: _struct_pb2.Struct
    enabled: bool
    required_asset_capabilities: _containers.RepeatedScalarFieldContainer[str]
    output_mapping: _struct_pb2.Struct
    source_application_id: str
    source_version: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., graph: _Optional[_Union[ExecutionGraphProtoDTO, _Mapping]] = ..., input_schema: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., output_schema: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., default_config: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., enabled: bool = ..., required_asset_capabilities: _Optional[_Iterable[str]] = ..., output_mapping: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., source_application_id: _Optional[str] = ..., source_version: _Optional[str] = ...) -> None: ...

class ApplicationChangeProtoDTO(_message.Message):
    __slots__ = ("at", "author", "note", "automatic")
    AT_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    AUTOMATIC_FIELD_NUMBER: _ClassVar[int]
    at: _timestamp_pb2.Timestamp
    author: str
    note: str
    automatic: bool
    def __init__(self, at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., author: _Optional[str] = ..., note: _Optional[str] = ..., automatic: bool = ...) -> None: ...

class ApplicationProtoDTO(_message.Message):
    __slots__ = ("id", "version", "name", "description", "skills", "scopes", "default_config", "enabled", "revision", "created_at", "modified_at", "organization_id", "changelog", "change_note")
    ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    CHANGELOG_FIELD_NUMBER: _ClassVar[int]
    CHANGE_NOTE_FIELD_NUMBER: _ClassVar[int]
    id: str
    version: str
    name: str
    description: str
    skills: _containers.RepeatedCompositeFieldContainer[SkillProtoDTO]
    scopes: _containers.RepeatedCompositeFieldContainer[ApplicationScopeProtoDTO]
    default_config: _struct_pb2.Struct
    enabled: bool
    revision: str
    created_at: _timestamp_pb2.Timestamp
    modified_at: _timestamp_pb2.Timestamp
    organization_id: str
    changelog: _containers.RepeatedCompositeFieldContainer[ApplicationChangeProtoDTO]
    change_note: str
    def __init__(self, id: _Optional[str] = ..., version: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., skills: _Optional[_Iterable[_Union[SkillProtoDTO, _Mapping]]] = ..., scopes: _Optional[_Iterable[_Union[ApplicationScopeProtoDTO, _Mapping]]] = ..., default_config: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., enabled: bool = ..., revision: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., modified_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., organization_id: _Optional[str] = ..., changelog: _Optional[_Iterable[_Union[ApplicationChangeProtoDTO, _Mapping]]] = ..., change_note: _Optional[str] = ...) -> None: ...

class ApplicationPauseProtoDTO(_message.Message):
    __slots__ = ("application_id", "skill_id", "paused_by", "paused_at", "reason", "organization_id")
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    PAUSED_BY_FIELD_NUMBER: _ClassVar[int]
    PAUSED_AT_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    application_id: str
    skill_id: str
    paused_by: str
    paused_at: _timestamp_pb2.Timestamp
    reason: str
    organization_id: str
    def __init__(self, application_id: _Optional[str] = ..., skill_id: _Optional[str] = ..., paused_by: _Optional[str] = ..., paused_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., reason: _Optional[str] = ..., organization_id: _Optional[str] = ...) -> None: ...

class ApplicationEnvironmentPointerProtoDTO(_message.Message):
    __slots__ = ("application_id", "environment", "version", "updated_at", "updated_by")
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_BY_FIELD_NUMBER: _ClassVar[int]
    application_id: str
    environment: _capability_execution_types_pb2.ApplicationEnvironmentProto
    version: str
    updated_at: _timestamp_pb2.Timestamp
    updated_by: str
    def __init__(self, application_id: _Optional[str] = ..., environment: _Optional[_Union[_capability_execution_types_pb2.ApplicationEnvironmentProto, str]] = ..., version: _Optional[str] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_by: _Optional[str] = ...) -> None: ...

class SimpleExecutionSpecProto(_message.Message):
    __slots__ = ("command_id", "target", "parameters", "expected_schema_version")
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_SCHEMA_VERSION_FIELD_NUMBER: _ClassVar[int]
    command_id: str
    target: _device_control_contracts_pb2.CapabilityTarget
    parameters: _struct_pb2.Struct
    expected_schema_version: str
    def __init__(self, command_id: _Optional[str] = ..., target: _Optional[_Union[_device_control_contracts_pb2.CapabilityTarget, _Mapping]] = ..., parameters: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., expected_schema_version: _Optional[str] = ...) -> None: ...

class ApplicationExecutionSpecProto(_message.Message):
    __slots__ = ("application_id", "skill_id", "application_version", "parameters")
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_VERSION_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    application_id: str
    skill_id: str
    application_version: str
    parameters: _struct_pb2.Struct
    def __init__(self, application_id: _Optional[str] = ..., skill_id: _Optional[str] = ..., application_version: _Optional[str] = ..., parameters: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class SkillExecutionSpecProto(_message.Message):
    __slots__ = ("simple", "application")
    SIMPLE_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_FIELD_NUMBER: _ClassVar[int]
    simple: SimpleExecutionSpecProto
    application: ApplicationExecutionSpecProto
    def __init__(self, simple: _Optional[_Union[SimpleExecutionSpecProto, _Mapping]] = ..., application: _Optional[_Union[ApplicationExecutionSpecProto, _Mapping]] = ...) -> None: ...

class SkillExecutionOptionsProto(_message.Message):
    __slots__ = ("dry_run", "validate_only", "auto_start", "priority", "timeout_seconds", "failure_strategy", "retry_policy", "preflight_profile", "nfz_policy_profile", "config_overrides", "no_fly_zone_override")
    DRY_RUN_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    AUTO_START_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_SECONDS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    RETRY_POLICY_FIELD_NUMBER: _ClassVar[int]
    PREFLIGHT_PROFILE_FIELD_NUMBER: _ClassVar[int]
    NFZ_POLICY_PROFILE_FIELD_NUMBER: _ClassVar[int]
    CONFIG_OVERRIDES_FIELD_NUMBER: _ClassVar[int]
    NO_FLY_ZONE_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    dry_run: bool
    validate_only: bool
    auto_start: bool
    priority: int
    timeout_seconds: int
    failure_strategy: _capability_execution_types_pb2.ExecutionFailureStrategyProto
    retry_policy: _mission_autonomy_dto_pb2.RetryPolicyProtoDTO
    preflight_profile: str
    nfz_policy_profile: str
    config_overrides: _struct_pb2.Struct
    no_fly_zone_override: bool
    def __init__(self, dry_run: bool = ..., validate_only: bool = ..., auto_start: bool = ..., priority: _Optional[int] = ..., timeout_seconds: _Optional[int] = ..., failure_strategy: _Optional[_Union[_capability_execution_types_pb2.ExecutionFailureStrategyProto, str]] = ..., retry_policy: _Optional[_Union[_mission_autonomy_dto_pb2.RetryPolicyProtoDTO, _Mapping]] = ..., preflight_profile: _Optional[str] = ..., nfz_policy_profile: _Optional[str] = ..., config_overrides: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., no_fly_zone_override: bool = ...) -> None: ...

class ExecutionNodeStateProtoDTO(_message.Message):
    __slots__ = ("id", "node_id", "command_id", "target", "parameters", "status", "attempt", "progress", "external_execution_id", "started_at", "completed_at", "error", "output", "dispatched_asset_sn", "dispatch_reason", "warnings")
    ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_AT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    DISPATCHED_ASSET_SN_FIELD_NUMBER: _ClassVar[int]
    DISPATCH_REASON_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    id: str
    node_id: str
    command_id: str
    target: _device_control_contracts_pb2.CapabilityTarget
    parameters: _struct_pb2.Struct
    status: _capability_execution_types_pb2.ExecutionNodeStatusProto
    attempt: int
    progress: float
    external_execution_id: str
    started_at: _timestamp_pb2.Timestamp
    completed_at: _timestamp_pb2.Timestamp
    error: _base_pb2.GlobalErrorMessage
    output: _struct_pb2.Struct
    dispatched_asset_sn: str
    dispatch_reason: str
    warnings: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., node_id: _Optional[str] = ..., command_id: _Optional[str] = ..., target: _Optional[_Union[_device_control_contracts_pb2.CapabilityTarget, _Mapping]] = ..., parameters: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., status: _Optional[_Union[_capability_execution_types_pb2.ExecutionNodeStatusProto, str]] = ..., attempt: _Optional[int] = ..., progress: _Optional[float] = ..., external_execution_id: _Optional[str] = ..., started_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., completed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ..., output: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., dispatched_asset_sn: _Optional[str] = ..., dispatch_reason: _Optional[str] = ..., warnings: _Optional[_Iterable[str]] = ...) -> None: ...

class SkillExecutionProtoDTO(_message.Message):
    __slots__ = ("id", "asset_sn", "asset_id", "organization_id", "location_id", "theatre_id", "spec", "options", "status", "node_states", "active_node_ids", "progress", "idempotency_key", "requested_by", "created_at", "started_at", "completed_at", "modified_at", "error", "output", "resolved_config", "graph_snapshot", "application_revision")
    ID_FIELD_NUMBER: _ClassVar[int]
    ASSET_SN_FIELD_NUMBER: _ClassVar[int]
    ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    THEATRE_ID_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NODE_STATES_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_NODE_IDS_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_BY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_AT_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_CONFIG_FIELD_NUMBER: _ClassVar[int]
    GRAPH_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_REVISION_FIELD_NUMBER: _ClassVar[int]
    id: str
    asset_sn: str
    asset_id: str
    organization_id: str
    location_id: str
    theatre_id: str
    spec: SkillExecutionSpecProto
    options: SkillExecutionOptionsProto
    status: _capability_execution_types_pb2.SkillExecutionStatusProto
    node_states: _containers.RepeatedCompositeFieldContainer[ExecutionNodeStateProtoDTO]
    active_node_ids: _containers.RepeatedScalarFieldContainer[str]
    progress: float
    idempotency_key: str
    requested_by: str
    created_at: _timestamp_pb2.Timestamp
    started_at: _timestamp_pb2.Timestamp
    completed_at: _timestamp_pb2.Timestamp
    modified_at: _timestamp_pb2.Timestamp
    error: _base_pb2.GlobalErrorMessage
    output: _struct_pb2.Struct
    resolved_config: _struct_pb2.Struct
    graph_snapshot: ExecutionGraphProtoDTO
    application_revision: str
    def __init__(self, id: _Optional[str] = ..., asset_sn: _Optional[str] = ..., asset_id: _Optional[str] = ..., organization_id: _Optional[str] = ..., location_id: _Optional[str] = ..., theatre_id: _Optional[str] = ..., spec: _Optional[_Union[SkillExecutionSpecProto, _Mapping]] = ..., options: _Optional[_Union[SkillExecutionOptionsProto, _Mapping]] = ..., status: _Optional[_Union[_capability_execution_types_pb2.SkillExecutionStatusProto, str]] = ..., node_states: _Optional[_Iterable[_Union[ExecutionNodeStateProtoDTO, _Mapping]]] = ..., active_node_ids: _Optional[_Iterable[str]] = ..., progress: _Optional[float] = ..., idempotency_key: _Optional[str] = ..., requested_by: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., started_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., completed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., modified_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ..., output: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., resolved_config: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., graph_snapshot: _Optional[_Union[ExecutionGraphProtoDTO, _Mapping]] = ..., application_revision: _Optional[str] = ...) -> None: ...

class SkillExecutionEventProto(_message.Message):
    __slots__ = ("event_id", "execution_id", "asset_sn", "type", "execution_status", "node_id", "node_status", "progress", "occurred_at", "error", "data")
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    ASSET_SN_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_STATUS_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_STATUS_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    OCCURRED_AT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    event_id: str
    execution_id: str
    asset_sn: str
    type: _capability_execution_types_pb2.SkillExecutionEventTypeProto
    execution_status: _capability_execution_types_pb2.SkillExecutionStatusProto
    node_id: str
    node_status: _capability_execution_types_pb2.ExecutionNodeStatusProto
    progress: float
    occurred_at: _timestamp_pb2.Timestamp
    error: _base_pb2.GlobalErrorMessage
    data: _struct_pb2.Struct
    def __init__(self, event_id: _Optional[str] = ..., execution_id: _Optional[str] = ..., asset_sn: _Optional[str] = ..., type: _Optional[_Union[_capability_execution_types_pb2.SkillExecutionEventTypeProto, str]] = ..., execution_status: _Optional[_Union[_capability_execution_types_pb2.SkillExecutionStatusProto, str]] = ..., node_id: _Optional[str] = ..., node_status: _Optional[_Union[_capability_execution_types_pb2.ExecutionNodeStatusProto, str]] = ..., progress: _Optional[float] = ..., occurred_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ..., data: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...
