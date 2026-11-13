"""Transactional BG-2 review packaging with mocked, tiny runtime (no network)."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

import pytest
import os
import subprocess
import sys

from scripts import build_browser_lab as builder
from scripts import package_bg2_candidate as pack
from scripts import vendor_browser_pyodide as vendor


def test_direct_packager_cli_imports_without_pythonpath(tmp_path):
    environment = {key: value for key, value in os.environ.items() if key != "PYTHONPATH"}
    result = subprocess.run([sys.executable, str(pack.ROOT/"scripts/package_bg2_candidate.py"),
                             "--help"], cwd=tmp_path, env=environment,
                            capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    assert "--source-sha" in result.stdout


def _fixture_vendor(tmp_path, monkeypatch):
    folder = tmp_path/"fake-pyodide"
    folder.mkdir()
    payloads = {name:("mock:"+name).encode() for name in vendor.ROOT_ASSETS}
    payloads["numpy-test.whl"] = b"mock scientific wheel"
    for name,data in payloads.items():
        (folder/name).write_bytes(data)
    observed = {name:hashlib.sha256(data).hexdigest()
                for name,data in payloads.items()}
    monkeypatch.setattr(vendor, "PINNED_LOCK_SHA256",
                        observed["pyodide-lock.json"])
    manifest = {
        "distribution":"Pyodide", "version":vendor.VERSION,
        "root_lock_sha256":observed["pyodide-lock.json"],
        "core_root_status":"UNPINNED_OBSERVED_ONLY_BLOCK_RELEASE",
        "files_sha256":observed,
        "bytes":sum(len(x) for x in payloads.values()),
    }
    (folder/"acecog-runtime-manifest.json").write_text(
        json.dumps(manifest,sort_keys=True),encoding="utf-8")
    return folder


def test_exact_head_manifest_and_full_artifact_hashes_are_reproducible(tmp_path,monkeypatch):
    vendor_folder = _fixture_vendor(tmp_path,monkeypatch)
    sha=builder.checked_out_source_revision()
    assert len(sha)==40
    target=tmp_path/"review.zip"
    first=pack.build_candidate(target,sha,vendor_folder)
    assert first["source_revision"]==sha
    assert first["runtime_pin_status"]=="UNPINNED_OBSERVED_ONLY_BLOCK_RELEASE"
    assert first["files"]>10
    assert first["archive_sha256"]==hashlib.sha256(target.read_bytes()).hexdigest()
    result=pack.verify_review_zip(target,sha)
    assert result["releasable"] is False
    assert result["independent_qa_go"] is False
    assert result["source_tree_sha"]==pack.git_tree()
    with ZipFile(target) as z:
        src=json.loads(z.read("source-manifest.json"))
        assert src["source_revision"]==sha
        assert result["source_manifest_sha256"]==hashlib.sha256(
            z.read("source-manifest.json")).hexdigest()
        assert result["runtime_manifest_sha256"]==hashlib.sha256(
            z.read("vendor/pyodide/acecog-runtime-manifest.json")).hexdigest()
    other=tmp_path/"second.zip"
    assert pack.build_candidate(other,sha,vendor_folder)["archive_sha256"]==first["archive_sha256"]
    assert target.read_bytes()==other.read_bytes(), "Rebuild must be byte-identical"


def test_reject_incorrect_checkout_source_head(tmp_path,monkeypatch):
    vendor_folder=_fixture_vendor(tmp_path,monkeypatch)
    with pytest.raises(RuntimeError,match="source SHA"):
        pack.build_candidate(tmp_path/"wrong.zip","0"*40,vendor_folder)
    assert not (tmp_path/"wrong.zip").exists()


def test_interrupted_rebuild_preserves_prior_complete_zip(tmp_path,monkeypatch):
    vendor_folder=_fixture_vendor(tmp_path,monkeypatch)
    sha=builder.checked_out_source_revision()
    output=tmp_path/"review.zip"
    pack.build_candidate(output,sha,vendor_folder)
    original=output.read_bytes()
    def interrupted(_directory):
        raise RuntimeError("injected crash before promotion")
    monkeypatch.setattr(pack,"_listed_files",interrupted)
    with pytest.raises(RuntimeError,match="injected crash"):
        pack.build_candidate(output,sha,vendor_folder)
    assert output.read_bytes()==original
    assert not list(tmp_path.glob(".bg2-package-stage-*"))


def test_archive_tamper_or_unexpected_asset_fails_independent_verification(tmp_path,monkeypatch):
    vendor_folder=_fixture_vendor(tmp_path,monkeypatch)
    sha=builder.checked_out_source_revision()
    good=tmp_path/"good.zip"
    pack.build_candidate(good,sha,vendor_folder)
    bad=tmp_path/"tampered.zip"
    with ZipFile(good) as src, ZipFile(bad,"w",compression=ZIP_DEFLATED) as dest:
        for name in src.namelist():
            payload=src.read(name)
            if name=="python/src/acecog/engine.py":
                payload += b"\n# malicious change\n"
            dest.writestr(name,payload)
    with pytest.raises(RuntimeError,match="manifest digest"):
        pack.verify_review_zip(bad,sha)
    with pytest.raises(RuntimeError,match="release SHA"):
        pack.verify_review_zip(good,"0"*40)


def test_extra_vendor_file_never_overwrites_old_review_zip(tmp_path,monkeypatch):
    vendor_folder=_fixture_vendor(tmp_path,monkeypatch)
    sha=builder.checked_out_source_revision()
    output=tmp_path/"review.zip"
    pack.build_candidate(output,sha,vendor_folder)
    previous=output.read_bytes()
    (vendor_folder/"unreviewed-old-file.txt").write_text("stale")
    with pytest.raises(RuntimeError,match="contaminated"):
        pack.build_candidate(output,sha,vendor_folder)
    assert output.read_bytes()==previous


def test_failed_vendor_stage_preserves_existing_target(tmp_path,monkeypatch):
    target=tmp_path/"vendor"
    target.mkdir()
    (target/"old").write_bytes(b"prior reviewed directory")
    before=(target/"old").read_bytes()
    def interrupted(stage,expected):
        (stage/"partial.wasm").write_bytes(b"unverified")
        raise RuntimeError("interrupted remote download")
    monkeypatch.setattr(vendor,"_build_clean",interrupted)
    with pytest.raises(RuntimeError,match="interrupted"):
        vendor.vendor(target)
    assert (target/"old").read_bytes()==before
    assert not (target/"partial.wasm").exists()
    assert not list(tmp_path.glob(".bg2-vendor-stage-*"))


def test_failed_vendor_promotion_restores_original(tmp_path,monkeypatch):
    target=tmp_path/"vendor"
    target.mkdir()
    (target/"old").write_bytes(b"prior complete vendor output")
    def mock_built(stage,expected):
        (stage/"new").write_bytes(b"new candidate")
        return {"state":"candidate"}
    monkeypatch.setattr(vendor,"_build_clean",mock_built)
    real_replace=vendor.os.replace
    def fail_new_once(src,dst):
        if Path(src).name=="new" and Path(dst)==target:
            raise OSError("forced atomic promotion error")
        return real_replace(src,dst)
    monkeypatch.setattr(vendor.os,"replace",fail_new_once)
    with pytest.raises(OSError,match="forced"):
        vendor.vendor(target)
    assert (target/"old").read_bytes()==b"prior complete vendor output"
    assert not (target/"new").exists()
    assert not list(tmp_path.glob(".bg2-vendor-stage-*"))


def test_source_checkout_drift_rejected_before_zip_promotion(tmp_path,monkeypatch):
    vendor_folder=_fixture_vendor(tmp_path,monkeypatch)
    sha=builder.checked_out_source_revision()
    output=tmp_path/"review.zip"
    pack.build_candidate(output,sha,vendor_folder)
    original=output.read_bytes()
    actual=pack._read_git_blob
    def injected_wrong_blob(name):
        if name=="scripts/lab_preview_assets/lab.js":
            return b"uncommitted replacement bytes"
        return actual(name)
    monkeypatch.setattr(pack,"_read_git_blob",injected_wrong_blob)
    with pytest.raises(RuntimeError,match="Source input differs from Git HEAD"):
        pack.build_candidate(output,sha,vendor_folder)
    assert output.read_bytes()==original


def test_self_consistent_forged_manifest_fails_exact_git_rebuild(tmp_path,monkeypatch):
    # Even if an adversary adjusts *every* included hash to match an altered
    # JavaScript asset, release verification must compare against the exact
    # reviewed Git tree rather than accepting mutually consistent claims.
    vendor_folder=_fixture_vendor(tmp_path,monkeypatch)
    sha=builder.checked_out_source_revision()
    good=tmp_path/"good.zip"
    pack.build_candidate(good,sha,vendor_folder)
    with ZipFile(good) as z:
        files={name:z.read(name) for name in z.namelist()}
    files["lab.js"]+=b"\n// forged browser code\n"
    source_manifest=json.loads(files["source-manifest.json"])
    source_manifest["files"]["lab.js"]=pack.sha256(files["lab.js"])
    files["source-manifest.json"]=(
        json.dumps(source_manifest,indent=2,sort_keys=True)+"\n").encode()
    release=json.loads(files["release-manifest.json"])
    content={k:v for k,v in files.items() if k!="release-manifest.json"}
    hashes={k:pack.sha256(v) for k,v in content.items()}
    release["file_sha256"]=hashes
    release["source_manifest_sha256"]=hashes["source-manifest.json"]
    release["artifact_tree_sha256"]=pack.sha256(pack.canonical(hashes))
    files["release-manifest.json"]=pack.canonical(release)+b"\n"
    forged=tmp_path/"forged.zip"
    with ZipFile(forged,"w",compression=ZIP_DEFLATED) as z:
        for name,data in sorted(files.items()):
            z.writestr(name,data)
    with pytest.raises(RuntimeError,match="differs from reproducible Git source"):
        pack.verify_review_zip(forged,sha)
    assert pack.verify_review_zip(good,sha)["source_revision"]==sha
