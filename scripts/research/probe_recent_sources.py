"""Small reproducible public-source probe; not a production crawler.

Usage: python probe_recent_sources.py seeds.json output_directory
Seeds: [{"id": "...", "url": "...", ...}], all metadata preserved.
TLS verification remains enabled. Existing successful downloads are reused.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path

MAX_BYTES = 30 * 1024 * 1024
USER_AGENT = "FinancialAnalysisPlatform-ResearchProbe/0.1"


class Links(HTMLParser):
    def __init__(self, base):
        super().__init__()
        self.base = base
        self.links = []
        self.current = None

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if tag == "a" and values.get("href"):
            self.current = {
                "url": urllib.parse.urljoin(self.base, values["href"]),
                "text": "",
                "attributes": values,
            }

    def handle_data(self, data):
        if self.current is not None:
            self.current["text"] += data + " "

    def handle_endtag(self, tag):
        if tag == "a" and self.current is not None:
            self.current["text"] = " ".join(self.current["text"].split())
            self.links.append(self.current)
            self.current = None


def fold(value):
    return "".join(c for c in unicodedata.normalize("NFD", value.lower()) if not unicodedata.combining(c)).replace("đ", "d")


def inspect_pdf(path, output):
    import pdfplumber

    patterns = {
        "cash_equivalents": r"tien va (?:cac khoan )?tuong duong tien|cash and cash equivalents",
        "total_assets": r"tong (?:cong )?tai san|total assets",
        "total_liabilities": r"^no phai tra\b|total liabilities",
        "total_equity": r"^von chu so huu\b|total equity|^owners.? equity",
        "net_income_total": r"loi nhuan sau thue thu nhap doanh nghiep|loi nhuan sau thue \(?60|net profit after tax|profit after tax|net profit for the (?:year|period)",
        "cfo": r"luu chuyen tien (?:thuan|tuan) tu hoat dong kinh doanh|net cash (?:flows? )?(?:generated from|from|used in) operating activities",
    }
    pages = []
    hits = {key: [] for key in patterns}
    with pdfplumber.open(path) as pdf:
        for i, page in enumerate(pdf.pages, 1):
            content = page.extract_text() or ""
            pages.append({"page": i, "chars": len(content)})
            (output / f"{path.stem}-page-{i:03}.txt").write_text(content, encoding="utf-8")
            for line in content.splitlines():
                normalized = fold(line)
                for key, pattern in patterns.items():
                    if re.search(pattern, normalized):
                        hits[key].append({"page": i, "line": line})
    return {
        "pages": len(pages),
        "text_pages": sum(p["chars"] > 100 for p in pages),
        "page_text_counts": pages,
        "label_candidates": hits,
        "warning": "Label hits are candidates, not validated extracted facts or gold accuracy.",
    }


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    seeds = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8-sig"))
    output = Path(sys.argv[2]).resolve()
    output.mkdir(parents=True, exist_ok=True)
    manifest_path = output / "manifest.json"
    previous = json.loads(manifest_path.read_text(encoding="utf-8")) if manifest_path.exists() else []
    records = {r["id"]: r for r in previous}
    for seed in seeds:
        if not re.fullmatch(r"[a-zA-Z0-9_-]+", seed["id"]):
            raise ValueError("Seed id must be a plain safe file name")
        cached = records.get(seed["id"])
        if cached and cached.get("ok") and cached.get("url") == seed["url"]:
            print(json.dumps({"id": seed["id"], "cached": True}), flush=True)
            continue
        started = time.monotonic()
        record = dict(seed)
        record["retrieved_at"] = datetime.now(timezone.utc).isoformat()
        if seed.get("probe_allowed") is False:
            record.update(ok=False, skipped=True, error=seed.get("skip_reason", "Seed excluded from automated probe"))
            records[seed["id"]] = record
            manifest_path.write_text(json.dumps(list(records.values()), ensure_ascii=False, indent=2), encoding="utf-8")
            print(json.dumps({"id": seed["id"], "skipped": True, "reason": record["error"]}), flush=True)
            continue
        try:
            request = urllib.request.Request(seed["url"], headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(request, timeout=20) as response:
                data = response.read(MAX_BYTES + 1)
                if len(data) > MAX_BYTES:
                    raise ValueError("Download exceeded 30 MiB probe limit")
                record.update(status=response.status, final_url=response.url,
                              content_type=response.headers.get("Content-Type"),
                              last_modified=response.headers.get("Last-Modified"))
            record.update(ok=True, bytes=len(data), sha256=hashlib.sha256(data).hexdigest())
            if data.startswith(b"%PDF"):
                path = output / (seed["id"] + ".pdf")
                path.write_bytes(data)
                record["file"] = str(path)
                record["kind"] = "pdf"
                try:
                    inspection = inspect_pdf(path, output)
                    inspection_path = output / (seed["id"] + "-inspection.json")
                    inspection_path.write_text(json.dumps(inspection, ensure_ascii=False, indent=2), encoding="utf-8")
                    record.update(pages=inspection["pages"], text_pages=inspection["text_pages"],
                                  candidate_metric_count=sum(bool(v) for v in inspection["label_candidates"].values()),
                                  inspection_file=str(inspection_path))
                except Exception as exc:
                    record["inspection_error"] = str(exc)
            else:
                path = output / (seed["id"] + ".html")
                path.write_bytes(data)
                record.update(file=str(path), kind="html_or_text")
                content = data.decode("utf-8", errors="replace")
                parser = Links(record["final_url"])
                parser.feed(content)
                anchors_path = output / (seed["id"] + "-links.json")
                anchors_path.write_text(json.dumps(parser.links, ensure_ascii=False, indent=2), encoding="utf-8")
                record["links_file"] = str(anchors_path)
                record["link_count"] = len(parser.links)
        except Exception as exc:
            record.update(ok=False, error_type=type(exc).__name__, error=str(exc))
            if isinstance(exc, urllib.error.HTTPError):
                record["status"] = exc.code
        record["elapsed_seconds"] = round(time.monotonic() - started, 3)
        records[seed["id"]] = record
        manifest_path.write_text(json.dumps(list(records.values()), ensure_ascii=False, indent=2), encoding="utf-8")
        print(json.dumps({key: record.get(key) for key in
                          ("id", "ok", "status", "kind", "bytes", "pages", "text_pages", "candidate_metric_count", "error")}, ensure_ascii=False), flush=True)
        time.sleep(1)


if __name__ == "__main__":
    main()
