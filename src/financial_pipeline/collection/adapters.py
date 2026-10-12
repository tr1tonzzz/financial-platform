"""Adapters interpret official HTML; selection rules live in models, not adapters."""
from dataclasses import dataclass, field
from html.parser import HTMLParser
import json
import re
from urllib.parse import urljoin, urlsplit, parse_qs, urlencode, urlunsplit
from .models import CollectionError, publication_date


@dataclass
class Node:
    tag: str
    attrs: dict
    parent: object = None
    content: list = field(default_factory=list)

    def text(self):
        return ' '.join(' '.join(x.text() if isinstance(x, Node) else x for x in self.content).split())

    def has_class(self, name):
        return name in self.attrs.get('class', '').split()

    def ancestor(self, predicate):
        current = self.parent
        while current:
            if predicate(current):
                return current
            current = current.parent
        return None


class Tree(HTMLParser):
    VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}

    def __init__(self, body):
        super().__init__(convert_charrefs=True)
        self.root = Node('root', {})
        self.stack = [self.root]
        self.nodes = []
        self.feed(body.decode('utf-8-sig', errors='replace'))

    def handle_starttag(self, tag, attrs):
        node = Node(tag, dict(attrs), self.stack[-1])
        self.stack[-1].content.append(node)
        self.nodes.append(node)
        if tag not in self.VOID:
            self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    def handle_endtag(self, tag):
        for index in range(len(self.stack)-1, 0, -1):
            if self.stack[index].tag == tag:
                del self.stack[index:]
                break

    def handle_data(self, data):
        if self.stack[-1].tag not in ['script', 'style']:
            self.stack[-1].content.append(data)


def query_url(url, **values):
    parsed = urlsplit(url)
    query = parse_qs(parsed.query)
    query.update({k: [str(v)] for k, v in values.items()})
    return urlunsplit((parsed.scheme, parsed.netloc, parsed.path, urlencode(query, doseq=True), ''))


def initial_catalog(source, target):
    parameter = 'year' if source.get('adapter') == 'vinamilk' else source.get('year_parameter')
    return query_url(source['catalog_url'], **{parameter: target.year}) if parameter else source['catalog_url']


def parse_catalog(body, source, page_url):
    tree = Tree(body)
    kind = source.get('adapter', 'html')
    if kind == 'html':
        from .generic_html import parse_html_catalog
        return parse_html_catalog(tree, source, page_url)
    if kind not in ['vinamilk', 'hoaphat']:
        raise CollectionError('unsupported_adapter', 'Source adapter is not registered')
    found = {}
    for node in tree.nodes:
        if node.tag != 'a' or not node.attrs.get('href'):
            continue
        url = urljoin(page_url, node.attrs['href'])
        url = urlunsplit((*urlsplit(url)[:4], ''))
        if not urlsplit(url).path.lower().endswith('.pdf'):
            continue
        if kind == 'hoaphat':
            row = node.ancestor(lambda n: n.tag == 'div' and n.has_class('item'))
            if not row:
                continue
            if node.text().lower() == 'download':
                continue  # The same item has a named anchor; avoid generic duplicate metadata.
        else:
            row = node
        title = node.text()
        candidate = {'url': url, 'title': title, 'published_at': publication_date(row.text()),
                     'catalog_url': page_url, 'publication_date_evidence': row.text()[:500]}
        if url in found and found[url]['title'] != title:
            raise CollectionError('conflicting_duplicate_link', 'One PDF URL has conflicting titles within a catalog page', {'url': url})
        found[url] = candidate

    if kind == 'hoaphat':
        controls = [n for n in tree.nodes if n.has_class('pagination')]
        if len(controls) != 1:
            raise CollectionError('catalog_structure_changed', 'Expected one HPG pagination control')
        urls = []
        for n in tree.nodes:
            if n.tag == 'a' and n.ancestor(lambda p: p is controls[0]) and n.attrs.get('href'):
                url = urljoin(page_url, n.attrs['href'])
                p, base = urlsplit(url), urlsplit(source['catalog_url'])
                if p.scheme != 'https' or p.hostname != base.hostname or p.path.rstrip('/') != base.path.rstrip('/'):
                    raise CollectionError('invalid_pagination_link', 'Pagination escaped the registered catalog')
                params = parse_qs(p.query)
                if set(params) != {'page'} or len(params['page']) != 1 or not params['page'][0].isdigit() or int(params['page'][0]) < 1:
                    raise CollectionError('invalid_pagination_link', 'Unsupported pagination parameters')
                urls.append(url)
        last = max([int(parse_qs(urlsplit(u).query)['page'][0]) for u in urls], default=1)
        current = int(parse_qs(urlsplit(page_url).query).get('page', ['1'])[0])
        page_count = max(last, current)
        return list(found.values()), urls, {'page': current, 'page_count': page_count, 'coverage_basis': 'observed_hpg_pagination_links'}

    # Next.js Flight payloads are JSON strings, never executed as JavaScript.
    payload = []
    for match in re.finditer(r'self\.__next_f\.push\((\[.*?\])\)</script>', body.decode('utf-8'), re.DOTALL):
        try:
            part = json.loads(match[1])
        except ValueError:
            continue
        if len(part) > 1 and part[0] == 1 and isinstance(part[1], str):
            payload.append(part[1])
    counts = {int(x) for x in re.findall(r'"pageCount"\s*:\s*(\d+)', ''.join(payload))}
    if len(counts) != 1:
        raise CollectionError('catalog_structure_changed', 'Missing/ambiguous VNM pageCount; do not assume complete coverage')
    page_count = max(1, next(iter(counts)))
    if page_count > source['max_pages']:
        raise CollectionError('catalog_page_limit', 'VNM pageCount exceeds the configured coverage limit')
    current = int(parse_qs(urlsplit(page_url).query).get('page', ['1'])[0])
    # page query was verified in the source site's pagination component.
    urls = [query_url(page_url, page=p) for p in range(2, page_count+1)]
    return list(found.values()), urls, {'page': current, 'page_count': page_count, 'coverage_basis': 'vnm_server_pageCount_and_verified_page_query'}
