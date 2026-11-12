"""R1 independent-origin tarball/root-pin and full-dependency negative tests."""
from __future__ import annotations
from contextlib import contextmanager
import hashlib
import io
import json
from pathlib import Path
import tarfile
from zipfile import ZipFile

import pytest
from scripts import verify_bg2_upstream as upstream
from scripts import build_bg2_sbom as sbom
from scripts import vendor_browser_pyodide as vendor

def _fake_release(tmp_path, monkeypatch, omit=None, alter=None):
    files={name:("certification-test:"+name).encode()
           for name in vendor.CORE_ROOT_ASSETS}
    candidate={name:hashlib.sha256(data).hexdigest()
               for name,data in files.items()}
    buf=io.BytesIO()
    with tarfile.open(fileobj=buf,mode="w:bz2") as t:
        for name,data in files.items():
            if name==omit: continue
            if name==alter: data+=b"tampered after candidate pinset"
            info=tarfile.TarInfo("pyodide-core/full/"+name)
            info.size=len(data)
            t.addfile(info,io.BytesIO(data))
    archive=buf.getvalue()
    official={
      "repository":"https://github.com/pyodide/pyodide",
      "release_commit":"mock-immutable-publisher-tag",
      "published_at":"2026-09-14T05:06:54Z",
      "asset_name":"pyodide-core-314.0.7.tar.bz2",
      "asset_sha256":hashlib.sha256(archive).hexdigest(),
      "asset_url":"https://github.com/pyodide/pyodide/releases/download/314.0.7/pyodide-core-314.0.7.tar.bz2"
    }
    spec={"schema":vendor.PINSET_SCHEMA,"pyodide_version":vendor.VERSION,
          "root_lock_sha256":vendor.PINNED_LOCK_SHA256,
          "sha256":candidate,"official_release":official}
    path=tmp_path/"candidate.json"
    path.write_text(json.dumps(spec))
    packet={"tag_name":vendor.VERSION,"target_commitish":official["release_commit"],
            "published_at":official["published_at"],
            "assets":[{"name":official["asset_name"],"digest":"sha256:"+official["asset_sha256"],
                       "browser_download_url":official["asset_url"]}]}
    monkeypatch.setattr(upstream,"load_https",
                        lambda url,cap: json.dumps(packet).encode() if url==upstream.RELEASE_API else archive)
    return path,archive

def test_official_archive_hash_and_each_four_root_file_verified(tmp_path,monkeypatch):
    path,blob=_fake_release(tmp_path,monkeypatch)
    rec=upstream.verify_official(path)
    assert rec["root_files_verified"]
    assert set(rec["root_file_sha256"])==set(vendor.CORE_ROOT_ASSETS)
    assert rec["independent_QA_signoff"]=="REQUIRED"
    assert rec["observed_archive_sha256"]==hashlib.sha256(blob).hexdigest()

def test_altered_or_missing_publisher_asset_fails_closed(tmp_path,monkeypatch):
    for name in vendor.CORE_ROOT_ASSETS:
        p,a=_fake_release(tmp_path,monkeypatch,alter=name)
        with pytest.raises(RuntimeError,match="mismatch"):
            upstream.verify_official(p)
        p,a=_fake_release(tmp_path,monkeypatch,omit=name)
        with pytest.raises(RuntimeError,match="lacks"):
            upstream.verify_official(p)

def test_official_publisher_archive_metadata_is_mandatory(tmp_path,monkeypatch):
    path,_blob=_fake_release(tmp_path,monkeypatch)
    obj=json.loads(path.read_text())
    obj["official_release"]["asset_sha256"]="0"*64
    path.write_text(json.dumps(obj))
    with pytest.raises(RuntimeError,match="digest/URL mismatch"):
        upstream.verify_official(path)

def test_sbom_contains_transitive_dependencies_and_license_hold(tmp_path,monkeypatch):
    directory=tmp_path/"vendor"
    directory.mkdir()
    wheel=directory/"child-1.2.3-py3-none-any.whl"
    with ZipFile(wheel,"w") as archive:
        archive.writestr("child-1.2.3.dist-info/METADATA",
             "Metadata-Version: 2.4\nName: child\nVersion: 1.2.3\nLicense-Expression: MIT\n")
        archive.writestr("child-1.2.3.dist-info/licenses/LICENSE","MIT license text")
    digest=hashlib.sha256(wheel.read_bytes()).hexdigest()
    root=directory/"root-4.0-py3-none-any.whl"
    with ZipFile(root,"w") as archive:
        archive.writestr("root-4.0.dist-info/METADATA",
             "Metadata-Version: 2.4\nName: root\nVersion: 4.0\n")
    root_hash=hashlib.sha256(root.read_bytes()).hexdigest()
    for name in vendor.CORE_ROOT_ASSETS:
        (directory/name).write_bytes(b"stub")
    (directory/"acecog-runtime-manifest.json").write_text("{}")
    fake={"files_sha256":{"child-1.2.3-py3-none-any.whl":digest,
                          "root-4.0-py3-none-any.whl":root_hash,
                          **{n:hashlib.sha256(b"stub").hexdigest()
                             for n in vendor.CORE_ROOT_ASSETS}},
          "packages":["root","child"],"package_roots":["root"],
          "package_lock_metadata":{
              "root":{"package_file":root.name,"depends":["child"]},
              "child":{"package_file":wheel.name,"depends":[]}},
          "core_root_status":"EXACT_PINSET_VERIFIED_PENDING_INDEPENDENT_QA"}
    monkeypatch.setattr(vendor,"verify_vendor_directory",lambda _p:fake)
    b,disposition=sbom.build_inventory(directory)
    assert b["bomFormat"]=="CycloneDX"
    assert b["specVersion"]=="1.6"
    assert disposition["package_count"]==2
    assert disposition["transitive_package_count"]==1
    assert disposition["acceptance"]=="HOLD"
    assert len(disposition["undetermined_license_items"])==1
    deps={d["ref"]:d["dependsOn"] for d in b["dependencies"]}
    assert deps["pkg:pypi/root@4.0"]==["pkg:pypi/child@1.2.3"]
