import datetime

from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from . import common_pb2 as _common_pb2
from . import base_pb2 as _base_pb2
from . import asset_pb2 as _asset_pb2
from . import device_control_contracts_pb2 as _device_control_contracts_pb2
from . import detection_pb2 as _detection_pb2
from . import mission_autonomy_types_pb2 as _mission_autonomy_types_pb2
from . import mission_autonomy_dto_pb2 as _mission_autonomy_dto_pb2
from . import events_pb2 as _events_pb2
from . import mission_autonomy_contracts_pb2 as _mission_autonomy_contracts_pb2
from . import mission_autonomy_dto_pb2 as _mission_autonomy_dto_pb2_1
from . import capability_execution_contracts_pb2 as _capability_execution_contracts_pb2
from . import capability_execution_dto_pb2 as _capability_execution_dto_pb2
from . import device_control_contracts_pb2 as _device_control_contracts_pb2_1
from . import media_pb2 as _media_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SkillContractStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SKILL_CONTRACT_STATUS_ACTIVE: _ClassVar[SkillContractStatus]
    SKILL_CONTRACT_STATUS_DRAFT: _ClassVar[SkillContractStatus]
    SKILL_CONTRACT_STATUS_DEPRECATED: _ClassVar[SkillContractStatus]
    SKILL_CONTRACT_STATUS_RETIRED: _ClassVar[SkillContractStatus]

class SkillContractCompatibility(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SKILL_CONTRACT_COMPATIBILITY_UNKNOWN: _ClassVar[SkillContractCompatibility]
    SKILL_CONTRACT_COMPATIBILITY_NEW: _ClassVar[SkillContractCompatibility]
    SKILL_CONTRACT_COMPATIBILITY_COMPATIBLE: _ClassVar[SkillContractCompatibility]
    SKILL_CONTRACT_COMPATIBILITY_BREAKING: _ClassVar[SkillContractCompatibility]

class TelemetryType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TELEMETRY_TYPE_UNSPECIFIED: _ClassVar[TelemetryType]
    TELEMETRY_TYPE_ASSET: _ClassVar[TelemetryType]
    TELEMETRY_TYPE_SUBASSET: _ClassVar[TelemetryType]
SKILL_CONTRACT_STATUS_ACTIVE: SkillContractStatus
SKILL_CONTRACT_STATUS_DRAFT: SkillContractStatus
SKILL_CONTRACT_STATUS_DEPRECATED: SkillContractStatus
SKILL_CONTRACT_STATUS_RETIRED: SkillContractStatus
SKILL_CONTRACT_COMPATIBILITY_UNKNOWN: SkillContractCompatibility
SKILL_CONTRACT_COMPATIBILITY_NEW: SkillContractCompatibility
SKILL_CONTRACT_COMPATIBILITY_COMPATIBLE: SkillContractCompatibility
SKILL_CONTRACT_COMPATIBILITY_BREAKING: SkillContractCompatibility
TELEMETRY_TYPE_UNSPECIFIED: TelemetryType
TELEMETRY_TYPE_ASSET: TelemetryType
TELEMETRY_TYPE_SUBASSET: TelemetryType

class AuthenticateUserRequest(_message.Message):
    __slots__ = ("base", "email", "password")
    BASE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    email: str
    password: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., email: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class AuthenticatedUserProtoDTO(_message.Message):
    __slots__ = ("user_id", "email", "organization_id", "roles", "enabled", "created_at", "provider")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    email: str
    organization_id: str
    roles: _containers.RepeatedScalarFieldContainer[str]
    enabled: bool
    created_at: _timestamp_pb2.Timestamp
    provider: str
    def __init__(self, user_id: _Optional[str] = ..., email: _Optional[str] = ..., organization_id: _Optional[str] = ..., roles: _Optional[_Iterable[str]] = ..., enabled: bool = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., provider: _Optional[str] = ...) -> None: ...

class AuthenticateUserResponse(_message.Message):
    __slots__ = ("has_errors", "meta", "user", "error")
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    has_errors: bool
    meta: _base_pb2.ResponseMeta
    user: AuthenticatedUserProtoDTO
    error: _base_pb2.GlobalErrorMessage
    def __init__(self, has_errors: bool = ..., meta: _Optional[_Union[_base_pb2.ResponseMeta, _Mapping]] = ..., user: _Optional[_Union[AuthenticatedUserProtoDTO, _Mapping]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ...) -> None: ...

class CreateUserRequest(_message.Message):
    __slots__ = ("base", "organization_id", "email", "password", "roles", "user_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    organization_id: str
    email: str
    password: str
    roles: _containers.RepeatedScalarFieldContainer[str]
    user_id: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., organization_id: _Optional[str] = ..., email: _Optional[str] = ..., password: _Optional[str] = ..., roles: _Optional[_Iterable[str]] = ..., user_id: _Optional[str] = ...) -> None: ...

class CreateUserResponse(_message.Message):
    __slots__ = ("has_errors", "meta", "user", "error")
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    has_errors: bool
    meta: _base_pb2.ResponseMeta
    user: AuthenticatedUserProtoDTO
    error: _base_pb2.GlobalErrorMessage
    def __init__(self, has_errors: bool = ..., meta: _Optional[_Union[_base_pb2.ResponseMeta, _Mapping]] = ..., user: _Optional[_Union[AuthenticatedUserProtoDTO, _Mapping]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ...) -> None: ...

class ResetPasswordRequest(_message.Message):
    __slots__ = ("base", "user_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    user_id: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., user_id: _Optional[str] = ...) -> None: ...

class ResetPasswordResponse(_message.Message):
    __slots__ = ("has_errors", "meta", "new_password", "error")
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    NEW_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    has_errors: bool
    meta: _base_pb2.ResponseMeta
    new_password: str
    error: _base_pb2.GlobalErrorMessage
    def __init__(self, has_errors: bool = ..., meta: _Optional[_Union[_base_pb2.ResponseMeta, _Mapping]] = ..., new_password: _Optional[str] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ...) -> None: ...

class RecordAuthAuditEventRequest(_message.Message):
    __slots__ = ("base", "event_type", "user_id", "organization_id", "email", "source_ip", "detail")
    BASE_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    SOURCE_IP_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    event_type: str
    user_id: str
    organization_id: str
    email: str
    source_ip: str
    detail: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., event_type: _Optional[str] = ..., user_id: _Optional[str] = ..., organization_id: _Optional[str] = ..., email: _Optional[str] = ..., source_ip: _Optional[str] = ..., detail: _Optional[str] = ...) -> None: ...

class ListUsersRequest(_message.Message):
    __slots__ = ("base",)
    BASE_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ...) -> None: ...

class ListUsersResponse(_message.Message):
    __slots__ = ("has_errors", "meta", "users", "error")
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    USERS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    has_errors: bool
    meta: _base_pb2.ResponseMeta
    users: _containers.RepeatedCompositeFieldContainer[AuthenticatedUserProtoDTO]
    error: _base_pb2.GlobalErrorMessage
    def __init__(self, has_errors: bool = ..., meta: _Optional[_Union[_base_pb2.ResponseMeta, _Mapping]] = ..., users: _Optional[_Iterable[_Union[AuthenticatedUserProtoDTO, _Mapping]]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ...) -> None: ...

class GetUserByIdRequest(_message.Message):
    __slots__ = ("base", "user_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    user_id: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., user_id: _Optional[str] = ...) -> None: ...

class UpdateUserRolesRequest(_message.Message):
    __slots__ = ("base", "user_id", "roles")
    BASE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    user_id: str
    roles: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., user_id: _Optional[str] = ..., roles: _Optional[_Iterable[str]] = ...) -> None: ...

class SetUserEnabledRequest(_message.Message):
    __slots__ = ("base", "user_id", "enabled")
    BASE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    user_id: str
    enabled: bool
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., user_id: _Optional[str] = ..., enabled: bool = ...) -> None: ...

class DeleteUserRequest(_message.Message):
    __slots__ = ("base", "user_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    user_id: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., user_id: _Optional[str] = ...) -> None: ...

class IdentityProviderConfigProtoDTO(_message.Message):
    __slots__ = ("organization_id", "issuer_url", "client_id", "client_secret", "email_domains", "role_claim_name", "claim_role_mapping", "enabled", "created_at", "updated_at")
    class ClaimRoleMappingEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    ISSUER_URL_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
    EMAIL_DOMAINS_FIELD_NUMBER: _ClassVar[int]
    ROLE_CLAIM_NAME_FIELD_NUMBER: _ClassVar[int]
    CLAIM_ROLE_MAPPING_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    organization_id: str
    issuer_url: str
    client_id: str
    client_secret: str
    email_domains: _containers.RepeatedScalarFieldContainer[str]
    role_claim_name: str
    claim_role_mapping: _containers.ScalarMap[str, str]
    enabled: bool
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, organization_id: _Optional[str] = ..., issuer_url: _Optional[str] = ..., client_id: _Optional[str] = ..., client_secret: _Optional[str] = ..., email_domains: _Optional[_Iterable[str]] = ..., role_claim_name: _Optional[str] = ..., claim_role_mapping: _Optional[_Mapping[str, str]] = ..., enabled: bool = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class UpsertIdentityProviderRequest(_message.Message):
    __slots__ = ("base", "config")
    BASE_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    config: IdentityProviderConfigProtoDTO
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., config: _Optional[_Union[IdentityProviderConfigProtoDTO, _Mapping]] = ...) -> None: ...

class GetIdentityProviderRequest(_message.Message):
    __slots__ = ("base", "organization_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    organization_id: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., organization_id: _Optional[str] = ...) -> None: ...

class FindIdentityProviderByEmailDomainRequest(_message.Message):
    __slots__ = ("base", "email")
    BASE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    email: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., email: _Optional[str] = ...) -> None: ...

class IdentityProviderResponse(_message.Message):
    __slots__ = ("has_errors", "meta", "config", "error")
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    has_errors: bool
    meta: _base_pb2.ResponseMeta
    config: IdentityProviderConfigProtoDTO
    error: _base_pb2.GlobalErrorMessage
    def __init__(self, has_errors: bool = ..., meta: _Optional[_Union[_base_pb2.ResponseMeta, _Mapping]] = ..., config: _Optional[_Union[IdentityProviderConfigProtoDTO, _Mapping]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ...) -> None: ...

class FindOidcUserRequest(_message.Message):
    __slots__ = ("base", "organization_id", "external_subject")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_SUBJECT_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    organization_id: str
    external_subject: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., organization_id: _Optional[str] = ..., external_subject: _Optional[str] = ...) -> None: ...

class UpsertOidcUserRequest(_message.Message):
    __slots__ = ("base", "organization_id", "external_subject", "email", "roles", "user_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_SUBJECT_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    organization_id: str
    external_subject: str
    email: str
    roles: _containers.RepeatedScalarFieldContainer[str]
    user_id: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., organization_id: _Optional[str] = ..., external_subject: _Optional[str] = ..., email: _Optional[str] = ..., roles: _Optional[_Iterable[str]] = ..., user_id: _Optional[str] = ...) -> None: ...

class PersistSkillExecutionRequest(_message.Message):
    __slots__ = ("base", "execution")
    BASE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    execution: _capability_execution_dto_pb2.SkillExecutionProtoDTO
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., execution: _Optional[_Union[_capability_execution_dto_pb2.SkillExecutionProtoDTO, _Mapping]] = ...) -> None: ...

class AppendSkillExecutionEventRequest(_message.Message):
    __slots__ = ("base", "event")
    BASE_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    event: _capability_execution_dto_pb2.SkillExecutionEventProto
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., event: _Optional[_Union[_capability_execution_dto_pb2.SkillExecutionEventProto, _Mapping]] = ...) -> None: ...

