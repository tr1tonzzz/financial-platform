"""Extract six annual VNM candidates from logged Paddle boxes, never PDF native text.

Rules check statement, label, row code, year header and numeric geometry together.
References produced here are OCR-derived and await human visual review, not gold.
"""
import csv
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import unicodedata

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'workspace/week1/data/vnm-2025'
RULES = {
    'net_income_total': ('income_statement','60','Lợi nhuận sau thuế'),
    'cfo': ('cash_flow_statement','20','Lưu chuyển tiền thuần từ hoạt động kinh doanh'),
    'cash_equivalents': ('balance_sheet','110','Tiền và các khoản tương đương tiền'),
    'total_assets': ('balance_sheet','270','Tổng tài sản'),
    'total_liabilities': ('balance_sheet','300','Nợ phải trả'),
    'total_equity': ('balance_sheet','400','Vốn chủ sở hữu'),
}


def skeleton(text):
    # Latin model loses some Vietnamese vowels/diacritics. Preserve raw text and
    # use consonants only for candidate matching, never to repair numeric values.
    text = unicodedata.normalize('NFD', text.lower().replace('đ','d'))
    return ''.join(c for c in text if c.isalnum() and c not in 'aeiouy' and not unicodedata.combining(c))


def cy(e):
    return (e['bbox'][1]+e['bbox'][3])/2


def cx(e):
    return e.get('selection_x',(e['bbox'][0]+e['bbox'][2])/2)


def money(raw):
    if not re.fullmatch(r'\(?-?\d{1,3}(?:[.,]\d{3})*\)?', raw):
        return None
    if ('(' in raw or ')' in raw) and not (raw.startswith('(') and raw.endswith(')')):
        return None
    value = int(raw.strip('()').replace('.','').replace(',',''))
    return -value if raw.startswith('(') else value


def statement(entries):
    title = skeleton(' '.join(e['text'] for e in entries if e['bbox'][1]<220))
    for name, label in [('balance_sheet','Báo cáo tình hình tài chính'),('income_statement','Báo cáo kết quả hoạt động kinh doanh'),('cash_flow_statement','Báo cáo lưu chuyển tiền tệ')]:
        if skeleton(label) in title:
            return name
    return None


def row(entries, code, current_x, comparative_x=None):
    anchors = [e for e in entries if (e['text'].strip()==code and e['bbox'][0]>500 and e['bbox'][0]<850) or (e['text'].strip().endswith(' '+code) and e['bbox'][2]<850)]
    if len(anchors)!=1:
        raise ValueError(f'Expected unique row code {code}, found {len(anchors)}')
    anchor = anchors[0]
    height = anchor['bbox'][3]-anchor['bbox'][1]
    numeric=[]
    for e in entries:
        if abs(cy(e)-cy(anchor))>=height*0.65 or e['bbox'][0]<=anchor['bbox'][2]+80:
            continue
        if money(e['text']) is not None:
            numeric.append(e)
        elif comparative_x is not None:
            tokens=e['text'].split()
            if len(tokens)==2 and all(money(t) is not None for t in tokens) and e['bbox'][0]<min(current_x,comparative_x) and e['bbox'][2]>max(current_x,comparative_x):
                # Paddle merged two columns into one detected region. Split only
                # whitespace-delimited complete numeric tokens; retain whole-box
                # geometry/confidence and disclose that there is no cell bbox.
                for i,token in enumerate(tokens):
                    numeric.append({**e,'id':f"{e['id']}:token-{i}",'parent_ocr_id':e['id'],'parent_ocr_text':e['text'],'text':token,'token_index':i,'selection_x':sorted([current_x,comparative_x])[i],'bbox_precision':'whole_merged_row','confidence_scope':'whole_merged_row'})
    if len(numeric)!=2:
        raise ValueError(f'Row {code}: expected two numeric columns, found {len(numeric)}')
    selected = min(numeric,key=lambda e:abs(cx(e)-current_x))
    if abs(cx(selected)-current_x)>100:
        raise ValueError('Number is not aligned with current year header')
    # Wrapped labels often end at the code's line. Include preceding line, not
    # the next row; keep every raw token and bbox in evidence.
    labels = sorted([e for e in entries if e['bbox'][2]<anchor['bbox'][0]-20 and -height*1.8 < cy(e)-cy(anchor) < height*0.75],key=lambda e:(cy(e),cx(e)))
    return anchor, selected, labels, numeric


def save(path, value):
    path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')


