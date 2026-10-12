"""Official catalog discovery and targeted PDF collection."""
from .models import ReportTarget, CollectionError
from .service import collect_report

__all__ = ['ReportTarget', 'CollectionError', 'collect_report']