class UpsertAssetPayloadRequest(_message.Message):
    __slots__ = ("base", "payload", "sub_asset_sn", "owner", "update_mask")
    BASE_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    SUB_ASSET_SN_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    payload: _asset_pb2.AssetPayloadProtoDTO
    sub_asset_sn: str
    owner: AssetPayloadOwner
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., payload: _Optional[_Union[_asset_pb2.AssetPayloadProtoDTO, _Mapping]] = ..., sub_asset_sn: _Optional[str] = ..., owner: _Optional[_Union[AssetPayloadOwner, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class AssetPayloadOwner(_message.Message):
    __slots__ = ("asset_id", "sub_asset_id")
    ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    SUB_ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    asset_id: str
    sub_asset_id: str
    def __init__(self, asset_id: _Optional[str] = ..., sub_asset_id: _Optional[str] = ...) -> None: ...

class ListAssetPayloadsRequest(_message.Message):
    __slots__ = ("base", "owner")
    BASE_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    owner: AssetPayloadOwner
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., owner: _Optional[_Union[AssetPayloadOwner, _Mapping]] = ...) -> None: ...

class DeleteAssetPayloadRequest(_message.Message):
    __slots__ = ("base", "owner", "payload_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    owner: AssetPayloadOwner
    payload_id: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., owner: _Optional[_Union[AssetPayloadOwner, _Mapping]] = ..., payload_id: _Optional[str] = ...) -> None: ...

class AssetPayloadResponse(_message.Message):
    __slots__ = ("tid", "has_errors", "payload", "error")
    TID_FIELD_NUMBER: _ClassVar[int]
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    tid: str
    has_errors: bool
    payload: _asset_pb2.AssetPayloadProtoDTO
    error: _base_pb2.GlobalErrorMessage
    def __init__(self, tid: _Optional[str] = ..., has_errors: bool = ..., payload: _Optional[_Union[_asset_pb2.AssetPayloadProtoDTO, _Mapping]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ...) -> None: ...

class AssetPayloadListResponse(_message.Message):
    __slots__ = ("tid", "has_errors", "payloads", "error")
    TID_FIELD_NUMBER: _ClassVar[int]
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    PAYLOADS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    tid: str
    has_errors: bool
    payloads: _containers.RepeatedCompositeFieldContainer[_asset_pb2.AssetPayloadProtoDTO]
    error: _base_pb2.GlobalErrorMessage
    def __init__(self, tid: _Optional[str] = ..., has_errors: bool = ..., payloads: _Optional[_Iterable[_Union[_asset_pb2.AssetPayloadProtoDTO, _Mapping]]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ...) -> None: ...

class SetAssetPropertyRequest(_message.Message):
    __slots__ = ("base", "sn", "key", "value", "description")
    BASE_FIELD_NUMBER: _ClassVar[int]
    SN_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    sn: str
    key: str
    value: _struct_pb2.Value
    description: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., sn: _Optional[str] = ..., key: _Optional[str] = ..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ..., description: _Optional[str] = ...) -> None: ...

class ListAssetPropertiesRequest(_message.Message):
    __slots__ = ("base", "sn")
    BASE_FIELD_NUMBER: _ClassVar[int]
    SN_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    sn: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., sn: _Optional[str] = ...) -> None: ...

class DeleteAssetPropertyRequest(_message.Message):
    __slots__ = ("base", "sn", "key")
    BASE_FIELD_NUMBER: _ClassVar[int]
    SN_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    sn: str
    key: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., sn: _Optional[str] = ..., key: _Optional[str] = ...) -> None: ...

class AssetPropertyResponse(_message.Message):
    __slots__ = ("tid", "has_errors", "property", "error")
    TID_FIELD_NUMBER: _ClassVar[int]
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    tid: str
    has_errors: bool
    property: _asset_pb2.AssetPropertyProtoDTO
    error: _base_pb2.GlobalErrorMessage
    def __init__(self, tid: _Optional[str] = ..., has_errors: bool = ..., property: _Optional[_Union[_asset_pb2.AssetPropertyProtoDTO, _Mapping]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ...) -> None: ...

class AssetPropertyListResponse(_message.Message):
    __slots__ = ("tid", "has_errors", "properties", "error")
    TID_FIELD_NUMBER: _ClassVar[int]
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    tid: str
    has_errors: bool
    properties: _containers.RepeatedCompositeFieldContainer[_asset_pb2.AssetPropertyProtoDTO]
    error: _base_pb2.GlobalErrorMessage
    def __init__(self, tid: _Optional[str] = ..., has_errors: bool = ..., properties: _Optional[_Iterable[_Union[_asset_pb2.AssetPropertyProtoDTO, _Mapping]]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ...) -> None: ...

class SkillContractProtoDTO(_message.Message):
    __slots__ = ("id", "command_id", "skill_id", "display_name", "description", "schema_version", "input_schema", "output_schema", "errors", "events", "requirements", "source", "provider", "status", "first_seen_at", "last_seen_at", "previous_schema_version", "compatibility", "compatibility_notes", "required_permissions")
    ID_FIELD_NUMBER: _ClassVar[int]
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_VERSION_FIELD_NUMBER: _ClassVar[int]
    INPUT_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    REQUIREMENTS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    FIRST_SEEN_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_SEEN_AT_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_SCHEMA_VERSION_FIELD_NUMBER: _ClassVar[int]
    COMPATIBILITY_FIELD_NUMBER: _ClassVar[int]
    COMPATIBILITY_NOTES_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    id: str
    command_id: str
    skill_id: str
    display_name: str
    description: str
    schema_version: str
    input_schema: _struct_pb2.Struct
    output_schema: _struct_pb2.Struct
    errors: _containers.RepeatedCompositeFieldContainer[_device_control_contracts_pb2_1.CapabilityErrorProto]
    events: _containers.RepeatedCompositeFieldContainer[_device_control_contracts_pb2_1.CapabilityEventProto]
    requirements: _device_control_contracts_pb2_1.CapabilityRequirementsProto
    source: _device_control_contracts_pb2_1.CapabilitySourceProto
    provider: str
    status: SkillContractStatus
    first_seen_at: _timestamp_pb2.Timestamp
    last_seen_at: _timestamp_pb2.Timestamp
    previous_schema_version: str
    compatibility: SkillContractCompatibility
    compatibility_notes: _containers.RepeatedScalarFieldContainer[str]
    required_permissions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., command_id: _Optional[str] = ..., skill_id: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., schema_version: _Optional[str] = ..., input_schema: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., output_schema: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., errors: _Optional[_Iterable[_Union[_device_control_contracts_pb2_1.CapabilityErrorProto, _Mapping]]] = ..., events: _Optional[_Iterable[_Union[_device_control_contracts_pb2_1.CapabilityEventProto, _Mapping]]] = ..., requirements: _Optional[_Union[_device_control_contracts_pb2_1.CapabilityRequirementsProto, _Mapping]] = ..., source: _Optional[_Union[_device_control_contracts_pb2_1.CapabilitySourceProto, str]] = ..., provider: _Optional[str] = ..., status: _Optional[_Union[SkillContractStatus, str]] = ..., first_seen_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., last_seen_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., previous_schema_version: _Optional[str] = ..., compatibility: _Optional[_Union[SkillContractCompatibility, str]] = ..., compatibility_notes: _Optional[_Iterable[str]] = ..., required_permissions: _Optional[_Iterable[str]] = ...) -> None: ...

class UpsertSkillContractRequest(_message.Message):
    __slots__ = ("base", "contract")
    BASE_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    contract: SkillContractProtoDTO
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., contract: _Optional[_Union[SkillContractProtoDTO, _Mapping]] = ...) -> None: ...

