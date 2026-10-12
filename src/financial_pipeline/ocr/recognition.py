"""Recognize only Paddle-detected crops using VietOCR. Preserve stage provenance."""
import argparse
from datetime import datetime, timezone
import hashlib
from importlib.metadata import version
import json
from pathlib import Path
import sys
import time
from financial_pipeline.cache import recognition_cache_matches


def save(path, value):
    path.write_text(json.dumps(value,ensure_ascii=False,indent=2),encoding='utf-8')


def predict_line(predictor, image):
    """Split very long detected lines only at blank word gaps, never at page numbers."""
    import numpy as np
    pixels=np.array(image.convert('L'))
    height,width=pixels.shape
    limit=height*10
    segments=[]
    start=0
    while width-start>height*12:
        white=(pixels < 180).sum(axis=0)<=1
        lo=start+int(limit*.65)
        hi=min(width-1,start+int(limit))
        candidates=np.flatnonzero(white[lo:hi])+lo
        if len(candidates)==0:
            break
        split=int(candidates[-1])
        if split<=start:
            break
        segments.append((start,split))
        start=split
    segments.append((start,width))
    results=[]
    for left,right in segments:
        text,prob=predictor.predict(image.crop((left,0,right,height)),return_prob=True)
        results.append({'left':left,'right':right,'text':text,'probability':float(prob)})
    return ' '.join(r['text'] for r in results),min(r['probability'] for r in results),results


def recognize_report(work_dir, settings, pages='all', dpi=180):
    from types import SimpleNamespace
    WS = settings.workspace
    args = SimpleNamespace(work_dir=settings.processing_directory(work_dir), pages=pages, dpi=dpi)
    from PIL import Image
    import torch
    from vietocr.tool.config import Cfg
    from vietocr.tool.predictor import Predictor
    torch.set_num_threads(4)
    config = Cfg.load_config_from_file(str(settings.vietocr_config))
    config['weights']=str(settings.vietocr_weights)
    model_lock = json.loads((settings.vietocr_lock).read_text(encoding='utf-8'))
    if hashlib.sha256(Path(config['weights']).read_bytes()).hexdigest() != model_lock['weights_sha256']:
        raise ValueError('VietOCR model hash mismatch')
    predictor = Predictor(config)
    source = json.loads((args.work_dir/'source.json').read_text(encoding='utf-8'))
    indices = set()
    if args.pages == 'all':
        detection_run=json.loads((args.work_dir/'detection/run.json').read_text(encoding='utf-8'))
        indices.update(range(detection_run['pdf_pages']))
    else:
        for token in args.pages.split(','):
            bounds = token.split('-')
            indices.update(range(int(bounds[0])-1,int(bounds[-1])))
    out = args.work_dir/'ocr'
    out.mkdir(parents=True,exist_ok=True)
    config_hash = hashlib.sha256((settings.vietocr_config).read_bytes()).hexdigest()
    code_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    packages = {p:version(p) for p in ['vietocr','torch','torchvision']}
    run = {'started_at':datetime.now(timezone.utc).isoformat(),'pipeline':'paddle_detection_vietocr_recognition',
           'document_sha256':source['sha256'],'recognizer_model_sha256':model_lock['weights_sha256'],
           'config_sha256':config_hash,'device':'cpu','packages':packages,'recognizer_code_sha256':code_hash,
           'pages':[],'error':None}
    started = time.monotonic()
    try:
        for index in sorted(indices):
            page_start = time.monotonic()
            det_path = args.work_dir/'detection'/f'page-{index+1:03}.json'
            detection = json.loads(det_path.read_text(encoding='utf-8'))
            if detection['document_sha256'] != source['sha256']:
                raise ValueError('Detection PDF mismatch')
            entries = []
            cache_path=out/f'page-{index+1:03}.json'
            cached={}
            if cache_path.exists():
                old=json.loads(cache_path.read_text(encoding='utf-8'))
                if recognition_cache_matches(old,source['sha256'],model_lock['weights_sha256'],config_hash,code_hash,packages):
                    cached={e['id']:e for e in old['entries']}
            cache_count=0
            with torch.inference_mode():
                for entry in detection['entries']:
                    crop = WS/entry['crop_path']
                    if hashlib.sha256(crop.read_bytes()).hexdigest() != entry['crop_sha256']:
                        raise ValueError('Crop hash mismatch')
                    with Image.open(crop) as image:
                        old_entry=cached.get(entry['id'])
                        if old_entry and old_entry.get('crop_sha256')==entry['crop_sha256'] and (old_entry.get('preprocessing_version')==3 or image.width<=image.height*12):
                            entries.append({**old_entry,'preprocessing_version':3})
                            cache_count+=1
                            continue
                        text,prob,segments=predict_line(predictor,image.convert('RGB'))
                    entries.append({**entry,'text':text,'confidence':float(prob),
                                    'recognition_engine':'VietOCR','confidence_scope':'minimum_segment_probability' if len(segments)>1 else 'vietocr_sequence_probability',
                                    'recognition_segments':segments,'preprocessing_version':3})
            data = {'engine':'PaddleDetection+VietOCR','engine_version':version('vietocr'),
                    'models':{'text_detection_model_name':'PP-OCRv5_mobile_det','text_recognition_model_name':'vgg_seq2seq'},
                    'document_sha256':source['sha256'],'pdf_page_index':index,
                    'image':detection['image'],'image_width':detection['image_width'],'image_height':detection['image_height'],
                    'image_sha256':detection['image_sha256'],
                    'detection_result':str(det_path.relative_to(WS)),
                    'detection_sha256':hashlib.sha256(det_path.read_bytes()).hexdigest(),
                    'recognizer_model_sha256':model_lock['weights_sha256'],'config_sha256':config_hash,
                    'recognizer_code_sha256':code_hash,'runtime_packages':packages,
                    'entries':entries,'seconds':round(time.monotonic()-page_start,3)}
            save(out/f'page-{index+1:03}.json',data)
            run['pages'].append({'pdf_page_index':index,'entries':len(entries),'seconds':data['seconds'],'cached_entries':cache_count,'recomputed_entries':len(entries)-cache_count})
            save(out/'run.json',run)
            print(f'page-{index+1:03}: {len(entries)} VietOCR lines, {data["seconds"]}s')
    except Exception as exc:
        run['error'] = f'{type(exc).__name__}: {exc}'
        raise
    finally:
        run.update(finished_at=datetime.now(timezone.utc).isoformat(),seconds=round(time.monotonic()-started,3))
        save(out/'run.json',run)

