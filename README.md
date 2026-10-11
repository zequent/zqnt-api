# zqnt-api

The public API of the Zequent platform: the protobuf/gRPC contracts customers and adapters build
against, the code generated from them for Go, Java and Python, the telemetry mapping between the
2.x and 3.x contracts, and the small helpers the SDKs share. The Edge and Client SDKs depend on
this repository only.

## Layout

```
zqnt-api/
  buf.yaml           two buf modules: proto/v2 (MINIMAL lint), proto/v3 (STANDARD lint)
  proto/
    v2/              frozen 2.x contracts, package `zqnt`, wire-compatible with 2.0.0
    v3/              3.x contracts, packages `zqnt.<domain>.v3` under zqnt/<domain>/v3/
      COMMAND_CATALOG.md, command_catalog.json   the dotted command ids
  go/                Go module github.com/zequent/zqnt-api/go/v3   (gen/ is generated, committed)
  java/              Maven artifact com.zqnt:zqnt-api-java          (generated at build time)
  python/            Python package zqnt-api, module zqnt_api       (zqnt_api/generated is committed)
```

`proto/v2` and `proto/v3` are the two proto roots: `-I proto/v2` for `import "base.proto"`,
`-I proto/v3` for `import "zqnt/common/v3/common.proto"`.

## Install

### Go

```bash
go get github.com/zequent/zqnt-api/go/v3@<version>
```

Import paths are below `github.com/zequent/zqnt-api/go/v3/`, e.g.
`github.com/zequent/zqnt-api/go/v3/gen/zqnt/edge/v3` and `.../go/v3/telemetry`. See
[go/README.md](go/README.md).

### Java

```xml
<dependency>
    <groupId>com.zqnt</groupId>
    <artifactId>zqnt-api-java</artifactId>
    <version>${zqnt-api.version}</version>
</dependency>
```

The artifact is published to GitHub Packages, `https://maven.pkg.github.com/Zequent/zqnt-api`
(Maven needs a GitHub token with `read:packages` in `settings.xml`). See
[java/README.md](java/README.md).

### Python

```toml
[project]
dependencies = ["zqnt-api"]

[tool.uv.sources]
zqnt-api = { git = "https://github.com/zequent/zqnt-api", subdirectory = "python", tag = "v3.0.0" }
```

or `uv add "zqnt-api @ git+https://github.com/zequent/zqnt-api@v3.0.0#subdirectory=python"`.
See [python/README.md](python/README.md).

## Versions

One version for everything in this repository, starting at 3.0.0 to match platform 3.0. A
release is the tag `vX.Y.Z`, cut by the maintainer; the release workflow adds the Go module tag
`go/vX.Y.Z`, publishes `com.zqnt:zqnt-api-java:X.Y.Z` and attaches the Python wheel to the GitHub
Release.

Until a release exists there are previews. Every PR build

- is tagged `pr-<n>-<sha>`: Go `go get github.com/zequent/zqnt-api/go/v3@pr-<n>-<sha>` (resolves
  to a pseudo-version), Python `tag = "pr-<n>-<sha>"` (or `rev = "<commit>"`);
- publishes `com.zqnt:zqnt-api-java:3.0.0-PR<n>-<sha>-SNAPSHOT`.

`<sha>` is the commit CI built (for a PR, GitHub's merge commit), shown in the job summary. Move to
the release once it is out.

## Changing a contract

1. Change the `.proto` under `proto/v3` (`proto/v2` only to fix a bug; it is frozen).
2. Regenerate what is committed:
   ```bash
   (cd go && ./scripts/gen_protos.sh)                                   # protoc 3.21.12, protoc-gen-go v1.36.11, protoc-gen-go-grpc v1.6.1
   (cd python && PYTHONDONTWRITEBYTECODE=1 uv run python scripts/gen_protos.py)
   ```
   Java generates at build time (`mvn verify` in `java/`).
3. Open a PR. CI checks:
   - `buf build`, `buf lint`, `buf format` and that `proto/v2` stays wire- and JSON-compatible
     with 2.0.0 (`.github/buf/v2-2.0.0.binpb`); a v3 break against the target branch is reported;
   - per language: build, tests, and that the committed generated code matches the protos;
   - a secret scan (gitleaks).

Platform-internal contracts import these protos; they live elsewhere and never the other way
round: nothing here may import a proto that is not in this repository.

## License

Licensed under the [Apache License, Version 2.0](LICENSE); see [NOTICE](NOTICE).
