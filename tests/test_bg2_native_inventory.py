"""Offline, synthetic-only checks for the conservative binary inventory."""
import hashlib
from pathlib import Path
from zipfile import ZipFile

import pytest

from scripts.bg2_native_inventory import inventory_wheel


def test_exact_bytes_and_fail_closed_attribution(tmp_path: Path):
    wheel = tmp_path / "example.whl"
    with ZipFile(wheel, "w") as archive:
        archive.writestr("pkg/module.so", b"native-bytes")
        archive.writestr("pkg/readme.txt", b"not native")
    digest = hashlib.sha256(wheel.read_bytes()).hexdigest()
    result = inventory_wheel(wheel, digest)
    assert len(result) == 1
    assert result[0]["member_path"] == "pkg/module.so"
    assert result[0]["sha256"] == hashlib.sha256(b"native-bytes").hexdigest()
    assert result[0]["license_applicability"] == "UNKNOWN_BLOCKING"
    assert result[0]["linked_libraries"] == "UNVERIFIED"
    with pytest.raises(RuntimeError, match="SHA-256 mismatch"):
        inventory_wheel(wheel, "0" * 64)


def test_rejects_unsafe_native_member(tmp_path: Path):
    wheel = tmp_path / "unsafe.whl"
    with ZipFile(wheel, "w") as archive:
        archive.writestr("../escape.so", b"x")
    digest = hashlib.sha256(wheel.read_bytes()).hexdigest()
    with pytest.raises(RuntimeError, match="Unsafe wheel member"):
        inventory_wheel(wheel, digest)
