"""Verify the installed distribution without access to the source checkout."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[2]


def test_wheel_cli_and_child_process_run_outside_checkout(tmp_path):
    source = tmp_path/'build-source'
    source.mkdir()
    shutil.copy2(ROOT/'pyproject.toml', source/'pyproject.toml')
    shutil.copytree(ROOT/'src/financial_pipeline', source/'src/financial_pipeline',
                    ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
    wheels = tmp_path/'wheels'
    subprocess.run([sys.executable, '-m', 'pip', '--disable-pip-version-check', 'wheel', '--no-index', '--no-deps', '--no-build-isolation',
                    '--wheel-dir', str(wheels), str(source)], check=True, capture_output=True, text=True)
    installed = tmp_path/'installed'
    subprocess.run([sys.executable, '-m', 'pip', '--disable-pip-version-check', 'install', '--no-index', '--no-deps', '--target', str(installed),
                    str(next(wheels.glob('*.whl')))], check=True, capture_output=True, text=True)
    registry = tmp_path/'sources.json'
    shutil.copy2(ROOT/'config/report-sources.json', registry)
    config = tmp_path/'pipeline.json'
    from financial_pipeline.settings import PipelineSettings
    fields = {field: 'unused/'+field for field in PipelineSettings.__dataclass_fields__}
    fields.update(workspace=str(tmp_path/'work'), inference_python=sys.executable,
                  detector_python=sys.executable, source_registry=str(registry))
    config.write_text(json.dumps({'base_dir': '.', **fields}), encoding='utf-8')
    bootstrap = '''
import sys
from pathlib import Path
sys.path = [p for p in sys.path if Path(p).resolve() != Path(sys.argv[2]).resolve()]
sys.path.insert(0, sys.argv[1])
import financial_pipeline
import financial_pipeline.ocr.detection
import financial_pipeline.ocr.recognition
import financial_pipeline.storage.service
import financial_pipeline.storage.models
import financial_pipeline.storage.migrate
assert Path(financial_pipeline.__file__).is_relative_to(Path(sys.argv[1]))
assert Path(financial_pipeline.storage.migrate.__file__).parent.joinpath('migrations/versions/001_collection_pipeline.py').exists()
import runpy
arguments = sys.argv[3:]
sys.argv = ['financial_pipeline', *arguments]
runpy.run_module('financial_pipeline', run_name='__main__')
'''
    command = [sys.executable, '-c', bootstrap, str(installed), str(ROOT/'src')]
    environment = {key: value for key, value in os.environ.items() if key != 'PYTHONPATH'}
    help_result = subprocess.run([*command, '--help'], cwd=tmp_path, env=environment,
                                 capture_output=True, text=True)
    assert help_result.returncode == 0, help_result.stderr
    assert '--config' in help_result.stdout and '--ticker' in help_result.stdout
    # Unknown company stops before HTTP, OCR or DB; the child must also use the wheel.
    result = subprocess.run([*command, '--config', str(config), '--ticker', 'UNKNOWN', '--year', '2025', '--collect-only'],
                            cwd=tmp_path, env=environment, capture_output=True, text=True)
    assert result.returncode != 0
    run_path = next((tmp_path/'work/data/runs').glob('*/run.json'))
    run = json.loads(run_path.read_text(encoding='utf-8'))
    assert not run['completed'] and len(run['stages']) == 1
    log = (run_path.parent/'UNKNOWN_collect_catalog.log').read_text(encoding='utf-8')
    assert str(installed) in log and str(ROOT/'src') not in log
    assert not (tmp_path/'work/data/raw').exists()
    if os.getenv('FINANCIAL_PIPELINE_LIVE') == '1':
        collected = subprocess.run([*command, '--config', str(config), '--ticker', 'VNM', '--year', '2025', '--collect-only'],
                                   cwd=tmp_path, env=environment, capture_output=True, text=True)
        assert collected.returncode == 0, collected.stderr
        successful = [json.loads(path.read_text(encoding='utf-8')) for path in (tmp_path/'work/data/runs').glob('*/run.json')]
        assert any(run['completed'] and run['tickers'] == ['VNM'] for run in successful)
        source_path = next((tmp_path/'work/runtime/processing').glob('*/source.json'))
        source_metadata = json.loads(source_path.read_text(encoding='utf-8'))
        assert source_metadata['acquisition_mode'] == 'automatic_official_catalog'
        assert source_metadata['discovery']['complete']
