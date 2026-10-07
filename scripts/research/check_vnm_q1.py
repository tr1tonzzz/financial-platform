"""Extract six numeric candidates from raw OCR, then compare with manual reference."""
import argparse
import json
import re
import subprocess
from pathlib import Path
from crawl_official_reports import fold


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=["prepare", "check"])
    parser.add_argument("output", type=Path)
    parser.add_argument("--pdftoppm")
    args = parser.parse_args()
    root = args.output.resolve()
    source = json.loads((root / "source-probe.json").read_text(encoding="utf-8"))
    if args.mode == "prepare":
        if not args.pdftoppm:
            parser.error("--pdftoppm is required for prepare")
        jobs = []
        for page in [12, 13, 14]:
            subprocess.run([args.pdftoppm, "-f", str(page), "-l", str(page), "-r", "220", "-png", str(root / source["pdf_path"]), str(root / "ocr-page")], check=True)
            jobs.append({"id": f"vnm-q1-2026-p{page}", "image": str(root / f"ocr-page-{page}.png"), "pdf_page": page, "render_dpi": 220})
        (root / "page-jobs.json").write_text(json.dumps(jobs, indent=2), encoding="utf-8")
        return
    # Candidate extraction does not read reference values.
    candidates = {}
    for key, page, label in [("net_income", 12, "loi nhuan sau thue"), ("cfo", 13, "luu chuyen tien thuan tu hoat dong"), ("cash_dividends_paid", 14, "tien chi tra co tuc")]:
        lines = (root / "ocr" / f"vnm-q1-2026-p{page}-ocr.txt").read_text(encoding="utf-8").splitlines()
        for index, line in enumerate(lines):
            if label in fold(line):
                window = " ".join(lines[index:index + 2])
                numbers = re.findall(r"\(?\d{1,3}(?:\.\d{3}){2,}\)?", window)
                candidates[key] = [(-1 if value.startswith("(") else 1) * int(value.strip("()").replace(".", "")) for value in numbers[:2]]
                break
    reference_path = Path(__file__).resolve().parents[2] / "docs/research-profit-cash-dividend/evidence/case-vnm-q1-2026.json"
    reference = json.loads(reference_path.read_text(encoding="utf-8"))
    if source["pdf_sha256"] != reference["pdf_sha256"]:
        raise RuntimeError("Changed PDF: review page selection and reference before comparing")
    rows = []
    for fact in reference["facts"]:
        for index, expected in enumerate(fact["values"]):
            values = candidates.get(fact["key"], [])
            actual = values[index] if index < len(values) else None
            rows.append({"field": fact["key"], "quarter": ["Q1/2026", "Q1/2025"][index], "pdf_page": fact["pdf_page"], "actual": actual, "reference": expected, "result": "missing" if actual is None else "correct" if actual == expected else "wrong"})
    counts = {state: sum(row["result"] == state for row in rows) for state in ["correct", "wrong", "missing"]}
    metrics = {}
    if all(row["result"] == "correct" for row in rows[:4]):
        ni, cfo = candidates["net_income"], candidates["cfo"]
        metrics = {"net_income_growth_percent": (ni[0] / ni[1] - 1) * 100, "cfo_change_vnd": cfo[0] - cfo[1], "cfo_net_income_ratio_2026": cfo[0] / ni[0], "cfo_net_income_ratio_2025": cfo[1] / ni[1]}
    result = {"counts": counts, "rows": rows, "metrics": metrics, "warning": "Six selected development cells only; same-person manual reference; no measured general OCR accuracy."}
    (root / "comparison.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
