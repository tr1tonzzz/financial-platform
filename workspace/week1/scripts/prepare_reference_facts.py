"""Package manually transcribed references; does not extract, review or publish facts.

Run from any directory. Paths in the input are relative to the repository root.
This narrow exporter supports the VND dot-grouped numbers in this first source.
"""
import argparse
import csv
import hashlib
import json
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]


def vnd(raw):
    if not re.fullmatch(r"\(?-?\d{1,3}(?:\.\d{3})*\)?", raw):
        raise ValueError(f"Ambiguous VND input: {raw!r}")
    negative = raw.startswith("(") and raw.endswith(")")
    if ("(" in raw or ")" in raw) and not negative:
        raise ValueError("Unmatched parentheses")
    return (-1 if negative else 1) * int(raw.strip("()").replace(".", ""))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    input_path = args.input.resolve()
    payload = json.loads(input_path.read_text(encoding="utf-8"))
    doc = payload["document"]
    review = payload["reference_review"]
    manifest = json.loads((Path(__file__).resolve().parents[1] / "config/pilot-scope.json").read_text(encoding="utf-8"))
    refs = payload["references"]
    if sorted(r["metric_code"] for r in refs) != sorted(manifest["core_metrics"]):
        raise ValueError("Expect exactly one reference/status per core metric")
    original = ROOT / doc["original_pdf_path"]
    digest = hashlib.sha256(original.read_bytes()).hexdigest()
    if digest != doc["pdf_sha256"] or original.stat().st_size != doc["pdf_bytes"]:
        raise ValueError("Original PDF hash/size mismatch")
    if doc["raw_unit"] != "VND" or doc["dataset_partition"] != "development":
        raise ValueError("This exporter expects VND development references")
    if review["review_status"] != "self_checked_reference" or doc["independent_test_eligible"]:
        raise ValueError("References must not be promoted to published/independent facts")
    checks = []
    rows = []
    for ref in refs:
        if not 0 <= ref["pdf_page_index"] < doc["pdf_pages"]:
            raise ValueError("PDF page locator out of range")
        if not (ROOT / ref["evidence_image"]).is_file():
            raise FileNotFoundError(ref["evidence_image"])
        duration = ref["metric_code"] in {"net_income_total", "cfo"}
        if duration:
            if (ref["period_kind"], ref["period_start"], ref["period_end"], ref["as_of_date"]) != (
                "duration", doc["period_start"], doc["period_end"], None
            ):
                raise ValueError("Incorrect duration period")
        elif (ref["period_kind"], ref["period_start"], ref["period_end"], ref["as_of_date"]) != (
            "instant", None, None, doc["period_end"]
        ):
            raise ValueError("Incorrect balance date")
        value = ref["normalized_value_vnd"]
        if value is None:
            if ref["raw_value"] is not None or not ref["reason"]:
                raise ValueError("Missing/ambiguous references need null and reason")
            value_status = "missing_or_ambiguous"
        else:
            if str(vnd(ref["raw_value"])) != value:
                raise ValueError("Normalization differs from supplied reference")
            value_status = "present"
        row = {
            "reference_id": f"{doc['document_version_id']}:{ref['metric_code']}:reference-r1",
            "ticker": doc["ticker"], "fiscal_year": doc["fiscal_year"], "scope": doc["scope"],
            **ref, "raw_unit": doc["raw_unit"], "value_status": value_status,
            "normalization_rule_version": "vnd-dot-grouping-v1",
            "column_role": "current", "reported_in_year": doc["fiscal_year"],
            "restatement_status": "current_as_reported", "bbox": None,
            **{k: doc[k] for k in ("document_version_id", "source_url", "pdf_sha256", "retrieved_at", "published_at", "acquisition_mode", "dataset_partition", "document_family_id")},
            **{k: review[k] for k in ("review_status", "reviewer", "review_date", "extraction_method", "engine_version", "model_name", "confidence", "revision_id")},
            "review_reason": review["reason"]
        }
        rows.append(row)
    values = {r["metric_code"]: int(r["normalized_value_vnd"]) for r in refs if r["normalized_value_vnd"] is not None}
    for control in payload["supporting_controls"]:
        actual = sum(vnd(n) for n in control["raw_operands"])
        expected = values.get(control["metric_code"])
        checks.append({**control, "sum_vnd": str(actual), "reference_vnd": None if expected is None else str(expected), "passed": None if expected is None else actual == expected, "status": "skipped_missing_reference" if expected is None else "executed"})
    balance_available = all(k in values for k in ("total_assets", "total_liabilities", "total_equity"))
    balance = values["total_liabilities"] + values["total_equity"] if balance_available else None
    checks.append({"check": "assets_equals_liabilities_plus_equity", "sum_vnd": None if balance is None else str(balance), "passed": None if balance is None else balance == values["total_assets"], "status": "executed" if balance_available else "skipped_missing_reference"})
    if any(c["passed"] is False for c in checks):
        raise ValueError("Source arithmetic reconciliation failed; inspect input")
    destination = ROOT / doc["preserved_pdf_path"]
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists() and hashlib.sha256(destination.read_bytes()).hexdigest() != digest:
        raise ValueError("Existing preserved PDF differs")
    if not destination.exists():
        shutil.copyfile(original, destination)
    if hashlib.sha256(destination.read_bytes()).hexdigest() != digest:
        raise ValueError("Preserved PDF hash mismatch")
    output = ROOT / "workspace/week1/data"
    csv_path = output / "reference-facts.csv"
    if csv_path.exists():
        with csv_path.open(encoding="utf-8-sig", newline="") as stream:
            existing = list(csv.DictReader(stream))
        if any(r["document_version_id"] != doc["document_version_id"] for r in existing):
            raise ValueError("CSV contains other documents; merge separately instead of overwriting")
    with csv_path.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    with csv_path.open(encoding="utf-8-sig", newline="") as stream:
        restored = list(csv.DictReader(stream))
    for expected, actual in zip(rows, restored, strict=True):
        if any(actual[k] != ("" if v is None else str(v)) for k, v in expected.items()):
            raise ValueError("CSV round trip changed a field")
    validated_at = datetime.now(timezone.utc).isoformat()
    (output / "source-manifest.json").write_text(json.dumps({**doc, "validated_at": validated_at}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {"validated_at": validated_at, "input": str(input_path.relative_to(ROOT)), "input_sha256": hashlib.sha256(input_path.read_bytes()).hexdigest(), "pdf_hash_verified": True, "preserved_pdf_hash_verified": True, "reference_count": len(rows), "csv_round_trip_all_fields": True, "csv_sha256": hashlib.sha256(csv_path.read_bytes()).hexdigest(), "checks": checks, "reviewed_fact_count": 0, "independent_gold": False, "ocr_executed": False}
    (output / "reference-validation.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
