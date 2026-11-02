import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EnrollmentPurpose(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ENROLLMENT_PURPOSE_UNSPECIFIED: _ClassVar[EnrollmentPurpose]
    ENROLLMENT_PURPOSE_ENROLL: _ClassVar[EnrollmentPurpose]
    ENROLLMENT_PURPOSE_ROTATE: _ClassVar[EnrollmentPurpose]
    ENROLLMENT_PURPOSE_RENEW: _ClassVar[EnrollmentPurpose]

class KeyProtection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    KEY_PROTECTION_UNSPECIFIED: _ClassVar[KeyProtection]
    KEY_PROTECTION_SOFTWARE_DEV: _ClassVar[KeyProtection]
    KEY_PROTECTION_SOFTWARE_SEALED: _ClassVar[KeyProtection]
    KEY_PROTECTION_TPM: _ClassVar[KeyProtection]
    KEY_PROTECTION_SECURE_ELEMENT: _ClassVar[KeyProtection]
    KEY_PROTECTION_MOBILE_TEE: _ClassVar[KeyProtection]
    KEY_PROTECTION_MOBILE_SECURE_HW: _ClassVar[KeyProtection]

class AttestationFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ATTESTATION_FORMAT_UNSPECIFIED: _ClassVar[AttestationFormat]
    ATTESTATION_FORMAT_TPM2_CERTIFY: _ClassVar[AttestationFormat]
    ATTESTATION_FORMAT_NXP_SE050: _ClassVar[AttestationFormat]
    ATTESTATION_FORMAT_ANDROID_KEY_ATTESTATION: _ClassVar[AttestationFormat]
    ATTESTATION_FORMAT_APPLE_APP_ATTEST: _ClassVar[AttestationFormat]

class NodeClass(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NODE_CLASS_UNSPECIFIED: _ClassVar[NodeClass]
    NODE_CLASS_INFRASTRUCTURE: _ClassVar[NodeClass]
    NODE_CLASS_PERSONAL: _ClassVar[NodeClass]
ENROLLMENT_PURPOSE_UNSPECIFIED: EnrollmentPurpose
ENROLLMENT_PURPOSE_ENROLL: EnrollmentPurpose
ENROLLMENT_PURPOSE_ROTATE: EnrollmentPurpose
ENROLLMENT_PURPOSE_RENEW: EnrollmentPurpose
KEY_PROTECTION_UNSPECIFIED: KeyProtection
KEY_PROTECTION_SOFTWARE_DEV: KeyProtection
KEY_PROTECTION_SOFTWARE_SEALED: KeyProtection
KEY_PROTECTION_TPM: KeyProtection
KEY_PROTECTION_SECURE_ELEMENT: KeyProtection
KEY_PROTECTION_MOBILE_TEE: KeyProtection
KEY_PROTECTION_MOBILE_SECURE_HW: KeyProtection
ATTESTATION_FORMAT_UNSPECIFIED: AttestationFormat
ATTESTATION_FORMAT_TPM2_CERTIFY: AttestationFormat
ATTESTATION_FORMAT_NXP_SE050: AttestationFormat
ATTESTATION_FORMAT_ANDROID_KEY_ATTESTATION: AttestationFormat
ATTESTATION_FORMAT_APPLE_APP_ATTEST: AttestationFormat
NODE_CLASS_UNSPECIFIED: NodeClass
NODE_CLASS_INFRASTRUCTURE: NodeClass
NODE_CLASS_PERSONAL: NodeClass

class BeginEnrollmentRequest(_message.Message):
    __slots__ = ("purpose",)
    PURPOSE_FIELD_NUMBER: _ClassVar[int]
    purpose: EnrollmentPurpose
    def __init__(self, purpose: _Optional[_Union[EnrollmentPurpose, str]] = ...) -> None: ...

class BeginEnrollmentResponse(_message.Message):
    __slots__ = ("challenge", "expires_at")
    CHALLENGE_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    challenge: bytes
    expires_at: _timestamp_pb2.Timestamp
    def __init__(self, challenge: _Optional[bytes] = ..., expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class IdentityKey(_message.Message):
    __slots__ = ("alg", "public_key", "protection")
    ALG_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    PROTECTION_FIELD_NUMBER: _ClassVar[int]
    alg: int
    public_key: bytes
    protection: KeyProtection
    def __init__(self, alg: _Optional[int] = ..., public_key: _Optional[bytes] = ..., protection: _Optional[_Union[KeyProtection, str]] = ...) -> None: ...

class Attestation(_message.Message):
    __slots__ = ("format", "evidence")
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    EVIDENCE_FIELD_NUMBER: _ClassVar[int]
    format: AttestationFormat
    evidence: bytes
    def __init__(self, format: _Optional[_Union[AttestationFormat, str]] = ..., evidence: _Optional[bytes] = ...) -> None: ...

class EnrollingAsset(_message.Message):
    __slots__ = ("sn", "name", "vendor", "type")
    SN_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VENDOR_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    sn: str
    name: str
    vendor: str
    type: str
    def __init__(self, sn: _Optional[str] = ..., name: _Optional[str] = ..., vendor: _Optional[str] = ..., type: _Optional[str] = ...) -> None: ...

class CompleteEnrollmentRequest(_message.Message):
    __slots__ = ("claim_code", "challenge", "identity_key", "crypto_suites", "attestation", "assets", "runtime_version", "display_name", "signature")
    CLAIM_CODE_FIELD_NUMBER: _ClassVar[int]
    CHALLENGE_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_KEY_FIELD_NUMBER: _ClassVar[int]
    CRYPTO_SUITES_FIELD_NUMBER: _ClassVar[int]
    ATTESTATION_FIELD_NUMBER: _ClassVar[int]
    ASSETS_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_VERSION_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    claim_code: str
    challenge: bytes
    identity_key: IdentityKey
    crypto_suites: _containers.RepeatedScalarFieldContainer[int]
    attestation: Attestation
    assets: _containers.RepeatedCompositeFieldContainer[EnrollingAsset]
    runtime_version: str
    display_name: str
    signature: bytes
    def __init__(self, claim_code: _Optional[str] = ..., challenge: _Optional[bytes] = ..., identity_key: _Optional[_Union[IdentityKey, _Mapping]] = ..., crypto_suites: _Optional[_Iterable[int]] = ..., attestation: _Optional[_Union[Attestation, _Mapping]] = ..., assets: _Optional[_Iterable[_Union[EnrollingAsset, _Mapping]]] = ..., runtime_version: _Optional[str] = ..., display_name: _Optional[str] = ..., signature: _Optional[bytes] = ...) -> None: ...

class TrustAnchor(_message.Message):
    __slots__ = ("key_id", "alg", "public_key")
    KEY_ID_FIELD_NUMBER: _ClassVar[int]
    ALG_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    key_id: bytes
    alg: int
    public_key: bytes
    def __init__(self, key_id: _Optional[bytes] = ..., alg: _Optional[int] = ..., public_key: _Optional[bytes] = ...) -> None: ...

class CompleteEnrollmentResponse(_message.Message):
    __slots__ = ("node_id", "organization_id", "organization_name", "installation_id", "anchors", "credential", "credential_expires_at", "identity_key_id", "allowed_suites", "node_class")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_NAME_FIELD_NUMBER: _ClassVar[int]
    INSTALLATION_ID_FIELD_NUMBER: _ClassVar[int]
    ANCHORS_FIELD_NUMBER: _ClassVar[int]
    CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    CREDENTIAL_EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_SUITES_FIELD_NUMBER: _ClassVar[int]
    NODE_CLASS_FIELD_NUMBER: _ClassVar[int]
    node_id: str
    organization_id: str
    organization_name: str
    installation_id: str
    anchors: _containers.RepeatedCompositeFieldContainer[TrustAnchor]
    credential: str
    credential_expires_at: _timestamp_pb2.Timestamp
    identity_key_id: bytes
    allowed_suites: _containers.RepeatedScalarFieldContainer[int]
    node_class: NodeClass
    def __init__(self, node_id: _Optional[str] = ..., organization_id: _Optional[str] = ..., organization_name: _Optional[str] = ..., installation_id: _Optional[str] = ..., anchors: _Optional[_Iterable[_Union[TrustAnchor, _Mapping]]] = ..., credential: _Optional[str] = ..., credential_expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., identity_key_id: _Optional[bytes] = ..., allowed_suites: _Optional[_Iterable[int]] = ..., node_class: _Optional[_Union[NodeClass, str]] = ...) -> None: ...

class RotateIdentityKeyRequest(_message.Message):
    __slots__ = ("challenge", "old_key_id", "new_key", "attestation", "signature_old", "signature_new")
    CHALLENGE_FIELD_NUMBER: _ClassVar[int]
    OLD_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    NEW_KEY_FIELD_NUMBER: _ClassVar[int]
    ATTESTATION_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_OLD_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_NEW_FIELD_NUMBER: _ClassVar[int]
    challenge: bytes
    old_key_id: bytes
    new_key: IdentityKey
    attestation: Attestation
    signature_old: bytes
    signature_new: bytes
    def __init__(self, challenge: _Optional[bytes] = ..., old_key_id: _Optional[bytes] = ..., new_key: _Optional[_Union[IdentityKey, _Mapping]] = ..., attestation: _Optional[_Union[Attestation, _Mapping]] = ..., signature_old: _Optional[bytes] = ..., signature_new: _Optional[bytes] = ...) -> None: ...

class RotateIdentityKeyResponse(_message.Message):
    __slots__ = ("identity_key_id",)
    IDENTITY_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    identity_key_id: bytes
    def __init__(self, identity_key_id: _Optional[bytes] = ...) -> None: ...

class RenewCredentialRequest(_message.Message):
    __slots__ = ("challenge", "key_id", "signature")
    CHALLENGE_FIELD_NUMBER: _ClassVar[int]
    KEY_ID_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    challenge: bytes
    key_id: bytes
    signature: bytes
    def __init__(self, challenge: _Optional[bytes] = ..., key_id: _Optional[bytes] = ..., signature: _Optional[bytes] = ...) -> None: ...

class RenewCredentialResponse(_message.Message):
    __slots__ = ("credential", "credential_expires_at")
    CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    CREDENTIAL_EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    credential: str
    credential_expires_at: _timestamp_pb2.Timestamp
    def __init__(self, credential: _Optional[str] = ..., credential_expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
