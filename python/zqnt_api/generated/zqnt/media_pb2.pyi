import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from . import common_pb2 as _common_pb2
from . import base_pb2 as _base_pb2
from . import asset_pb2 as _asset_pb2
from . import device_control_contracts_pb2 as _device_control_contracts_pb2
from . import detection_pb2 as _detection_pb2
from . import mission_autonomy_types_pb2 as _mission_autonomy_types_pb2
from . import mission_autonomy_dto_pb2 as _mission_autonomy_dto_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MediaType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MEDIA_TYPE_UNSPECIFIED: _ClassVar[MediaType]
    MEDIA_TYPE_PHOTO: _ClassVar[MediaType]
    MEDIA_TYPE_VIDEO: _ClassVar[MediaType]
    MEDIA_TYPE_OTHER: _ClassVar[MediaType]

class MediaFileStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MEDIA_FILE_STATUS_UNSPECIFIED: _ClassVar[MediaFileStatus]
    MEDIA_FILE_STATUS_STORED: _ClassVar[MediaFileStatus]
    MEDIA_FILE_STATUS_PENDING: _ClassVar[MediaFileStatus]
MEDIA_TYPE_UNSPECIFIED: MediaType
MEDIA_TYPE_PHOTO: MediaType
MEDIA_TYPE_VIDEO: MediaType
MEDIA_TYPE_OTHER: MediaType
MEDIA_FILE_STATUS_UNSPECIFIED: MediaFileStatus
MEDIA_FILE_STATUS_STORED: MediaFileStatus
MEDIA_FILE_STATUS_PENDING: MediaFileStatus

class MediaCapturePosition(_message.Message):
    __slots__ = ("latitude", "longitude", "absolute_altitude", "relative_altitude", "gimbal_yaw")
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    ABSOLUTE_ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    GIMBAL_YAW_FIELD_NUMBER: _ClassVar[int]
    latitude: float
    longitude: float
    absolute_altitude: float
    relative_altitude: float
    gimbal_yaw: float
    def __init__(self, latitude: _Optional[float] = ..., longitude: _Optional[float] = ..., absolute_altitude: _Optional[float] = ..., relative_altitude: _Optional[float] = ..., gimbal_yaw: _Optional[float] = ...) -> None: ...

class MediaFileProtoDTO(_message.Message):
    __slots__ = ("id", "media_type", "status", "file_name", "content_type", "size_bytes", "bucket", "object_key", "folder_path", "asset_sn", "device_sn", "organization_id", "organization_name", "execution_id", "application_id", "application_name", "skill_id", "skill_name", "captured_at", "uploaded_at", "position", "vendor_flight_id", "metadata", "download_url")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    MEDIA_TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    OBJECT_KEY_FIELD_NUMBER: _ClassVar[int]
    FOLDER_PATH_FIELD_NUMBER: _ClassVar[int]
    ASSET_SN_FIELD_NUMBER: _ClassVar[int]
    DEVICE_SN_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_NAME_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_NAME_FIELD_NUMBER: _ClassVar[int]
    SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    SKILL_NAME_FIELD_NUMBER: _ClassVar[int]
    CAPTURED_AT_FIELD_NUMBER: _ClassVar[int]
    UPLOADED_AT_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    VENDOR_FLIGHT_ID_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_URL_FIELD_NUMBER: _ClassVar[int]
    id: str
    media_type: MediaType
    status: MediaFileStatus
    file_name: str
    content_type: str
    size_bytes: int
    bucket: str
    object_key: str
    folder_path: str
    asset_sn: str
    device_sn: str
    organization_id: str
    organization_name: str
    execution_id: str
    application_id: str
    application_name: str
    skill_id: str
    skill_name: str
    captured_at: _timestamp_pb2.Timestamp
    uploaded_at: _timestamp_pb2.Timestamp
    position: MediaCapturePosition
    vendor_flight_id: str
    metadata: _containers.ScalarMap[str, str]
    download_url: str
    def __init__(self, id: _Optional[str] = ..., media_type: _Optional[_Union[MediaType, str]] = ..., status: _Optional[_Union[MediaFileStatus, str]] = ..., file_name: _Optional[str] = ..., content_type: _Optional[str] = ..., size_bytes: _Optional[int] = ..., bucket: _Optional[str] = ..., object_key: _Optional[str] = ..., folder_path: _Optional[str] = ..., asset_sn: _Optional[str] = ..., device_sn: _Optional[str] = ..., organization_id: _Optional[str] = ..., organization_name: _Optional[str] = ..., execution_id: _Optional[str] = ..., application_id: _Optional[str] = ..., application_name: _Optional[str] = ..., skill_id: _Optional[str] = ..., skill_name: _Optional[str] = ..., captured_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., uploaded_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., position: _Optional[_Union[MediaCapturePosition, _Mapping]] = ..., vendor_flight_id: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., download_url: _Optional[str] = ...) -> None: ...

class RegisterMediaFileRequest(_message.Message):
    __slots__ = ("base", "asset_sn", "device_sn", "source_bucket", "source_object_key", "file_name", "execution_id", "vendor_flight_id", "captured_at", "position", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    ASSET_SN_FIELD_NUMBER: _ClassVar[int]
    DEVICE_SN_FIELD_NUMBER: _ClassVar[int]
    SOURCE_BUCKET_FIELD_NUMBER: _ClassVar[int]
    SOURCE_OBJECT_KEY_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    VENDOR_FLIGHT_ID_FIELD_NUMBER: _ClassVar[int]
    CAPTURED_AT_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    asset_sn: str
    device_sn: str
    source_bucket: str
    source_object_key: str
    file_name: str
    execution_id: str
    vendor_flight_id: str
    captured_at: _timestamp_pb2.Timestamp
    position: MediaCapturePosition
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., asset_sn: _Optional[str] = ..., device_sn: _Optional[str] = ..., source_bucket: _Optional[str] = ..., source_object_key: _Optional[str] = ..., file_name: _Optional[str] = ..., execution_id: _Optional[str] = ..., vendor_flight_id: _Optional[str] = ..., captured_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., position: _Optional[_Union[MediaCapturePosition, _Mapping]] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ListMediaFilesRequest(_message.Message):
    __slots__ = ("organization_id", "folder_path", "execution_id", "asset_sn", "limit", "page_token")
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    FOLDER_PATH_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    ASSET_SN_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    organization_id: str
    folder_path: str
    execution_id: str
    asset_sn: str
    limit: int
    page_token: str
    def __init__(self, organization_id: _Optional[str] = ..., folder_path: _Optional[str] = ..., execution_id: _Optional[str] = ..., asset_sn: _Optional[str] = ..., limit: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListMediaFilesResponse(_message.Message):
    __slots__ = ("files", "folders", "next_page_token")
    FILES_FIELD_NUMBER: _ClassVar[int]
    FOLDERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    files: _containers.RepeatedCompositeFieldContainer[MediaFileProtoDTO]
    folders: _containers.RepeatedScalarFieldContainer[str]
    next_page_token: str
    def __init__(self, files: _Optional[_Iterable[_Union[MediaFileProtoDTO, _Mapping]]] = ..., folders: _Optional[_Iterable[str]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetMediaFileRequest(_message.Message):
    __slots__ = ("id", "organization_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    organization_id: str
    def __init__(self, id: _Optional[str] = ..., organization_id: _Optional[str] = ...) -> None: ...
