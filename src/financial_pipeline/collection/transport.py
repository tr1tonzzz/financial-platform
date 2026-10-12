"""Bounded HTTP transport. Redirects are validated before making the next request."""
from dataclasses import dataclass
from datetime import datetime, timezone
import hashlib
import time
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import Request, HTTPRedirectHandler, build_opener
from .models import CollectionError


def validate_url(url, hosts):
    p = urlsplit(url)
    if p.scheme != 'https' or p.hostname not in hosts or p.username or p.password or p.port not in [None, 443]:
        raise CollectionError('unregistered_source_url', 'URL is outside the registered HTTPS source', {'url': url})


class CheckedRedirect(HTTPRedirectHandler):
    def __init__(self, hosts):
        super().__init__()
        self.hosts = hosts

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        validate_url(newurl, self.hosts)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


@dataclass(frozen=True)
class Response:
    body: bytes
    event: dict


class HttpClient:
    def __init__(self, timeout=45, attempts=3, interval=.2):
        self.timeout, self.attempts, self.interval = timeout, attempts, interval
        self.last = 0.

    def fetch(self, url, hosts, limit):
        validate_url(url, hosts)
        for attempt in range(self.attempts):
            time.sleep(max(0., self.interval-(time.monotonic()-self.last)))
            try:
                opener = build_opener(CheckedRedirect(hosts))
                with opener.open(Request(url, headers={'User-Agent': 'FinancialAnalysisPlatform/1.0', 'Accept-Encoding': 'identity'}), timeout=self.timeout) as r:
                    validate_url(r.url, hosts)
                    body = r.read(limit+1)
                    if len(body) > limit:
                        raise CollectionError('response_too_large', 'Response exceeds the configured byte limit', {'url': url, 'limit': limit})
                    return Response(body, {'url': url, 'final_url': r.url, 'status': r.status,
                                          'retrieved_at': datetime.now(timezone.utc).isoformat(),
                                          'sha256': hashlib.sha256(body).hexdigest(), 'bytes': len(body),
                                          'content_type': r.headers.get_content_type(), 'attempts': attempt+1,
                                          'etag': r.headers.get('ETag'), 'last_modified': r.headers.get('Last-Modified')})
            except HTTPError as exc:
                if exc.code not in [408, 429, 500, 502, 503, 504] or attempt == self.attempts-1:
                    raise CollectionError('http_error', f'HTTP {exc.code}', {'url': url, 'status': exc.code}) from exc
            except (URLError, TimeoutError) as exc:
                if attempt == self.attempts-1:
                    raise CollectionError('network_error', str(exc), {'url': url}) from exc
            finally:
                self.last = time.monotonic()
            time.sleep(min(4., 2.**attempt))
        raise AssertionError('Unreachable retry state')
