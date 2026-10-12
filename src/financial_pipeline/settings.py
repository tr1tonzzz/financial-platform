"""Explicit runtime paths; importing this module opens no files or connections."""
from dataclasses import dataclass
import json
from pathlib import Path


@dataclass(frozen=True)
class PipelineSettings:
    workspace: Path
    detector_python: Path
    inference_python: Path
    paddle_model_dir: Path
    detector_lock: Path
    vietocr_config: Path
    vietocr_lock: Path
    vietocr_weights: Path
    database_env: Path
    source_registry: Path

    def processing_directory(self, path):
        resolved = Path(path).resolve()
        root = (self.workspace / 'runtime/processing').resolve()
        if resolved == root or not resolved.is_relative_to(root):
            raise ValueError('Processing directory must be inside configured workspace/runtime/processing')
        return resolved


def load_settings(profile):
    profile = Path(profile).resolve()
    values = json.loads(profile.read_text(encoding='utf-8'))
    base = (profile.parent / values.pop('base_dir', '.')).resolve()
    expected = set(PipelineSettings.__dataclass_fields__)
    if set(values) != expected:
        raise ValueError(f'Runtime profile fields must be {sorted(expected)}')
    return PipelineSettings(**{key: (base / Path(value).expanduser()).resolve() for key, value in values.items()})
