# zqnt-api: Go

The public Go API of the Zequent platform: the protobuf/gRPC types customers build against, and
the telemetry mapping between the 2.x and 3.x contracts. The Go Edge SDK
([`zqnt-edge-sdk-go`](https://github.com/Zequent/zqnt-edge-sdk-go)) and Client SDK
([`zqnt-client-sdk-go`](https://github.com/Zequent/zqnt-client-sdk-go)) depend on this module only.

```bash
go get github.com/zequent/zqnt-api/go/v3@<version>
```

## Packages

| Import path | Contract |
|---|---|
| `gen/zqnt/application_simulation/v3` | `zqnt.application_simulation.v3`: `SimulationService`, simulating an Application on a virtual fleet and reading its trace |
| `gen/zqnt/capability/v3` | `zqnt.capability.v3`: Capability, CommandSafety, Command, CommandResult, CommandEvent |
| `gen/zqnt/common/v3` | `zqnt.common.v3`: AssetRef, RequestContext, Error, paging, GeoPoint |
| `gen/zqnt/control/v3` | `zqnt.control.v3`: `RemoteControlService` for clients |
| `gen/zqnt/edge/v3` | `zqnt.edge.v3`: `EdgeAdapterService` (adapter side), `EdgeGatewayService` (platform side) |
| `gen/zqnt/stream/v3` | `zqnt.stream.v3`: `LiveStreamService`, the live video streams of an organization |
| `gen/zqnt/telemetry/v3` | `zqnt.telemetry.v3`: TelemetrySample and the telemetry service |
| `gen/common/...`, `gen/edge/sdk/proto`, `gen/livedata/proto`, `gen/remotecontrol/proto`, `gen/connector/proto`, `gen/missionautonomy/...`, `gen/execution/...`, `gen/devicecontrol/...`, `gen/events/proto`, `gen/media/proto` | the frozen 2.x contracts (package `zqnt`), wire-compatible with 2.0.0 |
| `telemetry` | v2 `Telemetry` ⇄ v3 `TelemetrySample`, and the catalog of telemetry detail keys |

All import paths are below `github.com/zequent/zqnt-api/go/v3/`. The `.proto` files are in
[`../proto`](../proto): `proto/v2` and `proto/v3` are the two proto roots (`-I proto/v3` for
`import "zqnt/common/v3/common.proto"`).

## Where it comes from

`gen/` is generated from [`../proto`](../proto) by `scripts/gen_protos.sh` with protoc 3.21.12,
protoc-gen-go v1.36.11 and protoc-gen-go-grpc v1.6.1, and committed with the `.proto` change; do
not edit it by hand. CI regenerates `gen/` on every PR and fails if it differs.

## Versions

The module lives in the `go/` subdirectory of `github.com/zequent/zqnt-api` and starts at major
version 3, matching platform 3.0, so its path is `github.com/zequent/zqnt-api/go/v3`. Releases are
tagged `go/v3.Y.Z` (next to the repository tag `v3.Y.Z`), cut by the maintainer. Until then there
are only previews: every commit resolves to a pseudo-version, and PR builds are tagged
`pr-<n>-<sha>`:

```bash
go get github.com/zequent/zqnt-api/go/v3@pr-<n>-<sha>    # or @<commit>
```

Move to the release tag once it exists.

## License

Licensed under the [Apache License, Version 2.0](LICENSE); see [NOTICE](NOTICE).
