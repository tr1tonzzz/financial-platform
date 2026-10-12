"""Content-based statement/column/row discovery. No company, page or pixel templates."""
from decimal import Decimal
import json
from pathlib import Path
import re
import unicodedata
from .normalization import UNIT_MULTIPLIERS as MULTIPLIERS, monetary_unit

RULES = {
    'net_income_total': ('income_statement', '60', ['Lợi nhuận sau thuế']),
    'cfo': ('cash_flow_statement', '20', ['Lưu chuyển tiền thuần từ hoạt động kinh doanh',
                                       'Tiền thuần từ hoạt động kinh doanh']),
    'cash_equivalents': ('balance_sheet', '110', ['Tiền và các khoản tương đương tiền', 'Tiền và tương đương tiền']),
    'total_assets': ('balance_sheet', '270', ['Tổng tài sản', 'Tổng cộng tài sản']),
    'total_liabilities': ('balance_sheet', '300', ['Nợ phải trả']),
    'total_equity': ('balance_sheet', '400', ['Vốn chủ sở hữu']),
}
TITLES = {
    'balance_sheet': ['Bảng cân đối kế toán', 'Báo cáo tình hình tài chính'],
    'income_statement': ['Báo cáo kết quả hoạt động kinh doanh', 'Báo cáo kết quả kinh doanh'],
    'cash_flow_statement': ['Báo cáo lưu chuyển tiền tệ'],
}


def norm(text):
    text = unicodedata.normalize('NFD', text.lower().replace('đ', 'd'))
    return ''.join(c for c in text if c.isalnum() and not unicodedata.combining(c))


def center(entry):
    x0, y0, x1, y1 = entry['bbox']
    return (x0 + x1) / 2, (y0 + y1) / 2


def amount(raw):
    text = raw.strip()
    if not re.fullmatch(r'(?:-?(?:\d+|\d{1,3}(?:[.,]\d{3})+)|\((?:\d+|\d{1,3}(?:[.,]\d{3})+)\))', text):
        return None
    value = int(text.strip('()').replace('.', '').replace(',', ''))
    return -value if text.startswith('(') else value


def header_entries(page):
    return [e for e in page['entries'] if e['bbox'][1] < page['image_height'] * .30]


def classify(page):
    headers = [norm(e['text']) for e in header_entries(page)]
    if any(t.startswith(norm('Thuyết minh')) for t in headers):
        return None
    kinds = [kind for kind, aliases in TITLES.items() if any(t.startswith(norm(a)) for t in headers for a in aliases)]
    return kinds[0] if len(kinds) == 1 else None


def unit(page):
    hits = []
    for e in header_entries(page):
        try:
            value = monetary_unit(e['text'])
        except ValueError:
            return None, []
        if value:
            hits.append((value, e))
    distinct = {v for v, _ in hits}
    return (next(iter(distinct)), [e for _, e in hits]) if len(distinct) == 1 else (None, [])


def columns(page, kind, year):
    candidates = {'current': [], 'comparative': []}
    for e in header_entries(page):
        text = norm(e['text'])
        if len(text) > 40:
            continue
        current = comparative = False
        if kind == 'balance_sheet':
            current = text in [f'3112{year}', f'3112nam{year}', 'socuoinam', 'cuoinam', 'socuoiky', 'cuoiky']
            comparative = text in [f'11{year}', f'0101{year}', f'3112{year-1}', 'sodaunam', 'daunam', 'sodauky', 'dauky']
        else:
            current = text in [str(year), f'nam{year}', 'namnay', 'namhientai']
            comparative = text in [str(year-1), f'nam{year-1}', 'namtruoc']
        if current:
            candidates['current'].append(e)
        if comparative:
            candidates['comparative'].append(e)
    result = {}
    for role, entries in candidates.items():
        if not entries:
            raise ValueError('No ' + role + ' column header')
        xs = [center(e)[0] for e in entries]
        if max(xs) - min(xs) > page['image_width'] * .08:
            raise ValueError('Conflicting ' + role + ' column headers')
        result[role] = {'x': sum(xs) / len(xs), 'entries': entries}
    if abs(result['current']['x'] - result['comparative']['x']) < page['image_width'] * .08:
        raise ValueError('Columns are not spatially distinct')
    return result


def extract_row(page, code, aliases, cols):
    anchors = [e for e in page['entries'] if e['text'].strip() == code]
    if not anchors:
        anchors = [e for e in page['entries'] if re.search(r'\s'+re.escape(code)+r'$', e['text'].strip())
                   and any(norm(a) in norm(e['text']) for a in aliases)]
    if len(anchors) != 1:
        raise ValueError('Missing/ambiguous row code ' + code)
    anchor = anchors[0]
    _, y = center(anchor)
    height = anchor['bbox'][3] - anchor['bbox'][1]
    left = min(cols['current']['x'], cols['comparative']['x'])
    labels = sorted([e for e in page['entries'] if center(e)[0] < left - abs(cols['current']['x']-cols['comparative']['x']) * .45
                     and any(c.isalpha() for c in e['text'])
                     and -height * 1.8 < center(e)[1] - y < height * 1.8], key=lambda e: center(e)[1])
    label = ' '.join(e['text'] for e in labels)
    if not any(norm(a) in norm(label) for a in aliases):
        raise ValueError('Business label not matched: ' + label)
    spacing = abs(cols['current']['x'] - cols['comparative']['x'])
    numeric = []
    for e in page['entries']:
        if abs(center(e)[1] - y) > max(height, e['bbox'][3] - e['bbox'][1]) * .75:
            continue
        if e['bbox'][0] <= anchor['bbox'][2] or center(e)[0] < left - spacing * .45:
            continue
        if amount(e['text']) is not None:
            numeric.append({**e, 'selection_x': center(e)[0], 'token_index': None, 'bbox_precision': 'single_region'})
        else:
            tokens = e['text'].split()
            right = max(cols['current']['x'], cols['comparative']['x'])
            if len(tokens) == 2 and all(amount(t) is not None for t in tokens) and e['bbox'][0] < left and e['bbox'][2] > right:
                for i, token in enumerate(tokens):
                    numeric.append({**e, 'text': token, 'selection_x': sorted([left, right])[i],
                                    'token_index': i, 'bbox_precision': 'whole_merged_row'})
    current = [e for e in numeric if abs(e['selection_x'] - cols['current']['x']) < spacing * .45]
    if len(current) != 1:
        raise ValueError('Missing/ambiguous current-column value')
    return current[0], anchor, labels


