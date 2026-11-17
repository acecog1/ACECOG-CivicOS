from unittest.mock import patch, Mock
import pytest
from scripts import bg2_https as https
from scripts import snapshot_bg1, verify_bg2_served
from scripts.bg2_publication_gate import digest, read_archive


@pytest.mark.parametrize('url', [
    'file:///ACECOG-CivicOS/index.html',
    'http://acecog1.github.io/ACECOG-CivicOS/index.html',
    'https://evil.example/ACECOG-CivicOS/index.html',
    'https://acecog1.github.io.evil.example/ACECOG-CivicOS/index.html',
    'https://user@acecog1.github.io/ACECOG-CivicOS/index.html',
    'https://acecog1.github.io/ACECOG-CivicOS/%2e%2e/private',
    'https://acecog1.github.io/other/index.html',
])
def test_unexpected_scheme_origin_or_path_never_opens_connection(url):
    with patch.object(https.http.client, 'HTTPSConnection') as connection:
        with pytest.raises(RuntimeError, match='Unexpected Pages URL'):
            https.fetch_pages(url)
        connection.assert_not_called()


def test_allowed_https_returns_actual_bytes_and_closes_connection():
    with patch.object(https.http.client, 'HTTPSConnection') as factory:
        response = factory.return_value.getresponse.return_value
        response.status, response.read.return_value = 200, b'exact fixture bytes'
        assert https.fetch_pages('https://acecog1.github.io/ACECOG-CivicOS/index.html') == b'exact fixture bytes'
        factory.assert_called_once_with('acecog1.github.io', timeout=30)
        factory.return_value.close.assert_called_once()


@pytest.mark.parametrize('status', [301, 302, 404, 500])
def test_redirect_or_error_never_passes(status):
    with patch.object(https.http.client, 'HTTPSConnection') as factory:
        factory.return_value.getresponse.return_value.status = status
        with pytest.raises(RuntimeError, match='failed or redirected'):
            https.fetch_pages('https://acecog1.github.io/ACECOG-CivicOS/index.html')
        factory.return_value.close.assert_called_once()


def test_capture_retains_hash_verified_control_and_fetches_public_assets(tmp_path):
    inventory = tmp_path / 'hashes.txt'
    inventory.write_text(digest(b'') + '  build/site/.nojekyll\n' +
                         digest(b'fixture') + '  build/site/index.html\n')
    with patch.object(snapshot_bg1, 'fetch_pages', return_value=b'fixture') as fetch:
        snapshot_bg1.snapshot(inventory, tmp_path / 'site.zip')
        fetch.assert_called_once_with(snapshot_bg1.URL + 'index.html')
    assert read_archive(tmp_path / 'site.zip') == {'.nojekyll': b'', 'index.html': b'fixture'}


def test_wrong_control_hash_is_not_silently_accepted(tmp_path):
    inventory = tmp_path / 'hashes.txt'
    inventory.write_text('a' * 64 + '  build/site/.nojekyll\n')
    with pytest.raises(RuntimeError, match='differs from retained'):
        snapshot_bg1.snapshot(inventory, tmp_path / 'site.zip')
    assert not (tmp_path / 'site.zip').exists()


def test_served_probe_reports_controls_separately_from_http_results(tmp_path):
    (tmp_path / '.nojekyll').write_bytes(b'')
    (tmp_path / 'index.html').write_bytes(b'fixture')
    with patch.object(verify_bg2_served, 'fetch_pages', return_value=b'fixture') as fetch:
        receipt = verify_bg2_served.verify(tmp_path, snapshot_bg1.URL)
        fetch.assert_called_once_with(snapshot_bg1.URL + 'index.html')
    assert receipt['unserved_host_controls'][0]['path'] == '.nojekyll'
    assert [r['path'] for r in receipt['files']] == ['index.html']
