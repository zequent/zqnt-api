import datetime

from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TargetType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TARGET_TYPE_UNSPECIFIED: _ClassVar[TargetType]
    TARGET_TYPE_ASSET: _ClassVar[TargetType]
    TARGET_TYPE_SUB_ASSET: _ClassVar[TargetType]
    TARGET_TYPE_PAYLOAD: _ClassVar[TargetType]
    TARGET_TYPE_COMPONENT: _ClassVar[TargetType]

class CapabilityState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CAPABILITY_STATE_UNSPECIFIED: _ClassVar[CapabilityState]
    CAPABILITY_STATE_AVAILABLE: _ClassVar[CapabilityState]
    CAPABILITY_STATE_TEMPORARILY_UNAVAILABLE: _ClassVar[CapabilityState]
    CAPABILITY_STATE_UNSUPPORTED: _ClassVar[CapabilityState]
    CAPABILITY_STATE_REQUIRES_AUTHORIZATION: _ClassVar[CapabilityState]

class CommandRisk(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COMMAND_RISK_UNSPECIFIED: _ClassVar[CommandRisk]
    COMMAND_RISK_OBSERVE: _ClassVar[CommandRisk]
    COMMAND_RISK_ADJUST: _ClassVar[CommandRisk]
    COMMAND_RISK_MOVE: _ClassVar[CommandRisk]
    COMMAND_RISK_CRITICAL: _ClassVar[CommandRisk]

class CompletionMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COMPLETION_MODE_UNSPECIFIED: _ClassVar[CompletionMode]
    COMPLETION_MODE_ON_REPLY: _ClassVar[CompletionMode]
    COMPLETION_MODE_ASYNCHRONOUS: _ClassVar[CompletionMode]

class CapabilitySource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CAPABILITY_SOURCE_UNSPECIFIED: _ClassVar[CapabilitySource]
    CAPABILITY_SOURCE_BUILT_IN: _ClassVar[CapabilitySource]
    CAPABILITY_SOURCE_EDGE_ADAPTER: _ClassVar[CapabilitySource]
    CAPABILITY_SOURCE_RUNTIME: _ClassVar[CapabilitySource]
    CAPABILITY_SOURCE_USER: _ClassVar[CapabilitySource]
    CAPABILITY_SOURCE_APPLICATION: _ClassVar[CapabilitySource]
    CAPABILITY_SOURCE_INTEGRATION: _ClassVar[CapabilitySource]
    CAPABILITY_SOURCE_AI_GENERATED: _ClassVar[CapabilitySource]

class SnapshotState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SNAPSHOT_STATE_UNSPECIFIED: _ClassVar[SnapshotState]
    SNAPSHOT_STATE_CURRENT: _ClassVar[SnapshotState]
    SNAPSHOT_STATE_STALE: _ClassVar[SnapshotState]
    SNAPSHOT_STATE_NO_DATA: _ClassVar[SnapshotState]

class TelemetryValueType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TELEMETRY_VALUE_TYPE_UNSPECIFIED: _ClassVar[TelemetryValueType]
    TELEMETRY_VALUE_TYPE_NUMBER: _ClassVar[TelemetryValueType]
    TELEMETRY_VALUE_TYPE_STRING: _ClassVar[TelemetryValueType]
    TELEMETRY_VALUE_TYPE_BOOLEAN: _ClassVar[TelemetryValueType]
TARGET_TYPE_UNSPECIFIED: TargetType
TARGET_TYPE_ASSET: TargetType
TARGET_TYPE_SUB_ASSET: TargetType
TARGET_TYPE_PAYLOAD: TargetType
TARGET_TYPE_COMPONENT: TargetType
CAPABILITY_STATE_UNSPECIFIED: CapabilityState
CAPABILITY_STATE_AVAILABLE: CapabilityState
CAPABILITY_STATE_TEMPORARILY_UNAVAILABLE: CapabilityState
CAPABILITY_STATE_UNSUPPORTED: CapabilityState
CAPABILITY_STATE_REQUIRES_AUTHORIZATION: CapabilityState
COMMAND_RISK_UNSPECIFIED: CommandRisk
COMMAND_RISK_OBSERVE: CommandRisk
COMMAND_RISK_ADJUST: CommandRisk
COMMAND_RISK_MOVE: CommandRisk
COMMAND_RISK_CRITICAL: CommandRisk
COMPLETION_MODE_UNSPECIFIED: CompletionMode
COMPLETION_MODE_ON_REPLY: CompletionMode
COMPLETION_MODE_ASYNCHRONOUS: CompletionMode
CAPABILITY_SOURCE_UNSPECIFIED: CapabilitySource
CAPABILITY_SOURCE_BUILT_IN: CapabilitySource
CAPABILITY_SOURCE_EDGE_ADAPTER: CapabilitySource
CAPABILITY_SOURCE_RUNTIME: CapabilitySource
CAPABILITY_SOURCE_USER: CapabilitySource
CAPABILITY_SOURCE_APPLICATION: CapabilitySource
CAPABILITY_SOURCE_INTEGRATION: CapabilitySource
CAPABILITY_SOURCE_AI_GENERATED: CapabilitySource
SNAPSHOT_STATE_UNSPECIFIED: SnapshotState
SNAPSHOT_STATE_CURRENT: SnapshotState
SNAPSHOT_STATE_STALE: SnapshotState
SNAPSHOT_STATE_NO_DATA: SnapshotState
TELEMETRY_VALUE_TYPE_UNSPECIFIED: TelemetryValueType
TELEMETRY_VALUE_TYPE_NUMBER: TelemetryValueType
TELEMETRY_VALUE_TYPE_STRING: TelemetryValueType
TELEMETRY_VALUE_TYPE_BOOLEAN: TelemetryValueType

class Target(_message.Message):
    __slots__ = ("type", "ref")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    REF_FIELD_NUMBER: _ClassVar[int]
    type: TargetType
    ref: str
    def __init__(self, type: _Optional[_Union[TargetType, str]] = ..., ref: _Optional[str] = ...) -> None: ...

class CommandSafety(_message.Message):
    __slots__ = ("risk", "reversible", "undo_command_id", "preconditions", "effects")
    RISK_FIELD_NUMBER: _ClassVar[int]
    REVERSIBLE_FIELD_NUMBER: _ClassVar[int]
    UNDO_COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    PRECONDITIONS_FIELD_NUMBER: _ClassVar[int]
    EFFECTS_FIELD_NUMBER: _ClassVar[int]
    risk: CommandRisk
    reversible: bool
    undo_command_id: str
    preconditions: _containers.RepeatedScalarFieldContainer[str]
    effects: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, risk: _Optional[_Union[CommandRisk, str]] = ..., reversible: bool = ..., undo_command_id: _Optional[str] = ..., preconditions: _Optional[_Iterable[str]] = ..., effects: _Optional[_Iterable[str]] = ...) -> None: ...

