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
    with pytest.raises(RuntimeError, match="Unsafe or duplicate wheel member"):
        inventory_wheel(wheel, digest)


def test_versioned_native_and_non_native_traversal_rejected(tmp_path: Path):
    wheel = tmp_path / "versioned.whl"
    with ZipFile(wheel, "w") as archive:
        archive.writestr("lib/libopenblas.so.1", b"candidate")
        archive.writestr("lib/libboost.so.1.2.3", b"candidate")
        archive.writestr("pkg/readme.txt", b"plain")
    digest = hashlib.sha256(wheel.read_bytes()).hexdigest()
    paths = [item["member_path"] for item in inventory_wheel(wheel, digest)]
    assert paths == ["lib/libboost.so.1.2.3", "lib/libopenblas.so.1"]
    unsafe = tmp_path / "unsafe-text.whl"
    with ZipFile(unsafe, "w") as archive:
        archive.writestr("../escape.txt", b"not native")
    with pytest.raises(RuntimeError, match="Unsafe or duplicate"):
        inventory_wheel(unsafe, hashlib.sha256(unsafe.read_bytes()).hexdigest())


def test_rejects_duplicate_member_names(tmp_path: Path):
    from warnings import catch_warnings, simplefilter

    wheel = tmp_path / "duplicate.whl"
    with catch_warnings():
        simplefilter("ignore", UserWarning)
        with ZipFile(wheel, "w") as archive:
            archive.writestr("pkg/module.so", b"first")
            archive.writestr("pkg/module.so", b"second")
    with pytest.raises(RuntimeError, match="Unsafe or duplicate wheel member"):
        inventory_wheel(wheel, hashlib.sha256(wheel.read_bytes()).hexdigest())
