# zqnt-api-python

The public Python API of the Zequent platform: the protobuf/gRPC modules customers build against,
the telemetry mapping between the 2.x and 3.x contracts, and the small helpers the Python SDKs
share. The Python Edge SDK ([`zqnt-edge-sdk-python`](https://github.com/Zequent/zqnt-edge-sdk-python))
and Client SDK ([`zqnt-client-sdk-python`](https://github.com/Zequent/zqnt-client-sdk-python))
depend on this package only.

```bash
uv add "zqnt-api @ git+https://github.com/Zequent/zqnt-api-python@vX.Y.Z"
```

## Modules

| Module | Content |
|---|---|
| `zqnt_api.generated.zqnt.capability.v3` | `zqnt.capability.v3`: Capability, CommandSafety, Command, CommandResult, CommandEvent |
| `zqnt_api.generated.zqnt.common.v3` | `zqnt.common.v3`: AssetRef, RequestContext, Error, paging, GeoPoint |
| `zqnt_api.generated.zqnt.control.v3` | `zqnt.control.v3`: `RemoteControlService` for clients |
| `zqnt_api.generated.zqnt.edge.v3` | `zqnt.edge.v3`: `EdgeAdapterService` (adapter side), `EdgeGatewayService` (platform side) |
| `zqnt_api.generated.zqnt.telemetry.v3` | `zqnt.telemetry.v3`: TelemetrySample and the telemetry service |
| `zqnt_api.generated.zqnt.<file>_pb2` | the frozen 2.x contracts (package `zqnt`), wire-compatible with 2.0.0 |
| `zqnt_api.telemetry` | v2 `Telemetry` ⇄ v3 `TelemetrySample`, and the catalog of telemetry detail keys |
| `zqnt_api.proto_utils`, `zqnt_api.core` | proto enum helpers, `EdgeEndpointDTO` |

## Where it comes from

`proto/` is a copy of the public contracts of the platform's contract repository at the commit in
[`proto/ZQNT_PROTOS_COMMIT`](proto/ZQNT_PROTOS_COMMIT); `zqnt_api/generated/` is generated from it by
`scripts/gen_protos.py` with the grpcio-tools and mypy-protobuf versions in `uv.lock`. Both are
updated by an automated PR after every contract change; do not edit them by hand. CI regenerates
the code on every PR and fails if it differs.

## Development

```bash
uv sync && uv run pytest -q && uv run ruff check .
PYTHONDONTWRITEBYTECODE=1 uv run python scripts/gen_protos.py
```
