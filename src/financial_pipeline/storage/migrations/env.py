from alembic import context
from financial_pipeline.storage.models import Base

connection = context.config.attributes.get("connection")
if connection is None:
    raise RuntimeError("Use upgrade_schema(engine) with an explicit connection")
context.configure(connection=connection, target_metadata=Base.metadata)
with context.begin_transaction():
    context.run_migrations()
