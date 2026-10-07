"""Bounded Vinamilk Q1/2026 catalog discovery and PDF text probe.

Reuses the research crawler's host, robots, timeout and size controls.
No PDF seed: selects one consolidated Q1/2026 link from live catalog HTML.
"""
import argparse
import json
from pathlib import Path
from urllib.parse import urljoin, urlsplit

from lxml import html
from pypdf import PdfReader
from crawl_official_reports import Client, clean, fold, persist_pdf, utc

CATALOG = "https://www.vinamilk.com.vn/investor/reports/financial"
HOSTS = ["www.vinamilk.com.vn", "d8um25gjecm9v.cloudfront.net"]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path)
    parser.add_argument("--allow-unknown-robots", action="store_true", help="Bounded public-file probe; never overrides parsed Disallow")
    args = parser.parse_args()
    root = args.output.resolve()
    root.mkdir(parents=True, exist_ok=True)
    client = Client(root, HOSTS, args.allow_unknown_robots)
    run = {"started_at": utc(), "catalog_url": CATALOG, "budget": "1 catalog, 1 PDF", "allow_unknown_robots": args.allow_unknown_robots, "candidates": []}
    try:
        policy = client.policy(CATALOG)
        run["catalog_robots"] = policy
        if not policy["allowed"]:
            raise RuntimeError("Catalog robots policy prevents fetch")
        status, _, body = client.fetch(CATALOG)
        (root / "catalog.html").write_bytes(body)
        run["catalog_status"] = status
        for anchor in html.fromstring(body).xpath("//a[@href]"):
            url = urljoin(CATALOG, anchor.get("href"))
            if not urlsplit(url).path.lower().endswith(".pdf"):
                continue
            title = clean(anchor.text_content())
            run["candidates"].append({"title": title, "url": url})
        selected = [item for item in run["candidates"] if "2026" in item["title"] and "Q1" in item["title"] and "bao cao tai chinh hop nhat" in fold(item["title"])]
        if len(selected) != 1:
            raise RuntimeError("Expected exactly one consolidated Q1/2026 candidate")
        item = selected[0]
        run["selected"] = item
        policy = client.policy(item["url"])
        run["pdf_robots"] = policy
        if not policy["allowed"]:
            raise RuntimeError("PDF robots policy prevents fetch")
        status, headers, body = client.fetch(item["url"])
        digest, relative = persist_pdf(body, root)
        run.update(pdf_status=status, pdf_sha256=digest, pdf_path=relative, pdf_bytes=len(body), etag=headers.get("ETag"))
        reader = PdfReader(root / relative)
        pages = []
        for number, page in enumerate(reader.pages, 1):
            text = page.extract_text() or ""
            (root / f"page-{number:02d}.txt").write_text(text, encoding="utf-8")
            pages.append({"pdf_page": number, "text_chars": len(text)})
        run["pages"] = pages
    except Exception as error:
        run["error"] = str(error)
        raise
    finally:
        run.update(finished_at=utc(), requests=client.requests, robots=client.policies)
        (root / "source-probe.json").write_text(json.dumps(run, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({key: run[key] for key in ("pdf_sha256", "pdf_path", "pages")}, ensure_ascii=False))


if __name__ == "__main__":
    main()