def write_csv(path, rows):
    with path.open('w',encoding='utf-8-sig',newline='') as stream:
        writer=csv.DictWriter(stream,fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    with path.open(encoding='utf-8-sig',newline='') as stream:
        restored=list(csv.DictReader(stream))
    assert len(restored)==len(rows)
    for expected, actual in zip(rows,restored,strict=True):
        assert all(actual[k]==('' if v is None else str(v)) for k,v in expected.items())


def main():
    source=json.loads((OUT/'source.json').read_text(encoding='utf-8'))
    pages=[]
    for path in sorted((OUT/'ocr').glob('page-*.json')):
        data=json.loads(path.read_text(encoding='utf-8'))
        if data['document_sha256']!=source['sha256'] or data['engine']!='PaddleOCR':
            raise ValueError('OCR source/engine mismatch')
        pages.append((path,data,statement(data['entries'])))
    found={}
    evidence=[]
    row_controls={}
    for path,data,kind in pages:
        if kind is None:
            continue
        entries=data['entries']
        current=[e for e in entries if e['text'].strip()==('31/12/2025' if kind=='balance_sheet' else '2025') and e['bbox'][1]<600 and e['bbox'][0]>800]
        comparative=[e for e in entries if e['text'].strip()==('1/1/2025' if kind=='balance_sheet' else '2024') and e['bbox'][1]<600 and e['bbox'][0]>800]
        if len(current)!=1 or len(comparative)!=1:
            continue
        unit=[e for e in entries if e['text'].strip()=='VND' and e['bbox'][1]<650]
        if not unit:
            continue
        printed=[e['text'].strip() for e in entries if e['bbox'][1]>1800 and e['text'].strip().isdigit() and cx(e)>1250 and cx(e)<1400]
        for metric,(expected_kind,code,label) in RULES.items():
            if expected_kind!=kind or not any(e['text'].strip()==code for e in entries):
                continue
            try:
                anchor,selected,labels,numeric=row(entries,code,cx(current[0]),cx(comparative[0]))
                raw_label=' '.join(e['text'] for e in labels)
                if skeleton(label) not in skeleton(raw_label):
                    raise ValueError(f'Label check failed: {raw_label}')
                if metric in found:
                    if found[metric]['normalized_value_vnd']==str(money(selected['text'])):
                        evidence.append({'metric':metric,'page':data['pdf_page_index']+1,'carried_forward_same_value':True,'value_entry':selected})
                        continue
                    raise ValueError(f'Duplicate conflicting candidate {metric}; needs review')
                instant=kind=='balance_sheet'
                comp_value=next(e for e in numeric if e['id']!=selected['id'])
                found[metric]={
                    'reference_id':f"VNM-FY2025-{source['sha256'][:12]}:{metric}:r1",
                    'ticker':'VNM','fiscal_year':2025,'scope':'consolidated','metric_code':metric,
                    'period_kind':'instant' if instant else 'duration',
                    'period_start':None if instant else '2025-01-01','period_end':None if instant else '2025-12-31',
                    'as_of_date':'2025-12-31' if instant else None,
                    'raw_value':selected['text'],'raw_unit':'VND','normalized_value_vnd':str(money(selected['text'])),
                    'normalization_rule_version':'vnd-ocr-three-digit-groups-v1',
                    'statement_type':kind,'row_label_ocr':raw_label,'metric_label':label,'row_code':code,
                    'pdf_page_index':data['pdf_page_index'],'printed_page_label':printed[0] if len(printed)==1 else None,
                    'column_label':current[0]['text'],'column_role':'current','reported_in_year':2025,
                    'comparative_column_label':comparative[0]['text'],'comparative_raw_value':comp_value['text'],
                    'restatement_status':'current_as_reported','comparative_restatement_status':'no_marker_in_processed_header_notes_not_fully_checked',
                    'bbox':json.dumps(selected['bbox']),'confidence':selected['confidence'],
                    'bbox_precision':selected.get('bbox_precision','single_ocr_region'),'confidence_scope':selected.get('confidence_scope','single_ocr_region'),'value_token_index':selected.get('token_index'),
                    'extraction_method':'paddleocr','engine_version':data['engine_version'],'model_name':data['models']['text_recognition_model_name'],
                    'source_url':source['url'],'pdf_sha256':source['sha256'],'retrieved_at':source['retrieved_at'],'published_at':source['published_at'],
                    'review_status':'paddle_reference_pending_visual_review','dataset_partition':'development',
                    'reference_origin':'same_paddle_run_not_independent_gold',
                    'reason':'Paddle candidate matched label/code/current column; human source-image review still required',
                    'ocr_result':str(path.relative_to(ROOT)),'revision_id':'r1'
                }
                evidence.append({'metric':metric,'page':data['pdf_page_index']+1,'label_entries':labels,'row_code_entry':anchor,'value_entry':selected,'current_header':current[0],'comparative_header':comparative[0],'unit_entries':unit})
            except ValueError as exc:
                evidence.append({'metric':metric,'page':data['pdf_page_index']+1,'error':str(exc)})
        for code in ['111','112','100','200','310','330','61','62','410','440']:
            try:
                _,number,_,_=row(entries,code,cx(current[0]),cx(comparative[0]))
                row_controls[f'{kind}:{code}']={'raw_value':number['text'],'value':money(number['text']),'pdf_page_index':data['pdf_page_index'],'bbox':number['bbox'],'ocr_result':str(path.relative_to(ROOT))}
            except ValueError:
                pass
    rows=[]
    for metric in RULES:
        if metric in found:
            rows.append(found[metric])
        else:
            # Same schema, missing never becomes zero.
            base=dict(next(iter(found.values()))) if found else None
            if base is None:
                raise ValueError('No financial candidate found; inspect OCR results')
            instant=RULES[metric][0]=='balance_sheet'
            base.update(reference_id=f"VNM-FY2025:{metric}:missing",metric_code=metric,metric_label=RULES[metric][2],period_kind='instant' if instant else 'duration',raw_value=None,normalized_value_vnd=None,bbox=None,confidence=None,bbox_precision=None,confidence_scope=None,value_token_index=None,review_status='missing_or_ambiguous',reason='No unique matching row/label/year/unit in logged OCR pages')
            for key in ['row_label_ocr','row_code','pdf_page_index','printed_page_label','column_label','comparative_column_label','comparative_raw_value','ocr_result','statement_type','period_start','period_end','as_of_date']:
                base[key]=None
            base.update(period_start=None if instant else '2025-01-01',period_end=None if instant else '2025-12-31',as_of_date='2025-12-31' if instant else None)
            rows.append(base)
    checks=[]
    def check(name,keys,metric):
        if all(k in row_controls for k in keys) and metric in found:
            total=sum(row_controls[k]['value'] for k in keys)
            expected=int(found[metric]['normalized_value_vnd'])
            checks.append({'name':name,'operands':[row_controls[k] for k in keys],'sum_vnd':str(total),'target_vnd':str(expected),'passed':total==expected})
        else:
            checks.append({'name':name,'passed':None,'reason':'Some supporting OCR rows are missing/ambiguous'})
    check('cash_110_equals_111_plus_112',['balance_sheet:111','balance_sheet:112'],'cash_equivalents')
    check('assets_270_equals_100_plus_200',['balance_sheet:100','balance_sheet:200'],'total_assets')
    check('liabilities_300_equals_310_plus_330',['balance_sheet:310','balance_sheet:330'],'total_liabilities')
    check('income_60_equals_61_plus_62',['income_statement:61','income_statement:62'],'net_income_total')
    if all(k in found for k in ['total_assets','total_liabilities','total_equity']):
        total=int(found['total_liabilities']['normalized_value_vnd'])+int(found['total_equity']['normalized_value_vnd'])
        checks.append({'name':'assets_equals_liabilities_plus_equity','sum_vnd':str(total),'target_vnd':found['total_assets']['normalized_value_vnd'],'passed':str(total)==found['total_assets']['normalized_value_vnd']})
    if any(c['passed'] is False for c in checks):
        for r in rows:
            r['reason']+='; at least one arithmetic check failed, inspect validation log'
    save(OUT/'candidate-evidence.json',evidence)
    save(OUT/'candidates.json',rows)
    write_csv(OUT/'reference-facts.csv',rows)
    save(OUT/'extraction-validation.json',{'ran_at':datetime.now(timezone.utc).isoformat(),'present_count':len(found),'target_count':6,'csv_all_fields_round_trip':True,'checks':checks,'reviewed_fact_count':0,'independent_gold':False,'input_script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()})
    print(json.dumps({'present':len(found),'targets':6,'values':[{'metric':r['metric_code'],'raw':r['raw_value'],'page':None if r['pdf_page_index'] is None else r['pdf_page_index']+1,'status':r['review_status']} for r in rows],'checks':checks},ensure_ascii=False,indent=2))


if __name__=='__main__':
    main()
