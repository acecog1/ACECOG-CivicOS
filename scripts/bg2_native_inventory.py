"""Conservative native-binary inventory from exact wheel bytes (review evidence only).

No linkage or licensing conclusion is inferred from a filename. Use
inventory_locked for evidence bound to the source-pinned Pyodide lock.
"""
from __future__ import annotations

import hashlib
import io
import json
from pathlib import Path
import re
from zipfile import ZipFile
from scripts import vendor_browser_pyodide as runtime

NATIVE_SUFFIXES = (".so", ".wasm", ".a", ".dylib", ".dll", ".pyd")


def is_native(name: str) -> bool:
    lower = name.lower()
    return lower.endswith(NATIVE_SUFFIXES) or bool(re.search(r"\.so(?:\.[0-9]+)+$", lower))


def inventory_wheel(wheel: Path, expected_sha256: str) -> list[dict]:
    return inventory_wheel_bytes(wheel.name, wheel.read_bytes(), expected_sha256)


def inventory_wheel_bytes(filename: str, raw: bytes, expected_sha256: str) -> list[dict]:
    actual = hashlib.sha256(raw).hexdigest()
    if actual != expected_sha256:
        raise RuntimeError("Wheel SHA-256 mismatch: " + filename)
    entries = []
    seen: set[str] = set()
    with ZipFile(io.BytesIO(raw)) as archive:
        for info in sorted(archive.infolist(), key=lambda item: item.filename):
            name = info.filename
            if name.startswith("/") or ".." in Path(name).parts or "\\" in name or not name or name in seen:
                raise RuntimeError("Unsafe or duplicate wheel member: " + name)
            seen.add(name)
            if info.is_dir() or not is_native(name):
                continue
            data = archive.read(info)
            entries.append({
                "wheel": filename,
                "wheel_sha256": actual,
                "member_path": name,
                "bytes": len(data),
                "sha256": hashlib.sha256(data).hexdigest(),
                "linked_libraries": "UNVERIFIED",
                "license_applicability": "UNKNOWN_BLOCKING",
            })
    return entries


def inventory_locked(lock_bytes: bytes, wheel_bytes: dict[str, bytes]) -> dict:
    """Derive the complete requested wheel closure from the fixed root lock.

    Neither expected wheel digests nor package selection come from a caller's
    runtime manifest. The lock itself must match the source-pinned SHA-256.
    The same operation runs again on inner review ZIP bytes during verification.
    """
    lock_digest = hashlib.sha256(lock_bytes).hexdigest()
    runtime.verify_digest("pyodide-lock.json", lock_digest, runtime.PINNED_LOCK_SHA256)
    packages = json.loads(lock_bytes)["packages"]
    lookup = {runtime.normalized(key): value for key, value in packages.items()}
    selected = set()
    pending = list(runtime.PACKAGE_ROOTS)
    while pending:
        key = runtime.normalized(pending.pop())
        if key in selected:
            continue
        if key not in lookup:
            raise RuntimeError("Missing locked dependency: " + key)
        selected.add(key)
        pending.extend(lookup[key].get("depends", []))
    wheels = []
    seen = set()
    for key in sorted(selected):
        entry = lookup[key]
        name = entry["file_name"]
        if (not isinstance(name, str) or "/" in name or "\\" in name
                or ":" in name or name.startswith(".") or not name.endswith(".whl")
                or name in seen):
            raise RuntimeError("Unsafe/duplicate locked wheel filename")
        seen.add(name)
        if name not in wheel_bytes:
            raise RuntimeError("Missing locked wheel: " + name)
        native = inventory_wheel_bytes(name, wheel_bytes[name], entry["sha256"])
        wheels.append({"package": key, "version": entry["version"],
                       "wheel": name, "wheel_sha256": entry["sha256"],
                       "native_members": native})
    if set(wheel_bytes) != seen:
        raise RuntimeError("Extra wheel outside locked dependency closure")
    return {"schema": "ACECOG-BG2-LOCKED-NATIVE-INVENTORY-v1",
            "pyodide_lock_sha256": lock_digest, "wheels": wheels,
            "compiled_attribution": "UNKNOWN_BLOCKING",
            "license_acceptance": "HOLD"}


def inventory_directory(folder: Path) -> dict:
    return inventory_locked((folder / "pyodide-lock.json").read_bytes(),
                            {p.name: p.read_bytes() for p in folder.glob("*.whl")})


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vendor", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    report = inventory_directory(args.vendor)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True)+"\n",
                           encoding="utf-8", newline="\n")
    print("Locked wheels:", len(report["wheels"]), "license acceptance: HOLD")
