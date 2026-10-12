"""Paddle text detection only. Render PDF, crop detected regions, save geometry.

Run with the existing Paddle environment; no Paddle recognizer is instantiated.
"""
import argparse
from datetime import datetime, timezone
import hashlib
from importlib.metadata import version
import json
import os
from pathlib import Path
import time
import sys



def save(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')


def detect_report(work_dir, settings, pages='all', dpi=180, append=False):
    from types import SimpleNamespace
    WS = settings.workspace
    args = SimpleNamespace(work_dir=settings.processing_directory(work_dir), pages=pages, dpi=dpi)
    source = json.loads((args.work_dir/'source.json').read_text(encoding='utf-8'))
    pdf = WS/source['path']
    if hashlib.sha256(pdf.read_bytes()).hexdigest() != source['sha256']:
        raise ValueError('PDF hash does not match collection')
    import pymupdf
    import numpy as np
    from PIL import Image
    os.environ.setdefault('PADDLE_PDX_DISABLE_MODEL_SOURCE_CHECK', 'True')
    from paddleocr import TextDetection
    model_dir=settings.paddle_model_dir
    model_hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in model_dir.iterdir() if p.is_file()} if model_dir.exists() else {}
    model_lock=settings.detector_lock
    if model_lock.exists() and model_hashes!=json.loads(model_lock.read_text(encoding='utf-8'))['files_sha256']:
        raise ValueError('Paddle detector model hash mismatch; restore locked model before replay')
    config = dict(model_name='PP-OCRv5_mobile_det', device='cpu', enable_mkldnn=False,
                  cpu_threads=4, limit_side_len=1600, limit_type='max')
    detector = TextDetection(model_dir=str(model_dir), **config)
    model_hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in model_dir.iterdir() if p.is_file()}
    indices = set()
    if args.pages == 'all':
        with pymupdf.open(pdf) as document:
            indices.update(range(len(document)))
    else:
        for token in args.pages.split(','):
            bounds = token.split('-')
            indices.update(range(int(bounds[0])-1, int(bounds[-1])))
    out = args.work_dir/'detection'
    out.mkdir(parents=True, exist_ok=True)
    run = {'started_at': datetime.now(timezone.utc).isoformat(), 'stage': 'paddle_detection_only',
           'detector_code_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'pdf_sha256': source['sha256'], 'config': config, 'dpi': args.dpi,
           'packages': {p:version(p) for p in ['paddleocr','paddlepaddle','pymupdf']}, 'model_files_sha256':model_hashes, 'pages': [], 'error': None}
    started = time.monotonic()
    if append:
        previous = json.loads((out/'run.json').read_text(encoding='utf-8'))
        for key in ['detector_code_sha256', 'pdf_sha256', 'config', 'dpi', 'packages', 'model_files_sha256']:
            if previous.get(key) != run[key]:
                raise ValueError('Cannot append detection with changed source/config/model/runtime/code')
        if previous.get('error') or not previous.get('finished_at'):
            raise ValueError('Cannot append an unfinished detection batch')
        run['pages'] = [p for p in previous['pages'] if p['pdf_page_index'] not in indices]
        run['started_at'] = previous['started_at']
    try:
        with pymupdf.open(pdf) as doc:
            run['pdf_pages'] = len(doc)
            for index in sorted(indices):
                if not 0 <= index < len(doc):
                    raise ValueError('Page out of range')
                page_start = time.monotonic()
                image_path = out/f'page-{index+1:03}.png'
                doc[index].get_pixmap(dpi=args.dpi).save(image_path)
                image = Image.open(image_path).convert('RGB')
                result = list(detector.predict(str(image_path)))[0]
                polys = result['dt_polys']
                scores = result['dt_scores']
                crop_dir = out/f'page-{index+1:03}-crops'
                crop_dir.mkdir(exist_ok=True)
                entries = []
                # The demo document is axis-aligned. Retain polygons, use bounded
                # rectangular crops with padding; no invented text or native PDF text.
                ordered = sorted(zip(polys, scores, strict=True), key=lambda ps: (int(ps[0][:,1].min())//10, int(ps[0][:,0].min())))
                for region_id, (poly, score) in enumerate(ordered):
                    box = [max(0,int(poly[:,0].min())-2), max(0,int(poly[:,1].min())-2),
                           min(image.width,int(poly[:,0].max())+3), min(image.height,int(poly[:,1].max())+3)]
                    regions = [box]
                    # Detection may merge two monetary columns. Split only a wide
                    # right-half crop at a large white gap; keep original polygon.
                    if box[0] > image.width*.5 and box[2]-box[0] > 7*(box[3]-box[1]):
                        pixels = np.array(image.crop(tuple(box)).convert('L'))
                        ink = (pixels < 180).sum(axis=0) > 1
                        active = np.flatnonzero(ink)
                        gaps = [(int(a),int(b)) for a,b in zip(active[:-1],active[1:]) if b-a > 2*(box[3]-box[1])]
                        if len(gaps) == 1:
                            split = box[0]+sum(gaps[0])//2
                            regions = [[box[0],box[1],split,box[3]], [split,box[1],box[2],box[3]]]
                    for part, crop_box in enumerate(regions):
                        crop_path = crop_dir/f'{region_id:03}-{part}.png'
                        image.crop(tuple(crop_box)).save(crop_path)
                        entries.append({'id': f'{region_id}:{part}', 'bbox': crop_box, 'polygon': poly.tolist(),
                                        'detection_confidence': float(score), 'crop_path': str(crop_path.relative_to(WS)),
                                        'crop_sha256': hashlib.sha256(crop_path.read_bytes()).hexdigest(),
                                        'crop_rule': 'large_white_gap_split' if len(regions)>1 else 'padded_rectangle',
                                        'parent_region_id': region_id})
                data = {'stage':'paddle_detection_only', 'pdf_page_index':index,
                        'document_sha256':source['sha256'], 'image':str(image_path.relative_to(WS)),
                        'image_sha256':hashlib.sha256(image_path.read_bytes()).hexdigest(),
                        'image_width':image.width, 'image_height':image.height,
                        'config':config, 'entries':entries, 'seconds':round(time.monotonic()-page_start,3)}
                save(out/f'page-{index+1:03}.json', data)
                run['pages'].append({'pdf_page_index':index,'regions':len(entries),'seconds':data['seconds']})
                run['pages'].sort(key=lambda page: page['pdf_page_index'])
                save(out/'run.json',run)
                print(f'page-{index+1:03}: {len(entries)} crops, {data["seconds"]}s')
    except Exception as exc:
        run['error'] = f'{type(exc).__name__}: {exc}'
        raise
    finally:
        run.update(finished_at=datetime.now(timezone.utc).isoformat(),seconds=round(time.monotonic()-started,3))
        save(out/'run.json',run)

