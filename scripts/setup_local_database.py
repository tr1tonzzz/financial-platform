"""Initialize and start the local PostgreSQL development database."""
import argparse
import os
from pathlib import Path
import secrets
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'src'))
from financial_pipeline.settings import load_settings
BIN = ROOT / '.tools/postgresql/pgsql/bin'


def command(name, *args, env=None):
    subprocess.run([str(BIN / (name + '.exe')), *map(str, args)], check=True,
                   env=env, creationflags=subprocess.CREATE_NO_WINDOW)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=Path, default=ROOT/'config/pipeline.json')
    args = parser.parse_args()
    WS = load_settings(args.config).workspace
    runtime = WS / 'runtime'
    runtime.mkdir(exist_ok=True)
    password_file = runtime / 'pipeline-password.txt'
    if not password_file.exists():
        password_file.write_text(secrets.token_hex(24), encoding='ascii')
    password = password_file.read_text(encoding='ascii').strip()
    cluster = runtime / 'pipeline-postgres'
    if not (cluster / 'PG_VERSION').exists():
        command('initdb', '-D', cluster, '-U', 'vnm_pipeline', '-A', 'scram-sha-256',
                '--pwfile', password_file, '-E', 'UTF8', '--locale=C')
    status = subprocess.run([str(BIN / 'pg_ctl.exe'), '-D', str(cluster), 'status'], capture_output=True)
    if status.returncode != 0:
        command('pg_ctl', '-D', cluster, '-l', runtime / 'pipeline-postgres.log',
                '-o', '-p 55433 -h 127.0.0.1', '-w', 'start')
    env = {**os.environ, 'PGPASSWORD': password}
    check = subprocess.run([str(BIN / 'psql.exe'), '-h', '127.0.0.1', '-p', '55433',
                            '-U', 'vnm_pipeline', '-d', 'postgres', '-tAc',
                            "SELECT 1 FROM pg_database WHERE datname='vnm2025_pipeline'"],
                           check=True, env=env, capture_output=True, text=True)
    if not check.stdout.strip():
        command('createdb', '-h', '127.0.0.1', '-p', '55433', '-U', 'vnm_pipeline',
                'vnm2025_pipeline', env=env)
    (runtime / 'database.env').write_text(
        f'DATABASE_URL=postgresql+psycopg://vnm_pipeline:{password}@127.0.0.1:55433/vnm2025_pipeline\n',
        encoding='ascii')
    print('PostgreSQL ready: 127.0.0.1:55433/vnm2025_pipeline')


if __name__ == '__main__':
    main()
