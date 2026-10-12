from datetime import datetime, timezone
from decimal import Decimal
from sqlalchemy import CheckConstraint, DateTime, ForeignKey, Integer, Numeric, String, UniqueConstraint
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Document(Base):
    __tablename__ = 'documents'
    __table_args__ = (UniqueConstraint('ticker', 'fiscal_year', 'scope'),)
    id: Mapped[int] = mapped_column(primary_key=True)
    ticker: Mapped[str] = mapped_column(String(12))
    fiscal_year: Mapped[int] = mapped_column(Integer)
    scope: Mapped[str] = mapped_column(String(30))


class DocumentVersion(Base):
    __tablename__ = 'document_versions'
    id: Mapped[int] = mapped_column(primary_key=True)
    document_id: Mapped[int] = mapped_column(ForeignKey('documents.id'))
    sha256: Mapped[str] = mapped_column(String(64), unique=True)
    path: Mapped[str] = mapped_column(String(500))
    source: Mapped[dict] = mapped_column(JSONB)


class ExtractionRun(Base):
    __tablename__ = 'extraction_runs'
    id: Mapped[int] = mapped_column(primary_key=True)
    document_version_id: Mapped[int] = mapped_column(ForeignKey('document_versions.id'))
    input_sha256: Mapped[str] = mapped_column(String(64), unique=True)
    pipeline: Mapped[str] = mapped_column(String(100))
    provenance: Mapped[dict] = mapped_column(JSONB)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))


class Candidate(Base):
    __tablename__ = 'candidates'
    __table_args__ = (UniqueConstraint('extraction_run_id', 'metric_code'),
                     CheckConstraint("status IN ('pending_review','missing_or_ambiguous')"),
                     CheckConstraint("(status='pending_review' AND value IS NOT NULL) OR (status='missing_or_ambiguous' AND value IS NULL)"))
    id: Mapped[int] = mapped_column(primary_key=True)
    extraction_run_id: Mapped[int] = mapped_column(ForeignKey('extraction_runs.id'))
    metric_code: Mapped[str] = mapped_column(String(60))
    value: Mapped[Decimal | None] = mapped_column(Numeric(30, 0), nullable=True)
    unit: Mapped[str] = mapped_column(String(20))
    status: Mapped[str] = mapped_column(String(30))
    evidence: Mapped[dict] = mapped_column(JSONB)
