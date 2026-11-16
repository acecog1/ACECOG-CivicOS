"""Fixed-origin, HTTPS-only Pages byte retrieval; redirects are refused."""
import http.client
from urllib.parse import urlsplit, unquote

HOST = 'acecog1.github.io'
PREFIX = '/ACECOG-CivicOS/'
LIMIT = 240 * 1024 * 1024


def fetch_pages(url: str) -> bytes:
    parsed = urlsplit(url)
    path = unquote(parsed.path)
    if (parsed.scheme != 'https' or parsed.netloc != HOST or
            not path.startswith(PREFIX) or parsed.query or parsed.fragment or
            '\\' in path or any(p in {'.', '..'} for p in path.split('/'))):
        raise RuntimeError('Unexpected Pages URL')
    connection = http.client.HTTPSConnection(HOST, timeout=30)
    try:
        connection.request('GET', parsed.path, headers={'Cache-Control': 'no-cache'})
        response = connection.getresponse()
        if response.status != 200:
            raise RuntimeError('Pages request failed or redirected: ' + str(response.status))
        data = response.read(LIMIT + 1)
        if len(data) > LIMIT:
            raise RuntimeError('Pages response exceeds byte limit')
        return data
    finally:
        connection.close()
