from . import base_pb2 as _base_pb2
from . import capability_execution_dto_pb2 as _capability_execution_dto_pb2
from . import capability_execution_types_pb2 as _capability_execution_types_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpsertApplicationRequest(_message.Message):
    __slots__ = ("base", "application", "expected_revision")
    BASE_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_REVISION_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    application: _capability_execution_dto_pb2.ApplicationProtoDTO
    expected_revision: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., application: _Optional[_Union[_capability_execution_dto_pb2.ApplicationProtoDTO, _Mapping]] = ..., expected_revision: _Optional[str] = ...) -> None: ...

class GetApplicationRequest(_message.Message):
    __slots__ = ("base", "application_id", "version")
    BASE_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    application_id: str
    version: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., application_id: _Optional[str] = ..., version: _Optional[str] = ...) -> None: ...

class ListApplicationsRequest(_message.Message):
    __slots__ = ("base", "scope", "enabled_only", "page_size", "page_token")
    BASE_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    ENABLED_ONLY_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    scope: _capability_execution_dto_pb2.ApplicationScopeProtoDTO
    enabled_only: bool
    page_size: int
    page_token: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., scope: _Optional[_Union[_capability_execution_dto_pb2.ApplicationScopeProtoDTO, _Mapping]] = ..., enabled_only: bool = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class DeleteApplicationRequest(_message.Message):
    __slots__ = ("base", "application_id", "version", "expected_revision")
    BASE_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_REVISION_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    application_id: str
    version: str
    expected_revision: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., application_id: _Optional[str] = ..., version: _Optional[str] = ..., expected_revision: _Optional[str] = ...) -> None: ...

class GetApplicationEnvironmentsRequest(_message.Message):
    __slots__ = ("base", "application_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    application_id: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., application_id: _Optional[str] = ...) -> None: ...

class PromoteApplicationVersionRequest(_message.Message):
    __slots__ = ("base", "application_id", "version", "environment")
    BASE_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    application_id: str
    version: str
    environment: _capability_execution_types_pb2.ApplicationEnvironmentProto
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., application_id: _Optional[str] = ..., version: _Optional[str] = ..., environment: _Optional[_Union[_capability_execution_types_pb2.ApplicationEnvironmentProto, str]] = ...) -> None: ...

class CreateSkillExecutionRequest(_message.Message):
    __slots__ = ("base", "spec", "options", "idempotency_key", "organization_id", "location_id", "theatre_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    THEATRE_ID_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    spec: _capability_execution_dto_pb2.SkillExecutionSpecProto
    options: _capability_execution_dto_pb2.SkillExecutionOptionsProto
    idempotency_key: str
    organization_id: str
    location_id: str
    theatre_id: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., spec: _Optional[_Union[_capability_execution_dto_pb2.SkillExecutionSpecProto, _Mapping]] = ..., options: _Optional[_Union[_capability_execution_dto_pb2.SkillExecutionOptionsProto, _Mapping]] = ..., idempotency_key: _Optional[str] = ..., organization_id: _Optional[str] = ..., location_id: _Optional[str] = ..., theatre_id: _Optional[str] = ...) -> None: ...

class ExecuteSkillRequest(_message.Message):
    __slots__ = ("base", "spec", "options", "idempotency_key", "organization_id", "location_id", "theatre_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    THEATRE_ID_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    spec: _capability_execution_dto_pb2.SkillExecutionSpecProto
    options: _capability_execution_dto_pb2.SkillExecutionOptionsProto
    idempotency_key: str
    organization_id: str
    location_id: str
    theatre_id: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., spec: _Optional[_Union[_capability_execution_dto_pb2.SkillExecutionSpecProto, _Mapping]] = ..., options: _Optional[_Union[_capability_execution_dto_pb2.SkillExecutionOptionsProto, _Mapping]] = ..., idempotency_key: _Optional[str] = ..., organization_id: _Optional[str] = ..., location_id: _Optional[str] = ..., theatre_id: _Optional[str] = ...) -> None: ...