class CapabilityErrorSpec(_message.Message):
    __slots__ = ("code", "description")
    CODE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    code: str
    description: str
    def __init__(self, code: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class CapabilityEventSpec(_message.Message):
    __slots__ = ("name", "description", "payload_schema")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    payload_schema: _struct_pb2.Struct
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., payload_schema: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class CapabilityRequirements(_message.Message):
    __slots__ = ("asset_types", "payloads", "runtime_features", "properties")
    ASSET_TYPES_FIELD_NUMBER: _ClassVar[int]
    PAYLOADS_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_FEATURES_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    asset_types: _containers.RepeatedScalarFieldContainer[str]
    payloads: _containers.RepeatedScalarFieldContainer[str]
    runtime_features: _containers.RepeatedScalarFieldContainer[str]
    properties: _struct_pb2.Struct
    def __init__(self, asset_types: _Optional[_Iterable[str]] = ..., payloads: _Optional[_Iterable[str]] = ..., runtime_features: _Optional[_Iterable[str]] = ..., properties: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class Capability(_message.Message):
    __slots__ = ("command_id", "display_name", "description", "state", "unavailable_reason", "target", "input_schema", "output_schema", "schema_version", "safety", "errors", "events", "requirements", "skill_id", "source", "provider", "constraints", "metadata", "deprecated_by", "completion", "completion_event")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    UNAVAILABLE_REASON_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    INPUT_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_VERSION_FIELD_NUMBER: _ClassVar[int]
    SAFETY_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    REQUIREMENTS_FIELD_NUMBER: _ClassVar[int]
    SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_BY_FIELD_NUMBER: _ClassVar[int]
    COMPLETION_FIELD_NUMBER: _ClassVar[int]
    COMPLETION_EVENT_FIELD_NUMBER: _ClassVar[int]
    command_id: str
    display_name: str
    description: str
    state: CapabilityState
    unavailable_reason: str
    target: Target
    input_schema: _struct_pb2.Struct
    output_schema: _struct_pb2.Struct
    schema_version: str
    safety: CommandSafety
    errors: _containers.RepeatedCompositeFieldContainer[CapabilityErrorSpec]
    events: _containers.RepeatedCompositeFieldContainer[CapabilityEventSpec]
    requirements: CapabilityRequirements
    skill_id: str
    source: CapabilitySource
    provider: str
    constraints: _struct_pb2.Struct
    metadata: _containers.ScalarMap[str, str]
    deprecated_by: str
    completion: CompletionMode
    completion_event: str
    def __init__(self, command_id: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., state: _Optional[_Union[CapabilityState, str]] = ..., unavailable_reason: _Optional[str] = ..., target: _Optional[_Union[Target, _Mapping]] = ..., input_schema: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., output_schema: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., schema_version: _Optional[str] = ..., safety: _Optional[_Union[CommandSafety, _Mapping]] = ..., errors: _Optional[_Iterable[_Union[CapabilityErrorSpec, _Mapping]]] = ..., events: _Optional[_Iterable[_Union[CapabilityEventSpec, _Mapping]]] = ..., requirements: _Optional[_Union[CapabilityRequirements, _Mapping]] = ..., skill_id: _Optional[str] = ..., source: _Optional[_Union[CapabilitySource, str]] = ..., provider: _Optional[str] = ..., constraints: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., metadata: _Optional[_Mapping[str, str]] = ..., deprecated_by: _Optional[str] = ..., completion: _Optional[_Union[CompletionMode, str]] = ..., completion_event: _Optional[str] = ...) -> None: ...

class CapabilitySet(_message.Message):
    __slots__ = ("asset_sn", "asset_type", "capabilities", "observed_at", "valid_until", "revision", "snapshot_state", "telemetry_fields")
    ASSET_SN_FIELD_NUMBER: _ClassVar[int]
    ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    OBSERVED_AT_FIELD_NUMBER: _ClassVar[int]
    VALID_UNTIL_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_STATE_FIELD_NUMBER: _ClassVar[int]
    TELEMETRY_FIELDS_FIELD_NUMBER: _ClassVar[int]
    asset_sn: str
    asset_type: str
    capabilities: _containers.RepeatedCompositeFieldContainer[Capability]
    observed_at: _timestamp_pb2.Timestamp
    valid_until: _timestamp_pb2.Timestamp
    revision: str
    snapshot_state: SnapshotState
    telemetry_fields: _containers.RepeatedCompositeFieldContainer[TelemetryField]
    def __init__(self, asset_sn: _Optional[str] = ..., asset_type: _Optional[str] = ..., capabilities: _Optional[_Iterable[_Union[Capability, _Mapping]]] = ..., observed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., valid_until: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., revision: _Optional[str] = ..., snapshot_state: _Optional[_Union[SnapshotState, str]] = ..., telemetry_fields: _Optional[_Iterable[_Union[TelemetryField, _Mapping]]] = ...) -> None: ...

class TelemetryField(_message.Message):
    __slots__ = ("key", "type", "unit", "description", "allowed_values")
    KEY_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_VALUES_FIELD_NUMBER: _ClassVar[int]
    key: str
    type: TelemetryValueType
    unit: str
    description: str
    allowed_values: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, key: _Optional[str] = ..., type: _Optional[_Union[TelemetryValueType, str]] = ..., unit: _Optional[str] = ..., description: _Optional[str] = ..., allowed_values: _Optional[_Iterable[str]] = ...) -> None: ...
