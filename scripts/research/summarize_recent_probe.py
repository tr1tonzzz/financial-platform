"""Summarize the saved probe and a small, visually reviewed OCR check.

This is a development-set inspection, not an independent accuracy benchmark.
Usage: python summarize_recent_probe.py <evidence-dir> <report-dir>
"""
import hashlib
import json
import re
import statistics
import sys
from datetime import datetime, timezone
from pathlib import Path

from probe_recent_sources import fold


TARGETS = {
    "vnm-q12026": {
        "cash_equivalents": (7, r"tien.*tuong duong tien", 2077596293461),
        "total_assets": (9, r"tong tai san", 55429011127169),
        "total_liabilities": (10, r"no phai tra", 18740931850130),
        "total_equity": (10, r"von chu so huu", 36688079277039),
        "net_income_total": (11, r"loi nhuan sau thue tndn", 2458221002532),
        "cfo": (13, r"luu chuyen tien thuan tu hoat dong", 269326997516),
    },
    "dhg-fy2025": {
        "cash_equivalents": (7, r"tien.*tuong duong tien", 129895664996),
        "total_assets": (8, r"tong cong tai san", 5173881628997),
        "total_liabilities": (9, r"no\s*phai tra", 1036616453045),
        "total_equity": (9, r"von chu so huu", 4137265175952),
        "net_income_total": (10, r"loi nhuan sau thue thu nhap doanh nghiep", 852354107582),
        "cfo": (11, r"luu chuyen tien thuan tu hoat dong kinh doanh", 1212967705385),
    },
}


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    evidence = Path(sys.argv[1]).resolve()
    report = Path(sys.argv[2]).resolve()
    report.mkdir(parents=True, exist_ok=True)
    manifest = json.loads((evidence / "manifest.json").read_text(encoding="utf-8"))
    curl_path = evidence / "hnx-vhe-fy2025-curl.pdf"
    if curl_path.exists():
        inspection = json.loads((evidence / "hnx-vhe-fy2025-curl-inspection.json").read_text(encoding="utf-8"))
        data = curl_path.read_bytes()
        manifest.append({
            "id": "hnx-vhe-fy2025-curl", "company": "VHE", "period": "FY2025",
            "url": "https://owa.hnx.vn/ftp///cims/2026/3_W4/000000016025637_VI_BaoCaoTaiChinh_Nam_2025_BaoCaoHopNhat.pdf",
            "discovered_from": "hnx-vhe-curl.html attachment link", "transport": "curl 8.13.0 Schannel",
            "ok": True, "status": 200, "kind": "pdf", "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest(), "pages": inspection["pages"],
            "text_pages": inspection["text_pages"], "tls_verified": True,
            "download_seconds_observed": 1.223809,
            "retrieved_date": "2026-10-03", "retrieved_at_exact": None,
        })
    # Publish reproducible evidence metadata, not machine-specific absolute paths.
    cleaned = []
    for record in manifest:
        row = {key: value for key, value in record.items()
               if key not in ("file", "links_file", "inspection_file")}
        cleaned.append(row)
    (report / "download-evidence.json").write_text(json.dumps(cleaned, ensure_ascii=False, indent=2), encoding="utf-8")

    checks = []
    for document, targets in TARGETS.items():
        for metric, (page, pattern, reviewed_value) in targets.items():
            text_path = evidence / "ocr" / f"{document}-p{page:02}-ocr.txt"
            lines = text_path.read_text(encoding="utf-8").splitlines()
            candidates = []
            for index, line in enumerate(lines):
                if re.search(pattern, fold(line)):
                    window = " ".join(lines[index:index + 3])
                    amounts = re.findall(r"\(?\d{1,3}(?:[.,]\d{3}){2,}\)?", window)
                    if amounts:
                        raw = amounts[0]
                        value = int(re.sub(r"\D", "", raw)) * (-1 if raw.startswith("(") else 1)
                        candidates.append({"raw": raw, "value_vnd": value, "context": window})
            candidate = candidates[0] if candidates else None
            checks.append({
                "document": document, "metric": metric, "pdf_page": page,
                "printed_page": page - (1 if document.startswith("vnm") else 2),
                "candidate": candidate, "visually_reviewed_vnd": reviewed_value,
                "candidate_matches_visual": candidate is not None and candidate["value_vnd"] == reviewed_value,
                "review_note": "Same agent selected pages, wrote extraction rules, and reviewed images; not independent gold.",
            })
    (report / "ocr-core-check.json").write_text(json.dumps(checks, ensure_ascii=False, indent=2), encoding="utf-8")
    run = json.loads((evidence / "ocr" / "ocr-run.json").read_text(encoding="utf-8"))
    pdfs = [r for r in manifest if r.get("ok") and r.get("kind") == "pdf"]
    stats = {
        "summary_generated_at": datetime.now(timezone.utc).isoformat(),
        "pdf_files_downloaded": len(pdfs),
        "pdf_companies": sorted({r["company"] for r in pdfs}),
        "pdf_files_zero_text_pages": sum(r.get("text_pages") == 0 for r in pdfs),
        "total_pdf_pages": sum(r["pages"] for r in pdfs),
        "six_metric_documents_reviewed": len(TARGETS),
        "ocr_core_candidates": len(checks),
        "ocr_candidates_matching_visual": sum(c["candidate_matches_visual"] for c in checks),
        "ocr_pages": len(run["results"]),
        "ocr_total_seconds": sum(r["elapsed_seconds"] for r in run["results"]),
        "ocr_median_seconds": statistics.median(r["elapsed_seconds"] for r in run["results"]),
        "ocr_initialization_seconds": run["initialization_seconds"],
        "runtime": {"python": sys.version.split()[0], "node_observed": "24.15.0", "tesseract_js": run["tesseract_js_version"], "languages": run["languages"]},
        "balance_residuals_vnd": {
            document: values["total_assets"][2] - values["total_liabilities"][2] - values["total_equity"][2]
            for document, values in TARGETS.items()
        },
        "warning": "Convenience sample and selected-page OCR check; not full market coverage, end-to-end accuracy or independent benchmark.",
    }
    (report / "probe-summary.json").write_text(json.dumps(stats, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(stats, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
