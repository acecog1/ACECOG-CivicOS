"""R3 offline-only version selector, lossless prior-version rollback rehearsal."""
from __future__ import annotations
import hashlib
from pathlib import Path
from zipfile import ZipFile
import pytest
from scripts import bg2_stage as stage
from scripts import package_bg2_candidate as pack

SHA="a"*40

def _zip(path:Path, bytes_:bytes):
    with ZipFile(path,"w") as z:
        z.writestr("index.html",bytes_)
        z.writestr("release-manifest.json",b"review receipt")
    return {
        "file_sha256":{"index.html":hashlib.sha256(bytes_).hexdigest()},
    }

def test_atomic_versioned_rehearsal_rollback_and_tamper_detection(tmp_path,monkeypatch):
    one=tmp_path/"one.zip"
    two=tmp_path/"two.zip"
    versions={str(one):_zip(one,b"v1 fictional preview"),
              str(two):_zip(two,b"v2 fictional preview")}
    monkeypatch.setattr(pack,"verify_review_zip",
                        lambda archive,expected:versions[str(archive)])
    root=tmp_path/"bg2-offline"
    stage.stage(root,"bg2-v0.1",one,SHA)
    stage.select(root,"bg2-v0.1")
    stage.stage(root,"bg2-v0.2",two,SHA)
    stage.select(root,"bg2-v0.2")
    assert (root/"current.json").read_text().find("bg2-v0.2")>=0
    stage.rollback(root)
    assert (root/"current.json").read_text().find("bg2-v0.1")>=0
    assert (root/"versions/bg2-v0.1/index.html").read_bytes()==b"v1 fictional preview"
    assert (root/"versions/bg2-v0.2/index.html").read_bytes()==b"v2 fictional preview"
    (root/"versions/bg2-v0.2/index.html").write_bytes(b"tampered")
    with pytest.raises(RuntimeError,match="modified"):
        stage.select(root,"bg2-v0.2")
    assert (root/"current.json").read_text().find("bg2-v0.1")>=0

def test_refuse_unsafe_versions_and_bg1_existing_site_root(tmp_path,monkeypatch):
    root=tmp_path/"bg1-root"
    root.mkdir()
    (root/"index.html").write_text("BG1 original must not be modified")
    with pytest.raises(RuntimeError,match="existing static site"):
        stage.select(root,"bg2-v0.1")
    with pytest.raises(RuntimeError,match="Unsafe BG-2 version"):
        stage.select(tmp_path/"bg2","../BG1")
    assert (root/"index.html").read_text()=="BG1 original must not be modified"
