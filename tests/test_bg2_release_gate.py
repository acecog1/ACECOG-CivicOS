"""Fail-closed BG-2 R3 preflight policy. Does not publish the website."""
from pathlib import Path
import os
import subprocess
import pytest
ROOT=Path(__file__).resolve().parents[1]
def test_bg2_manual_approval_gates_without_deploy():
    s=(ROOT/".github/workflows/bg2-release-gated.yml").read_text()
    assert "workflow_dispatch:" in s
    assert "\n  push:" not in s and "\n  pull_request:" not in s
    assert "environment: bg2-publication" in s
    assert "cancel-in-progress: false" in s
    assert "permissions:\n  contents: read\n  actions: read" in s
    for token in ("BG2_OWNER_PUBLICATION_GO_SHA","BG2_R1_INDEPENDENT_QA_SHA",
       "BG2_R2_INDEPENDENT_QA_SHA","BG2_R3_INDEPENDENT_QA_SHA",
       "BG2_R4_INDEPENDENT_QA_SHA","BG2_R5_PLAN_STEWARD_SHA",
       "BG2_LICENSE_REVIEW_GO_SHA","BG2_PROTECTED_ENV_AUDIT_SHA",
       "BG2_RELEASE_ARTIFACT_SHA256","BG2_APPROVED_SBOM_SHA256"):
        assert token in s
    assert 'test "$signed" = "$EXPECTED_SHA"' in s
    assert 'test "$DEDICATED_HOST_REPO" != "$GITHUB_REPOSITORY"' in s
    assert "sha256sum -c -" in s
    assert "python scripts/package_bg2_candidate.py verify" in s
    assert "gh run download" in s
    assert "uses: actions/deploy-pages" not in s

@pytest.mark.parametrize("event,ref,repo,allowed", [
    ("workflow_dispatch", "refs/heads/main", "acecog1/ACECOG-CivicOS", True),
    ("push", "refs/heads/main", "acecog1/ACECOG-CivicOS", False),
    ("workflow_dispatch", "refs/heads/feature/bg2-sovereign-browser-worker-poc", "acecog1/ACECOG-CivicOS", False),
    ("workflow_dispatch", "refs/tags/bg2-v1.0", "acecog1/ACECOG-CivicOS", False),
    ("workflow_dispatch", "refs/heads/main", "acecog1/unreviewed-static-host", False),
])
def test_default_branch_ref_guard(event, ref, repo, allowed):
    """Exercise the *actual inline workflow gate* against positive/negative contexts."""
    workflow = (ROOT/".github/workflows/bg2-release-gated.yml").read_text()
    section = workflow.split(
        "      - name: Refuse non-default-branch dispatch (no silent skip)\n", 1
    )[1].split(
        "      - name: Refuse absent/contradictory/unauthorized attestation before checkout\n", 1
    )[0]
    script = "\n".join(line[10:] for line in section.splitlines()
                       if line.startswith("          "))
    env = {**os.environ, "GITHUB_EVENT_NAME": event,
           "GITHUB_REF": ref, "GITHUB_REPOSITORY": repo}
    result = subprocess.run(["bash", "-c", script], env=env,
                            capture_output=True, text=True, check=False)
    assert (result.returncode == 0) is allowed, result.stdout + result.stderr
