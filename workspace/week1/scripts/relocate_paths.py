"""Update week-one links after moving files; preserve original OCR run logs."""
import json
import os
from pathlib import Path
import re

WEEK = Path(__file__).resolve().parents[1]
ROOT = WEEK.parents[1]
MAPPING = json.loads((WEEK / 'relocation-map.json').read_text(encoding='utf-8-sig'))


def moved(path):
    for old, new in MAPPING:
        source = ROOT / old
        if path == source or source in path.parents:
            return ROOT / new / path.relative_to(source)
    return path


def update(value):
    for old, new in MAPPING:
        value = value.replace(old, new).replace(old.replace('/', '\\'), new.replace('/', '\\'))
    return value


def main():
    for path in (WEEK / 'scripts').glob('*.py'):
        if path.name == Path(__file__).name:
            continue
        content = path.read_text(encoding='utf-8')
        content = content.replace('Path(__file__).resolve().parents[2]', 'Path(__file__).resolve().parents[3]')
        content = update(content)
        content = content.replace("ROOT / 'config/pilot-scope.json'", "Path(__file__).resolve().parents[1] / 'config/pilot-scope.json'")
        content = content.replace('ROOT / "config/pilot-scope.json"', 'Path(__file__).resolve().parents[1] / "config/pilot-scope.json"')
        path.write_text(content, encoding='utf-8')
    for path in (WEEK / 'docs').rglob('*.md'):
        old_base = ROOT / 'docs/research-platform/execution-v4' / path.relative_to(WEEK / 'docs')
        def link(match):
            target = match[1]
            if '://' in target or target.startswith('#'):
                return match[0]
            destination = moved((old_base.parent / target).resolve())
            return '](' + Path(os.path.relpath(destination, path.parent)).as_posix() + ')'
        content = re.sub(r'\]\(([^)]+)\)', link, path.read_text(encoding='utf-8'))
        path.write_text(update(content), encoding='utf-8')
    for config in [ROOT / 'config/pilot-scope.json', WEEK / 'config/pilot-scope.json']:
        config.write_text(update(config.read_text(encoding='utf-8')), encoding='utf-8')
    # Historical commands, timings and run hashes remain unchanged. The map
    # resolves their former paths. Regenerated candidates use current paths.
    for path in (WEEK / 'data').rglob('*.json'):
        if path.name == 'run.json':
            continue
        data = json.loads(path.read_text(encoding='utf-8-sig'))
        def walk(item):
            if isinstance(item, str):
                return update(item)
            if isinstance(item, list):
                return [walk(x) for x in item]
            if isinstance(item, dict):
                return {k: walk(v) for k, v in item.items()}
            return item
        path.write_text(json.dumps(walk(data), ensure_ascii=False, indent=2), encoding='utf-8')
    for path in (WEEK / 'data').rglob('*.csv'):
        path.write_text(update(path.read_text(encoding='utf-8-sig')), encoding='utf-8-sig')
    print('Updated code, document links, metadata and manifest; original run logs retained')


if __name__ == '__main__':
    main()
