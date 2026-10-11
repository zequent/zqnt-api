"""
Public Python API of the Zequent platform.

    from zqnt_api.generated.zqnt.capability.v3 import command_pb2
    from zqnt_api.generated.zqnt import common_pb2
    from zqnt_api.telemetry import to_sample, to_request
"""

from importlib.metadata import PackageNotFoundError
from importlib.metadata import version as _pkg_version

try:
    __version__ = _pkg_version("zqnt-api")
except PackageNotFoundError:
    __version__ = "0.0.0"

__all__ = ["__version__"]
