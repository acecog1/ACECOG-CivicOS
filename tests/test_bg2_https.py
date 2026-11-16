from unittest.mock import patch, Mock
import pytest
from scripts import bg2_https as https


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
