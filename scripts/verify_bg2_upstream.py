"""Verify BG-2 Pyodide root pins against independently published official release bytes.

Source of authority: official pyodide/pyodide GitHub Releases API includes the
SHA-256 of the core archive. This program downloads that exact archive,
checks its publisher-supplied SHA, then independently hashes its four contents.
It never generates new expected pins from the candidate's own build output.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib
import io
import json
from pathlib import Path
import tarfile
from urllib.parse import urlsplit
from urllib.request import Request, urlopen
from scripts import vendor_browser_pyodide as vendor

RELEASE_API="https://api.github.com/repos/pyodide/pyodide/releases/tags/314.0.7"
MAX_ARCHIVE=16*1024*1024
MAX_INNER=80*1024*1024

def load_https(url: str, limit: int) -> bytes:
    if urlsplit(url).scheme!="https":
        raise RuntimeError("Only HTTPS upstream release URLs are permitted")
    req=Request(url,headers={"User-Agent":"ACECOG-BG2-official-source-attestation"})
    with urlopen(req,timeout=100) as response:
        final=urlsplit(response.geturl())
        # The release API, GitHub assets and GitHub's signed asset-CDN redirect
        # are allowed, not arbitrary mirrors.
        if final.scheme!="https" or final.hostname not in {
            "api.github.com","github.com","release-assets.githubusercontent.com",
            "objects.githubusercontent.com"}:
            raise RuntimeError("Unexpected release redirect/host")
        result=response.read(limit+1)
    if len(result)>limit:
        raise RuntimeError("Official asset exceeds bounded expected size")
    return result

def verify_official(pinset: Path, archive: Path | None = None) -> dict:
    spec=json.loads(pinset.read_text(encoding="utf-8"))
    candidate=vendor.load_root_pinset(pinset)
    official=spec["official_release"]
    release=json.loads(load_https(RELEASE_API,2*1024*1024))
    if (release.get("tag_name")!=vendor.VERSION or
            release.get("target_commitish")!=official["release_commit"] or
            release.get("published_at")!=official["published_at"]):
        raise RuntimeError("Official Pyodide release identity changed")
    assets=[a for a in release.get("assets",[]) if a.get("name")==official["asset_name"]]
    if len(assets)!=1:
        raise RuntimeError("Official core archive missing or ambiguous")
    asset=assets[0]
    checksum="sha256:"+official["asset_sha256"]
    if asset.get("digest")!=checksum or asset.get("browser_download_url")!=official["asset_url"]:
        raise RuntimeError("Official publisher archive digest/URL mismatch")
    raw=archive.read_bytes() if archive else load_https(official["asset_url"],MAX_ARCHIVE)
    if len(raw)>MAX_ARCHIVE or hashlib.sha256(raw).hexdigest()!=official["asset_sha256"]:
        raise RuntimeError("Official core archive checksum mismatch")
    contents={}
    with tarfile.open(fileobj=io.BytesIO(raw),mode="r:bz2") as t:
        for m in t.getmembers():
            if not m.isfile():
                continue
            name=Path(m.name).name
            if name not in vendor.CORE_ROOT_ASSETS:
                continue
            if name in contents:
                raise RuntimeError("Ambiguous upstream core root file")
            if m.size>MAX_INNER:
                raise RuntimeError("Oversize upstream core file")
            content=t.extractfile(m)
            if content is None:
                raise RuntimeError("Unable to extract upstream core root")
            data=content.read(MAX_INNER+1)
            if len(data)!=m.size:
                raise RuntimeError("Truncated upstream file")
            contents[name]=hashlib.sha256(data).hexdigest()
    if set(contents)!=set(vendor.CORE_ROOT_ASSETS):
        raise RuntimeError("Official archive lacks one or more core root assets")
    for name, digest in contents.items():
        vendor.verify_digest(name,digest,candidate[name])
    return {
        "schema":"ACECOG-BG2-OFFICIAL-CORE-VERIFY-v1",
        "retrieved_utc":datetime.now(timezone.utc).isoformat(),
        "publisher_release_api":RELEASE_API,
        "publisher_tag":vendor.VERSION,
        "publisher_release_commit":official["release_commit"],
        "core_archive_url":official["asset_url"],
        "publisher_archive_sha256":official["asset_sha256"],
        "observed_archive_sha256":hashlib.sha256(raw).hexdigest(),
        "root_file_sha256":contents,
        "root_files_verified":True,
        "license_disposition":"NOT_CERTIFIED",
        "independent_QA_signoff":"REQUIRED",
        "method":"Official GitHub Release API SHA-256 -> checksum-verified core tar.bz2 -> independently extracted root file SHA-256 vs fixed candidate pinset",
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--pinset",type=Path,required=True)
    ap.add_argument("--archive",type=Path,help="Offline copy of official archive, still requires authenticated Release API metadata")
    ap.add_argument("--output",type=Path,required=True)
    args=ap.parse_args()
    receipt=verify_official(args.pinset,args.archive)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(receipt,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps(receipt,sort_keys=True))

if __name__=="__main__":
    main()
