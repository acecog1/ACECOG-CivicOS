"""Capture live BG-1 bytes against its retained deployment inventory, no rebuild."""
import argparse
import hashlib
from pathlib import Path
import re
import urllib.request
from urllib.parse import quote
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

URL = 'https://acecog1.github.io/ACECOG-CivicOS/'


def snapshot(inventory: Path, output: Path) -> str:
    files = {}
    for line in inventory.read_text().splitlines():
        match = re.fullmatch(r'([a-f0-9]{64})  build/site/(.+)', line)
        if not match:
            raise RuntimeError('Invalid retained deployment inventory')
        expected, name = match.groups()
        if any(p in {'', '.', '..'} for p in name.split('/')) or '\\' in name or ':' in name:
            raise RuntimeError('Unsafe prior deployment path')
        if name in files or name.startswith('beta/'):
            raise RuntimeError('Duplicate or unexpected beta in BG-1 inventory')
        with urllib.request.urlopen(URL + quote(name), timeout=30) as response:
            if not response.url.startswith(URL):
                raise RuntimeError('Unexpected BG-1 redirect')
            data = response.read(240 * 1024 * 1024)
        if hashlib.sha256(data).hexdigest() != expected:
            raise RuntimeError('Live BG-1 differs from retained deployment: ' + name)
        files[name] = data
    if 'index.html' not in files or not files:
        raise RuntimeError('Missing BG-1 inventory/index')
    if output.exists():
        raise RuntimeError('Snapshot output already exists')
    output.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(output, 'w') as z:
        for name, data in sorted(files.items()):
            entry = ZipInfo(name, (1980, 1, 1, 0, 0, 0))
            entry.compress_type = ZIP_DEFLATED
            z.writestr(entry, data)
    return hashlib.sha256(output.read_bytes()).hexdigest()


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--inventory', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    a = p.parse_args()
    print(snapshot(a.inventory, a.output))
