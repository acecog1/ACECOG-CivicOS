"""Conservative native-binary inventory from exact wheel bytes (review evidence only).

No linkage or licensing conclusion is inferred from a filename. The caller must
verify the wheel digest against the approved Pyodide lock before using this.
"""
from __future__ import annotations

import hashlib
from pathlib import Path
from zipfile import ZipFile

NATIVE_SUFFIXES = (".so", ".wasm", ".a", ".dylib", ".dll", ".pyd")


def inventory_wheel(wheel: Path, expected_sha256: str) -> list[dict]:
    actual = hashlib.sha256(wheel.read_bytes()).hexdigest()
    if actual != expected_sha256:
        raise RuntimeError("Wheel SHA-256 mismatch: " + wheel.name)
    entries = []
    with ZipFile(wheel) as archive:
        for info in sorted(archive.infolist(), key=lambda item: item.filename):
            name = info.filename
            if info.is_dir() or not name.lower().endswith(NATIVE_SUFFIXES):
                continue
            if name.startswith("/") or ".." in Path(name).parts or "\\" in name:
                raise RuntimeError("Unsafe wheel member: " + name)
            data = archive.read(info)
            entries.append({
                "wheel": wheel.name,
                "wheel_sha256": actual,
                "member_path": name,
                "bytes": len(data),
                "sha256": hashlib.sha256(data).hexdigest(),
                "linked_libraries": "UNVERIFIED",
                "license_applicability": "UNKNOWN_BLOCKING",
            })
    return entries
