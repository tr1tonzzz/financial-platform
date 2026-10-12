"""Source versions, extraction runs and unreviewed normalized candidates."""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB

revision = '001_collection_pipeline'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('documents', sa.Column('id', sa.Integer, primary_key=True),
                    sa.Column('ticker', sa.String(12), nullable=False),
                    sa.Column('fiscal_year', sa.Integer, nullable=False),
                    sa.Column('scope', sa.String(30), nullable=False),
                    sa.UniqueConstraint('ticker', 'fiscal_year', 'scope'))
    op.create_table('document_versions', sa.Column('id', sa.Integer, primary_key=True),
                    sa.Column('document_id', sa.Integer, sa.ForeignKey('documents.id'), nullable=False),
                    sa.Column('sha256', sa.String(64), nullable=False, unique=True),
                    sa.Column('path', sa.String(500), nullable=False), sa.Column('source', JSONB, nullable=False))
    op.create_table('extraction_runs', sa.Column('id', sa.Integer, primary_key=True),
                    sa.Column('document_version_id', sa.Integer, sa.ForeignKey('document_versions.id'), nullable=False),
                    sa.Column('input_sha256', sa.String(64), unique=True, nullable=False),
                    sa.Column('pipeline', sa.String(100), nullable=False), sa.Column('provenance', JSONB, nullable=False),
                    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False))
    op.create_table('candidates', sa.Column('id', sa.Integer, primary_key=True),
                    sa.Column('extraction_run_id', sa.Integer, sa.ForeignKey('extraction_runs.id'), nullable=False),
                    sa.Column('metric_code', sa.String(60), nullable=False), sa.Column('value', sa.Numeric(30, 0)),
                    sa.Column('unit', sa.String(20), nullable=False), sa.Column('status', sa.String(30), nullable=False),
                    sa.Column('evidence', JSONB, nullable=False), sa.UniqueConstraint('extraction_run_id', 'metric_code'),
                    sa.CheckConstraint("status IN ('pending_review','missing_or_ambiguous')"),
                    sa.CheckConstraint("(status='pending_review' AND value IS NOT NULL) OR (status='missing_or_ambiguous' AND value IS NULL)"))


def downgrade():
    for name in ['candidates', 'extraction_runs', 'document_versions', 'documents']:
        op.drop_table(name)