class ListSkillContractsRequest(_message.Message):
    __slots__ = ("base", "status", "command_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    status: SkillContractStatus
    command_id: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., status: _Optional[_Union[SkillContractStatus, str]] = ..., command_id: _Optional[str] = ...) -> None: ...

class SetSkillContractStatusRequest(_message.Message):
    __slots__ = ("base", "id", "status")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    id: str
    status: SkillContractStatus
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., id: _Optional[str] = ..., status: _Optional[_Union[SkillContractStatus, str]] = ...) -> None: ...

class SetSkillContractPermissionsRequest(_message.Message):
    __slots__ = ("base", "id", "required_permissions")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    id: str
    required_permissions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., id: _Optional[str] = ..., required_permissions: _Optional[_Iterable[str]] = ...) -> None: ...

class SkillContractResponse(_message.Message):
    __slots__ = ("tid", "has_errors", "contract", "error")
    TID_FIELD_NUMBER: _ClassVar[int]
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    tid: str
    has_errors: bool
    contract: SkillContractProtoDTO
    error: _base_pb2.GlobalErrorMessage
    def __init__(self, tid: _Optional[str] = ..., has_errors: bool = ..., contract: _Optional[_Union[SkillContractProtoDTO, _Mapping]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ...) -> None: ...

class SkillContractListResponse(_message.Message):
    __slots__ = ("tid", "has_errors", "contracts", "error")
    TID_FIELD_NUMBER: _ClassVar[int]
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    CONTRACTS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    tid: str
    has_errors: bool
    contracts: _containers.RepeatedCompositeFieldContainer[SkillContractProtoDTO]
    error: _base_pb2.GlobalErrorMessage
    def __init__(self, tid: _Optional[str] = ..., has_errors: bool = ..., contracts: _Optional[_Iterable[_Union[SkillContractProtoDTO, _Mapping]]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ...) -> None: ...

class ConnectorGetAssetByIdRequest(_message.Message):
    __slots__ = ("base", "asset_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    asset_id: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., asset_id: _Optional[str] = ...) -> None: ...

class ConnectorAssetList(_message.Message):
    __slots__ = ("assets",)
    ASSETS_FIELD_NUMBER: _ClassVar[int]
    assets: _containers.RepeatedCompositeFieldContainer[_asset_pb2.AssetProtoDTO]
    def __init__(self, assets: _Optional[_Iterable[_Union[_asset_pb2.AssetProtoDTO, _Mapping]]] = ...) -> None: ...

class ListAssetsRequest(_message.Message):
    __slots__ = ("base",)
    BASE_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ...) -> None: ...

class AssetListResponse(_message.Message):
    __slots__ = ("tid", "has_errors", "assets", "error")
    TID_FIELD_NUMBER: _ClassVar[int]
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    ASSETS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    tid: str
    has_errors: bool
    assets: _containers.RepeatedCompositeFieldContainer[_asset_pb2.AssetProtoDTO]
    error: _base_pb2.GlobalErrorMessage
    def __init__(self, tid: _Optional[str] = ..., has_errors: bool = ..., assets: _Optional[_Iterable[_Union[_asset_pb2.AssetProtoDTO, _Mapping]]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ...) -> None: ...

class ConnectorRegisterAssetRequest(_message.Message):
    __slots__ = ("base", "asset")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    asset: _asset_pb2.AssetProtoDTO
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., asset: _Optional[_Union[_asset_pb2.AssetProtoDTO, _Mapping]] = ...) -> None: ...

class AssetClaimProtoDTO(_message.Message):
    __slots__ = ("id", "organization_id", "label", "created_by", "allowed_vendor", "allowed_type", "max_redemptions", "redemption_count", "expires_at", "revoked_at", "created_at", "redemptions")
    ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_VENDOR_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_TYPE_FIELD_NUMBER: _ClassVar[int]
    MAX_REDEMPTIONS_FIELD_NUMBER: _ClassVar[int]
    REDEMPTION_COUNT_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    REVOKED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    REDEMPTIONS_FIELD_NUMBER: _ClassVar[int]
    id: str
    organization_id: str
    label: str
    created_by: str
    allowed_vendor: _asset_pb2.AssetVendor
    allowed_type: _asset_pb2.AssetTypeEnum
    max_redemptions: int
    redemption_count: int
    expires_at: _timestamp_pb2.Timestamp
    revoked_at: _timestamp_pb2.Timestamp
    created_at: _timestamp_pb2.Timestamp
    redemptions: _containers.RepeatedCompositeFieldContainer[AssetClaimRedemptionProtoDTO]
    def __init__(self, id: _Optional[str] = ..., organization_id: _Optional[str] = ..., label: _Optional[str] = ..., created_by: _Optional[str] = ..., allowed_vendor: _Optional[_Union[_asset_pb2.AssetVendor, str]] = ..., allowed_type: _Optional[_Union[_asset_pb2.AssetTypeEnum, str]] = ..., max_redemptions: _Optional[int] = ..., redemption_count: _Optional[int] = ..., expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., revoked_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., redemptions: _Optional[_Iterable[_Union[AssetClaimRedemptionProtoDTO, _Mapping]]] = ...) -> None: ...

class AssetClaimRedemptionProtoDTO(_message.Message):
    __slots__ = ("id", "asset_id", "sn", "redeemed_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    SN_FIELD_NUMBER: _ClassVar[int]
    REDEEMED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    asset_id: str
    sn: str
    redeemed_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., asset_id: _Optional[str] = ..., sn: _Optional[str] = ..., redeemed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreateAssetClaimRequest(_message.Message):
    __slots__ = ("base", "organization_id", "label", "allowed_vendor", "allowed_type", "max_redemptions", "ttl_seconds")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_VENDOR_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_TYPE_FIELD_NUMBER: _ClassVar[int]
    MAX_REDEMPTIONS_FIELD_NUMBER: _ClassVar[int]
    TTL_SECONDS_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    organization_id: str
    label: str
    allowed_vendor: _asset_pb2.AssetVendor
    allowed_type: _asset_pb2.AssetTypeEnum
    max_redemptions: int
    ttl_seconds: int
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., organization_id: _Optional[str] = ..., label: _Optional[str] = ..., allowed_vendor: _Optional[_Union[_asset_pb2.AssetVendor, str]] = ..., allowed_type: _Optional[_Union[_asset_pb2.AssetTypeEnum, str]] = ..., max_redemptions: _Optional[int] = ..., ttl_seconds: _Optional[int] = ...) -> None: ...

class AssetClaimResponse(_message.Message):
    __slots__ = ("tid", "has_errors", "error", "claim", "code")
    TID_FIELD_NUMBER: _ClassVar[int]
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CLAIM_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    tid: str
    has_errors: bool
    error: _base_pb2.GlobalErrorMessage
    claim: AssetClaimProtoDTO
    code: str
    def __init__(self, tid: _Optional[str] = ..., has_errors: bool = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ..., claim: _Optional[_Union[AssetClaimProtoDTO, _Mapping]] = ..., code: _Optional[str] = ...) -> None: ...

class RedeemAssetClaimRequest(_message.Message):
    __slots__ = ("base", "code", "asset")
    BASE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    code: str
    asset: _asset_pb2.AssetProtoDTO
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., code: _Optional[str] = ..., asset: _Optional[_Union[_asset_pb2.AssetProtoDTO, _Mapping]] = ...) -> None: ...

class DescribeAssetClaimRequest(_message.Message):
    __slots__ = ("base", "code")
    BASE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    code: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., code: _Optional[str] = ...) -> None: ...

