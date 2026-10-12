"""Construct database resources explicitly, never at import time."""
import os
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Database:
    def __init__(self, url):
        if not url or not url.startswith('postgresql+psycopg://'):
            raise ValueError('Supply a PostgreSQL psycopg DATABASE_URL')
        self.engine = create_engine(url, pool_pre_ping=True)
        self.sessions = sessionmaker(self.engine, expire_on_commit=False)

    @classmethod
    def from_env_file(cls, path):
        from dotenv import dotenv_values
        url = os.environ.get('DATABASE_URL') or dotenv_values(Path(path)).get('DATABASE_URL')
        return cls(url)

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self.engine.dispose()
