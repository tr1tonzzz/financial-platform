"""Target contract and catalog metadata. Catalog fields are candidates, not PDF facts."""
from dataclasses import dataclass
from datetime import datetime
import re
import unicodedata
from urllib.parse import unquote, urlsplit


class CollectionError(Exception):
    def __init__(self, code, message, details=None):
        super().__init__(message)
        self.code = code
        self.details = details or {}


@dataclass(frozen=True)
class ReportTarget:
    ticker: str
    year: int
    period: str = 'annual'
    scope: str = 'consolidated'
    assurance: str = 'audited'
    language: str = 'vi'

    def __post_init__(self):
        if not re.fullmatch(r'[A-Z0-9]{1,12}', self.ticker) or not 1900 <= self.year <= 2100:
            raise ValueError('Invalid ticker/year')
        if (self.period, self.scope, self.assurance, self.language) != ('annual', 'consolidated', 'audited', 'vi'):
            raise ValueError('Current extraction contract supports annual consolidated audited Vietnamese reports only')


def fold(text):
    return ' '.join(''.join(c for c in unicodedata.normalize('NFD', text.lower())
                           if not unicodedata.combining(c)).replace('đ', 'd').split())


def publication_date(text):
    dates = []
    for m in re.finditer(r'\b(\d{1,2})/(\d{1,2})/(20\d{2})\b', text):
        try:
            dates.append(datetime(int(m[3]), int(m[2]), int(m[1])).date().isoformat())
        except ValueError:
            pass
    unique = set(dates)
    return next(iter(unique)) if len(unique) == 1 else None


def assurance(text):
    if any(s in text for s in ['chua kiem toan', 'chua soat xet', 'unaudited', 'non audited', 'non reviewed']):
        return 'unreviewed'
    audit = 'kiem toan' in text or 'audited' in text
    review = 'soat xet' in text or 'reviewed' in text
    return 'audited_or_reviewed' if audit and review else 'audited' if audit else 'reviewed' if review else 'unknown'


def classify(title, url, target):
    """Prefer the catalog label; never infer report year from upload directories/date."""
    title_clean = re.sub(r'\b\d{1,2}/\d{1,2}/20\d{2}\b', '', fold(title))
    filename = re.sub(r'[_\-]+', ' ', fold(unquote(urlsplit(url).path.rsplit('/', 1)[-1])))
    text = title_clean
    meta = {'catalog_period': 'unknown', 'scope': 'unknown', 'assurance': 'unknown',
            'language': 'vi', 'revision': False, 'requires_pdf_period_verification': True}
    if any(s in text for s in ['giai trinh', 'cong van', 'tong quan', 'cbtt', 'thong bao', 'nghi quyet', 'explanation', 'overview']):
        return {**meta, 'eligible': False, 'reason': 'supplement_or_notice'}
    if not any(s in text for s in ['bao cao tai chinh', 'bctc', 'financial statement']):
        return {**meta, 'eligible': False, 'reason': 'not_financial_statement'}
    years = set(re.findall(r'(?<!\d)(20\d{2})(?!\d)', text))
    if len(years) != 1:
        return {**meta, 'eligible': False, 'reason': 'missing_or_ambiguous_report_year'}
    meta['report_year'] = int(next(iter(years)))
    filename_years = set(re.findall(r'(?<!\d)(20\d{2})(?!\d)', filename))
    if filename_years and str(meta['report_year']) not in filename_years:
        return {**meta, 'eligible': False, 'reason': 'conflicting_report_year'}
    if meta['report_year'] != target.year:
        return {**meta, 'eligible': False, 'reason': 'other_report_year'}
    separate = any(s in text for s in ['rieng', 'cong ty me', 'separate'])
    consolidated = any(s in text for s in ['hop nhat', 'consolidated'])
    meta['scope'] = 'ambiguous' if separate and consolidated else 'separate' if separate else 'consolidated' if consolidated else 'unknown'
    if meta['scope'] != target.scope:
        return {**meta, 'eligible': False, 'reason': 'separate_or_unknown_scope'}
    english = bool(re.search(r'(?:\ben\b|\benglish\b|tieng anh)', filename+' '+text)) or ('financial statement' in text and not re.search(r'\bvn\b|tieng viet', filename+' '+text))
    meta['language'] = 'en' if english else 'vi'
    if meta['language'] != target.language:
        return {**meta, 'eligible': False, 'reason': 'other_language'}
    title_assurance, file_assurance = assurance(text), assurance(filename)
    meta['assurance'] = file_assurance if title_assurance == 'audited_or_reviewed' and file_assurance in ['audited', 'reviewed'] else title_assurance
    if meta['assurance'] == 'unknown' and file_assurance != 'unknown':
        meta['assurance'] = file_assurance
    if title_assurance in ['unreviewed', 'reviewed'] and file_assurance == 'audited':
        return {**meta, 'eligible': False, 'reason': 'conflicting_assurance'}
    if meta['assurance'] != target.assurance:
        return {**meta, 'eligible': False, 'reason': 'not_confirmed_audited_candidate'}
    quarter = re.search(r'\b(?:quy|qu\s*y|q)\s*(iv|iii|ii|i|[1-4])\b', text)
    half = any(s in text for s in ['6 thang', 'ban nien', 'half year', 'first half', 'h1'])
    if half:
        meta['catalog_period'] = 'half_year'
        return {**meta, 'eligible': False, 'reason': 'not_annual'}
    if quarter:
        number = {'i': 1, 'ii': 2, 'iii': 3, 'iv': 4}.get(quarter[1], int(quarter[1]) if quarter[1].isdigit() else 0)
        meta['catalog_period'] = f'Q{number}'
        # An audited Q4 catalog label can link to the audited full-year PDF.
        # Preserve the label and require annual period verification inside the PDF.
        if number != 4 or file_assurance != 'audited' or re.search(r'\b(?:quy|q)\s*(?:iv|[1-4])\b', filename):
            return {**meta, 'eligible': False, 'reason': 'not_annual'}
        selection = 'audited_q4_label_requires_annual_pdf_verification'
    else:
        meta['catalog_period'] = 'annual_candidate'
        selection = 'annual_audited_catalog_candidate'
    meta['revision'] = any(s in text for s in ['dinh chinh', 'dieu chinh', 'thay the', 'cap nhat', 'revised', 'restated'])
    return {**meta, 'eligible': True, 'reason': selection}


def select_candidate(candidates):
    """Do not use newest date alone as proof that two distinct reports replace each other."""
    eligible = [c for c in candidates if c['metadata']['eligible']]
    if not eligible:
        raise CollectionError('report_not_found', 'No matching report in the completed catalog scope')
    if len(eligible) == 1:
        return eligible[0], 'only_matching_candidate'
    revised = [c for c in eligible if c['metadata']['revision'] and c['published_at']]
    if len(revised) == 1 and all(c['published_at'] and c['published_at'] < revised[0]['published_at'] for c in eligible if c is not revised[0]):
        return revised[0], 'single_explicit_revision_published_after_other_candidates'
    raise CollectionError('ambiguous_report_versions', 'Multiple matching reports without a unique explicit revision',
                          {'matching_candidates': [{'url': c['url'], 'title': c['title'], 'published_at': c['published_at']} for c in eligible]})