class AssetClaimDescriptionResponse(_message.Message):
    __slots__ = ("tid", "has_errors", "error", "organization_name")
    TID_FIELD_NUMBER: _ClassVar[int]
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_NAME_FIELD_NUMBER: _ClassVar[int]
    tid: str
    has_errors: bool
    error: _base_pb2.GlobalErrorMessage
    organization_name: str
    def __init__(self, tid: _Optional[str] = ..., has_errors: bool = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ..., organization_name: _Optional[str] = ...) -> None: ...

class ListAssetClaimsRequest(_message.Message):
    __slots__ = ("base", "include_closed")
    BASE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_CLOSED_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    include_closed: bool
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., include_closed: bool = ...) -> None: ...

class AssetClaimListResponse(_message.Message):
    __slots__ = ("tid", "has_errors", "claims", "error")
    TID_FIELD_NUMBER: _ClassVar[int]
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    CLAIMS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    tid: str
    has_errors: bool
    claims: _containers.RepeatedCompositeFieldContainer[AssetClaimProtoDTO]
    error: _base_pb2.GlobalErrorMessage
    def __init__(self, tid: _Optional[str] = ..., has_errors: bool = ..., claims: _Optional[_Iterable[_Union[AssetClaimProtoDTO, _Mapping]]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ...) -> None: ...

class RevokeAssetClaimRequest(_message.Message):
    __slots__ = ("base", "claim_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    CLAIM_ID_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    claim_id: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., claim_id: _Optional[str] = ...) -> None: ...

class ConnectorUpdateAssetRequest(_message.Message):
    __slots__ = ("base", "asset", "asset_id", "update_mask")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    asset: _asset_pb2.AssetProtoDTO
    asset_id: str
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., asset: _Optional[_Union[_asset_pb2.AssetProtoDTO, _Mapping]] = ..., asset_id: _Optional[str] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ConnectorUpdateSubAssetRequest(_message.Message):
    __slots__ = ("base", "sub_asset", "sub_asset_id", "update_mask")
    BASE_FIELD_NUMBER: _ClassVar[int]
    SUB_ASSET_FIELD_NUMBER: _ClassVar[int]
    SUB_ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    sub_asset: _asset_pb2.SubAssetProtoDTO
    sub_asset_id: str
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., sub_asset: _Optional[_Union[_asset_pb2.SubAssetProtoDTO, _Mapping]] = ..., sub_asset_id: _Optional[str] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ConnectorResponse(_message.Message):
    __slots__ = ("tid", "id", "timestamp", "has_errors", "asset_id", "response_message", "empty", "error", "asset", "sub_asset", "organization")
    TID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    EMPTY_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    SUB_ASSET_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    tid: str
    id: str
    timestamp: _timestamp_pb2.Timestamp
    has_errors: bool
    asset_id: str
    response_message: str
    empty: _empty_pb2.Empty
    error: _base_pb2.GlobalErrorMessage
    asset: _asset_pb2.AssetProtoDTO
    sub_asset: _asset_pb2.SubAssetProtoDTO
    organization: _asset_pb2.OrganizationProtoDTO
    def __init__(self, tid: _Optional[str] = ..., id: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., has_errors: bool = ..., asset_id: _Optional[str] = ..., response_message: _Optional[str] = ..., empty: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ..., asset: _Optional[_Union[_asset_pb2.AssetProtoDTO, _Mapping]] = ..., sub_asset: _Optional[_Union[_asset_pb2.SubAssetProtoDTO, _Mapping]] = ..., organization: _Optional[_Union[_asset_pb2.OrganizationProtoDTO, _Mapping]] = ...) -> None: ...

class AssetMonitoringResponse(_message.Message):
    __slots__ = ("tid", "timestamp", "has_errors", "empty", "error", "assets")
    TID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    EMPTY_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ASSETS_FIELD_NUMBER: _ClassVar[int]
    tid: str
    timestamp: _timestamp_pb2.Timestamp
    has_errors: bool
    empty: _empty_pb2.Empty
    error: _base_pb2.GlobalErrorMessage
    assets: ConnectorAssetList
    def __init__(self, tid: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., has_errors: bool = ..., empty: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ..., assets: _Optional[_Union[ConnectorAssetList, _Mapping]] = ...) -> None: ...

class ConnectorGetOrganizationRequest(_message.Message):
    __slots__ = ("base", "bind_code")
    BASE_FIELD_NUMBER: _ClassVar[int]
    BIND_CODE_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    bind_code: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., bind_code: _Optional[str] = ...) -> None: ...

class ConnectorStoreTelemetryRequest(_message.Message):
    __slots__ = ("base", "type", "asset_telemetry", "sub_asset_telemetry")
    BASE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ASSET_TELEMETRY_FIELD_NUMBER: _ClassVar[int]
    SUB_ASSET_TELEMETRY_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    type: TelemetryType
    asset_telemetry: AssetTelemetryProto
    sub_asset_telemetry: SubAssetTelemetryProto
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., type: _Optional[_Union[TelemetryType, str]] = ..., asset_telemetry: _Optional[_Union[AssetTelemetryProto, _Mapping]] = ..., sub_asset_telemetry: _Optional[_Union[SubAssetTelemetryProto, _Mapping]] = ...) -> None: ...

class ConnectorStoreDetectionRequest(_message.Message):
    __slots__ = ("base", "asset_sn", "sub_asset_sn", "task_id", "object_id", "object_type", "confidence", "bounding_box_x", "bounding_box_y", "bounding_box_width", "bounding_box_height", "stream_url", "detected_at", "position")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ASSET_SN_FIELD_NUMBER: _ClassVar[int]
    SUB_ASSET_SN_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    BOUNDING_BOX_X_FIELD_NUMBER: _ClassVar[int]
    BOUNDING_BOX_Y_FIELD_NUMBER: _ClassVar[int]
    BOUNDING_BOX_WIDTH_FIELD_NUMBER: _ClassVar[int]
    BOUNDING_BOX_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    STREAM_URL_FIELD_NUMBER: _ClassVar[int]
    DETECTED_AT_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    asset_sn: str
    sub_asset_sn: str
    task_id: str
    object_id: str
    object_type: str
    confidence: float
    bounding_box_x: float
    bounding_box_y: float
    bounding_box_width: float
    bounding_box_height: float
    stream_url: str
    detected_at: _timestamp_pb2.Timestamp
    position: _detection_pb2.DetectionPosition
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., asset_sn: _Optional[str] = ..., sub_asset_sn: _Optional[str] = ..., task_id: _Optional[str] = ..., object_id: _Optional[str] = ..., object_type: _Optional[str] = ..., confidence: _Optional[float] = ..., bounding_box_x: _Optional[float] = ..., bounding_box_y: _Optional[float] = ..., bounding_box_width: _Optional[float] = ..., bounding_box_height: _Optional[float] = ..., stream_url: _Optional[str] = ..., detected_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., position: _Optional[_Union[_detection_pb2.DetectionPosition, _Mapping]] = ...) -> None: ...

class AssetTelemetryProto(_message.Message):
    __slots__ = ("asset_id", "timestamp", "latitude", "longitude", "altitude", "relative_altitude", "heading", "temperature", "humidity", "wind_speed", "battery_percentage", "network_type", "network_quality", "operational_mode", "is_online", "source_system", "telemetry_data")
    class TelemetryDataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    HEADING_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    HUMIDITY_FIELD_NUMBER: _ClassVar[int]
    WIND_SPEED_FIELD_NUMBER: _ClassVar[int]
    BATTERY_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    NETWORK_TYPE_FIELD_NUMBER: _ClassVar[int]
    NETWORK_QUALITY_FIELD_NUMBER: _ClassVar[int]
    OPERATIONAL_MODE_FIELD_NUMBER: _ClassVar[int]
    IS_ONLINE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    TELEMETRY_DATA_FIELD_NUMBER: _ClassVar[int]
    asset_id: str
    timestamp: _timestamp_pb2.Timestamp
    latitude: float
    longitude: float
    altitude: float
    relative_altitude: float
    heading: float
    temperature: float
    humidity: float
    wind_speed: float
    battery_percentage: float
    network_type: str
    network_quality: int
    operational_mode: str
    is_online: bool
    source_system: str
    telemetry_data: _containers.ScalarMap[str, str]
    def __init__(self, asset_id: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., latitude: _Optional[float] = ..., longitude: _Optional[float] = ..., altitude: _Optional[float] = ..., relative_altitude: _Optional[float] = ..., heading: _Optional[float] = ..., temperature: _Optional[float] = ..., humidity: _Optional[float] = ..., wind_speed: _Optional[float] = ..., battery_percentage: _Optional[float] = ..., network_type: _Optional[str] = ..., network_quality: _Optional[int] = ..., operational_mode: _Optional[str] = ..., is_online: bool = ..., source_system: _Optional[str] = ..., telemetry_data: _Optional[_Mapping[str, str]] = ...) -> None: ...

