"""Use one parser for any supplied report. Persist six targets and minimal provenance."""
import argparse
import csv
from datetime import datetime, timezone
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import shutil
import sys
from .repository import persist
from financial_pipeline.ocr import detection as detection_service, recognition as recognition_service
from financial_pipeline.storage.models import Candidate, Document, DocumentVersion, ExtractionRun

from financial_pipeline.extraction import parser as financial_parser
from financial_pipeline.extraction import normalization
from financial_pipeline.extraction.parser import parse_report, RULES


def save(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding='utf-8')




def store_report(work_dir, settings, sessions, cleanup=False):
    WS = settings.workspace
    work = settings.processing_directory(work_dir)
    source = json.loads((work/'source.json').read_text(encoding='utf-8'))
    if source.get('acquisition_mode') != 'automatic_official_catalog' or not source.get('discovery', {}).get('complete'):
        raise ValueError('Current pipeline requires a completed official catalog discovery')
    if source['discovery']['pages_visited'] != source['discovery']['expected_pages'] or not source.get('catalog_candidate', {}).get('eligible'):
        raise ValueError('Source selection/coverage is unresolved')
    pdf = (WS/source['path']).resolve()
    if not pdf.is_relative_to((WS/'data/raw').resolve()) or hashlib.sha256(pdf.read_bytes()).hexdigest() != source['sha256']:
        raise ValueError('Original PDF identity mismatch')
    detection_run = json.loads((work/'detection/run.json').read_text(encoding='utf-8'))
    recognition_run = json.loads((work/'ocr/run.json').read_text(encoding='utf-8'))
    pages = [json.loads(p.read_text(encoding='utf-8')) for p in sorted((work/'ocr').glob('page-*.json'))]
    if not detection_run.get('finished_at') or not recognition_run.get('finished_at') or detection_run['error'] or recognition_run['error'] or len(pages) != detection_run['pdf_pages']:
        raise ValueError('All-page OCR incomplete; do not store a partial run')
    if detection_run['pdf_sha256'] != source['sha256'] or recognition_run['document_sha256'] != source['sha256']:
        raise ValueError('Run source mismatch')
    if {p['pdf_page_index'] for p in detection_run['pages']} != set(range(detection_run['pdf_pages'])) or {p['pdf_page_index'] for p in recognition_run['pages']} != set(range(detection_run['pdf_pages'])):
        raise ValueError('Stage page coverage mismatch')
    if {p['pdf_page_index'] for p in pages} != set(range(detection_run['pdf_pages'])):
        raise ValueError('Page coverage mismatch')
    config_hash = hashlib.sha256((settings.vietocr_config).read_bytes()).hexdigest()
    model_hash = json.loads((settings.vietocr_lock).read_text(encoding='utf-8'))['weights_sha256']
    recognizer_code = hashlib.sha256(Path(recognition_service.__file__).read_bytes()).hexdigest()
    if recognition_run.get('recognizer_code_sha256') != recognizer_code:
        raise ValueError('Recognizer code changed; rerun recognition rather than relabeling old OCR')
    detector_code = hashlib.sha256(Path(detection_service.__file__).read_bytes()).hexdigest()
    if detection_run.get('detector_code_sha256') != detector_code:
        raise ValueError('Detector code changed; regenerate detection before storing')
    for page in pages:
        if page['document_sha256'] != source['sha256'] or page['engine'] != 'PaddleDetection+VietOCR' or page['config_sha256'] != config_hash or page['recognizer_model_sha256'] != model_hash:
            raise ValueError('OCR source/engine/config/model mismatch')
        if page.get('recognizer_code_sha256') != recognizer_code or page.get('runtime_packages') != recognition_run['packages']:
            raise ValueError('OCR page code/runtime differs from its recognition run')
        detection = (WS/page['detection_result']).resolve()
        if not detection.is_relative_to(work) or hashlib.sha256(detection.read_bytes()).hexdigest() != page['detection_sha256']:
            raise ValueError('Detection evidence mismatch')
        detected = json.loads(detection.read_text(encoding='utf-8'))
        if {e['id']:e['crop_sha256'] for e in detected['entries']} != {e['id']:e['crop_sha256'] for e in page['entries']}:
            raise ValueError('Not every detected region was recognized')
        for entry in page['entries']:
            crop = (WS/entry['crop_path']).resolve()
            if not crop.is_relative_to(work) or hashlib.sha256(crop.read_bytes()).hexdigest() != entry['crop_sha256']:
                raise ValueError('Crop evidence mismatch')
    rows, summary = parse_report(pages, source)
    summary.update({'pdf_pages': detection_run['pdf_pages'], 'all_pages_processed': True,
                    'parser_sha256': hashlib.sha256(Path(financial_parser.__file__).read_bytes()).hexdigest(),
                    'normalization_sha256': hashlib.sha256(Path(normalization.__file__).read_bytes()).hexdigest(),
                    'dpi': detection_run['dpi'], 'detector_packages': detection_run['packages'],
                    'recognizer_packages': recognition_run['packages'], 'detector_config': detection_run['config'],
                    'detector_model_hashes': detection_run['model_files_sha256'],
                    'recognizer_model_sha256': model_hash, 'recognition_config_sha256': config_hash,
                    'recognizer_code_sha256': recognizer_code, 'detector_code_sha256': detector_code,
                    'line_preprocessing_versions': sorted({e.get('preprocessing_version', 1) for p in pages for e in p['entries']}),
                    'recognition_cache_entries': sum(p.get('cached_entries', 0) for p in recognition_run['pages']),
                    'recognition_recomputed_entries': sum(p.get('recomputed_entries', len(p['entries']) if isinstance(p.get('entries'),list) else p['entries']) for p in recognition_run['pages']),
                    'checked_at': datetime.now(timezone.utc).isoformat(),
                    'scope': 'Vietnamese calendar-year consolidated financial statements; six core targets'})
    source['context_status'] = 'verified_from_paddle_vietocr_text' if summary['context']['verified'] else 'unresolved_document_context'
    source['scope'] = 'consolidated'
    run_id, output = persist(source, rows, summary, sessions)
    destination = WS/'data/processed'/f'{source["ticker"]}-{source["fiscal_year"]}-{source["sha256"][:12]}'
    destination.mkdir(parents=True, exist_ok=True)
    save(destination/'source.json', source)
    save(destination/'processing.json', summary)
    save(destination/'candidates.json', rows)
    with (destination/'database-readback.csv').open('w', encoding='utf-8-sig', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=list(output[0]))
        writer.writeheader()
        writer.writerows(output)
    print(json.dumps({'ticker': source['ticker'], 'pdf_pages': len(pages), 'present': summary['present_count'],
                      'targets': 6, 'context': summary['context'], 'database_run_id': run_id,
                      'selected_statement_pages': [p['pdf_page'] for p in summary['statement_pages']],
                      'output': str(destination)}, ensure_ascii=False), flush=True)
    if cleanup:
        expected = WS/'runtime/processing'
        if not work.is_relative_to(expected.resolve()) or work == expected.resolve():
            raise ValueError('Cleanup outside task temporary directory')
        shutil.rmtree(work)

    return run_id, destination
