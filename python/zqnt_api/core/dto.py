"""
Core DTOs – mirrors com.zqnt.utils.core.EdgeEndpointDTO.
"""

import json
from dataclasses import dataclass


@dataclass
class EdgeEndpointDTO:
    """
    Mirrors the Java ``EdgeEndpointDTO``.

    Serialises to/from the same JSON format so the platform can deserialise it::

        {
          "endpoint":   "grpc://adapter.internal:50051",
          "online":     true,
          "assetType":  "DOCK",
          "assetVendor": "DJI"
        }
    """

    endpoint: str
    online: bool
    asset_type: str  # enum name, e.g. "DOCK"
    asset_vendor: str  # enum name, e.g. "DJI"

    def to_json(self) -> str:
        return json.dumps(
            {
                "endpoint": self.endpoint,
                "online": self.online,
                "assetType": self.asset_type,
                "assetVendor": self.asset_vendor,
            }
        )

    @classmethod
    def from_json(cls, data: str) -> "EdgeEndpointDTO":
        d = json.loads(data)
        return cls(
            endpoint=d["endpoint"],
            online=d["online"],
            asset_type=d["assetType"],
            asset_vendor=d["assetVendor"],
        )
