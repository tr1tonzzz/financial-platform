"""Verify document context using only Paddle output text; preserve uncertainty."""
import json
import re
from pathlib import Path
from extract_vnm_paddle_facts import skeleton, save, OUT


def main():
    pages=[]
    for folder in ['ocr','ocr-context']:
        for path in sorted((OUT/folder).glob('page-*.json')):
            data=json.loads(path.read_text(encoding='utf-8'))
            pages.append((path,data))
    def find(phrase):
        needle=skeleton(phrase)
        hits=[]
        for path,data in pages:
            entries=data['entries']
            for i in range(len(entries)):
                chunk=entries[i:i+3]
                text=' '.join(e['text'] for e in chunk)
                matched=re.search(re.escape(needle)+(r'(?!\d)' if phrase[-1:].isdigit() else ''),skeleton(text)) is not None
                if phrase in ['VNM','VND']:
                    matched=re.search(r'\b'+phrase+r'\b',text) is not None
                if phrase=='ngày 1 tháng 1':
                    matched=matched and skeleton('kỳ kế toán năm') in skeleton(text) and skeleton('ngày 31 tháng 12') in skeleton(text)
                if matched:
                    hits.append({'pdf_page_index':data['pdf_page_index'],'ocr_file':str(path),'entries':chunk,'raw_text':text})
                    break
        return hits
    checks={
        'issuer_legal_name':find('Công ty Cổ phần Sữa Việt Nam'),
        'consolidated_scope':find('báo cáo tài chính hợp nhất'),
        'annual_period_end':find('cho năm kết thúc ngày 31 tháng 12 năm 2025'),
        'independent_audit':find('Báo cáo kiểm toán độc lập'),
        'currency_vnd':find('VND'),
        'annual_period_start_policy':find('ngày 1 tháng 1'),
        'annual_period_end_policy':find('ngày 31 tháng 12'),
        'indirect_cashflow':find('Phương pháp gián tiếp'),
        'ticker_literal_vnm':find('VNM'),
        'comparative_reclassified_marker':find('phân loại lại'),
        'comparative_restated_marker':find('trình bày lại'),
    }
    # A ticker string need not occur in the PDF. Resolve from the user's manifest
    # and official issuer catalog, backed by matched PDF legal name, explicitly.
    required=['issuer_legal_name','consolidated_scope','annual_period_end','independent_audit','currency_vnd','annual_period_start_policy']
    valid=all(checks[k] for k in required)
    result={'required_context_verified':valid,'checks':checks,'ticker_resolution':'literal_in_ocr' if checks['ticker_literal_vnm'] else 'VNM manifest + official Vinamilk catalog + matching PDF legal name; literal ticker not located in processed OCR pages', 'processed_pages':sorted(d['pdf_page_index']+1 for _,d in pages),'notes':'Consonant matching tolerates omitted Vietnamese vowels. Raw OCR retained; context self-check is not independent human verification.'}
    save(OUT/'context-verification.json',result)
    source=json.loads((OUT/'source.json').read_text(encoding='utf-8'))
    source.update(context_status='verified_from_paddle_text' if valid else 'partially_verified_from_paddle_text',ticker_resolution=result['ticker_resolution'],context_evidence='context-verification.json',pages=63)
    if valid:
        source.update(period_start='2025-01-01',period_end='2025-12-31',scope='consolidated',report_type='annual_audited',issuer_legal_name='Công ty Cổ phần Sữa Việt Nam',raw_unit='VND')
    save(OUT/'source.json',source)
    print(json.dumps({'required_context_verified':valid,'hits':{k:[x['pdf_page_index']+1 for x in v] for k,v in checks.items()},'ticker_resolution':result['ticker_resolution']},ensure_ascii=False,indent=2))


if __name__=='__main__':
    main()
