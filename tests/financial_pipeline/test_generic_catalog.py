"""One adapter across unrelated catalog layouts; no real company data."""
import pytest
from financial_pipeline.collection import CollectionError, collect_report
from financial_pipeline.collection.adapters import initial_catalog, parse_catalog
from financial_pipeline.collection.service import discover
from test_collection import TARGET, TITLE, URL, SOURCE, FakeClient, pdf


GENERIC = {**SOURCE, 'adapter': 'html', 'pagination': {'mode': 'single_page'}}


@pytest.mark.parametrize('tag', ['tr', 'li', 'article'])
def test_common_containers_relative_uppercase_pdf_and_duplicate_buttons(tag, tmp_path):
    link = 'https://files.test/reports/annual.PDF?download=1'
    body = f'<{tag}><a href="{link}#page=1">{TITLE}</a><time datetime="2026-03-27">27/03/2026</time><a href="{link}">Download</a></{tag}>'.encode()
    entries, pages, coverage = parse_catalog(body, GENERIC, SOURCE['catalog_url'])
    assert len(entries) == 1 and entries[0]['published_at'] == '2026-03-27'
    assert entries[0]['url'] == link and not pages and coverage['page_count'] == 1
    result = collect_report(TARGET, {'schema_version': 1, 'sources': {'FIX': GENERIC}}, tmp_path,
                            FakeClient({SOURCE['catalog_url']: body, link: pdf()}))
    assert result.source['discovery']['complete'] and result.source['catalog_candidate']['eligible']
    assert result.source['catalog_context'] == TITLE


def test_div_cards_and_icon_title_are_reused_without_company_adapter():
    body = f'<div class="report"><a href="{URL}" title="{TITLE}"><svg></svg></a><time datetime="2026-03-27"></time><a href="{URL}">Tải về</a></div>'.encode()
    source = {**GENERIC, 'entry': {'tag': 'div', 'class': 'report'}}
    entries, _, _ = parse_catalog(body, source, SOURCE['catalog_url'])
    assert len(entries) == 1 and entries[0]['title'] == TITLE
    assert entries[0]['published_at'] == '2026-03-27'


def test_filename_is_metadata_evidence_when_anchor_is_only_download():
    url = 'https://files.test/BCTC_hop_nhat_nam_2025_da_kiem_toan.pdf'
    entries, _, _ = parse_catalog(f'<a href="{url}">Download</a>'.encode(), GENERIC, SOURCE['catalog_url'])
    from financial_pipeline.collection.models import classify
    assert classify(entries[0]['title'], url, TARGET)['eligible']
    assert entries[0]['anchor_text'] == 'Download' and entries[0]['filename_evidence']


def test_relative_pdf_links_and_default_html_adapter(tmp_path):
    source = {key: value for key, value in GENERIC.items() if key != 'adapter'}
    source['download_hosts'] = ['catalog.test']
    body = f'<li><a href="../reports/annual.PDF?download=1#page=2">{TITLE}</a></li>'.encode()
    expected = 'https://catalog.test/reports/annual.PDF?download=1'
    result = collect_report(TARGET, {'schema_version': 1, 'sources': {'FIX': source}}, tmp_path,
                            FakeClient({SOURCE['catalog_url']: body, expected: pdf()}))
    assert result.source['url'] == expected and result.source['discovery']['complete']


@pytest.mark.parametrize('start', [0, 1])
def test_custom_page_parameter_zero_based_and_year_filter(start):
    source = {**GENERIC, 'year_parameter': 'year',
              'pagination': {'mode': 'numbered', 'parameter': 'p', 'start': start, 'container': {'tag': 'nav', 'class': 'pages'}}}
    first = initial_catalog(source, TARGET)
    second = first+f'&p={start+1}'
    body = f'<li><a href="{URL}">{TITLE}</a></li><nav class="pages"><a href="?year=2025&p={start+1}">Next</a></nav>'.encode()
    last = b'<nav class="pages"></nav><p>End of catalog</p>'
    candidates, coverage = discover(TARGET, source, FakeClient({first: body, second: last}))
    assert coverage['pages_visited'] == coverage['expected_pages'] == 2
    assert coverage['complete'] and candidates[0]['metadata']['eligible']


@pytest.mark.parametrize('body', [b'<div class="pagination"><a href="?page=2">2</a></div>',
                                  b'<a href="?page=2" rel="next">Next</a>'])
def test_single_page_does_not_hide_obvious_pagination(body):
    with pytest.raises(CollectionError) as failure:
        parse_catalog(body, GENERIC, SOURCE['catalog_url'])
    assert failure.value.code == 'catalog_pagination_unconfigured'


@pytest.mark.parametrize('link', ['https://other.test/financial?page=2', '?year=2024&page=2', '?year=2025&page=2&page=3', '?year=2025&page=-1'])
def test_numbered_pagination_rejects_escape_filter_change_and_invalid_numbers(link):
    source = {**GENERIC, 'pagination': {'mode': 'numbered'}}
    with pytest.raises(CollectionError):
        parse_catalog(f'<nav class="pagination"><a href="{link}">Next</a></nav>'.encode(), source, SOURCE['catalog_url']+'?year=2025')


def test_metadata_cannot_be_borrowed_from_another_report(tmp_path):
    body = f'<div class="report"><a href="{URL}">{TITLE}</a><a href="https://files.test/2024.pdf">BCTC năm 2024</a></div>'.encode()
    with pytest.raises(CollectionError) as failure:
        parse_catalog(body, {**GENERIC, 'entry': {'class': 'report'}}, SOURCE['catalog_url'])
    assert failure.value.code == 'ambiguous_catalog_entry'
    client = FakeClient({SOURCE['catalog_url']: b'<a href="https://files.test/document.pdf">Download</a>'})
    with pytest.raises(CollectionError) as failure:
        collect_report(TARGET, {'schema_version': 1, 'sources': {'FIX': GENERIC}}, tmp_path, client)
    assert failure.value.code == 'report_not_found' and len(client.calls) == 1


def test_generic_sources_must_declare_coverage_and_do_not_hide_missing_controls():
    for source in [{**GENERIC, 'pagination': {}}, {**GENERIC, 'pagination': {'mode': 'numbered'}}]:
        with pytest.raises(CollectionError):
            parse_catalog(b'<html></html>', source, SOURCE['catalog_url'])