class SubAssetTelemetryProto(_message.Message):
    __slots__ = ("asset_id", "timestamp", "latitude", "longitude", "altitude", "relative_altitude", "heading", "horizontal_speed", "vertical_speed", "wind_speed", "battery_percentage", "operational_mode", "is_online", "source_system", "telemetry_data")
    class TelemetryDataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    HEADING_FIELD_NUMBER: _ClassVar[int]
    HORIZONTAL_SPEED_FIELD_NUMBER: _ClassVar[int]
    VERTICAL_SPEED_FIELD_NUMBER: _ClassVar[int]
    WIND_SPEED_FIELD_NUMBER: _ClassVar[int]
    BATTERY_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    OPERATIONAL_MODE_FIELD_NUMBER: _ClassVar[int]
    IS_ONLINE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    TELEMETRY_DATA_FIELD_NUMBER: _ClassVar[int]
    asset_id: str
    timestamp: _timestamp_pb2.Timestamp
    latitude: float
    longitude: float
    altitude: float
    relative_altitude: float
    heading: float
    horizontal_speed: float
    vertical_speed: float
    wind_speed: float
    battery_percentage: float
    operational_mode: str
    is_online: bool
    source_system: str
    telemetry_data: _containers.ScalarMap[str, str]
    def __init__(self, asset_id: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., latitude: _Optional[float] = ..., longitude: _Optional[float] = ..., altitude: _Optional[float] = ..., relative_altitude: _Optional[float] = ..., heading: _Optional[float] = ..., horizontal_speed: _Optional[float] = ..., vertical_speed: _Optional[float] = ..., wind_speed: _Optional[float] = ..., battery_percentage: _Optional[float] = ..., operational_mode: _Optional[str] = ..., is_online: bool = ..., source_system: _Optional[str] = ..., telemetry_data: _Optional[_Mapping[str, str]] = ...) -> None: ...

class PolicyProtoDTO(_message.Message):
    __slots__ = ("id", "name", "description", "policy_type", "scope", "scope_target", "priority", "active", "strategy_type", "conditions", "constraints", "actions", "organization_id", "created_at", "modified_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    POLICY_TYPE_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    SCOPE_TARGET_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    STRATEGY_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    policy_type: str
    scope: str
    scope_target: str
    priority: int
    active: bool
    strategy_type: str
    conditions: str
    constraints: str
    actions: str
    organization_id: str
    created_at: _timestamp_pb2.Timestamp
    modified_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., policy_type: _Optional[str] = ..., scope: _Optional[str] = ..., scope_target: _Optional[str] = ..., priority: _Optional[int] = ..., active: bool = ..., strategy_type: _Optional[str] = ..., conditions: _Optional[str] = ..., constraints: _Optional[str] = ..., actions: _Optional[str] = ..., organization_id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., modified_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class PolicyProtoDTOList(_message.Message):
    __slots__ = ("policies",)
    POLICIES_FIELD_NUMBER: _ClassVar[int]
    policies: _containers.RepeatedCompositeFieldContainer[PolicyProtoDTO]
    def __init__(self, policies: _Optional[_Iterable[_Union[PolicyProtoDTO, _Mapping]]] = ...) -> None: ...

class ConnectorGetPoliciesRequest(_message.Message):
    __slots__ = ("base", "policy_type")
    BASE_FIELD_NUMBER: _ClassVar[int]
    POLICY_TYPE_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    policy_type: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., policy_type: _Optional[str] = ...) -> None: ...

class ConnectorGetAllPoliciesRequest(_message.Message):
    __slots__ = ("base", "include_inactive")
    BASE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_INACTIVE_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    include_inactive: bool
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., include_inactive: bool = ...) -> None: ...

class ConnectorPolicyResponse(_message.Message):
    __slots__ = ("tid", "has_errors", "timestamp", "error", "policy_list")
    TID_FIELD_NUMBER: _ClassVar[int]
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    POLICY_LIST_FIELD_NUMBER: _ClassVar[int]
    tid: str
    has_errors: bool
    timestamp: _timestamp_pb2.Timestamp
    error: _base_pb2.GlobalErrorMessage
    policy_list: PolicyProtoDTOList
    def __init__(self, tid: _Optional[str] = ..., has_errors: bool = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ..., policy_list: _Optional[_Union[PolicyProtoDTOList, _Mapping]] = ...) -> None: ...

class GetPolicyByIdRequest(_message.Message):
    __slots__ = ("base", "id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    id: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., id: _Optional[str] = ...) -> None: ...

class CreatePolicyRequest(_message.Message):
    __slots__ = ("base", "policy")
    BASE_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    policy: PolicyProtoDTO
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., policy: _Optional[_Union[PolicyProtoDTO, _Mapping]] = ...) -> None: ...

class UpdatePolicyRequest(_message.Message):
    __slots__ = ("base", "id", "policy")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    id: str
    policy: PolicyProtoDTO
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., id: _Optional[str] = ..., policy: _Optional[_Union[PolicyProtoDTO, _Mapping]] = ...) -> None: ...

class DeletePolicyRequest(_message.Message):
    __slots__ = ("base", "id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    id: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., id: _Optional[str] = ...) -> None: ...

class ConnectorPolicySingleResponse(_message.Message):
    __slots__ = ("tid", "has_errors", "timestamp", "error", "policy")
    TID_FIELD_NUMBER: _ClassVar[int]
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    tid: str
    has_errors: bool
    timestamp: _timestamp_pb2.Timestamp
    error: _base_pb2.GlobalErrorMessage
    policy: PolicyProtoDTO
    def __init__(self, tid: _Optional[str] = ..., has_errors: bool = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ..., policy: _Optional[_Union[PolicyProtoDTO, _Mapping]] = ...) -> None: ...

class ConnectorDeletePolicyResponse(_message.Message):
    __slots__ = ("tid", "has_errors", "timestamp", "deleted", "error")
    TID_FIELD_NUMBER: _ClassVar[int]
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    tid: str
    has_errors: bool
    timestamp: _timestamp_pb2.Timestamp
    deleted: bool
    error: _base_pb2.GlobalErrorMessage
    def __init__(self, tid: _Optional[str] = ..., has_errors: bool = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., deleted: bool = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ...) -> None: ...

class ConnectorGetAllOrganizationsRequest(_message.Message):
    __slots__ = ("base",)
    BASE_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ...) -> None: ...

class GetOrganizationByIdRequest(_message.Message):
    __slots__ = ("base", "id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    id: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., id: _Optional[str] = ...) -> None: ...

class CreateOrganizationRequest(_message.Message):
    __slots__ = ("base", "organization")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    organization: _asset_pb2.OrganizationProtoDTO
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., organization: _Optional[_Union[_asset_pb2.OrganizationProtoDTO, _Mapping]] = ...) -> None: ...

class UpdateOrganizationRequest(_message.Message):
    __slots__ = ("base", "id", "organization")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    id: str
    organization: _asset_pb2.OrganizationProtoDTO
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., id: _Optional[str] = ..., organization: _Optional[_Union[_asset_pb2.OrganizationProtoDTO, _Mapping]] = ...) -> None: ...

