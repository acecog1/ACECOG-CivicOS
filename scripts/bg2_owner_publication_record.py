"""Record an Owner-operated BG-2 Pages dispatch; never mint QA/Security approval.

The independently retained decision is verified separately by bg2_publication_gate.
This record is operational audit evidence, not a signature or legal opinion.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import urlparse
import os

REPO = "acecog1/ACECOG-CivicOS"
OWNER = "acecog1"
HEX40 = re.compile(r"[a-f0-9]{40}\Z")
HEX64 = re.compile(r"[a-f0-9]{64}\Z")
DIGEST_KEYS = ("CANDIDATE_SHA256", "DECISION_SHA256", "PREVIOUS_SHA256")
RUN_KEYS = ("CANDIDATE_RUN", "DECISION_RUN", "GITHUB_RUN_ID", "GITHUB_RUN_ATTEMPT")


def make_record(env: dict[str, str], status: str,
                served_receipt: Path | None = None, page_url: str = "") -> dict:
    if (env.get("GITHUB_REPOSITORY") != REPO or
            env.get("GITHUB_EVENT_NAME") != "workflow_dispatch" or
            env.get("GITHUB_REF") != "refs/heads/main"):
        raise ValueError("Only a manual default-branch CivicOS dispatch is permitted")
    if env.get("GITHUB_ACTOR") != OWNER or env.get("GITHUB_TRIGGERING_ACTOR") != OWNER:
        raise ValueError("Owner must initiate and, on retry, re-trigger publication")
    if env.get("OPERATION") not in ("publish", "restore"):
        raise ValueError("Invalid publication operation")
    if not HEX40.fullmatch(env.get("SOURCE_SHA", "")):
        raise ValueError("Invalid candidate source pin")
    if any(not HEX64.fullmatch(env.get(k, "")) for k in DIGEST_KEYS):
        raise ValueError("Missing or invalid independently pinned digest")
    if any(not re.fullmatch(r"[1-9][0-9]*", env.get(k, "")) for k in RUN_KEYS):
        raise ValueError("Missing or invalid retained run identity")
    if status not in ("DISPATCHED_UNVERIFIED", "SERVED_BYTES_VERIFIED"):
        raise ValueError("Invalid audit status")

    record = {
        "schema": "ACECOG-BG2-OWNER-PUBLICATION-RECORD-v1",
        "status": status,
        "repository": REPO,
        "owner_actor": env["GITHUB_ACTOR"],
        "triggering_actor": env["GITHUB_TRIGGERING_ACTOR"],
        "operation": env["OPERATION"],
        "workflow_run_id": env["GITHUB_RUN_ID"],
        "workflow_run_attempt": env["GITHUB_RUN_ATTEMPT"],
        "workflow_run_url": f"https://github.com/{REPO}/actions/runs/{env['GITHUB_RUN_ID']}",
        "source_sha": env["SOURCE_SHA"],
        "candidate_run_id": env["CANDIDATE_RUN"],
        "candidate_site_zip_sha256": env["CANDIDATE_SHA256"],
        "decision_run_id": env["DECISION_RUN"],
        "independent_decision_sha256": env["DECISION_SHA256"],
        "rollback_previous_site_zip_sha256": env["PREVIOUS_SHA256"],
        "recorded_at_utc": datetime.now(timezone.utc).isoformat(),
        "qa_security_acceptance": "REQUIRES_INDEPENDENT_VERIFIED_DECISION",
        "owner_hands_on_acceptance": "NOT_INFERRED",
        "native_device_acceptance": "NOT_INFERRED",
    }
    if status == "SERVED_BYTES_VERIFIED":
        if served_receipt is None or not served_receipt.is_file():
            raise ValueError("Actual served-byte receipt required")
        receipt_bytes = served_receipt.read_bytes()
        receipt = json.loads(receipt_bytes)
        parsed = urlparse(page_url)
        if (parsed.scheme != "https" or parsed.netloc != "acecog1.github.io" or
                parsed.path.rstrip("/") != "/ACECOG-CivicOS"):
            raise ValueError("Unexpected deployed Pages URL")
        for record_key, receipt_key in (
            ("operation", "operation"), ("source_sha", "source_sha"),
            ("candidate_site_zip_sha256", "candidate_sha256"),
            ("rollback_previous_site_zip_sha256", "previous_sha256"),
            ("workflow_run_id", "run_id")):
            if receipt.get(receipt_key) != record[record_key]:
                raise ValueError("Served receipt contradicts pinned Owner dispatch: " + receipt_key)
        if receipt.get("url") != page_url or not receipt.get("files"):
            raise ValueError("Served verification receipt is incomplete")
        record["served_pages_url"] = page_url
        record["served_receipt_sha256"] = hashlib.sha256(receipt_bytes).hexdigest()
        record["served_asset_count"] = len(receipt["files"])
    return record


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--status", choices=("DISPATCHED_UNVERIFIED", "SERVED_BYTES_VERIFIED"), required=True)
    parser.add_argument("--served-receipt", type=Path)
    parser.add_argument("--page-url", default="")
    args = parser.parse_args()
    result = make_record(dict(os.environ), args.status, args.served_receipt, args.page_url)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
