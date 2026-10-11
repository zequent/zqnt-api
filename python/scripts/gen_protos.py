#!/usr/bin/env python3
"""
Generate the Python protobuf / gRPC modules of zqnt_api from proto/.

proto/ is a copy of the public contracts of zqnt-protos at the commit in proto/ZQNT_PROTOS_COMMIT
(the contract repository is private, so this public repository carries the files themselves). It
has two proto roots:
  v2  frozen 2.x contracts -> zqnt_api/generated/zqnt/*_pb2.py
  v3  zqnt.<domain>.v3     -> zqnt_api/generated/zqnt/<domain>/v3/*_pb2.py

The output is committed; CI regenerates it and fails on a difference. Run with
PYTHONDONTWRITEBYTECODE=1 and the grpcio-tools version from uv.lock:

    PYTHONDONTWRITEBYTECODE=1 uv run python scripts/gen_protos.py
"""

import re
import shutil
import sys
from pathlib import Path

try:
    from grpc_tools import protoc
except ImportError:
    sys.exit("grpcio-tools is required: uv sync")

ROOT = Path(__file__).resolve().parent.parent
PROTO = ROOT / "proto"
GENERATED = ROOT / "zqnt_api" / "generated"
V2_OUT = GENERATED / "zqnt"
PACKAGE_PREFIX = "zqnt_api.generated."

WELL_KNOWN_PROTOS = Path(protoc.__file__).parent / "_proto"


def _protoc(proto_root: Path, out: Path, files: list[Path]) -> None:
    args = [
        "grpc_tools.protoc",
        f"--proto_path={proto_root}",
        f"--proto_path={WELL_KNOWN_PROTOS}",
        f"--python_out={out}",
        f"--pyi_out={out}",
        f"--grpc_python_out={out}",
        f"--mypy_grpc_out={out}",
        *[str(p) for p in files],
    ]
    rc = protoc.main(args)
    if rc != 0:
        sys.exit(f"protoc failed with exit code {rc}")


def ensure_init_files(directory: Path, stop: Path) -> None:
    for dirpath in [directory, *directory.parents]:
        init = dirpath / "__init__.py"
        if not init.exists():
            init.write_text("")
        if dirpath == stop:
            break


def generate_v2(v2_dir: Path) -> None:
    files = sorted(v2_dir.glob("*.proto"))
    print(f"v2: {len(files)} proto file(s) -> {V2_OUT.relative_to(ROOT)}")
    V2_OUT.mkdir(parents=True, exist_ok=True)
    ensure_init_files(V2_OUT, GENERATED)
    _protoc(v2_dir, V2_OUT, files)
    _fix_v2_imports(V2_OUT)


def generate_v3(v3_dir: Path) -> None:
    files = sorted(v3_dir.rglob("*.proto"))
    print(
        f"v3: {len(files)} proto file(s) -> {GENERATED.relative_to(ROOT)}/zqnt/<domain>/v3"
    )
    _protoc(v3_dir, GENERATED, files)
    for proto in files:
        ensure_init_files(GENERATED / proto.relative_to(v3_dir).parent, GENERATED)
    _fix_v3_imports(GENERATED)


def _fix_v2_imports(directory: Path) -> None:
    """
    grpc_tools emits absolute imports (`import common_pb2 as common__pb2`, and
    `from base_pb2 import *` for `import public`) that only work with the output directory on
    sys.path; they become relative imports inside zqnt_api.generated.zqnt.
    """
    bare_import = re.compile(r"^import (\w+_pb2) as (\w+)$", re.MULTILINE)
    public_import = re.compile(r"^from (\w+_pb2) import \*$", re.MULTILINE)

    for py_file in [*directory.glob("*.py"), *directory.glob("*.pyi")]:
        src = py_file.read_text()
        patched = bare_import.sub(r"from . import \1 as \2", src)
        patched = public_import.sub(r"from .\1 import *", patched)
        if patched != src:
            py_file.write_text(patched)


def _fix_v3_imports(directory: Path) -> None:
    """
    v3 modules import each other by package path (`from zqnt.capability.v3 import ...`); those
    get the zqnt_api.generated. prefix. In .py files only the import lines and the module name
    handed to the descriptor builder change -- the serialized descriptor must stay byte-exact.
    The .pyi stubs carry no descriptor, so their type references are rewritten throughout.
    """
    v3_module = r"zqnt\.[a-z_]+\.v3"
    py_import = re.compile(rf"^(from|import) ({v3_module})", re.MULTILINE)
    builder = re.compile(
        rf"(BuildTopDescriptorsAndMessages\(DESCRIPTOR, ')({v3_module})"
    )
    pyi_ref = re.compile(rf"(?<![\w.])({v3_module})")

    for py_file in (directory / "zqnt").rglob("*"):
        if py_file.suffix not in (".py", ".pyi") or "/v3/" not in py_file.as_posix():
            continue
        src = py_file.read_text()
        if py_file.suffix == ".py":
            patched = py_import.sub(rf"\1 {PACKAGE_PREFIX}\2", src)
            patched = builder.sub(rf"\1{PACKAGE_PREFIX}\2", patched)
        else:
            patched = pyi_ref.sub(rf"{PACKAGE_PREFIX}\1", src)
        if patched != src:
            py_file.write_text(patched)


if __name__ == "__main__":
    print(
        f"Generating from zqnt-protos {(PROTO / 'ZQNT_PROTOS_COMMIT').read_text().strip()}..."
    )
    shutil.rmtree(GENERATED, ignore_errors=True)
    generate_v2(PROTO / "v2")
    generate_v3(PROTO / "v3")
    print("Done.")
