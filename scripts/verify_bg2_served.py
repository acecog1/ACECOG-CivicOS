"""Verify anonymously served deployment bytes; never infer browser or AT PASS."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import time
import urllib.parse
import urllib.request


def verify(root: Path, url: str) -> dict:
    if not url.startswith('https://acecog1.github.io/ACECOG-CivicOS/'):
        raise RuntimeError('Unexpected Pages origin/path')
    results = []
    for path in sorted(root.rglob('*')):
        if not path.is_file():
            continue
        relative = path.relative_to(root).as_posix()
        target = url.rstrip('/') + '/' + urllib.parse.quote(relative)
        expected = hashlib.sha256(path.read_bytes()).hexdigest()
        error = None
        for attempt in range(5):
            try:
                req = urllib.request.Request(target, headers={'Cache-Control': 'no-cache'})
                with urllib.request.urlopen(req, timeout=30) as response:
                    if urllib.parse.urlsplit(response.url).netloc != 'acecog1.github.io':
                        raise RuntimeError('Unexpected redirect')
                    actual = hashlib.sha256(response.read(240 * 1024 * 1024)).hexdigest()
                    if actual != expected:
                        raise RuntimeError('Served digest mismatch: ' + relative)
                error = None
                break
            except Exception as exc:
                error = exc
                if attempt < 4:
                    time.sleep(3)
        if error:
            raise error
        results.append({'path': relative, 'sha256': expected})
    return {'url': url, 'operation': os.environ.get('OPERATION'),
            'run_id': os.environ.get('GITHUB_RUN_ID'), 'files': results,
            'source_sha': os.environ.get('SOURCE_SHA'),
            'candidate_sha256': os.environ.get('CANDIDATE_SHA256'),
            'previous_sha256': os.environ.get('PREVIOUS_SHA256'),
            'browser': 'NOT_TESTED_BY_BYTE_PROBE', 'native_device': 'NOT_TESTED',
            'rollback_drill': 'NOT_INFERRED_FROM_WORKFLOW_EXISTENCE'}


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--root', type=Path, required=True)
    p.add_argument('--url', required=True)
    p.add_argument('--receipt', type=Path, required=True)
    a = p.parse_args()
    a.receipt.write_text(json.dumps(verify(a.root, a.url), indent=2) + '\n')
