"""Pinned upstream license source texts for BG-2 independent redistribution review.

These are reference documents, not a certified complete binary license packet.
Exact upstream git-blob identity is checked before bundling and again from ZIP.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re

SCHEMA = "ACECOG-BG2-UPSTREAM-LICENSE-SOURCES-v0.1"
PROVENANCE_NAME = "LICENSE_SOURCE_PROVENANCE.json"
PREFIX = "third_party/upstream_license_sources/"
SOURCE_MANIFEST = "docs/evidence/bg2-license-upstream-sources-v0.1.json"


def git_blob_sha(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def records_from_manifest(data: bytes) -> list[dict]:
    obj = json.loads(data)
    records = obj.get("records")
    if (obj.get("schema") != SCHEMA or
            obj.get("independent_reviewer_signoff") != "PENDING" or
            not isinstance(records, list) or len(records) != 4):
        raise RuntimeError("Incomplete/unapproved upstream license-source manifest")
    paths = []
    for item in records:
        path = item.get("dest", "")
        sha = item.get("upstream_blob_sha1", "")
        commit = item.get("upstream_commit", "")
        if (not path.startswith("docs/evidence/bg2-license-sources/") or
                path != "docs/evidence/bg2-license-sources/" + Path(path).name or
                not re.fullmatch("[0-9a-f]{40}", sha) or
                not re.fullmatch("[0-9a-f]{40}", commit)):
            raise RuntimeError("Invalid license source identity")
        paths.append(Path(path).name)
    if len(set(paths)) != len(paths):
        raise RuntimeError("Duplicate upstream license-source name")
    return records


def copy_verified(root: Path, folder: Path) -> None:
    raw = (root / SOURCE_MANIFEST).read_bytes()
    records = records_from_manifest(raw)
    dst = folder / "upstream_license_sources"
    dst.mkdir(parents=True, exist_ok=False)
    for record in records:
        path = record["dest"]
        data = (root / path).read_bytes()
        if git_blob_sha(data) != record["upstream_blob_sha1"]:
            raise RuntimeError("Upstream license Git blob mismatch: " + path)
        (dst / Path(path).name).write_bytes(data)
    (folder / PROVENANCE_NAME).write_bytes(raw)


def verify_packet(files: dict[str, bytes]) -> set[str]:
    raw = files.get("third_party/" + PROVENANCE_NAME)
    if raw is None:
        raise RuntimeError("Missing upstream license provenance manifest")
    records = records_from_manifest(raw)
    names = {"third_party/" + PROVENANCE_NAME}
    for record in records:
        path = PREFIX + Path(record["dest"]).name
        data = files.get(path)
        if data is None:
            raise RuntimeError("Missing pinned upstream license file: " + path)
        if git_blob_sha(data) != record["upstream_blob_sha1"]:
            raise RuntimeError("Altered upstream license file: " + path)
        names.add(path)
    return names
