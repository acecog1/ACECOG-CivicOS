"""Offline BG-2 versioned staging and rollback rehearsal, NEVER GitHub Pages.

Version directories and an atomically swapped local current.json represent a
*mock host's* release selector. This cannot certify rollback of an actual host.
Refuses destination roots that look like existing BG-1 public site roots.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import tempfile
from zipfile import ZipFile
from scripts import package_bg2_candidate as pack

VERSION=re.compile(r"^bg2-v[0-9]+\.[0-9]+(?:\.[0-9]+)?$")

def ensure_root(root:Path)->Path:
    root=Path(root)
    if root.is_symlink() or (root.exists() and not root.is_dir()):
        raise RuntimeError("Unsafe BG-2 stage root")
    if (root/"index.html").exists() or (root/".git").exists():
        raise RuntimeError("Refusing to use an existing static site/Git checkout")
    return root

def _check_version(v:str):
    if not VERSION.fullmatch(v):
        raise RuntimeError("Unsafe BG-2 version identifier")

def _atomic_json(target:Path,data:dict)->None:
    with tempfile.NamedTemporaryFile(mode="w",encoding="utf-8",
        prefix=".bg2-pointer-",suffix=".json",dir=target.parent,delete=False) as f:
        filename=Path(f.name)
        json.dump(data,f,indent=2,sort_keys=True)
        f.write("\n")
    try:os.replace(filename,target)
    finally:filename.unlink(missing_ok=True)

def stage(root:Path,version:str,zip_path:Path,source_sha:str)->dict:
    """Unpack immutable source-verified ZIP and commit only complete versions."""
    _check_version(version)
    root=ensure_root(root)
    receipt=pack.verify_review_zip(zip_path,source_sha)
    root.mkdir(parents=True,exist_ok=True)
    dest=root/"versions"/version
    if dest.exists():
        raise RuntimeError("Version already staged, refusing overwrite")
    (root/"versions").mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".bg2-stage-",dir=root/"versions") as tmp:
        local=Path(tmp)/"content"
        local.mkdir()
        with ZipFile(zip_path) as z:
            for name in z.namelist():
                # Paths are already vetted by verify_review_zip above.
                target=local/name
                target.parent.mkdir(parents=True,exist_ok=True)
                target.write_bytes(z.read(name))
        hashes={k:hashlib.sha256(v).hexdigest()
                for k,v in pack._listed_files(local).items()}
        if hashes != {**receipt["file_sha256"],
                      "release-manifest.json":hashlib.sha256(
                          (local/"release-manifest.json").read_bytes()).hexdigest()}:
            raise RuntimeError("Versioned staging differs from verified ZIP")
        sha=hashlib.sha256(zip_path.read_bytes()).hexdigest()
        data={"version":version,"source_sha":source_sha,
              "archive_sha256":sha,"file_hashes_sha256":pack.sha256(pack.canonical(hashes)),
              "state":"STAGED_ONLY_NO_PUBLIC_DEPLOYMENT"}
        (local/"bg2-stage-receipt.json").write_text(json.dumps(data,sort_keys=True)+"\n")
        os.replace(local,dest)
    return data

def select(root:Path,version:str)->dict:
    """Atomically switch LOCAL pointer after verifying staged integrity."""
    _check_version(version)
    root=ensure_root(root)
    folder=root/"versions"/version
    receipt=json.loads((folder/"bg2-stage-receipt.json").read_text())
    if receipt.get("version")!=version:
        raise RuntimeError("Wrong staged version receipt")
    files=pack._listed_files(folder)
    stage_receipt=files.pop("bg2-stage-receipt.json")
    observed={k:hashlib.sha256(v).hexdigest() for k,v in files.items()}
    if pack.sha256(pack.canonical(observed))!=receipt["file_hashes_sha256"]:
        raise RuntimeError("Staged content modified; refuse activation or rollback")
    previous=None
    if (root/"current.json").exists():
        previous=json.loads((root/"current.json").read_text())
        if previous["version"]!=version:
            _atomic_json(root/"previous.json",previous)
    current={"version":version,
             "source_sha":receipt["source_sha"],
             "archive_sha256":receipt["archive_sha256"],
             "state":"OFFLINE_ROLLBACK_REHEARSAL_ONLY"}
    _atomic_json(root/"current.json",current)
    return current

def rollback(root:Path)->dict:
    root=ensure_root(root)
    if not (root/"previous.json").exists():
        raise RuntimeError("No independently staged previous version available")
    prev=json.loads((root/"previous.json").read_text())
    return select(root,prev["version"])

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("action",choices=["stage","select","rollback"])
    parser.add_argument("--root",type=Path,required=True)
    parser.add_argument("--version")
    parser.add_argument("--zip",type=Path)
    parser.add_argument("--source-sha")
    a=parser.parse_args()
    if a.action=="stage":
        if not a.zip or not a.version or not a.source_sha:
            parser.error("stage requires --zip --version --source-sha")
        result=stage(a.root,a.version,a.zip,a.source_sha)
    elif a.action=="select":
        if not a.version:parser.error("select requires --version")
        result=select(a.root,a.version)
    else:result=rollback(a.root)
    print(json.dumps(result,sort_keys=True))

if __name__=="__main__":
    main()
