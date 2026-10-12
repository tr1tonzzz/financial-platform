"""HTML PDF catalogs with configurable entry context and numbered pagination."""
from datetime import date
import re
from urllib.parse import parse_qs, unquote, urljoin, urlsplit, urlunsplit
from .models import CollectionError, fold


def pdf_url(href, base):
    parsed = urlsplit(urljoin(base, href))
    return urlunsplit((*parsed[:4], '')) if unquote(parsed.path).lower().endswith('.pdf') else None


def matches(node, rule):
    if not isinstance(rule, dict) or not rule or set(rule)-{'tag', 'class'} or not all(isinstance(value, str) and value for value in rule.values()):
        raise CollectionError('invalid_source_config', 'HTML entry/pagination selector uses tag and/or class')
    return (not rule.get('tag') or node.tag == rule['tag']) and (not rule.get('class') or node.has_class(rule['class']))


def financial_label(text):
    value = fold(text)
    return any(part in value for part in ['bctc', 'bao cao tai chinh', 'financial statement'])


def published(text):
    result = set()
    for day, month, year in re.findall(r'\b(\d{1,2})[/.-](\d{1,2})[/.-](\d{4})\b', text):
        try:
            result.add(date(int(year), int(month), int(day)).isoformat())
        except ValueError:
            pass
    for value in re.findall(r'\b\d{4}-\d{2}-\d{2}\b', text):
        try:
            result.add(date.fromisoformat(value).isoformat())
        except ValueError:
            pass
    return next(iter(result)) if len(result) == 1 else None


def parse_html_catalog(tree, source, page_url):
    anchors, urls_by_node, counts_by_node = [], {}, {}
    for node in tree.nodes:
        if node.tag != 'a' or not node.attrs.get('href'):
            continue
        url = pdf_url(node.attrs['href'], page_url)
        if not url:
            continue
        anchors.append((node, url))
        ancestor = node
        while ancestor:
            urls_by_node.setdefault(id(ancestor), set()).add(url)
            counts_by_node[id(ancestor)] = counts_by_node.get(id(ancestor), 0)+1
            ancestor = ancestor.parent

    def container(anchor, url):
        rule = source.get('entry')
        if rule:
            row = anchor.ancestor(lambda node: matches(node, rule))
            if not row or urls_by_node.get(id(row)) != {url}:
                raise CollectionError('ambiguous_catalog_entry', 'Configured entry is missing or groups different PDFs')
            return row
        row = anchor.ancestor(lambda node: node.tag in {'tr', 'li', 'article'} and urls_by_node.get(id(node)) == {url})
        if row:
            return row
        row = anchor.ancestor(lambda node: node.tag == 'div' and urls_by_node.get(id(node)) == {url}
                              and (counts_by_node[id(node)] > 1 or (published(node.text()) and financial_label(node.text()))))
        return row or anchor

    found = {}
    for anchor, url in anchors:
        row = container(anchor, url)
        context = row.text()
        # Icon links often carry their business label in title/aria-label.
        descriptions = []
        for node, other_url in anchors:
            if other_url == url and (node is row or node.ancestor(lambda parent: parent is row)):
                descriptions.extend(node.attrs.get(key, '') for key in ['title', 'aria-label'])
        context = ' '.join([context, *dict.fromkeys(value for value in descriptions if value and value not in context)]).strip()
        title = re.sub(r'\b(?:\d{1,2}[/.-]\d{1,2}[/.-]\d{4}|\d{4}-\d{2}-\d{2})\b', ' ', context)
        title = re.sub(r'\b(?:download|tải về|xem)\b', ' ', title, flags=re.I)
        filename = re.sub(r'[_-]+', ' ', unquote(urlsplit(url).path.rsplit('/', 1)[-1]))
        if not financial_label(title):
            title = title+' '+filename
        date_text = context
        for node in tree.nodes:
            if node.tag == 'time' and node.ancestor(lambda parent: parent is row):
                date_text += ' '+node.attrs.get('datetime', '')
        candidate = {'url': url, 'title': ' '.join(title.split()), 'published_at': published(date_text),
                     'catalog_url': page_url, 'publication_date_evidence': date_text[:500],
                     'anchor_text': anchor.text(), 'context_text': context, 'filename_evidence': filename}
        previous = found.get(url)
        if previous and any(previous[key] != candidate[key] for key in ['title', 'published_at']):
            raise CollectionError('conflicting_duplicate_link', 'One PDF has contradictory HTML entry metadata', {'url': url})
        found[url] = candidate

    pagination = source.get('pagination', {})
    mode = pagination.get('mode')
    if mode == 'single_page':
        visible_controls = any(any(node.has_class(name) for name in ['pagination', 'pager', 'paging'])
                               or 'next' in node.attrs.get('rel', '').lower().split() for node in tree.nodes)
        if visible_controls:
            raise CollectionError('catalog_pagination_unconfigured', 'Pagination is visible; single_page cannot prove coverage')
        return list(found.values()), [], {'page': 1, 'page_count': 1, 'coverage_basis': 'registered_single_page_catalog'}
    if mode != 'numbered':
        raise CollectionError('invalid_source_config', 'Generic HTML requires pagination mode single_page or numbered')
    parameter, start = pagination.get('parameter', 'page'), pagination.get('start', 1)
    if not isinstance(parameter, str) or not re.fullmatch(r'[A-Za-z][A-Za-z0-9_-]*', parameter) or type(start) is not int or start not in [0, 1]:
        raise CollectionError('invalid_source_config', 'Pagination parameter/start is invalid')
    rule = pagination.get('container', {'class': 'pagination'})
    controls = [node for node in tree.nodes if matches(node, rule)]
    if not controls:
        raise CollectionError('catalog_structure_changed', 'Configured pagination control is missing')
    parsed = urlsplit(page_url)
    current_query = parse_qs(parsed.query, keep_blank_values=True)
    def page_number(query):
        values = query.get(parameter, [str(start)])
        if len(values) != 1 or not values[0].isdigit() or int(values[0]) < start:
            raise CollectionError('invalid_pagination_link', 'Invalid numbered page parameter')
        return int(values[0])-start+1
    current = page_number(current_query)
    fixed = {key: value for key, value in current_query.items() if key != parameter}
    links = set()
    maximum = current
    for node in tree.nodes:
        if node.tag != 'a' or not node.attrs.get('href') or not node.ancestor(lambda parent: any(parent is control for control in controls)):
            continue
        link = urlsplit(urljoin(page_url, node.attrs['href']))
        query = parse_qs(link.query, keep_blank_values=True)
        if link.scheme != 'https' or link.hostname != parsed.hostname or link.path.rstrip('/') != parsed.path.rstrip('/'):
            raise CollectionError('invalid_pagination_link', 'Pagination escaped the registered catalog')
        if {key: value for key, value in query.items() if key != parameter} != fixed:
            raise CollectionError('invalid_pagination_link', 'Pagination changed the catalog filters')
        maximum = max(maximum, page_number(query))
        links.add(urlunsplit((*link[:4], '')))
    return list(found.values()), sorted(links), {'page': current, 'page_count': maximum,
        'pagination_parameter': parameter, 'pagination_start': start, 'coverage_basis': 'observed_registered_html_pagination'}
