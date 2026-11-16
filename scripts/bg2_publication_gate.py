"""Verify publication bytes against a protected, out-of-band review decision.

Schema validation is not a signature or legal opinion. The decision digest must
come from protected release configuration, never from the downloaded artifact.
"""
from __future__ import annotations
import argparse
import json
import hashlib
import re
import stat
from pathlib import Path
from zipfile import ZipFile

SCHEMA = "ACECOG-BG2-PUBLICATION-v1"
GROUPS = {"source-and-modifications", "recipient-notices", "rust-1.97.1",
          "cpython-sdk-libraries"}
LIMIT = 240 * 1024 * 1024


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def hold(message: str) -> None:
    raise RuntimeError("PUBLICATION HOLD: " + message)


def document(data: bytes) -> dict:
    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                hold("duplicate JSON key")
            result[key] = value
        return result
    result = json.loads(data, object_pairs_hook=unique)
    if not isinstance(result, dict):
        hold("JSON object required")
    return result


def read_archive(path: Path) -> dict[str, bytes]:
    if path.stat().st_size > LIMIT:
        hold("archive exceeds limit")
    files, folded, total = {}, set(), 0
    with ZipFile(path) as archive:
        for entry in archive.infolist():
            name = entry.filename
            total += entry.file_size
            if (entry.orig_filename != name or not name or name.startswith("/") or
                    any(c in name for c in "\\:\x00") or
                    any(not re.fullmatch(r"[A-Za-z0-9_@+.,()=-]+", p)
                        or p in {".", ".."} for p in name.split("/")) or
                    name.casefold() in folded or entry.is_dir() or
                    stat.S_ISLNK(entry.external_attr >> 16) or entry.flag_bits & 1 or
                    total > LIMIT or len(files) >= 10000):
                hold("unsafe, duplicate, encrypted or oversized ZIP entry")
            folded.add(name.casefold())
            files[name] = archive.read(entry)  # verifies CRC and local filename
    return files


def require_publication_artifact(path: Path, *, source_sha: str = "",
                                 archive_sha256: str = "", decision: Path | None = None,
                                 decision_sha256: str = "") -> dict:
    if (not re.fullmatch(r"[a-f0-9]{40}", source_sha) or
            not re.fullmatch(r"[a-f0-9]{64}", archive_sha256) or
            not re.fullmatch(r"[a-f0-9]{64}", decision_sha256) or decision is None):
        hold("protected source/archive/independent-decision pins required")
    if digest(path.read_bytes()) != archive_sha256:
        hold("archive bytes differ from reviewed digest")
    decision_bytes = decision.read_bytes()
    if digest(decision_bytes) != decision_sha256:
        hold("decision bytes differ from protected digest")
    approval = document(decision_bytes)
    files = read_archive(path)
    if "publication-manifest.json" not in files:
        hold("provisional format is not a publication artifact")
    manifest_bytes = files.pop("publication-manifest.json")
    manifest = document(manifest_bytes)
    if (manifest.get("schema") != SCHEMA or manifest.get("source_sha") != source_sha or
            manifest.get("file_sha256") != {n: digest(b) for n, b in files.items()}):
        hold("manifest/source/file inventory mismatch")
    baseline = manifest.get("bg1_file_sha256")
    if (not isinstance(baseline, dict) or not baseline or
            baseline != {n: digest(b) for n, b in files.items() if not n.startswith("beta/")}):
        hold("BG-1 baseline inventory differs from publication bytes")
    for name in ("index.html", "beta/index.html", "beta/legal/index.html", "beta/legal/SOURCE_ACCESS.txt",
                 "beta/legal/THIRD_PARTY_NOTICES.txt", "beta/legal/claims.json"):
        if not files.get(name):
            hold("missing recipient deliverable: " + name)
    if b"./legal/index.html" not in files["beta/index.html"]:
        hold("notice/source link missing from application")
    if (approval.get("schema") != "ACECOG-BG2-INDEPENDENT-DECISION-v1" or
            approval.get("source_sha") != source_sha or
            approval.get("archive_sha256") != archive_sha256 or
            approval.get("manifest_sha256") != digest(manifest_bytes) or
            approval.get("claims_sha256") != digest(files["beta/legal/claims.json"])):
        hold("independent decision does not bind exact candidate bytes")
    if approval.get("mandatory_groups") != {key: "CLOSED" for key in GROUPS}:
        hold("four mandatory notice/source groups require closure")
    # Owner 2026-11-16: formal qualified legal review is queued with final QA.
    # Mandatory notice/source duties still require a real Security disposition.
    for role in ("independent_qa", "security_licensing"):
        record = approval.get(role, {})
        if (record.get("decision") != "ACCEPT" or not record.get("reviewer") or
                not str(record.get("evidence_url", "")).startswith("https://")):
            hold("missing attributable disposition: " + role)
    claims = document(files["beta/legal/claims.json"]).get("claims")
    if not isinstance(claims, list) or not claims:
        hold("finite claim-level disposition required")
    ids = set()
    for claim in claims:
        cid, kind = claim.get("id"), claim.get("classification")
        if not isinstance(cid, str) or not cid or cid in ids:
            hold("claim IDs must be unique")
        ids.add(cid)
        if kind not in {"M", "R", "C"}:
            hold("unresolved applicability cannot become residual")
        refs = claim.get("evidence_paths")
        if not isinstance(refs, list) or not refs or any(r not in files for r in refs):
            hold("claim lacks packaged evidence")
        if claim.get("disposition") != {"M": "SATISFIED", "R": "ACCEPTED_RESIDUAL", "C": "CONTEXT"}[kind]:
            hold("mandatory or unresolved claim remains open")
    return manifest


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--zip", type=Path, required=True)
    parser.add_argument("--source-sha", required=True)
    parser.add_argument("--archive-sha256", required=True)
    parser.add_argument("--decision", type=Path, required=True)
    parser.add_argument("--decision-sha256", required=True)
    parser.add_argument("--extract", type=Path)
    args = parser.parse_args()
    result = require_publication_artifact(args.zip, source_sha=args.source_sha,
        archive_sha256=args.archive_sha256, decision=args.decision,
        decision_sha256=args.decision_sha256)
    if args.extract:
        if args.extract.exists():
            hold("extraction destination must be new")
        for name, data in read_archive(args.zip).items():
            target = args.extract / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
    print(json.dumps(result, sort_keys=True))
