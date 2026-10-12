"""Coordinate catalog collection and the reusable PDF-to-database pipeline."""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import subprocess
import time
import hashlib
import sys
import os

from financial_pipeline.settings import load_settings
from financial_pipeline.ocr import detection
from financial_pipeline.cache import detection_cache


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', '--profile', dest='profile', type=Path, required=True)
    parser.add_argument('--detection-batch-pages', type=int, default=10, help='Process isolation bounds Paddle memory; every PDF page is still processed')
    parser.add_argument('--resume', action='store_true', help='Rediscover catalogs; reuse only validated processing for the selected PDF')
    parser.add_argument('--keep-temporary', action='store_true')
    parser.add_argument('--collect-only', action='store_true')
    parser.add_argument('--ticker', action='append', required=True, help='Registered company; repeat for multiple companies')
    parser.add_argument('--year', type=int, required=True)
    parser.add_argument('--registry', type=Path)
    args = parser.parse_args()
    args.profile = args.profile.resolve()
    if args.registry:
        args.registry = args.registry.resolve()
    if args.detection_batch_pages < 1:
        parser.error('--detection-batch-pages must be positive')
    settings = load_settings(args.profile)
    args.registry = args.registry or settings.source_registry
    WS = settings.workspace
    cli = ['-m', 'financial_pipeline.cli']
    package_root = str(Path(__file__).resolve().parents[1])
    environment = {**os.environ, 'PYTHONPATH': package_root+os.pathsep+os.environ.get('PYTHONPATH', '')}
    tickers = list(dict.fromkeys(args.ticker))
    inference = settings.inference_python
    detector = settings.detector_python
    log_dir = WS/'data/runs'/datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    log_dir.mkdir(parents=True)
    run = {'started_at': datetime.now(timezone.utc).isoformat(), 'target_year': args.year, 'tickers': tickers,
           'mode': 'collection_only' if args.collect_only else 'catalog_through_database',
           'stages': [], 'completed': False}

    def stage(name, python, script, arguments=(), reused=False):
        print(('Reusing ' if reused else 'Running ')+name, flush=True)
        start = time.monotonic()
        if reused:
            result = None
        else:
            result = subprocess.run([str(python), *(script or []), *map(str, arguments), '--config', str(args.profile)],
                                    cwd=WS, env=environment, capture_output=True, text=True, encoding='utf-8', errors='replace')
            (log_dir/(name+'.log')).write_text(result.stdout+result.stderr, encoding='utf-8')
        run['stages'].append({'name': name, 'reused': reused, 'exit_code': None if reused else result.returncode,
                              'seconds': round(time.monotonic()-start, 3)})
        (log_dir/'run.json').write_text(json.dumps(run, indent=2), encoding='utf-8')
        if result and result.returncode:
            raise RuntimeError(f'{name} failed: {log_dir/(name+".log")}')
        return result

    try:
        # Collect all targets first. An unresolved source stops before expensive OCR.
        collected = []
        for ticker in tickers:
            result = stage(ticker+'_collect_catalog', inference, cli,
                           ['collect', '--ticker', ticker, '--year', args.year, '--registry', args.registry])
            collected.append((ticker, Path(result.stdout.strip().splitlines()[-1])))
        if not args.collect_only:
            stage('migrate', inference, cli, ['migrate'])
            for ticker, work in collected:
                can_reuse = False
                if args.resume:
                    runtime = subprocess.run([str(detector), '-c',
                        "import json; from importlib.metadata import version; print(json.dumps({p:version(p) for p in ['paddleocr','paddlepaddle','pymupdf']}))"],
                        capture_output=True, text=True, check=True)
                    model = json.loads((settings.detector_lock).read_text(encoding='utf-8'))
                    cache = detection_cache(work, WS, hashlib.sha256(Path(detection.__file__).read_bytes()).hexdigest(),
                                            model['files_sha256'], json.loads(runtime.stdout))
                    can_reuse = cache.reusable
                    run.setdefault('cache_decisions', {})[ticker] = cache.reason
                if can_reuse:
                    stage(ticker+'_detect_crop', detector, cli, reused=True)
                else:
                    source = json.loads((work/'source.json').read_text(encoding='utf-8'))
                    for first in range(1, source['pdf_pages']+1, args.detection_batch_pages):
                        last = min(source['pdf_pages'], first+args.detection_batch_pages-1)
                        stage(f'{ticker}_detect_crop_{first}_{last}', detector, cli,
                              ['detect', '--work-dir', work, '--pages', f'{first}-{last}',
                               *(['--append'] if first > 1 else [])])
                stage(ticker+'_recognize', inference, cli, ['recognize', '--work-dir', work, '--pages', 'all'])
                stage(ticker+'_extract_store_readback', inference, cli,
                      ['store', '--work-dir', work, *([] if args.keep_temporary else ['--cleanup'])])
        run['completed'] = True
    finally:
        run['finished_at'] = datetime.now(timezone.utc).isoformat()
        (log_dir/'run.json').write_text(json.dumps(run, indent=2), encoding='utf-8')
    print(f'Completed {run["mode"]}: {log_dir}', flush=True)


if __name__ == '__main__':
    main()
