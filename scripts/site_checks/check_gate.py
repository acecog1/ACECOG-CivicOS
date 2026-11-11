"""Prove a deliberate pytest failure stops the Site workflow's exact check command block.

Runs locally or in CI; does not invoke deployment or require GitHub credentials.
"""
import json
from pathlib import Path
import shlex
import subprocess
import tempfile

import yaml

ROOT = Path(__file__).resolve().parents[2]
workflow = yaml.safe_load((ROOT / '.github/workflows/site.yml').read_text())
steps = workflow['jobs']['build']['steps']
commands = next(s['run'] for s in steps if s.get('name') == 'Exact-commit acceptance and contract checks')
with tempfile.TemporaryDirectory(prefix='q31-gate-') as tmp:
    marker = Path(tmp) / 'artifact-upload-would-run'
    with tempfile.NamedTemporaryFile(mode='w', prefix='test_q31_probe_', suffix='.py',
                                     dir=ROOT / 'tests', delete=False) as handle:
        handle.write('def test_deliberate_failure():\n    assert False, "Q31 gate probe"\n')
        probe = Path(handle.name)
    try:
        result = subprocess.run(['bash', '-e', '-o', 'pipefail', '-c',
                                 commands + '\ntouch ' + shlex.quote(str(marker))],
                                cwd=ROOT, text=True, capture_output=True, timeout=120)
        passed = result.returncode != 0 and not marker.exists() and 'Q31 gate probe' in result.stdout
        output = ROOT / 'build/site-evidence'
        output.mkdir(parents=True, exist_ok=True)
        (output / 'negative-gate.txt').write_text(result.stdout + result.stderr)
        print(json.dumps({'deliberate_failure_blocks_later_commands': passed,
                          'returncode': result.returncode, 'marker_exists': marker.exists()}))
        if not passed:
            raise SystemExit('Gate probe failed; inspect build/site-evidence/negative-gate.txt')
    finally:
        probe.unlink()
