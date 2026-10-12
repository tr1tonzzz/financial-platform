"""Source-checkout entry point; business logic lives in financial_pipeline."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from financial_pipeline.cli import main

if __name__ == '__main__':
    main()