def document_context(pages, source):
    text = norm(' '.join(e['text'] for p in pages for e in p['entries']))
    year = source['fiscal_year']
    checks = {'issuer_name': norm(source['expected_legal_name']) in text,
              'consolidated': 'hopnhat' in text,
              'audit': 'baocaokiemtoandoclap' in text,
              'annual': bool(re.search(r'(?:chonam(?:taichinh)?|nam(?:taichinh)?ketthuc)(?:ketthuc)?(?:vaongay|ngay)?(?:31thang12|3112)?(?:nam)?'+str(year), text)),
              'calendar_year': bool(re.search(r'(?:kyketoannam|namtaichinh|namketoan|niendoketoan).{0,180}(?:ngay)?0?1th[a-z]{3}0?1.{0,120}(?:ngay)?31thang12', text))}
    return {'checks': checks, 'verified': all(checks.values())}


def parse_report(pages, source):
    context = document_context(pages, source)
    found = {metric: [] for metric in RULES}
    decisions = []
    for page in pages:
        kind = classify(page)
        if kind is None:
            continue
        decision = {'pdf_page': page['pdf_page_index'] + 1, 'statement_type': kind, 'errors': []}
        raw_unit, unit_entries = unit(page)
        try:
            if not raw_unit:
                raise ValueError('Missing/ambiguous statement unit')
            cols = columns(page, kind, source['fiscal_year'])
        except ValueError as exc:
            decision['errors'].append(str(exc))
            decisions.append(decision)
            continue
        for metric, (expected_kind, code, aliases) in RULES.items():
            if kind != expected_kind or not any(e['text'].strip() == code or re.search(r'\s'+re.escape(code)+r'$',e['text'].strip()) for e in page['entries']):
                continue
            try:
                value, anchor, labels = extract_row(page, code, aliases, cols)
                evidence = {'pdf_page_index': page['pdf_page_index'], 'statement_type': kind,
                            'row_code': code, 'raw_value': value['text'], 'raw_unit': raw_unit,
                            'unit_multiplier': MULTIPLIERS[raw_unit],
                            'bbox': value['bbox'], 'bbox_precision': value['bbox_precision'],
                            'token_index': value['token_index'], 'confidence': value['confidence'],
                            'label_entries': [{k: e[k] for k in ['text', 'bbox', 'confidence']} for e in labels],
                            'current_headers': [{k: e[k] for k in ['text', 'bbox', 'confidence']} for e in cols['current']['entries']],
                            'comparative_headers': [{k: e[k] for k in ['text', 'bbox', 'confidence']} for e in cols['comparative']['entries']],
                            'unit_entries': [{k: e[k] for k in ['text', 'bbox', 'confidence']} for e in unit_entries],
                            'image_width': page['image_width'], 'image_height': page['image_height'],
                            'crop_sha256': value['crop_sha256'], 'recognizer_model_sha256': page['recognizer_model_sha256'],
                            'recognition_config_sha256': page['config_sha256']}
                found[metric].append({'value_vnd': str(amount(value['text']) * MULTIPLIERS[raw_unit]), 'evidence': evidence})
            except ValueError as exc:
                decision['errors'].append({'metric': metric, 'reason': str(exc)})
        decisions.append(decision)
    rows = []
    for metric, (kind, _, _) in RULES.items():
        choices = found[metric]
        values = {c['value_vnd'] for c in choices}
        valid = context['verified'] and len(values) == 1
        reason = None if valid else 'Document context unverified' if not context['verified'] else 'No unambiguous matching row/column/unit' if not choices else 'Conflicting values in document'
        instant = kind == 'balance_sheet'
        rows.append({'metric_code': metric, 'ticker': source['ticker'], 'fiscal_year': source['fiscal_year'],
                     'scope': 'consolidated', 'value_vnd': next(iter(values)) if valid else None,
                     'unit': 'VND', 'status': 'pending_review' if valid else 'missing_or_ambiguous', 'reason': reason,
                     'period_kind': 'instant' if instant else 'duration',
                     'period_start': None if instant else f'{source["fiscal_year"]}-01-01',
                     'period_end': None if instant else f'{source["fiscal_year"]}-12-31',
                     'as_of_date': f'{source["fiscal_year"]}-12-31' if instant else None,
                     'evidence': choices[0]['evidence'] if valid else None,
                     'alternative_locations': [{'pdf_page_index': c['evidence']['pdf_page_index'], 'value_vnd': c['value_vnd']} for c in choices]})
    return rows, {'context': context, 'pages_scanned': len(pages), 'statement_pages': decisions,
                  'present_count': sum(r['value_vnd'] is not None for r in rows), 'target_count': 6}
