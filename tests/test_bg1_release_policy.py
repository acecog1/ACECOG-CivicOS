"""Q-31 Pages first-publication fail-closed proof. No external action is invoked."""
import os
import pathlib
import re
import subprocess
import yaml

ROOT = pathlib.Path(__file__).resolve().parents[1]
WORKFLOW = yaml.safe_load((ROOT / ".github/workflows/bg1-manual-pages.yml").read_text())
EVENTS = WORKFLOW.get("on", WORKFLOW.get(True))
PREFLIGHT = WORKFLOW["jobs"]["preflight"]
RUN = next(x["run"] for x in PREFLIGHT["steps"] if x.get("name") == "Require exact SHA and independent release attestations")


def test_deployment_event_and_permissions_are_hard_gated():
    assert set(EVENTS) == {"workflow_dispatch"}
    assert PREFLIGHT["if"].find("refs/heads/main") != -1
    assert WORKFLOW["concurrency"]["cancel-in-progress"] is False
    assert WORKFLOW["jobs"]["build"]["needs"] == "preflight"
    deploy = WORKFLOW["jobs"]["deploy"]
    assert deploy["needs"] == ["preflight", "build"]
    assert deploy["environment"]["name"] == "github-pages"
    assert deploy["permissions"]["pages"] == "write"
    assert deploy["permissions"]["id-token"] == "write"
    assert "actions/deploy-pages" not in str(WORKFLOW["jobs"]["preflight"])
    assert "actions/deploy-pages" not in str(WORKFLOW["jobs"]["build"])
    for flag in ("BG1_OWNER_PUBLICATION_GO_SHA", "BG1_QA_GO_SHA",
                 "BG1_DUAL_HOST_NOTICE_GO_SHA"):
        assert flag in (ROOT / ".github/workflows/bg1-manual-pages.yml").read_text()


def _run(sha, owner, qa, notice):
    env = os.environ.copy()
    env.update(REQUESTED=sha, GITHUB_SHA=sha,
               OWNER_APPROVED=owner, QA_APPROVED=qa,
               HOST_NOTICE_APPROVED=notice)
    return subprocess.run(["bash", "-e", "-o", "pipefail", "-c", RUN],
                          cwd=ROOT, env=env, text=True, capture_output=True, timeout=10)


def test_missing_owner_qa_or_notice_go_blocks_release():
    # Release gate shell is executed locally without GitHub credentials or
    # deployment. Passing all string checks is still NOT live approval.
    sha = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    assert re.fullmatch("[a-f0-9]{40}", sha)
    for owner, qa, notice in [("", "", ""), (sha, "", sha),
                              (sha, sha, ""), ("a" * 40, sha, sha)]:
        result = _run(sha, owner, qa, notice)
        assert result.returncode != 0
    result = _run("main", sha, sha, sha)
    assert result.returncode != 0


def test_site_build_is_not_a_publishing_workflow():
    wf = yaml.safe_load((ROOT / ".github/workflows/site.yml").read_text())
    assert "actions/deploy-pages" not in str(wf)
    assert wf["concurrency"]["cancel-in-progress"] is False
    assert "@fontsource/public-sans@5.3.0" in str(wf)
    assert "@fontsource/jetbrains-mono@5.3.0" in str(wf)
