"""Thin process boundary for the two isolated OCR environments."""
import argparse
import json
from pathlib import Path
import sys
from .settings import load_settings


def main():
    sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)
    parser = argparse.ArgumentParser()
    parser.add_argument('stage', choices=['collect', 'detect', 'recognize', 'store', 'migrate'])
    parser.add_argument('--config', '--profile', dest='profile', type=Path, required=True)
    parser.add_argument('--work-dir', type=Path)
    parser.add_argument('--pages', default='all')
    parser.add_argument('--dpi', type=int, default=180)
    parser.add_argument('--append', action='store_true')
    parser.add_argument('--cleanup', action='store_true')
    parser.add_argument('--ticker')
    parser.add_argument('--year', type=int)
    parser.add_argument('--period', default='annual')
    parser.add_argument('--scope', default='consolidated')
    parser.add_argument('--assurance', default='audited')
    parser.add_argument('--language', default='vi')
    parser.add_argument('--registry', type=Path)
    args = parser.parse_args()
    if args.stage == 'collect' and (args.ticker is None or args.year is None):
        parser.error('collect requires --ticker and --year')
    settings = load_settings(args.profile)
    if args.stage == 'collect':
        from .collection import ReportTarget, collect_report
        registry = json.loads((args.registry or settings.source_registry).read_text(encoding='utf-8'))
        target = ReportTarget(args.ticker, args.year, args.period, args.scope, args.assurance, args.language)
        result = collect_report(target, registry, settings.workspace)
        print(result.work_dir, flush=True)
    elif args.stage == 'detect':
        from .ocr.detection import detect_report
        detect_report(args.work_dir, settings, args.pages, args.dpi, args.append)
    elif args.stage == 'recognize':
        from .ocr.recognition import recognize_report
        recognize_report(args.work_dir, settings, args.pages)
    else:
        from .storage.database import Database
        with Database.from_env_file(settings.database_env) as database:
            if args.stage == 'migrate':
                from .storage.migrate import upgrade_schema
                upgrade_schema(database.engine)
            else:
                from .storage.service import store_report
                store_report(args.work_dir, settings, database.sessions, args.cleanup)


if __name__ == '__main__':
    main()
