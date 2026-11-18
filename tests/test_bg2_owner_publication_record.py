"""Owner-operated BG-2 workflow tests: synthetic contexts, never release approval."""
import json
from pathlib import Path

import pytest
from scripts.bg2_owner_publication_record import make_record

ROOT = Path(__file__).resolve().parents[1]


def valid_env():
    return {
        "GITHUB_REPOSITORY": "acecog1/ACECOG-CivicOS",
        "GITHUB_EVENT_NAME": "workflow_dispatch",
        "GITHUB_REF": "refs/heads/main",
        "GITHUB_ACTOR": "acecog1",
        "GITHUB_TRIGGERING_ACTOR": "acecog1",
        "GITHUB_RUN_ID": "44370000000",
        "GITHUB_RUN_ATTEMPT": "1",
        "OPERATION": "publish",
        "SOURCE_SHA": "a" * 40,
        "CANDIDATE_RUN": "44249533176",
        "CANDIDATE_SHA256": "b" * 64,
        "DECISION_RUN": "44359445452",
        "DECISION_SHA256": "c" * 64,
        "PREVIOUS_SHA256": "d" * 64,
    }


@pytest.mark.parametrize("operation", ["publish", "restore"])
def test_owner_can_dispatch_either_operation(operation):
    env = valid_env()
    env["OPERATION"] = operation
    receipt = make_record(env, "DISPATCHED_UNVERIFIED")
    assert receipt["owner_actor"] == receipt["triggering_actor"] == "acecog1"
    assert receipt["status"] == "DISPATCHED_UNVERIFIED"
    assert receipt["candidate_site_zip_sha256"] == "b" * 64
    assert receipt["independent_decision_sha256"] == "c" * 64
    assert receipt["rollback_previous_site_zip_sha256"] == "d" * 64
    assert receipt["qa_security_acceptance"] == "REQUIRES_INDEPENDENT_VERIFIED_DECISION"


@pytest.mark.parametrize("field,value", [
    ("GITHUB_ACTOR", "unapproved-user"),
    ("GITHUB_TRIGGERING_ACTOR", "unapproved-rerunner"),
    ("GITHUB_REPOSITORY", "other/repo"),
    ("GITHUB_EVENT_NAME", "push"),
    ("GITHUB_REF", "refs/heads/feature"),
    ("OPERATION", "publish-no-checks"),
    ("SOURCE_SHA", ""),
    ("SOURCE_SHA", "not-a-sha"),
    ("CANDIDATE_SHA256", "invalid"),
    ("DECISION_SHA256", ""),
    ("PREVIOUS_SHA256", "0" * 63),
    ("CANDIDATE_RUN", "0"),
    ("DECISION_RUN", ""),
    ("GITHUB_RUN_ID", "0"),
    ("GITHUB_RUN_ATTEMPT", "0"),
])
def test_fail_closed_owner_and_pin_inputs(field, value):
    env = valid_env()
    env[field] = value
    with pytest.raises(ValueError):
        make_record(env, "DISPATCHED_UNVERIFIED")


def test_verified_status_requires_actual_receipt(tmp_path):
    env = valid_env()
    with pytest.raises(ValueError, match="receipt required"):
        make_record(env, "SERVED_BYTES_VERIFIED", page_url="https://acecog1.github.io/ACECOG-CivicOS/")
    receipt = tmp_path / "served.json"
    receipt.write_text(json.dumps({
        "url": "https://acecog1.github.io/ACECOG-CivicOS/",
        "operation": env["OPERATION"],
        "source_sha": env["SOURCE_SHA"],
        "candidate_sha256": env["CANDIDATE_SHA256"],
        "previous_sha256": env["PREVIOUS_SHA256"],
        "run_id": env["GITHUB_RUN_ID"],
        "files": [{"path": "index.html", "sha256": "f" * 64}],
    }))
    record = make_record(env, "SERVED_BYTES_VERIFIED", receipt,
                         "https://acecog1.github.io/ACECOG-CivicOS/")
    assert record["status"] == "SERVED_BYTES_VERIFIED"
    assert record["served_asset_count"] == 1
    assert len(record["served_receipt_sha256"]) == 64
    for url in ("http://acecog1.github.io/ACECOG-CivicOS/",
                "https://evil.example/ACECOG-CivicOS/",
                "https://acecog1.github.io/unrelated/"):
        with pytest.raises(ValueError):
            make_record(env, "SERVED_BYTES_VERIFIED", receipt, url)
    altered = json.loads(receipt.read_text())
    altered["source_sha"] = "1" * 40
    receipt.write_text(json.dumps(altered))
    with pytest.raises(ValueError, match="contradicts"):
        make_record(env, "SERVED_BYTES_VERIFIED", receipt,
                    "https://acecog1.github.io/ACECOG-CivicOS/")


def test_real_workflow_uses_owner_gate_but_retains_independent_decision():
    workflow = (ROOT / ".github/workflows/bg2-pages-delivery.yml").read_text()
    assert "workflow_dispatch:" in workflow
    assert 'github.ref == \'refs/heads/main\'' in workflow
    assert "environment:" in workflow and "name: bg2-publication" in workflow
    assert "required_reviewers" not in workflow
    assert "prevent_self_review" not in workflow
    assert "scripts.bg2_owner_publication_record" in workflow
    for value in ("BG2_SOURCE_SHA", "BG2_CANDIDATE_SHA256",
                  "BG2_DECISION_SHA256", "BG2_PREVIOUS_SITE_SHA256",
                  "scripts.bg2_publication_gate", "decision/decision.json",
                  "scripts.bg2_pages_tree", "verify_bg2_served",
                  "actions/deploy-pages@v4", "owner-publication-record.json"):
        assert value in workflow
    assert "if: always()" in workflow
    assert "gh run download" in workflow
    assert "Retained bytes mismatch" in workflow
    assert "candidate-run.json" in workflow
