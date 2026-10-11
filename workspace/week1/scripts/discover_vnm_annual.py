"""Inspect official VNM catalog and its public frontend assets, using HTTP only."""
import json
import re
import sys
import hashlib
from pathlib import Path
from urllib.request import Request, urlopen
from datetime import datetime, timezone
from html.parser import HTMLParser
from urllib.parse import urljoin


class Links(HTMLParser):
    """Read catalog anchors only; no PDF text extraction dependency."""
    def __init__(self, base):
        super().__init__()
        self.base, self.links, self.current = base, [], None

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if tag == 'a' and values.get('href'):
            self.current = {'url': urljoin(self.base, values['href']), 'text': '', 'attributes': values}

    def handle_data(self, data):
        if self.current is not None:
            self.current['text'] += data + ' '

    def handle_endtag(self, tag):
        if tag == 'a' and self.current is not None:
            self.current['text'] = ' '.join(self.current['text'].split())
            self.links.append(self.current)
            self.current = None

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'workspace/week1/data/vnm-2025'
CATALOG = 'https://www.vinamilk.com.vn/investor/reports/financial'


def fetch(url, path):
    started = datetime.now(timezone.utc).isoformat()
    with urlopen(Request(url, headers={'User-Agent': 'FinancialAnalysisPlatform/0.1'}), timeout=40) as res:
        body = res.read()
        path.write_bytes(body)
        return {'url': url, 'retrieved_at': started, 'status': res.status, 'final_url': res.url, 'bytes': len(body), 'path': str(path.relative_to(ROOT))}


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    OUT.mkdir(parents=True, exist_ok=True)
    events = [fetch(CATALOG, OUT / 'catalog.html')]
    year_url = CATALOG + '?year=2025'
    events.append(fetch(year_url, OUT / 'catalog-2025.html'))
    parser = Links(year_url)
    parser.feed((OUT / 'catalog-2025.html').read_text(encoding='utf-8'))
    links = [x for x in parser.links if '.pdf' in x['url'].lower()]
    (OUT / 'discovered-pdf-links-2025.json').write_text(json.dumps(links, ensure_ascii=False, indent=2), encoding='utf-8')
    candidates = []
    seen = set()
    for link in links:
        if link['url'] in seen:
            continue
        seen.add(link['url'])
        name = link['url'].rsplit('/', 1)[-1].upper()
        selected = '2025' in name and 'HOP_NHAT' in name and 'KIEM_TOAN' in name and 'báo cáo tài chính hợp nhất' in link['text'].lower()
        candidates.append({**link, 'selected': selected, 'reason': 'Candidate annual audited consolidated; verify PDF by Paddle before confirming' if selected else 'Not the audited consolidated annual candidate (quarterly/separate/other document)'})
    selected = [x for x in candidates if x['selected']]
    if len(selected) != 1:
        raise RuntimeError(f'Expected one annual candidate, found {len(selected)}')
    item = selected[0]
    filename = item['url'].rsplit('/', 1)[-1]
    event = fetch(item['url'], OUT / filename)
    events.append(event)
    body = (OUT / filename).read_bytes()
    if not body.startswith(b'%PDF-'):
        raise ValueError('Response is not PDF')
    digest = hashlib.sha256(body).hexdigest()
    (OUT / f'{digest}.pdf').write_bytes(body)
    date = re.match(r'(\d{2})/(\d{2})/(\d{4})', item['text'])
    source = {**event, 'ticker_candidate': 'VNM', 'year_candidate': 2025, 'scope_candidate': 'consolidated', 'catalog_url': year_url, 'catalog_sha256': hashlib.sha256((OUT / 'catalog-2025.html').read_bytes()).hexdigest(), 'catalog_anchor': item['text'], 'published_at': f'{date[3]}-{date[2]}-{date[1]}' if date else None, 'publication_evidence': 'date displayed in the selected catalog anchor', 'sha256': digest, 'filename': filename, 'context_status': 'pending_paddle_verification', 'dataset_partition': 'development', 'document_family_id': 'VNM-consolidated-FY2025', 'independent_test_eligible': False}
    (OUT / 'source.json').write_text(json.dumps(source, ensure_ascii=False, indent=2), encoding='utf-8')
    (OUT / 'filtered-documents.json').write_text(json.dumps(candidates, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({'pdf_links':len(candidates),'selected':source},ensure_ascii=False,indent=2))
    (OUT / 'discovery-requests.json').write_text(json.dumps(events, ensure_ascii=False, indent=2), encoding='utf-8')


if __name__ == '__main__':
    main()
