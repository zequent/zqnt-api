"""
Helpers for converting protobuf enum integers to the string values expected
by the wire format after the AssetProtoDTO / TaskProtoDTO fields were changed
from enum to string.

Consumers that still reference enum constants (e.g. ``common_pb2.ASSET_TYPE_CAMERA``)
can migrate incrementally by wrapping the value in the appropriate function here
instead of rewriting all assignments at once.

Usage::

    from zqnt_api.proto_utils import asset_type, vendor, connection, task_type

    dto = common_pb2.AssetProtoDTO(
        type=asset_type(common_pb2.ASSET_TYPE_CAMERA),   # "ASSET_TYPE_CAMERA"
        vendor=vendor(common_pb2.AssetVendor.DJI),       # "DJI"
        connection=connection(common_pb2.AssetConnection.MQTT),  # "MQTT"
    )

All functions also accept a plain string and return it unchanged, so they are
safe to call on either form during a mixed rollout::

    asset_type("ASSET_TYPE_CAMERA")  # → "ASSET_TYPE_CAMERA"  (pass-through)
    asset_type(4)                    # → "ASSET_TYPE_CAMERA"  (enum int)
"""

from __future__ import annotations

from enum import IntEnum

from zqnt_api.generated.zqnt import common_pb2

# Proto enum string prefixes stripped when resolving an SDK enum by name.
_PROTO_PREFIXES = ("ASSET_TYPE_", "LIVE_STREAM_TYPE_")


def parse_enum[T: IntEnum](enum_cls: type[T], value: int | str, default: T) -> T:
    """Convert a proto enum value (int or proto string) to an SDK IntEnum.

    Handles both the old integer form and the new string form used after
    AssetProtoDTO fields were changed to string (e.g. ``"ASSET_TYPE_CAMERA"``).
    Known proto prefixes are stripped before name lookup.  Falls back to
    *default* if the value cannot be resolved.
    """
    if isinstance(value, int):
        try:
            return enum_cls(value)
        except ValueError:
            return default
    s = str(value)
    try:
        return enum_cls[s]
    except KeyError:
        pass
    for prefix in _PROTO_PREFIXES:
        if s.startswith(prefix):
            try:
                return enum_cls[s[len(prefix) :]]
            except KeyError:
                break
    return default


def _enum_to_str(descriptor, value: int | str) -> str:
    """Generic helper: int enum value → proto enum name string, string pass-through."""
    if isinstance(value, str):
        return value
    try:
        return descriptor.values_by_number[value].name
    except KeyError:
        return str(value)


def asset_type(value: int | str) -> str:
    """Convert ``AssetTypeEnum`` integer or string to its canonical string form."""
    return _enum_to_str(common_pb2.AssetTypeEnum.DESCRIPTOR, value)


def vendor(value: int | str) -> str:
    """Convert ``AssetVendor`` integer or string to its canonical string form."""
    return _enum_to_str(common_pb2.AssetVendor.DESCRIPTOR, value)


def connection(value: int | str) -> str:
    """Convert ``AssetConnection`` integer or string to its canonical string form."""
    return _enum_to_str(common_pb2.AssetConnection.DESCRIPTOR, value)


def task_type(value: int | str) -> str:
    """Convert ``TaskTypeProto`` integer or string to its canonical string form."""
    return _enum_to_str(common_pb2.TaskTypeProto.DESCRIPTOR, value)


def live_stream_type(value: int | str) -> str:
    """Convert ``LiveStreamTypeEnum`` integer or string to its canonical string form."""
    return _enum_to_str(common_pb2.LiveStreamTypeEnum.DESCRIPTOR, value)