class DeleteOrganizationRequest(_message.Message):
    __slots__ = ("base", "id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    id: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., id: _Optional[str] = ...) -> None: ...

class OrganizationProtoDTOList(_message.Message):
    __slots__ = ("organizations",)
    ORGANIZATIONS_FIELD_NUMBER: _ClassVar[int]
    organizations: _containers.RepeatedCompositeFieldContainer[_asset_pb2.OrganizationProtoDTO]
    def __init__(self, organizations: _Optional[_Iterable[_Union[_asset_pb2.OrganizationProtoDTO, _Mapping]]] = ...) -> None: ...

class ConnectorOrganizationResponse(_message.Message):
    __slots__ = ("tid", "has_errors", "timestamp", "error", "organization_list")
    TID_FIELD_NUMBER: _ClassVar[int]
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_LIST_FIELD_NUMBER: _ClassVar[int]
    tid: str
    has_errors: bool
    timestamp: _timestamp_pb2.Timestamp
    error: _base_pb2.GlobalErrorMessage
    organization_list: OrganizationProtoDTOList
    def __init__(self, tid: _Optional[str] = ..., has_errors: bool = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ..., organization_list: _Optional[_Union[OrganizationProtoDTOList, _Mapping]] = ...) -> None: ...

class ConnectorOrganizationSingleResponse(_message.Message):
    __slots__ = ("tid", "has_errors", "timestamp", "error", "organization")
    TID_FIELD_NUMBER: _ClassVar[int]
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    tid: str
    has_errors: bool
    timestamp: _timestamp_pb2.Timestamp
    error: _base_pb2.GlobalErrorMessage
    organization: _asset_pb2.OrganizationProtoDTO
    def __init__(self, tid: _Optional[str] = ..., has_errors: bool = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ..., organization: _Optional[_Union[_asset_pb2.OrganizationProtoDTO, _Mapping]] = ...) -> None: ...

class ConnectorDeleteOrganizationResponse(_message.Message):
    __slots__ = ("tid", "has_errors", "timestamp", "deleted", "error")
    TID_FIELD_NUMBER: _ClassVar[int]
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    tid: str
    has_errors: bool
    timestamp: _timestamp_pb2.Timestamp
    deleted: bool
    error: _base_pb2.GlobalErrorMessage
    def __init__(self, tid: _Optional[str] = ..., has_errors: bool = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., deleted: bool = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ...) -> None: ...

class TheatreProtoDTO(_message.Message):
    __slots__ = ("id", "organization_id", "name", "description", "geo_zone", "assets", "assigned_user_ids", "created_at", "modified_at", "parent_theatre_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    GEO_ZONE_FIELD_NUMBER: _ClassVar[int]
    ASSETS_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_USER_IDS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    PARENT_THEATRE_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    organization_id: str
    name: str
    description: str
    geo_zone: _mission_autonomy_dto_pb2_1.GeoAreaProtoDTO
    assets: _containers.RepeatedScalarFieldContainer[str]
    assigned_user_ids: _containers.RepeatedScalarFieldContainer[str]
    created_at: _timestamp_pb2.Timestamp
    modified_at: _timestamp_pb2.Timestamp
    parent_theatre_id: str
    def __init__(self, id: _Optional[str] = ..., organization_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., geo_zone: _Optional[_Union[_mission_autonomy_dto_pb2_1.GeoAreaProtoDTO, _Mapping]] = ..., assets: _Optional[_Iterable[str]] = ..., assigned_user_ids: _Optional[_Iterable[str]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., modified_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., parent_theatre_id: _Optional[str] = ...) -> None: ...

class TheatreProtoDTOList(_message.Message):
    __slots__ = ("theatres",)
    THEATRES_FIELD_NUMBER: _ClassVar[int]
    theatres: _containers.RepeatedCompositeFieldContainer[TheatreProtoDTO]
    def __init__(self, theatres: _Optional[_Iterable[_Union[TheatreProtoDTO, _Mapping]]] = ...) -> None: ...

class ConnectorGetAllTheatresRequest(_message.Message):
    __slots__ = ("base", "organization_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    organization_id: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., organization_id: _Optional[str] = ...) -> None: ...

class GetTheatreByIdRequest(_message.Message):
    __slots__ = ("base", "id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    id: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., id: _Optional[str] = ...) -> None: ...

class CreateTheatreRequest(_message.Message):
    __slots__ = ("base", "theatre")
    BASE_FIELD_NUMBER: _ClassVar[int]
    THEATRE_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    theatre: TheatreProtoDTO
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., theatre: _Optional[_Union[TheatreProtoDTO, _Mapping]] = ...) -> None: ...

class UpdateTheatreRequest(_message.Message):
    __slots__ = ("base", "id", "theatre")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    THEATRE_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    id: str
    theatre: TheatreProtoDTO
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., id: _Optional[str] = ..., theatre: _Optional[_Union[TheatreProtoDTO, _Mapping]] = ...) -> None: ...

class DeleteTheatreRequest(_message.Message):
    __slots__ = ("base", "id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    id: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., id: _Optional[str] = ...) -> None: ...

class ConnectorTheatreResponse(_message.Message):
    __slots__ = ("tid", "has_errors", "timestamp", "error", "theatre_list")
    TID_FIELD_NUMBER: _ClassVar[int]
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    THEATRE_LIST_FIELD_NUMBER: _ClassVar[int]
    tid: str
    has_errors: bool
    timestamp: _timestamp_pb2.Timestamp
    error: _base_pb2.GlobalErrorMessage
    theatre_list: TheatreProtoDTOList
    def __init__(self, tid: _Optional[str] = ..., has_errors: bool = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ..., theatre_list: _Optional[_Union[TheatreProtoDTOList, _Mapping]] = ...) -> None: ...

class ConnectorTheatreSingleResponse(_message.Message):
    __slots__ = ("tid", "has_errors", "timestamp", "error", "theatre")
    TID_FIELD_NUMBER: _ClassVar[int]
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    THEATRE_FIELD_NUMBER: _ClassVar[int]
    tid: str
    has_errors: bool
    timestamp: _timestamp_pb2.Timestamp
    error: _base_pb2.GlobalErrorMessage
    theatre: TheatreProtoDTO
    def __init__(self, tid: _Optional[str] = ..., has_errors: bool = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ..., theatre: _Optional[_Union[TheatreProtoDTO, _Mapping]] = ...) -> None: ...

class ConnectorDeleteTheatreResponse(_message.Message):
    __slots__ = ("tid", "has_errors", "timestamp", "deleted", "error")
    TID_FIELD_NUMBER: _ClassVar[int]
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    tid: str
    has_errors: bool
    timestamp: _timestamp_pb2.Timestamp
    deleted: bool
    error: _base_pb2.GlobalErrorMessage
    def __init__(self, tid: _Optional[str] = ..., has_errors: bool = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., deleted: bool = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ...) -> None: ...

class AssignUserToTheatreRequest(_message.Message):
    __slots__ = ("base", "user_id", "theatre_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    THEATRE_ID_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    user_id: str
    theatre_id: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., user_id: _Optional[str] = ..., theatre_id: _Optional[str] = ...) -> None: ...

class RemoveUserFromTheatreRequest(_message.Message):
    __slots__ = ("base", "user_id", "theatre_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    THEATRE_ID_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    user_id: str
    theatre_id: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., user_id: _Optional[str] = ..., theatre_id: _Optional[str] = ...) -> None: ...

class TheatreAssignmentResponse(_message.Message):
    __slots__ = ("tid", "has_errors", "timestamp", "error")
    TID_FIELD_NUMBER: _ClassVar[int]
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    tid: str
    has_errors: bool
    timestamp: _timestamp_pb2.Timestamp
    error: _base_pb2.GlobalErrorMessage
    def __init__(self, tid: _Optional[str] = ..., has_errors: bool = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ...) -> None: ...

class ListNoFlyZonesRequest(_message.Message):
    __slots__ = ("base", "organization_id", "active_only")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_ONLY_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    organization_id: str
    active_only: bool
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., organization_id: _Optional[str] = ..., active_only: bool = ...) -> None: ...

class UpsertNoFlyZoneRequest(_message.Message):
    __slots__ = ("base", "zone")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    zone: _mission_autonomy_dto_pb2_1.MissionZoneProtoDTO
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., zone: _Optional[_Union[_mission_autonomy_dto_pb2_1.MissionZoneProtoDTO, _Mapping]] = ...) -> None: ...

class DeleteNoFlyZoneRequest(_message.Message):
    __slots__ = ("base", "id", "organization_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    id: str
    organization_id: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., id: _Optional[str] = ..., organization_id: _Optional[str] = ...) -> None: ...

class NoFlyZoneListResponse(_message.Message):
    __slots__ = ("tid", "has_errors", "timestamp", "error", "zones")
    TID_FIELD_NUMBER: _ClassVar[int]
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ZONES_FIELD_NUMBER: _ClassVar[int]
    tid: str
    has_errors: bool
    timestamp: _timestamp_pb2.Timestamp
    error: _base_pb2.GlobalErrorMessage
    zones: _containers.RepeatedCompositeFieldContainer[_mission_autonomy_dto_pb2_1.MissionZoneProtoDTO]
    def __init__(self, tid: _Optional[str] = ..., has_errors: bool = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ..., zones: _Optional[_Iterable[_Union[_mission_autonomy_dto_pb2_1.MissionZoneProtoDTO, _Mapping]]] = ...) -> None: ...

class NoFlyZoneSingleResponse(_message.Message):
    __slots__ = ("tid", "has_errors", "timestamp", "error", "zone")
    TID_FIELD_NUMBER: _ClassVar[int]
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    tid: str
    has_errors: bool
    timestamp: _timestamp_pb2.Timestamp
    error: _base_pb2.GlobalErrorMessage
    zone: _mission_autonomy_dto_pb2_1.MissionZoneProtoDTO
    def __init__(self, tid: _Optional[str] = ..., has_errors: bool = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ..., zone: _Optional[_Union[_mission_autonomy_dto_pb2_1.MissionZoneProtoDTO, _Mapping]] = ...) -> None: ...

class DeleteNoFlyZoneResponse(_message.Message):
    __slots__ = ("tid", "has_errors", "timestamp", "error", "deleted")
    TID_FIELD_NUMBER: _ClassVar[int]
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    tid: str
    has_errors: bool
    timestamp: _timestamp_pb2.Timestamp
    error: _base_pb2.GlobalErrorMessage
    deleted: bool
    def __init__(self, tid: _Optional[str] = ..., has_errors: bool = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ..., deleted: bool = ...) -> None: ...

class ProvisionLicensedOrganizationRequest(_message.Message):
    __slots__ = ("base", "organization_id", "name", "description", "credentials")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    organization_id: str
    name: str
    description: str
    credentials: LicenseActivationCredentialsProtoDTO
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., organization_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., credentials: _Optional[_Union[LicenseActivationCredentialsProtoDTO, _Mapping]] = ...) -> None: ...

class ProvisionLicensedOrganizationResponse(_message.Message):
    __slots__ = ("tid", "has_errors", "timestamp", "error", "organization", "already_exists")
    TID_FIELD_NUMBER: _ClassVar[int]
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    ALREADY_EXISTS_FIELD_NUMBER: _ClassVar[int]
    tid: str
    has_errors: bool
    timestamp: _timestamp_pb2.Timestamp
    error: _base_pb2.GlobalErrorMessage
    organization: _asset_pb2.OrganizationProtoDTO
    already_exists: bool
    def __init__(self, tid: _Optional[str] = ..., has_errors: bool = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ..., organization: _Optional[_Union[_asset_pb2.OrganizationProtoDTO, _Mapping]] = ..., already_exists: bool = ...) -> None: ...

class LicenseActivationCredentialsProtoDTO(_message.Message):
    __slots__ = ("organization_id", "activation_id", "sealed_token", "sealing_scheme", "created_at", "modified_at")
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIVATION_ID_FIELD_NUMBER: _ClassVar[int]
    SEALED_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SEALING_SCHEME_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    organization_id: str
    activation_id: str
    sealed_token: bytes
    sealing_scheme: str
    created_at: _timestamp_pb2.Timestamp
    modified_at: _timestamp_pb2.Timestamp
    def __init__(self, organization_id: _Optional[str] = ..., activation_id: _Optional[str] = ..., sealed_token: _Optional[bytes] = ..., sealing_scheme: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., modified_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListLicenseActivationCredentialsRequest(_message.Message):
    __slots__ = ("base",)
    BASE_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ...) -> None: ...

class GetLicenseActivationCredentialsRequest(_message.Message):
    __slots__ = ("base", "organization_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    organization_id: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., organization_id: _Optional[str] = ...) -> None: ...

class PutLicenseActivationCredentialsRequest(_message.Message):
    __slots__ = ("base", "credentials")
    BASE_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    credentials: LicenseActivationCredentialsProtoDTO
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., credentials: _Optional[_Union[LicenseActivationCredentialsProtoDTO, _Mapping]] = ...) -> None: ...

class DeleteLicenseActivationCredentialsRequest(_message.Message):
    __slots__ = ("base", "organization_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    organization_id: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., organization_id: _Optional[str] = ...) -> None: ...

class LicenseActivationCredentialsListResponse(_message.Message):
    __slots__ = ("tid", "has_errors", "timestamp", "error", "credentials")
    TID_FIELD_NUMBER: _ClassVar[int]
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    tid: str
    has_errors: bool
    timestamp: _timestamp_pb2.Timestamp
    error: _base_pb2.GlobalErrorMessage
    credentials: _containers.RepeatedCompositeFieldContainer[LicenseActivationCredentialsProtoDTO]
    def __init__(self, tid: _Optional[str] = ..., has_errors: bool = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ..., credentials: _Optional[_Iterable[_Union[LicenseActivationCredentialsProtoDTO, _Mapping]]] = ...) -> None: ...

class LicenseActivationCredentialsSingleResponse(_message.Message):
    __slots__ = ("tid", "has_errors", "timestamp", "error", "credentials")
    TID_FIELD_NUMBER: _ClassVar[int]
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    tid: str
    has_errors: bool
    timestamp: _timestamp_pb2.Timestamp
    error: _base_pb2.GlobalErrorMessage
    credentials: LicenseActivationCredentialsProtoDTO
    def __init__(self, tid: _Optional[str] = ..., has_errors: bool = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ..., credentials: _Optional[_Union[LicenseActivationCredentialsProtoDTO, _Mapping]] = ...) -> None: ...

class DeleteLicenseActivationCredentialsResponse(_message.Message):
    __slots__ = ("tid", "has_errors", "timestamp", "error", "deleted")
    TID_FIELD_NUMBER: _ClassVar[int]
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    tid: str
    has_errors: bool
    timestamp: _timestamp_pb2.Timestamp
    error: _base_pb2.GlobalErrorMessage
    deleted: bool
    def __init__(self, tid: _Optional[str] = ..., has_errors: bool = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ..., deleted: bool = ...) -> None: ...

class EventTriggerProtoDTO(_message.Message):
    __slots__ = ("id", "name", "active", "event_type", "asset_sn", "object_type", "min_confidence", "telemetry_field", "comparison_operator", "comparison_value", "webhook_token", "application_id", "skill_id", "execution_parameters_json", "auto_start", "cooldown_seconds", "last_fired_at", "created_at", "modified_at", "bridge_id", "dispatch_target", "priority", "organization_id", "theatre_id", "attention_reason")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ASSET_SN_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    MIN_CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    TELEMETRY_FIELD_FIELD_NUMBER: _ClassVar[int]
    COMPARISON_OPERATOR_FIELD_NUMBER: _ClassVar[int]
    COMPARISON_VALUE_FIELD_NUMBER: _ClassVar[int]
    WEBHOOK_TOKEN_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_PARAMETERS_JSON_FIELD_NUMBER: _ClassVar[int]
    AUTO_START_FIELD_NUMBER: _ClassVar[int]
    COOLDOWN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    LAST_FIRED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    BRIDGE_ID_FIELD_NUMBER: _ClassVar[int]
    DISPATCH_TARGET_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    THEATRE_ID_FIELD_NUMBER: _ClassVar[int]
    ATTENTION_REASON_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    active: bool
    event_type: str
    asset_sn: str
    object_type: str
    min_confidence: float
    telemetry_field: str
    comparison_operator: str
    comparison_value: str
    webhook_token: str
    application_id: str
    skill_id: str
    execution_parameters_json: str
    auto_start: bool
    cooldown_seconds: int
    last_fired_at: _timestamp_pb2.Timestamp
    created_at: _timestamp_pb2.Timestamp
    modified_at: _timestamp_pb2.Timestamp
    bridge_id: str
    dispatch_target: str
    priority: int
    organization_id: str
    theatre_id: str
    attention_reason: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., active: bool = ..., event_type: _Optional[str] = ..., asset_sn: _Optional[str] = ..., object_type: _Optional[str] = ..., min_confidence: _Optional[float] = ..., telemetry_field: _Optional[str] = ..., comparison_operator: _Optional[str] = ..., comparison_value: _Optional[str] = ..., webhook_token: _Optional[str] = ..., application_id: _Optional[str] = ..., skill_id: _Optional[str] = ..., execution_parameters_json: _Optional[str] = ..., auto_start: bool = ..., cooldown_seconds: _Optional[int] = ..., last_fired_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., modified_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., bridge_id: _Optional[str] = ..., dispatch_target: _Optional[str] = ..., priority: _Optional[int] = ..., organization_id: _Optional[str] = ..., theatre_id: _Optional[str] = ..., attention_reason: _Optional[str] = ...) -> None: ...

class EventTriggerProtoDTOList(_message.Message):
    __slots__ = ("event_triggers",)
    EVENT_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    event_triggers: _containers.RepeatedCompositeFieldContainer[EventTriggerProtoDTO]
    def __init__(self, event_triggers: _Optional[_Iterable[_Union[EventTriggerProtoDTO, _Mapping]]] = ...) -> None: ...

class ConnectorGetAllEventTriggersRequest(_message.Message):
    __slots__ = ("base", "active_only")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_ONLY_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    active_only: bool
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., active_only: bool = ...) -> None: ...

