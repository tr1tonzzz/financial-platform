"""Real CPU PaddleOCR adapter and logged image/PDF-page runner.

No Codex PDF/image reading and no financial values embedded in this script.
PyMuPDF is used only to render pages. Paddle supplies all recognized text.
"""
import argparse
from datetime import datetime, timezone
import hashlib
from importlib.metadata import version
import json
import os
from pathlib import Path
import platform
import sys
import time

os.environ.setdefault('PADDLE_PDX_DISABLE_MODEL_SOURCE_CHECK', 'True')


def utc():
    return datetime.now(timezone.utc).isoformat()


def save(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding='utf-8')


class PaddleAdapter:
    def __init__(self):
        from paddleocr import PaddleOCR
        self.config = dict(lang='vi', ocr_version='PP-OCRv5', device='cpu',
                           text_detection_model_name='PP-OCRv5_mobile_det',
                           text_recognition_model_name='latin_PP-OCRv5_mobile_rec',
                           use_doc_orientation_classify=False, use_doc_unwarping=False,
                           use_textline_orientation=False, enable_mkldnn=False, cpu_threads=4,
                           text_det_limit_side_len=1600, text_det_limit_type='max')
        self.ocr = PaddleOCR(**self.config)

    def predict(self, image, pdf_page_index, document_sha256):
        result = list(self.ocr.predict(str(image)))[0]
        entries = []
        for i, (text, score, box) in enumerate(zip(result['rec_texts'], result['rec_scores'], result['rec_boxes'], strict=True)):
            entries.append({'id': i, 'text': text, 'bbox': [int(x) for x in box], 'confidence': float(score)})
        return {'engine': 'PaddleOCR', 'engine_version': version('paddleocr'), 'backend_version': version('paddlepaddle'), 'models': {k:v for k,v in self.config.items() if 'model_name' in k}, 'image': str(image), 'image_sha256': hashlib.sha256(image.read_bytes()).hexdigest(), 'pdf_page_index': pdf_page_index, 'document_sha256': document_sha256, 'entries': entries}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--pdf', type=Path)
    parser.add_argument('--pages', default='1-15')
    parser.add_argument('--image', type=Path)
    parser.add_argument('--dpi', type=int, default=180)
    args = parser.parse_args()
    sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)
    out = args.output.resolve()
    out.mkdir(parents=True, exist_ok=True)
    run = {'started_at': utc(), 'command': sys.argv, 'python': sys.version, 'executable': sys.executable, 'platform': platform.platform(), 'dpi': args.dpi, 'pages': [], 'error': None}
    started = time.monotonic()
    try:
        import paddle
        paddle.utils.run_check()
        adapter = PaddleAdapter()
        run['config'] = adapter.config
        run['packages'] = {p:version(p) for p in ['paddleocr','paddlepaddle','paddlex','pymupdf','numpy']}
        jobs = []
        if args.image:
            jobs.append((args.image.resolve(), None, 'smoke-existing-vnm-q1'))
            digest = None
        else:
            import pymupdf
            digest = hashlib.sha256(args.pdf.read_bytes()).hexdigest()
            doc = pymupdf.open(args.pdf)
            run.update(pdf_sha256=digest, pdf_pages=len(doc), pdf=str(args.pdf.resolve()))
            indices = set()
            for token in args.pages.split(','):
                bounds = token.split('-')
                lo, hi = int(bounds[0]), int(bounds[-1])
                indices.update(range(lo-1, hi))
            for index in sorted(indices):
                if index < 0 or index >= len(doc):
                    raise ValueError('Page out of range')
                image = out / f'page-{index+1:03}.png'
                doc[index].get_pixmap(dpi=args.dpi).save(image)
                jobs.append((image, index, f'page-{index+1:03}'))
        for image, index, name in jobs:
            page_start = time.monotonic()
            json_path = out / f'{name}.json'
            if json_path.exists():
                cached = json.loads(json_path.read_text(encoding='utf-8'))
                if cached.get('document_sha256') == digest and cached.get('image_sha256') == hashlib.sha256(image.read_bytes()).hexdigest() and cached.get('engine_version') == version('paddleocr'):
                    run['pages'].append({'pdf_page_index': index, 'cached': True, 'result': str(json_path), 'entries': len(cached['entries'])})
                    print(f'{name}: reused logged Paddle result', flush=True)
                    continue
            result = adapter.predict(image, index, digest)
            result['seconds'] = round(time.monotonic()-page_start, 3)
            save(json_path, result)
            lines = sorted(result['entries'], key=lambda x:(x['bbox'][1], x['bbox'][0]))
            (out / f'{name}.txt').write_text('\n'.join(f"{x['id']}\t{x['bbox']}\t{x['confidence']:.4f}\t{x['text']}" for x in lines), encoding='utf-8')
            run['pages'].append({'pdf_page_index':index, 'cached':False, 'result':str(json_path), 'entries':len(lines), 'seconds':result['seconds']})
            save(out / 'run.json', run)
            print(f"{name}: {len(lines)} boxes, {result['seconds']}s", flush=True)
    except Exception as exc:
        run['error'] = f'{type(exc).__name__}: {exc}'
        raise
    finally:
        run.update(finished_at=utc(), seconds=round(time.monotonic()-started,3))
        save(out / 'run.json', run)


if __name__ == '__main__':
    main()
