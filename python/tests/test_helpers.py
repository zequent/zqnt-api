from enum import IntEnum

from zqnt_api.core import EdgeEndpointDTO
from zqnt_api.generated.zqnt import common_pb2
from zqnt_api.proto_utils import asset_type, parse_enum


class AssetType(IntEnum):
    UNKNOWN = 0
    CAMERA = 4


def test_parse_enum_accepts_numbers_names_and_prefixed_names():
    assert parse_enum(AssetType, 4, AssetType.UNKNOWN) is AssetType.CAMERA
    assert parse_enum(AssetType, "CAMERA", AssetType.UNKNOWN) is AssetType.CAMERA
    assert (
        parse_enum(AssetType, "ASSET_TYPE_CAMERA", AssetType.UNKNOWN)
        is AssetType.CAMERA
    )
    assert parse_enum(AssetType, "NOPE", AssetType.UNKNOWN) is AssetType.UNKNOWN


def test_enum_helpers_return_the_proto_name():
    assert asset_type(common_pb2.ASSET_TYPE_CAMERA) == "ASSET_TYPE_CAMERA"
    assert asset_type("ASSET_TYPE_CAMERA") == "ASSET_TYPE_CAMERA"


def test_edge_endpoint_round_trips_through_the_platform_json():
    dto = EdgeEndpointDTO("grpc://adapter:50051", True, "DOCK", "DJI")
    assert '"assetVendor": "DJI"' in dto.to_json()
    assert EdgeEndpointDTO.from_json(dto.to_json()) == dto
