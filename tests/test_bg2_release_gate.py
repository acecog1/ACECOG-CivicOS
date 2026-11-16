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
       "BG2_R3_INDEPENDENT_QA_SHA",
       "BG2_R4_INDEPENDENT_QA_SHA",
       "BG2_LICENSE_REVIEW_GO_SHA","BG2_PROTECTED_ENV_AUDIT_SHA",
       "BG2_RELEASE_ARTIFACT_SHA256","BG2_APPROVED_SBOM_SHA256"):
        assert token in s
    assert 'test "$signed" = "$EXPECTED_SHA"' in s
    assert 'test "$STAGING_URL" = "https://acecog.org/beta"' in s
    assert "BG2_DEDICATED_HOST_REPO" not in s
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


@pytest.mark.parametrize("staging_url,allowed", [
    ("https://acecog.org/beta", True),
    ("https://acecog.org/", False),
    ("http://acecog.org/beta", False),
    ("https://acecog.com/beta", False),
    ("", False),
])
def test_owner_staging_target_fail_closed(staging_url, allowed):
    """The release check rejects other public origins or paths before an approved rollout."""
    workflow = (ROOT/".github/workflows/bg2-release-gated.yml").read_text()
    gate = next(line.strip() for line in workflow.splitlines()
                if 'test "$STAGING_URL" = "https://acecog.org/beta"' in line)
    env = {**os.environ, "STAGING_URL": staging_url}
    result = subprocess.run(["bash", "-c", gate], env=env,
                            capture_output=True, text=True, check=False)
    assert (result.returncode == 0) is allowed, result.stdout + result.stderr

@pytest.mark.parametrize("missing", [None, "OWNER_GO", "LICENSE_QA_GO", "APPROVED_ZIP_HASH"])
def test_initial_beta_preflight_does_not_require_schedule_signoff(missing):
    """Execute the real attestation gate: schedule absent is allowed; mandatory evidence absent is refused."""
    workflow = (ROOT/".github/workflows/bg2-release-gated.yml").read_text()
    assert "BG2_R5_PLAN_STEWARD_SHA" not in workflow
    assert "R5_PLAN_GO" not in workflow
    assert "BG2_R2_INDEPENDENT_QA_SHA" not in workflow
    section = workflow.split(
        "      - name: Refuse absent/contradictory/unauthorized attestation before checkout\n", 1
    )[1].split("      - uses: actions/checkout", 1)[0]
    script = "\n".join(line[10:] for line in section.splitlines()
                       if line.startswith("          "))
    sha = "1" * 40
    digest = "2" * 64
    env = {**os.environ, "EXPECTED_SHA": sha, "ARCHIVE_SHA": digest,
           "REVIEW_RUN": "123", "VERSION_ID": "bg2-v0.1",
           "APPROVED_ZIP_HASH": digest, "APPROVED_SBOM_HASH": "3" * 64,
           "STAGING_URL": "https://acecog.org/beta"}
    for key in ("OWNER_GO", "R1_QA_GO", "R3_QA_GO",
                "R4_QA_GO", "LICENSE_QA_GO", "ENV_REVIEW_GO"):
        env[key] = sha
    env.pop("R5_PLAN_GO", None)
    if missing:
        env[missing] = ""
    result = subprocess.run(["bash", "-c", script], env=env,
                            capture_output=True, text=True, check=False)
    assert (result.returncode == 0) is (missing is None), result.stdout + result.stderr
