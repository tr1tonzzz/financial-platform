"""Business and failure tests. All fixtures are synthetic; no company financial values."""
from dataclasses import replace
import hashlib
import json
from pathlib import Path
import sys
from urllib.error import HTTPError
import pytest
import pymupdf

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT/'src'))
from financial_pipeline.collection import ReportTarget, CollectionError, collect_report
from financial_pipeline.collection.models import classify, select_candidate
from financial_pipeline.collection.adapters import parse_catalog
from financial_pipeline.collection.service import discover
from financial_pipeline.collection.transport import Response, validate_url, CheckedRedirect, HttpClient

TARGET = ReportTarget('FIX', 2025)
SOURCE = {'adapter': 'hoaphat', 'catalog_url': 'https://catalog.test/financial', 'legal_name': 'Công ty kiểm thử',
          'catalog_hosts': ['catalog.test'], 'download_hosts': ['files.test'], 'max_pages': 10}
TITLE = 'BCTC hợp nhất năm 2025 sau kiểm toán'
URL = 'https://files.test/report.pdf'


def row(title=TITLE, url=URL, date='27/03/2026'):
    return f'<div class="item"><div class="name"><a href="{url}">{title}</a></div><div class="time">{date}</div><a href="{url}">Download</a></div>'


def catalog(*rows, pages=()):
    links = ''.join(f'<a href="?page={p}">{p}</a>' for p in pages)
    return ('<html>'+''.join(rows)+'<ul class="pagination">'+links+'</ul></html>').encode()


def flight(count):
    payload = [1, f'pagination:["$","$L1",null,{{"pageCount":{count}}}]']
    return ('<script>self.__next_f.push('+json.dumps(payload)+')</script>').encode()


def pdf(pages=1):
    with pymupdf.open() as doc:
        for _ in range(pages):
            doc.new_page()
        return doc.tobytes()


class FakeClient:
    def __init__(self, responses):
        self.responses, self.calls = responses, []

    def fetch(self, url, hosts, limit):
        validate_url(url, hosts)
        self.calls.append(url)
        body = self.responses[url]
        if isinstance(body, Exception):
            raise body
        return Response(body, {'url': url, 'final_url': url, 'status': 200, 'bytes': len(body),
                               'sha256': hashlib.sha256(body).hexdigest(), 'retrieved_at': 'synthetic time',
                               'content_type': 'application/pdf' if url.endswith('.pdf') else 'text/html'})


@pytest.mark.parametrize('title,url,reason', [
    ('BCTC hợp nhất Quý I năm 2025 đã kiểm toán', URL, 'not_annual'),
    ('BCTC hợp nhất 6 tháng 2025 đã kiểm toán', URL, 'not_annual'),
    ('BCTC công ty mẹ năm 2025 đã kiểm toán', URL, 'separate_or_unknown_scope'),
    ('Giải trình BCTC hợp nhất năm 2025 đã kiểm toán', URL, 'supplement_or_notice'),
    ('BCTC hợp nhất năm 2025 chưa kiểm toán', URL, 'not_confirmed_audited_candidate'),
    ('BCTC hợp nhất năm 2025 đã soát xét', URL, 'not_confirmed_audited_candidate'),
    (TITLE, 'https://files.test/report_EN.pdf', 'other_language'),
    ('BCTC hợp nhất năm 2024 đã kiểm toán', URL, 'other_report_year'),
    ('BCTC hợp nhất năm 2024 và 2025 đã kiểm toán', URL, 'missing_or_ambiguous_report_year'),
    (TITLE, 'https://files.test/bctc-2024.pdf', 'conflicting_report_year'),
])
def test_reject_wrong_period_scope_assurance_language_and_year(title, url, reason):
    result = classify(title, url, TARGET)
    assert not result['eligible'] and result['reason'] == reason


def test_report_year_is_not_upload_year_and_rules_accept_other_requested_year():
    assert classify('27/03/2026 '+TITLE, 'https://files.test/2026/03/report.pdf', TARGET)['eligible']
    assert classify('BCTC hợp nhất năm 2024 đã kiểm toán', URL, replace(TARGET, year=2024))['eligible']


def test_audited_q4_catalog_card_remains_provisional_until_pdf_verifies_annual_period():
    label = '27/02/2026 2025 Q4 Báo cáo tài chính hợp nhất Đã soát xét/kiểm toán Xem'
    result = classify(label, 'https://files.test/BCTC_KIEM_TOAN_2025_VN.pdf', TARGET)
    assert result['eligible'] and result['catalog_period'] == 'Q4'
    assert result['requires_pdf_period_verification']
    assert not classify(label, 'https://files.test/BCTC_SOAT_XET_2025_VN.pdf', TARGET)['eligible']
    assert not classify(label, 'https://files.test/BCTC_KIEM_TOAN_Q4_2025_VN.pdf', TARGET)['eligible']


