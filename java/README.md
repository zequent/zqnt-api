# zqnt-api-java

The public Java API of the Zequent platform: the protobuf/gRPC types customers build against, the
telemetry mapping between the 2.x and 3.x contracts, and the small DTO and helper classes the Java
SDKs share. The Java Edge SDK ([`zqnt-edge-sdk-java`](https://github.com/Zequent/zqnt-edge-sdk-java))
and Client SDK ([`zqnt-client-sdk-java`](https://github.com/Zequent/zqnt-client-sdk-java)) depend on
this artifact only.

```xml
<dependency>
    <groupId>com.zqnt</groupId>
    <artifactId>zqnt-api-java</artifactId>
    <version>${zqnt-api.version}</version>
</dependency>
```

## Packages

| Package | Content |
|---|---|
| `com.zqnt.protos.capability.v3` | `zqnt.capability.v3`: Capability, CommandSafety, Command, CommandResult, CommandEvent |
| `com.zqnt.protos.common.v3` | `zqnt.common.v3`: AssetRef, RequestContext, Error, paging, GeoPoint |
| `com.zqnt.protos.control.v3` | `zqnt.control.v3`: `RemoteControlService` for clients |
| `com.zqnt.protos.edge.v3` | `zqnt.edge.v3`: `EdgeAdapterService` (adapter side), `EdgeGatewayService` (platform side) |
| `com.zqnt.protos.telemetry.v3` | `zqnt.telemetry.v3`: TelemetrySample and the telemetry service |
| `com.zqnt.utils.*.proto` (`common`, `connector`, `devicecontrol`, `edge.sdk`, `events`, `execution`, `livedata`, `media`, `mission`, `remotecontrol`) | the frozen 2.x contracts (package `zqnt`), wire-compatible with 2.0.0 |
| `com.zqnt.utils.telemetry` | `TelemetrySampleMapper`: v2 `Telemetry` ⇄ v3 `TelemetrySample`, and the catalog of telemetry detail keys |
| `com.zqnt.utils.core`, `com.zqnt.utils` | protobuf/JSON helpers (`ProtobufHelpers`, `ProtoJsonUtils`, `JsonUtils`), MapStruct base configs |
| `com.zqnt.utils.{asset,edge.sdk,missionautonomy,detections}.domains` | the DTOs of the 2.x SDK APIs |

The Java packages are the ones the SDKs have always used, so moving from `zqnt-utils-java` to this
artifact changes no import. The `.proto` files are in the jar under `META-INF/proto/` and in
[`src/main/proto`](src/main/proto): `v2` and `v3` are the two proto roots.

## Where it comes from

`src/main/proto/` is a copy of the public contracts of the platform's contract repository at the
commit in [`src/main/proto/ZQNT_PROTOS_COMMIT`](src/main/proto/ZQNT_PROTOS_COMMIT); the Java code is
generated from it at build time (protoc 3.25.9, protoc-gen-grpc-java 1.76.0). It is updated by an
automated PR after every contract change; do not edit it by hand.

## Building

```bash
mvn verify
```

## Versions

Releases are `vX.Y.Z` tags. Every PR build is also published to GitHub Packages as
`<version>-PR<n>-<sha>-SNAPSHOT` for review.

The jar is not obfuscated: it is a public API whose sources and `.proto` files are published,
protobuf and gRPC resolve the generated classes by name, and users need readable stack traces.
