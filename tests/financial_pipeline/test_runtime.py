import importlib
import json
from pathlib import Path
import subprocess
import sys

import pytest
from financial_pipeline.settings import PipelineSettings, load_settings


def test_profile_resolves_paths_without_creating_workspace(tmp_path):
    profile = tmp_path/'runtime.json'
    values = {key: 'isolated/'+key for key in PipelineSettings.__dataclass_fields__}
    profile.write_text(json.dumps({'base_dir': '.', **values}), encoding='utf-8')
    settings = load_settings(profile)
    assert settings.workspace == tmp_path/'isolated/workspace'
    assert not settings.workspace.exists()
    valid = settings.workspace/'runtime/processing/report'
    assert settings.processing_directory(valid) == valid
    with pytest.raises(ValueError):
        settings.processing_directory(settings.workspace/'data/raw')
    with pytest.raises(ValueError):
        settings.processing_directory(settings.workspace/'runtime/processing')


def test_import_services_without_database_or_model_side_effects():
    code = '''
import os, sqlalchemy
os.environ.pop('DATABASE_URL', None)
def forbidden(*args, **kwargs):
    raise AssertionError('Engine created during import')
sqlalchemy.create_engine = forbidden
import financial_pipeline.storage.database
import financial_pipeline.storage.models
import financial_pipeline.storage.repository
import financial_pipeline.storage.service
import financial_pipeline.ocr.detection
import financial_pipeline.ocr.recognition
import sys
assert 'torch' not in sys.modules and 'paddleocr' not in sys.modules
assert 'PADDLE_PDX_DISABLE_MODEL_SOURCE_CHECK' not in os.environ
'''
    result = subprocess.run([sys.executable, '-c', code], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