class GetEventTriggerByIdRequest(_message.Message):
    __slots__ = ("base", "id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    id: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., id: _Optional[str] = ...) -> None: ...

class CreateEventTriggerRequest(_message.Message):
    __slots__ = ("base", "event_trigger")
    BASE_FIELD_NUMBER: _ClassVar[int]
    EVENT_TRIGGER_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    event_trigger: EventTriggerProtoDTO
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., event_trigger: _Optional[_Union[EventTriggerProtoDTO, _Mapping]] = ...) -> None: ...

class UpdateEventTriggerRequest(_message.Message):
    __slots__ = ("base", "id", "event_trigger")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_TRIGGER_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    id: str
    event_trigger: EventTriggerProtoDTO
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., id: _Optional[str] = ..., event_trigger: _Optional[_Union[EventTriggerProtoDTO, _Mapping]] = ...) -> None: ...

class DeleteEventTriggerRequest(_message.Message):
    __slots__ = ("base", "id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    id: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., id: _Optional[str] = ...) -> None: ...

class RecordEventTriggerFiredRequest(_message.Message):
    __slots__ = ("base", "id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    id: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., id: _Optional[str] = ...) -> None: ...

class RegenerateEventTriggerWebhookTokenRequest(_message.Message):
    __slots__ = ("base", "id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    id: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., id: _Optional[str] = ...) -> None: ...

class GetEventTriggerByWebhookTokenRequest(_message.Message):
    __slots__ = ("base", "token")
    BASE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    token: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., token: _Optional[str] = ...) -> None: ...

class ConnectorEventTriggerResponse(_message.Message):
    __slots__ = ("tid", "has_errors", "timestamp", "error", "event_trigger_list")
    TID_FIELD_NUMBER: _ClassVar[int]
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    EVENT_TRIGGER_LIST_FIELD_NUMBER: _ClassVar[int]
    tid: str
    has_errors: bool
    timestamp: _timestamp_pb2.Timestamp
    error: _base_pb2.GlobalErrorMessage
    event_trigger_list: EventTriggerProtoDTOList
    def __init__(self, tid: _Optional[str] = ..., has_errors: bool = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ..., event_trigger_list: _Optional[_Union[EventTriggerProtoDTOList, _Mapping]] = ...) -> None: ...

class ConnectorEventTriggerSingleResponse(_message.Message):
    __slots__ = ("tid", "has_errors", "timestamp", "error", "event_trigger")
    TID_FIELD_NUMBER: _ClassVar[int]
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    EVENT_TRIGGER_FIELD_NUMBER: _ClassVar[int]
    tid: str
    has_errors: bool
    timestamp: _timestamp_pb2.Timestamp
    error: _base_pb2.GlobalErrorMessage
    event_trigger: EventTriggerProtoDTO
    def __init__(self, tid: _Optional[str] = ..., has_errors: bool = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ..., event_trigger: _Optional[_Union[EventTriggerProtoDTO, _Mapping]] = ...) -> None: ...

class ConnectorDeleteEventTriggerResponse(_message.Message):
    __slots__ = ("tid", "has_errors", "timestamp", "deleted", "error")
    TID_FIELD_NUMBER: _ClassVar[int]
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    tid: str
    has_errors: bool
    timestamp: _timestamp_pb2.Timestamp
    deleted: bool
    error: _base_pb2.GlobalErrorMessage
    def __init__(self, tid: _Optional[str] = ..., has_errors: bool = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., deleted: bool = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ...) -> None: ...

class DetectionSummaryProtoDTO(_message.Message):
    __slots__ = ("id", "asset_sn", "object_type", "confidence", "detected_at", "object_id", "position")
    ID_FIELD_NUMBER: _ClassVar[int]
    ASSET_SN_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    DETECTED_AT_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    id: str
    asset_sn: str
    object_type: str
    confidence: float
    detected_at: _timestamp_pb2.Timestamp
    object_id: str
    position: _detection_pb2.DetectionPosition
    def __init__(self, id: _Optional[str] = ..., asset_sn: _Optional[str] = ..., object_type: _Optional[str] = ..., confidence: _Optional[float] = ..., detected_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., object_id: _Optional[str] = ..., position: _Optional[_Union[_detection_pb2.DetectionPosition, _Mapping]] = ...) -> None: ...

class ListRecentDetectionsRequest(_message.Message):
    __slots__ = ("base", "since", "asset_sn", "object_type", "min_confidence")
    BASE_FIELD_NUMBER: _ClassVar[int]
    SINCE_FIELD_NUMBER: _ClassVar[int]
    ASSET_SN_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    MIN_CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    since: _timestamp_pb2.Timestamp
    asset_sn: str
    object_type: str
    min_confidence: float
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., since: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., asset_sn: _Optional[str] = ..., object_type: _Optional[str] = ..., min_confidence: _Optional[float] = ...) -> None: ...

class ConnectorDetectionListResponse(_message.Message):
    __slots__ = ("tid", "has_errors", "timestamp", "detections", "error")
    TID_FIELD_NUMBER: _ClassVar[int]
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    DETECTIONS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    tid: str
    has_errors: bool
    timestamp: _timestamp_pb2.Timestamp
    detections: _containers.RepeatedCompositeFieldContainer[DetectionSummaryProtoDTO]
    error: _base_pb2.GlobalErrorMessage
    def __init__(self, tid: _Optional[str] = ..., has_errors: bool = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., detections: _Optional[_Iterable[_Union[DetectionSummaryProtoDTO, _Mapping]]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ...) -> None: ...

class GetLatestTelemetryForAssetRequest(_message.Message):
    __slots__ = ("base", "asset_sn")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ASSET_SN_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    asset_sn: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., asset_sn: _Optional[str] = ...) -> None: ...

class ConnectorTelemetrySingleResponse(_message.Message):
    __slots__ = ("tid", "has_errors", "timestamp", "error", "telemetry")
    TID_FIELD_NUMBER: _ClassVar[int]
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    TELEMETRY_FIELD_NUMBER: _ClassVar[int]
    tid: str
    has_errors: bool
    timestamp: _timestamp_pb2.Timestamp
    error: _base_pb2.GlobalErrorMessage
    telemetry: AssetTelemetryProto
    def __init__(self, tid: _Optional[str] = ..., has_errors: bool = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ..., telemetry: _Optional[_Union[AssetTelemetryProto, _Mapping]] = ...) -> None: ...

class TechnicalConfigProtoDTO(_message.Message):
    __slots__ = ("id", "config_key", "config_value", "value_type", "scope", "scope_target", "active", "description", "organization_id", "created_at", "modified_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_KEY_FIELD_NUMBER: _ClassVar[int]
    CONFIG_VALUE_FIELD_NUMBER: _ClassVar[int]
    VALUE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    SCOPE_TARGET_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    config_key: str
    config_value: str
    value_type: str
    scope: str
    scope_target: str
    active: bool
    description: str
    organization_id: str
    created_at: _timestamp_pb2.Timestamp
    modified_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., config_key: _Optional[str] = ..., config_value: _Optional[str] = ..., value_type: _Optional[str] = ..., scope: _Optional[str] = ..., scope_target: _Optional[str] = ..., active: bool = ..., description: _Optional[str] = ..., organization_id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., modified_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class TechnicalConfigProtoDTOList(_message.Message):
    __slots__ = ("configs",)
    CONFIGS_FIELD_NUMBER: _ClassVar[int]
    configs: _containers.RepeatedCompositeFieldContainer[TechnicalConfigProtoDTO]
    def __init__(self, configs: _Optional[_Iterable[_Union[TechnicalConfigProtoDTO, _Mapping]]] = ...) -> None: ...

class ConnectorGetConfigsRequest(_message.Message):
    __slots__ = ("base", "scope", "scope_target", "include_inactive")
    BASE_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    SCOPE_TARGET_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_INACTIVE_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    scope: str
    scope_target: str
    include_inactive: bool
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., scope: _Optional[str] = ..., scope_target: _Optional[str] = ..., include_inactive: bool = ...) -> None: ...

class ConnectorConfigResponse(_message.Message):
    __slots__ = ("tid", "has_errors", "timestamp", "error", "config_list")
    TID_FIELD_NUMBER: _ClassVar[int]
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CONFIG_LIST_FIELD_NUMBER: _ClassVar[int]
    tid: str
    has_errors: bool
    timestamp: _timestamp_pb2.Timestamp
    error: _base_pb2.GlobalErrorMessage
    config_list: TechnicalConfigProtoDTOList
    def __init__(self, tid: _Optional[str] = ..., has_errors: bool = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ..., config_list: _Optional[_Union[TechnicalConfigProtoDTOList, _Mapping]] = ...) -> None: ...

class GetTechnicalConfigByIdRequest(_message.Message):
    __slots__ = ("base", "id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    id: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., id: _Optional[str] = ...) -> None: ...

class CreateTechnicalConfigRequest(_message.Message):
    __slots__ = ("base", "config")
    BASE_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    config: TechnicalConfigProtoDTO
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., config: _Optional[_Union[TechnicalConfigProtoDTO, _Mapping]] = ...) -> None: ...

class UpdateTechnicalConfigRequest(_message.Message):
    __slots__ = ("base", "id", "config")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    id: str
    config: TechnicalConfigProtoDTO
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., id: _Optional[str] = ..., config: _Optional[_Union[TechnicalConfigProtoDTO, _Mapping]] = ...) -> None: ...

class DeleteTechnicalConfigRequest(_message.Message):
    __slots__ = ("base", "id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    id: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., id: _Optional[str] = ...) -> None: ...

class ConnectorConfigSingleResponse(_message.Message):
    __slots__ = ("tid", "has_errors", "timestamp", "error", "config")
    TID_FIELD_NUMBER: _ClassVar[int]
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    tid: str
    has_errors: bool
    timestamp: _timestamp_pb2.Timestamp
    error: _base_pb2.GlobalErrorMessage
    config: TechnicalConfigProtoDTO
    def __init__(self, tid: _Optional[str] = ..., has_errors: bool = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ..., config: _Optional[_Union[TechnicalConfigProtoDTO, _Mapping]] = ...) -> None: ...

class ConnectorDeleteConfigResponse(_message.Message):
    __slots__ = ("tid", "has_errors", "timestamp", "deleted", "error")
    TID_FIELD_NUMBER: _ClassVar[int]
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    tid: str
    has_errors: bool
    timestamp: _timestamp_pb2.Timestamp
    deleted: bool
    error: _base_pb2.GlobalErrorMessage
    def __init__(self, tid: _Optional[str] = ..., has_errors: bool = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., deleted: bool = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ...) -> None: ...