def test_duplicate_download_anchor_and_publication_date_in_nested_row():
    candidates, pages, coverage = parse_catalog(catalog(row(), pages=[2, 3]), SOURCE, SOURCE['catalog_url'])
    assert len(candidates) == 1 and candidates[0]['title'] == TITLE
    assert candidates[0]['published_at'] == '2026-03-27'
    assert len(pages) == 2 and coverage['page_count'] == 3


def test_vnm_server_page_count_drives_year_preserving_pagination():
    source = {**SOURCE, 'adapter': 'vinamilk'}
    url = 'https://catalog.test/financial?year=2025'
    body = f'<a href="{URL}">{TITLE}<button>Xem</button></a>'.encode()+flight(2)
    candidates, pages, _ = parse_catalog(body, source, url)
    assert len(candidates) == 1 and candidates[0]['title'].endswith('Xem')
    assert pages == ['https://catalog.test/financial?year=2025&page=2']
    with pytest.raises(CollectionError, match='pageCount'):
        parse_catalog(body.replace(flight(2), b''), source, url)
    with pytest.raises(CollectionError) as failure:
        parse_catalog(flight(1000000), source, url)
    assert failure.value.code == 'catalog_page_limit'


def test_incomplete_pagination_is_not_a_success():
    client = FakeClient({SOURCE['catalog_url']: catalog(row(), pages=[3]),
                         SOURCE['catalog_url']+'?page=3': catalog(row('BCTC hợp nhất năm 2023 đã kiểm toán', 'https://files.test/old.pdf'))})
    with pytest.raises(CollectionError) as failure:
        discover(TARGET, SOURCE, client)
    assert failure.value.code == 'incomplete_catalog'


def test_identical_responses_for_different_pages_are_not_complete_coverage():
    body = catalog(row(), pages=[2])
    client = FakeClient({SOURCE['catalog_url']: body, SOURCE['catalog_url']+'?page=2': body})
    with pytest.raises(CollectionError) as failure:
        discover(TARGET, SOURCE, client)
    assert failure.value.code == 'repeated_catalog_page'


def test_newest_date_without_explicit_revision_does_not_choose_report():
    candidate = dict(url=URL, title=TITLE, published_at='2026-03-27', metadata=classify(TITLE, URL, TARGET))
    newer = {**candidate, 'url': URL.replace('report', 'different'), 'published_at': '2026-04-01'}
    with pytest.raises(CollectionError) as failure:
        select_candidate([candidate, newer])
    assert failure.value.code == 'ambiguous_report_versions'
    revised_title = TITLE+' (bản điều chỉnh)'
    revised = {**newer, 'title': revised_title, 'metadata': classify(revised_title, newer['url'], TARGET)}
    assert select_candidate([candidate, revised])[0] == revised
    with pytest.raises(CollectionError):
        select_candidate([candidate, {**revised, 'published_at': None}])


def test_duplicate_rejected_historical_metadata_does_not_mask_target_conflict():
    historic = 'https://files.test/old.pdf'
    client = FakeClient({SOURCE['catalog_url']: catalog(row(), row('BCTC hợp nhất năm 2016 đã kiểm toán', historic), pages=[2]),
                         SOURCE['catalog_url']+'?page=2': catalog(row('BCTC hợp nhất năm 2017 đã kiểm toán', historic))})
    candidates, summary = discover(TARGET, SOURCE, client)
    assert summary['complete'] and summary['non_target_duplicate_conflicts'] == 1
    assert select_candidate(candidates)[0]['url'] == URL
    client.responses[SOURCE['catalog_url']+'?page=2'] = catalog(row(TITLE, URL, '28/03/2026'))
    with pytest.raises(CollectionError) as failure:
        discover(TARGET, SOURCE, client)
    assert failure.value.code == 'conflicting_duplicate_link'


def test_collects_only_target_and_preserves_hash_versions(tmp_path):
    other = 'https://files.test/quarter.pdf'
    client = FakeClient({SOURCE['catalog_url']: catalog(row(), row('BCTC hợp nhất Quý I năm 2025 chưa kiểm toán', other)), URL: pdf()})
    registry = {'schema_version': 1, 'sources': {'FIX': SOURCE}}
    first = collect_report(TARGET, registry, tmp_path, client)
    second = collect_report(TARGET, registry, tmp_path, client)
    assert first.source['sha256'] == second.source['sha256'] and other not in client.calls
    assert len(list((tmp_path/'data/raw').glob('*.pdf'))) == 1
    assert first.source['acquisition_mode'] == 'automatic_official_catalog'
    client.responses[URL] = pdf(2)
    third = collect_report(TARGET, registry, tmp_path, client)
    assert third.source['sha256'] != first.source['sha256'] and third.source['pdf_pages'] == 2
    assert len(list((tmp_path/'data/raw').glob('*.pdf'))) == 2