class GetSkillExecutionRequest(_message.Message):
    __slots__ = ("base", "execution_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    execution_id: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., execution_id: _Optional[str] = ...) -> None: ...

class ListSkillExecutionsRequest(_message.Message):
    __slots__ = ("base", "asset_sn", "organization_id", "status", "application_id", "skill_id", "theatre_id", "page_size", "page_token")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ASSET_SN_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    THEATRE_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    asset_sn: str
    organization_id: str
    status: _capability_execution_types_pb2.SkillExecutionStatusProto
    application_id: str
    skill_id: str
    theatre_id: str
    page_size: int
    page_token: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., asset_sn: _Optional[str] = ..., organization_id: _Optional[str] = ..., status: _Optional[_Union[_capability_execution_types_pb2.SkillExecutionStatusProto, str]] = ..., application_id: _Optional[str] = ..., skill_id: _Optional[str] = ..., theatre_id: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class SkillExecutionLifecycleRequest(_message.Message):
    __slots__ = ("base", "execution_id", "reason", "idempotency_key")
    BASE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    execution_id: str
    reason: str
    idempotency_key: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., execution_id: _Optional[str] = ..., reason: _Optional[str] = ..., idempotency_key: _Optional[str] = ...) -> None: ...

class SignalSkillExecutionRequest(_message.Message):
    __slots__ = ("base", "execution_id", "node_id", "event_type", "data", "approved", "idempotency_key")
    BASE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    APPROVED_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    execution_id: str
    node_id: str
    event_type: str
    data: _struct_pb2.Struct
    approved: bool
    idempotency_key: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., execution_id: _Optional[str] = ..., node_id: _Optional[str] = ..., event_type: _Optional[str] = ..., data: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., approved: bool = ..., idempotency_key: _Optional[str] = ...) -> None: ...

class ResolveExecutionConfigRequest(_message.Message):
    __slots__ = ("base", "context", "keys")
    BASE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    KEYS_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    context: _capability_execution_dto_pb2.ExecutionConfigContextProto
    keys: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., context: _Optional[_Union[_capability_execution_dto_pb2.ExecutionConfigContextProto, _Mapping]] = ..., keys: _Optional[_Iterable[str]] = ...) -> None: ...

