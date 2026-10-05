"""Summarize final raw runs, check file hashes and execute offline regression tests."""
import hashlib
import importlib.metadata
import json
import platform
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "data-sets/research-evidence/2026-10-03-crawl-methods/verified"
OUTPUT = ROOT / "docs/research-crawl-methods/crawl-evidence.json"


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    runs = [json.loads(p.read_text(encoding="utf-8")) for p in sorted(RAW.glob("run-*.json"))]
    if len(runs) != 2:
        raise ValueError("This dated evidence expects exactly the final two runs; review new runs separately")
    first, second = runs
    expected = {(c, p) for c in ["HPG", "DHG", "VHC", "HPA"] for p in ["FY-2025", "H1-2026"]}
    assert {(d["company"], d["period_candidate"]) for d in first["downloads"]} == expected
    assert all(d["http_status"] == 200 and d["result"] == "downloaded_new_content" for d in first["downloads"])
    assert all(d["http_status"] == 304 and d["result"] == "not_modified_304" for d in second["downloads"])
    for d in first["downloads"]:
        assert hashlib.sha256((RAW / d["saved_path"]).read_bytes()).hexdigest() == d["sha256"]
    history = json.loads((RAW / "history.json").read_text(encoding="utf-8"))
    assert len(history) == 8 and sum(len(v) for v in history.values()) == 8
    assert len(list((RAW / "pdf").glob("*.pdf"))) == 8
    hashes = {d["sha256"] for d in first["downloads"]}
    # Human visual observations are bound to these hashes, not applied to future PDFs.
    manual_reviews = [
        {"sha256": "d2e2c906474f96651e27f99fb54afb05b6551641dcb56bc072c1f0184a469ef3", "company": "HPA", "pdf_page": 1, "review_date": "2026-10-03", "method": "human_visual_read_of_rendered_cover_110dpi", "scope": "consolidated", "assurance": "audited", "period_end": "2025-12-31", "cover_description": "Annual audited consolidated financial statements for year ended 31 December 2025", "financial_values_reviewed": 0},
        {"sha256": "e278d2dacc38acf7da010f05a1162a69371aa8d69b744171ddb72d9464efa019", "company": "HPA", "pdf_page": 1, "review_date": "2026-10-03", "method": "human_visual_read_of_rendered_cover_110dpi", "scope": "consolidated", "assurance": "reviewed", "period_end": "2026-06-30", "cover_description": "Reviewed interim consolidated financial statements for six-month period ended 30 June 2026", "financial_values_reviewed": 0},
    ]
    assert all(r["sha256"] in hashes for r in manual_reviews)
    test = subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", "scripts/research", "-p", "test_crawl_official_reports.py", "-v"], cwd=ROOT, capture_output=True, text=True, timeout=30)
    if test.returncode:
        raise RuntimeError(test.stdout + test.stderr)
    count = int(re.search(r"Ran (\d+) tests", test.stderr)[1])
    reports = [{k: d.get(k) for k in ["company", "period_candidate", "scope_candidate", "assurance_candidate", "language_candidate", "metadata_status", "anchor_title", "catalog_url", "url", "publication_date_evidence", "checked_at", "http_status", "robots", "sha256", "saved_path", "bytes", "etag", "last_modified", "pdf_pages", "sampled_pages", "sampled_text_pages"]} for d in first["downloads"]]
    summaries = [{"run_id": r["run_id"], "started_at": r["started_at"], "finished_at": r["finished_at"], "config": r["config"], "catalogs": r["catalogs"], "robots": r["robots"], "http_requests": r["requests"], "pdf_results": [{k: d.get(k) for k in ["company", "period_candidate", "url", "http_status", "result", "sha256", "bytes", "conditional_request", "versions_for_url"]} for d in r["downloads"]]} for r in runs]
    script = ROOT / "scripts/research/crawl_official_reports.py"
    payload = {
        "research_date": "2026-10-03", "timezone_for_logs": "UTC", "raw_directory_relative_to_repo": RAW.relative_to(ROOT).as_posix(),
        "script_sha256": hashlib.sha256(script.read_bytes()).hexdigest(),
        "runtime": {"python": platform.python_version(), "packages": {p: importlib.metadata.version(p) for p in ["lxml", "pypdf"]}},
        "summary": {"companies": 4, "catalog_pages_per_run": 7, "target_pdfs": 8, "total_pdf_pages": sum(d["pdf_pages"] for d in reports), "downloaded_pdf_bytes_first_run": sum(d["bytes"] for d in reports), "sampled_pages": sum(d["sampled_pages"] for d in reports), "sampled_pages_with_more_than_100_text_chars": sum(d["sampled_text_pages"] for d in reports), "second_run_304": 8, "pdf_bytes_second_run": 0, "unique_source_urls": len(history), "content_versions": sum(len(v) for v in history.values()), "pdfs_with_unknown_robots_probe": sum(d["robots"].get("unknown_policy_probe", False) for d in reports)},
        "reports": reports, "runs": summaries, "manual_cover_metadata_reviews": manual_reviews,
        "offline_tests": {"command": "python -m unittest discover -s scripts/research -p test_crawl_official_reports.py -v", "passed": count, "returncode": test.returncode, "output": test.stderr},
        "limitations": ["Selected sources and metadata classifier are a development sample, not an independent market-wide benchmark", "Only first 12 pages per PDF sampled for text; not all 423 pages", "No nine-field numerical extraction benchmark executed in this experiment", "file.hoaphat.com.vn robots HTTP 403 is unknown; explicit bounded-probe mode used, not a known Allow", "Changed-content history validated with synthetic offline PDF fixture; no live financial restatement observed", "Two development misclassification downloads outside final targets retained in parent directory and excluded here", "Current script filters FY2025 and H1-2026, not configurable full historical collection", "history JSON is a single-process research store, not transactional production storage"],
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(payload["summary"], ensure_ascii=False))
    print("Runtime:", payload["runtime"], "Tests:", count)


if __name__ == "__main__":
    main()