@pytest.mark.parametrize('bad_pdf', [b'<html>blocked</html>', b'%PDF-corrupt'])
def test_failed_pdf_never_becomes_collected_data(tmp_path, bad_pdf):
    client = FakeClient({SOURCE['catalog_url']: catalog(row()), URL: bad_pdf})
    with pytest.raises(CollectionError):
        collect_report(TARGET, {'schema_version': 1, 'sources': {'FIX': SOURCE}}, tmp_path, client)
    assert not list((tmp_path/'data/raw').glob('*.pdf'))
    observation = json.loads(next((tmp_path/'data/collections/FIX-2025').glob('*.json')).read_text(encoding='utf-8'))
    assert observation['status'] in ['not_pdf', 'unreadable_pdf']


def test_http_failure_keeps_partial_coverage_and_does_not_fetch_pdf(tmp_path):
    client = FakeClient({SOURCE['catalog_url']: catalog(row(), pages=[2]),
                         SOURCE['catalog_url']+'?page=2': CollectionError('http_error', 'HTTP 503')})
    with pytest.raises(CollectionError):
        collect_report(TARGET, {'schema_version': 1, 'sources': {'FIX': SOURCE}}, tmp_path, client)
    observation = json.loads(next((tmp_path/'data/collections/FIX-2025').glob('*.json')).read_text(encoding='utf-8'))
    assert observation['status'] == 'http_error' and observation['discovery']['pages_visited'] == 1
    assert not observation['discovery']['complete'] and URL not in client.calls


def test_redirect_and_unregistered_hosts_fail_before_download():
    for url in ['http://files.test/a.pdf', 'https://other.test/a.pdf', 'https://user:password@files.test/a.pdf']:
        with pytest.raises(CollectionError):
            validate_url(url, ['files.test'])
    with pytest.raises(CollectionError):
        CheckedRedirect(['files.test']).redirect_request(None, None, 302, '', {}, 'https://other.test/a.pdf')


def test_no_match_and_ambiguous_match_do_not_fetch_any_pdf(tmp_path):
    registry = {'schema_version': 1, 'sources': {'FIX': SOURCE}}
    client = FakeClient({SOURCE['catalog_url']: catalog(row('BCTC hợp nhất năm 2024 đã kiểm toán'))})
    with pytest.raises(CollectionError) as missing:
        collect_report(TARGET, registry, tmp_path, client)
    assert missing.value.code == 'report_not_found' and client.calls == [SOURCE['catalog_url']]
    client.calls.clear()
    client.responses[SOURCE['catalog_url']] = catalog(row(), row(TITLE, 'https://files.test/second.pdf', '28/03/2026'))
    with pytest.raises(CollectionError) as ambiguous:
        collect_report(TARGET, registry, tmp_path, client)
    assert ambiguous.value.code == 'ambiguous_report_versions' and client.calls == [SOURCE['catalog_url']]


def test_corrupt_existing_pdf_is_not_overwritten(tmp_path):
    body = pdf()
    raw = tmp_path/'data/raw'/(hashlib.sha256(body).hexdigest()+'.pdf')
    raw.parent.mkdir(parents=True)
    raw.write_bytes(b'corrupt existing data')
    client = FakeClient({SOURCE['catalog_url']: catalog(row()), URL: body})
    with pytest.raises(CollectionError) as failure:
        collect_report(TARGET, {'schema_version': 1, 'sources': {'FIX': SOURCE}}, tmp_path, client)
    assert failure.value.code == 'existing_pdf_corrupt' and raw.read_bytes() == b'corrupt existing data'


def test_unregistered_company_has_a_failure_record_not_a_manual_pdf_fallback(tmp_path):
    with pytest.raises(CollectionError) as failure:
        collect_report(TARGET, {'schema_version': 1, 'sources': {}}, tmp_path, FakeClient({}))
    assert failure.value.code == 'unregistered_company'
    saved = json.loads(next((tmp_path/'data/collections/FIX-2025').glob('*.json')).read_text(encoding='utf-8'))
    assert saved['status'] == 'unregistered_company' and not (tmp_path/'data/raw').exists()


def test_http_retries_transient_failure_but_not_not_found(monkeypatch):
    import financial_pipeline.collection.transport as transport
    attempts = []
    class Opener:
        def open(self, request, timeout):
            attempts.append(request.full_url)
            code = 503 if len(attempts) < 3 else 404
            raise HTTPError(request.full_url, code, 'synthetic', {}, None)
    monkeypatch.setattr(transport, 'build_opener', lambda *args: Opener())
    monkeypatch.setattr(transport.time, 'sleep', lambda seconds: None)
    with pytest.raises(CollectionError) as failure:
        HttpClient().fetch(URL, ['files.test'], 1000)
    assert len(attempts) == 3 and failure.value.details['status'] == 404
    attempts[:] = ['already', 'already']
    with pytest.raises(CollectionError):
        HttpClient().fetch(URL, ['files.test'], 1000)
    assert len(attempts) == 3  # One request for a permanent 404.