class ResolveExecutionConfigResponse(_message.Message):
    __slots__ = ("has_errors", "meta", "config", "error")
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    has_errors: bool
    meta: _base_pb2.ResponseMeta
    config: _capability_execution_dto_pb2.ResolvedExecutionConfigProtoDTO
    error: _base_pb2.GlobalErrorMessage
    def __init__(self, has_errors: bool = ..., meta: _Optional[_Union[_base_pb2.ResponseMeta, _Mapping]] = ..., config: _Optional[_Union[_capability_execution_dto_pb2.ResolvedExecutionConfigProtoDTO, _Mapping]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ...) -> None: ...

class ApplicationResponse(_message.Message):
    __slots__ = ("has_errors", "meta", "application", "error", "empty", "warnings")
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    EMPTY_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    has_errors: bool
    meta: _base_pb2.ResponseMeta
    application: _capability_execution_dto_pb2.ApplicationProtoDTO
    error: _base_pb2.GlobalErrorMessage
    empty: _empty_pb2.Empty
    warnings: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, has_errors: bool = ..., meta: _Optional[_Union[_base_pb2.ResponseMeta, _Mapping]] = ..., application: _Optional[_Union[_capability_execution_dto_pb2.ApplicationProtoDTO, _Mapping]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ..., empty: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., warnings: _Optional[_Iterable[str]] = ...) -> None: ...

class ApplicationList(_message.Message):
    __slots__ = ("applications", "next_page_token")
    APPLICATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    applications: _containers.RepeatedCompositeFieldContainer[_capability_execution_dto_pb2.ApplicationProtoDTO]
    next_page_token: str
    def __init__(self, applications: _Optional[_Iterable[_Union[_capability_execution_dto_pb2.ApplicationProtoDTO, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class ApplicationListResponse(_message.Message):
    __slots__ = ("has_errors", "meta", "result", "error")
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    has_errors: bool
    meta: _base_pb2.ResponseMeta
    result: ApplicationList
    error: _base_pb2.GlobalErrorMessage
    def __init__(self, has_errors: bool = ..., meta: _Optional[_Union[_base_pb2.ResponseMeta, _Mapping]] = ..., result: _Optional[_Union[ApplicationList, _Mapping]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ...) -> None: ...

class ApplicationEnvironmentList(_message.Message):
    __slots__ = ("pointers",)
    POINTERS_FIELD_NUMBER: _ClassVar[int]
    pointers: _containers.RepeatedCompositeFieldContainer[_capability_execution_dto_pb2.ApplicationEnvironmentPointerProtoDTO]
    def __init__(self, pointers: _Optional[_Iterable[_Union[_capability_execution_dto_pb2.ApplicationEnvironmentPointerProtoDTO, _Mapping]]] = ...) -> None: ...

class ApplicationEnvironmentsResponse(_message.Message):
    __slots__ = ("has_errors", "meta", "result", "error")
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    has_errors: bool
    meta: _base_pb2.ResponseMeta
    result: ApplicationEnvironmentList
    error: _base_pb2.GlobalErrorMessage
    def __init__(self, has_errors: bool = ..., meta: _Optional[_Union[_base_pb2.ResponseMeta, _Mapping]] = ..., result: _Optional[_Union[ApplicationEnvironmentList, _Mapping]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ...) -> None: ...

class SkillExecutionResponse(_message.Message):
    __slots__ = ("has_errors", "meta", "execution", "error", "empty")
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    EMPTY_FIELD_NUMBER: _ClassVar[int]
    has_errors: bool
    meta: _base_pb2.ResponseMeta
    execution: _capability_execution_dto_pb2.SkillExecutionProtoDTO
    error: _base_pb2.GlobalErrorMessage
    empty: _empty_pb2.Empty
    def __init__(self, has_errors: bool = ..., meta: _Optional[_Union[_base_pb2.ResponseMeta, _Mapping]] = ..., execution: _Optional[_Union[_capability_execution_dto_pb2.SkillExecutionProtoDTO, _Mapping]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ..., empty: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ...) -> None: ...

class SkillExecutionList(_message.Message):
    __slots__ = ("executions", "next_page_token")
    EXECUTIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    executions: _containers.RepeatedCompositeFieldContainer[_capability_execution_dto_pb2.SkillExecutionProtoDTO]
    next_page_token: str
    def __init__(self, executions: _Optional[_Iterable[_Union[_capability_execution_dto_pb2.SkillExecutionProtoDTO, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class SkillExecutionListResponse(_message.Message):
    __slots__ = ("has_errors", "meta", "result", "error")
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    has_errors: bool
    meta: _base_pb2.ResponseMeta
    result: SkillExecutionList
    error: _base_pb2.GlobalErrorMessage
    def __init__(self, has_errors: bool = ..., meta: _Optional[_Union[_base_pb2.ResponseMeta, _Mapping]] = ..., result: _Optional[_Union[SkillExecutionList, _Mapping]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ...) -> None: ...

class SetApplicationPauseRequest(_message.Message):
    __slots__ = ("base", "application_id", "skill_id", "paused", "reason")
    BASE_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    PAUSED_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    application_id: str
    skill_id: str
    paused: bool
    reason: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., application_id: _Optional[str] = ..., skill_id: _Optional[str] = ..., paused: bool = ..., reason: _Optional[str] = ...) -> None: ...

class ListApplicationPausesRequest(_message.Message):
    __slots__ = ("base", "application_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    application_id: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., application_id: _Optional[str] = ...) -> None: ...

class ApplicationPauseList(_message.Message):
    __slots__ = ("pauses",)
    PAUSES_FIELD_NUMBER: _ClassVar[int]
    pauses: _containers.RepeatedCompositeFieldContainer[_capability_execution_dto_pb2.ApplicationPauseProtoDTO]
    def __init__(self, pauses: _Optional[_Iterable[_Union[_capability_execution_dto_pb2.ApplicationPauseProtoDTO, _Mapping]]] = ...) -> None: ...

class ApplicationPauseListResponse(_message.Message):
    __slots__ = ("has_errors", "meta", "result", "error")
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    has_errors: bool
    meta: _base_pb2.ResponseMeta
    result: ApplicationPauseList
    error: _base_pb2.GlobalErrorMessage
    def __init__(self, has_errors: bool = ..., meta: _Optional[_Union[_base_pb2.ResponseMeta, _Mapping]] = ..., result: _Optional[_Union[ApplicationPauseList, _Mapping]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ...) -> None: ...
