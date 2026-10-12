"""Financial statement discovery, six core metrics and VND normalization."""
from .parser import parse_report, RULES

__all__ = ['parse_report', 'RULES']
