"""Exercise preservation and restoration with fixture bytes, never a live host."""
import json
from pathlib import Path
from unittest.mock import patch
from zipfile import ZipFile
import pytest
from scripts import bg2_pages_tree as tree
from scripts import prepare_bg2_publication as prepare
from scripts.bg2_publication_gate import digest, read_archive


def make_zip(path, files):
    with ZipFile(path, 'w') as z:
        for n, b in files.items():
            z.writestr(n, b)
    return path


def test_restore_exact_retained_bytes_without_rebuilding(tmp_path):
    files = {'index.html': b'BG-1 unchanged', 'assets/data.json': b'{"fixture":true}'}
    archive = make_zip(tmp_path / 'prior.zip', files)
    output = tmp_path / 'served'
    result = tree.restore(archive, digest(archive.read_bytes()), output)
    assert result == {n: digest(b) for n, b in files.items()}
    assert {p.relative_to(output).as_posix(): p.read_bytes()
            for p in output.rglob('*') if p.is_file()} == files


def test_tampered_prior_archive_never_writes_destination(tmp_path):
    archive = make_zip(tmp_path / 'prior.zip', {'index.html': b'original'})
    expected = digest(archive.read_bytes())
    make_zip(archive, {'index.html': b'modified'})
    with pytest.raises(RuntimeError, match='hash mismatch'):
        tree.restore(archive, expected, tmp_path / 'served')
    assert not (tmp_path / 'served').exists()


def test_unsafe_archive_or_existing_destination_is_rejected(tmp_path):
    archive = make_zip(tmp_path / 'prior.zip', {'index.html': b'ok', '../escape': b'bad'})
    with pytest.raises(RuntimeError):
        tree.restore(archive, digest(archive.read_bytes()), tmp_path / 'served')
    assert not (tmp_path / 'escape').exists()
    archive = make_zip(archive, {'index.html': b'ok'})
    output = tmp_path / 'served'
    output.mkdir()
    with pytest.raises(RuntimeError, match='must be new'):
        tree.restore(archive, digest(archive.read_bytes()), output)


def test_assembly_preserves_bg1_and_recovered_texts_with_pending_dispositions(tmp_path):
    baseline = {'index.html': b'BG-1 original', 'assets/file.bin': b'\x00\xff'}
    previous = make_zip(tmp_path / 'previous.zip', baseline)
    runtime = make_zip(tmp_path / 'runtime.zip', {'index.html': b'<footer></footer>'})
    output = tmp_path / 'site.zip'
    # Unit fixture bypasses only runtime provenance; production calls the real
    # existing exact-Git verifier. All original/recovered packet bytes are real.
    with patch('scripts.package_bg2_candidate.verify_review_zip') as verify:
        prepare.assemble(previous, runtime, 'a' * 40, output)
        verify.assert_called_once_with(runtime, 'a' * 40)
    files = read_archive(output)
    manifest = json.loads(files['publication-manifest.json'])
    assert manifest['bg1_file_sha256'] == {n: digest(b) for n, b in baseline.items()}
    assert all(files[n] == b for n, b in baseline.items())
    assert b'./legal/index.html' in files['beta/index.html']
    rust = files['beta/legal/recovered/upstream/rust-1.97.1/rustc/share/doc/rust/COPYRIGHT-library.html']
    assert digest(rust) == '0a65bb747c49c7bb816cbc7188319bd6e4e8d08091c1190b8a3c0971c47968ed'
    assert all(c['disposition'] == 'PENDING' for c in json.loads(files['beta/legal/claims.json'])['claims'])
    assert manifest['file_sha256'] == {n: digest(b) for n, b in files.items() if n != 'publication-manifest.json'}
