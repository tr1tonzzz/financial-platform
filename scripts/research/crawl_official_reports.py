"""Bounded research crawler: official HTML catalogs -> classified PDF -> hash history.

No PDF URL seeds, browser automation, login or disabled TLS verification.
Requires lxml and pypdf. Research prototype, not a market-wide production service.
"""
from __future__ import annotations

import argparse
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
from pathlib import Path

from lxml import html
from pypdf import PdfReader

UA = "FinancialAnalysisPlatform-ResearchCrawler/0.2"
LIMIT = 30 * 1024 * 1024
SOURCES = [
    {"company": "HPG", "catalog": "https://www.hoaphat.com.vn/quan-he-co-dong/bao-cao-tai-chinh", "hosts": ["www.hoaphat.com.vn", "file.hoaphat.com.vn"], "adapter": "hoaphat"},
    {"company": "DHG", "catalog": "https://dhgpharma.com.vn/vi/bao-cao-tai-chinh", "hosts": ["dhgpharma.com.vn"], "adapter": "dhg", "first_page": 0},
    {"company": "VHC", "catalog": "https://www.vinhhoan.com/investors-2/", "hosts": ["www.vinhhoan.com"], "adapter": "vhc"},
    {"company": "HPA", "catalog": "https://nongnghiep.hoaphat.com.vn/quan-he-co-dong/bao-cao-tai-chinh", "hosts": ["nongnghiep.hoaphat.com.vn", "file.hoaphat.com.vn"], "adapter": "hoaphat"},
]


def utc():
    return datetime.now(timezone.utc).isoformat()


def fold(s):
    return "".join(c for c in unicodedata.normalize("NFD", s.lower()) if not unicodedata.combining(c)).replace("đ", "d")


def clean(s):
    return " ".join(s.split())


def classify(title, url):
    """Metadata candidates only; financial facts must later confirm PDF headers."""
    s = fold(title + " " + urllib.parse.unquote(urllib.parse.urlsplit(url).path.rsplit("/", 1)[-1]))
    s = re.sub(r"[_\-]+", " ", s)
    title_s = fold(title)
    full_title = any(x in title_s for x in ("bao cao tai chinh", "bctc", "financial statement", "consolidated fs"))
    exclusion_s = title_s if full_title else s
    if any(x in exclusion_s for x in ("giai trinh", "explanation", "variance", "tong quan", "overview", "cong van", "cbtt")):
        return {"eligible": False, "reason": "supplement_or_notice"}
    if not any(x in s for x in ("bao cao tai chinh", "bctc", "financial statement", " fs ")):
        return {"eligible": False, "reason": "not_financial_statement"}
    # Quarter markers take precedence over FY/year markers; upload year is not report year.
    q = re.search(r"(?:\bq(?:uy)?\s*([1-4])\s*[./ ]?\s*(?:nam\s*)?(20\d{2}|\d{2})\b|quy\s+(iv|iii|ii|i)\s*[/ ]?\s*(?:nam\s*)?(20\d{2}))", s)
    if q:
        n = int(q[1]) if q[1] else {"i": 1, "ii": 2, "iii": 3, "iv": 4}[q[3]]
        year = q[2] or q[4]
        period = f"Q{n}-{year if len(year) == 4 else '20' + year}"
    elif h := re.search(r"(?:6\s*(?:thang|t\b|m)|ban nien|first half|half.year|h1).*?(20\d{2})", s):
        period = "H1-" + h[1]
    elif h := re.search(r"30[./ ]0?6[./ ](20\d{2})", s):
        period = "H1-" + h[1]  # Calendar-year candidate; confirm start date inside PDF.
    elif year := re.search(r"\b20\d{2}\b", s):
        period = "FY-" + year[0]
    else:
        period = "unknown"
    scope = "consolidated" if any(x in s for x in ("hop nhat", "consolidated")) else "separate" if any(x in s for x in ("rieng", "cong ty me", "separate")) else "unknown"
    if "non reviewed" in s or "unaudited" in s or "chua kiem toan" in s:
        assurance = "unreviewed"
    elif "kiem toan" in s or "audited" in s:
        assurance = "audited"
    elif "soat xet" in s or "reviewed" in s:
        assurance = "reviewed"
    else:
        assurance = "unknown"
    language = "en" if re.search(r"\ben(?:\.pdf|\b)", s) or ("financial statement" in s and not re.search(r"\bvn\b", s)) else "vi_or_unknown"
    eligible = period in ("FY-2025", "H1-2026") and scope != "separate" and language != "en"
    return {"eligible": eligible, "reason": "selected_period_scope_language" if eligible else "outside_pilot_filter", "period_candidate": period, "scope_candidate": scope, "assurance_candidate": assurance, "language_candidate": language}


def discover(body, source, page_url):
    tree = html.fromstring(body.decode("utf-8-sig", errors="replace"))
    found = {}
    for a in tree.xpath("//a[@href]"):
        url = urllib.parse.urljoin(page_url, a.get("href"))
        if not urllib.parse.urlsplit(url).path.lower().endswith(".pdf"):
            continue
        title = clean(a.text_content())
        if source["adapter"] == "hoaphat":
            rows = a.xpath("ancestor::div[contains(concat(' ',normalize-space(@class),' '),' item ')][1]")
        elif source["adapter"] == "dhg":
            rows = a.xpath("ancestor::div[contains(concat(' ',normalize-space(@class),' '),' share-holders-body ')][1]")
        else:
            rows = [a.getparent()]
        row = rows[0] if rows else a.getparent()
        context = clean(row.text_content())
        dates = re.findall(r"\b\d{1,2}/\d{1,2}/20\d{2}\b|\d{1,2}\s+Tháng\s+\d{1,2},\s+20\d{2}", context)
        record = {"company": source["company"], "url": url, "catalog_url": page_url, "anchor_title": title, "context": context[:900], "publication_date_evidence": dates[0] if dates else None, "metadata_status": "candidate_from_catalog"}
        record.update(classify(title, url))
        if url not in found or (title.lower() != "download" and len(title) > len(found[url]["anchor_title"])):
            found[url] = record
    # Follow only observed next/page-2 links on the same catalog path, never arbitrary links.
    next_pages = []
    current_page = int(urllib.parse.parse_qs(urllib.parse.urlsplit(page_url).query).get("page", [source.get("first_page", 1)])[0])
    for a in tree.xpath("//a[@href]"):
        url = urllib.parse.urljoin(page_url, a.get("href"))
        p, b = urllib.parse.urlsplit(url), urllib.parse.urlsplit(source["catalog"])
        page_values = urllib.parse.parse_qs(p.query).get("page", [])
        if p.hostname == b.hostname and p.path == b.path and page_values and page_values[0].isdigit() and int(page_values[0]) > current_page:
            next_pages.append(url)
    return list(found.values()), sorted(set(next_pages), key=lambda u: int(urllib.parse.parse_qs(urllib.parse.urlsplit(u).query)["page"][0]))


def robots_decision(text, url):
    """Conservative common robots rules for this pilot, NOT a full RFC9309 parser.

    Applies wildcard group plus any matching named group (can over-block).
    Supports * and trailing $, longest literal match, Allow wins ties.
    """
    path = urllib.parse.unquote(urllib.parse.urlsplit(url).path or "/")
    query = urllib.parse.urlsplit(url).query
    path += ("?" + query) if query else ""
    agents, rules, groups = [], [], []
    for raw in text.splitlines() + ["User-agent: __end__"]:
        line = raw.split("#", 1)[0].strip()
        if ":" not in line:
            continue
        key, value = (s.strip() for s in line.split(":", 1))
        key = key.lower()
        if key == "user-agent":
            if rules:
                groups.append((agents, rules))
                agents, rules = [], []
            agents.append(value.lower())
        elif key in ("allow", "disallow", "crawl-delay") and agents:
            rules.append((key, value))
    matches, delays = [], []
    for agents, rules in groups:
        if not any(a == "*" or a in UA.lower() for a in agents):
            continue
        for key, value in rules:
            if key == "crawl-delay":
                try:
                    delays.append(float(value))
                except ValueError:
                    pass
                continue
            if not value:
                continue
            end = value.endswith("$")
            regex = "^" + re.escape(value[:-1] if end else value).replace(r"\*", ".*") + ("$" if end else "")
            if re.search(regex, path):
                matches.append((len(value.replace("*", "").rstrip("$")), key == "allow", value))
    best = max(matches, default=(0, True, ""))
    return {"allowed": best[1], "matched_rule": best[2], "crawl_delay": max(delays, default=0)}


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None  # No unchecked redirected host or robots bypass in this prototype.


class Client:
    def __init__(self, root, hosts, allow_unknown=False):
        self.root, self.hosts, self.allow_unknown = root, set(hosts), allow_unknown
        self.policies, self.requests, self.last, self.delays = {}, [], {}, {}
        self.opener = urllib.request.build_opener(NoRedirect)

    def fetch(self, url, headers=None):
        p = urllib.parse.urlsplit(url)
        if p.scheme != "https" or p.hostname not in self.hosts or p.username or p.password:
            raise ValueError("URL outside HTTPS host allowlist")
        for attempt in range(2):
            delay = max(1.0, self.delays.get(p.netloc, 0))
            time.sleep(max(0, delay - (time.monotonic() - self.last.get(p.netloc, 0))))
            started = time.monotonic()
            event = {"url": url, "started_at": utc(), "attempt": attempt + 1}
            try:
                req = urllib.request.Request(url, headers={"User-Agent": UA, **(headers or {})})
                with self.opener.open(req, timeout=20) as response:
                    content = response.read(LIMIT + 1)
                    if len(content) > LIMIT:
                        raise ValueError("Response exceeds 30 MiB limit")
                    event.update(status=response.status, bytes=len(content))
                    return response.status, dict(response.headers.items()), content
            except urllib.error.HTTPError as e:
                event["status"] = e.code
                if e.code == 304:
                    return 304, dict(e.headers.items()), b""
                if attempt == 0 and e.code in (429, 500, 502, 503, 504):
                    retry = e.headers.get("Retry-After", "2")
                    seconds = float(retry) if retry.isdigit() else 2
                    if seconds > 30:
                        raise RuntimeError("Retry-After exceeds bounded run; defer source") from e
                    time.sleep(max(2, seconds))
                    continue
                raise
            except Exception as e:
                event["error"] = type(e).__name__ + ": " + str(e)
                raise
            finally:
                self.last[p.netloc] = time.monotonic()
                event["seconds"] = round(time.monotonic() - started, 3)
                self.requests.append(event)

    def policy(self, url):
        p = urllib.parse.urlsplit(url)
        origin = p.scheme + "://" + p.netloc
        if origin not in self.policies:
            item = {"url": origin + "/robots.txt", "checked_at": utc()}
            try:
                status, headers, body = self.fetch(item["url"])
                text = body.decode("utf-8", errors="replace")
                item.update(http_status=status, sha256=hashlib.sha256(body).hexdigest())
                (self.root / (p.netloc + "-robots.txt")).write_bytes(body)
                if "<html" in text.lower() or "user-agent:" not in text.lower():
                    item["state"] = "unknown_non_robots_body"
                else:
                    item.update(state="parsed_pilot_rules", text=text)
            except urllib.error.HTTPError as e:
                item.update(http_status=e.code, state="absent_404" if e.code == 404 else "unknown_http_error")
            except Exception as e:
                item.update(state="unknown_fetch_error", error=str(e))
            self.policies[origin] = item
        item = self.policies[origin]
        if item["state"] == "parsed_pilot_rules":
            decision = robots_decision(item["text"], url)
            self.delays[p.netloc] = max(self.delays.get(p.netloc, 0), decision["crawl_delay"])
            return {"state": item["state"], **decision}
        return {"state": item["state"], "allowed": item["state"] == "absent_404" or self.allow_unknown, "unknown_policy_probe": item["state"] != "absent_404" and self.allow_unknown}


def persist_pdf(body, root):
    if not body.startswith(b"%PDF-"):
        raise ValueError("Downloaded response is not a PDF (magic check)")
    digest = hashlib.sha256(body).hexdigest()
    relative = "pdf/" + digest + ".pdf"
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and hashlib.sha256(path.read_bytes()).hexdigest() != digest:
        raise ValueError("Existing content-addressed file failed integrity check")
    if not path.exists():
        temp = path.with_suffix(".part")
        temp.write_bytes(body)
        temp.replace(path)
    return digest, relative


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("output", type=Path)
    ap.add_argument("--companies", default="HPG,DHG,VHC,HPA")
    ap.add_argument("--max-pages", type=int, default=1)
    ap.add_argument("--max-pdfs-per-company", type=int, default=2)
    ap.add_argument("--allow-unknown-robots", action="store_true", help="Explicit bounded public-file probe; never overrides parsed Disallow")
    args = ap.parse_args()
    if not 1 <= args.max_pages <= 3 or not 1 <= args.max_pdfs_per_company <= 3:
        ap.error("Research budgets: 1..3 pages and 1..3 PDFs per company")
    sources = [s for s in SOURCES if s["company"] in args.companies.split(",")]
    if not sources:
        ap.error("No supported company selected")
    root = args.output.resolve()
    root.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    run = {"run_id": stamp, "started_at": utc(), "config": {"companies": args.companies, "max_pages": args.max_pages, "max_pdfs_per_company": args.max_pdfs_per_company, "allow_unknown_robots": args.allow_unknown_robots}, "catalogs": [], "candidates": [], "downloads": []}
    history_path = root / "history.json"
    history = json.loads(history_path.read_text(encoding="utf-8")) if history_path.exists() else {}
    client = Client(root, [h for s in sources for h in s["hosts"]], args.allow_unknown_robots)
    for source in sources:
        queue, seen, candidates = [source["catalog"]], set(), {}
        while queue and len(seen) < args.max_pages:
            url = queue.pop(0)
            if url in seen:
                continue
            seen.add(url)
            event = {"company": source["company"], "url": url, "checked_at": utc()}
            try:
                event["robots"] = client.policy(url)
                if not event["robots"]["allowed"]:
                    event["result"] = "robots_skipped"
                    continue
                status, headers, body = client.fetch(url)
                filename = source["company"] + "-" + hashlib.sha256(url.encode()).hexdigest()[:12] + "-" + stamp + ".html"
                (root / filename).write_bytes(body)
                items, next_pages = discover(body, source, url)
                candidates.update({c["url"]: c for c in items})
                queue.extend(u for u in next_pages if u not in seen and u not in queue)
                event.update(result="live_html", status=status, sha256=hashlib.sha256(body).hexdigest(), bytes=len(body), saved_path=filename, pdf_links=len(items), observed_pagination=next_pages)
            except Exception as e:
                event.update(result="error", error=str(e))
            finally:
                run["catalogs"].append(event)
        all_candidates = list(candidates.values())
        run["candidates"].extend(all_candidates)
        eligible = sorted((c for c in all_candidates if c["eligible"]), key=lambda c: (c["period_candidate"] != "H1-2026", c["url"]))
        # One file per period in this pilot, so two variants cannot exhaust download budget.
        selected, periods = [], set()
        for c in eligible:
            if c["period_candidate"] not in periods:
                selected.append(c)
                periods.add(c["period_candidate"])
            if len(selected) == args.max_pdfs_per_company:
                break
        for c in selected:
            event = {**c, "checked_at": utc()}
            try:
                if urllib.parse.urlsplit(c["url"]).hostname not in source["hosts"]:
                    raise ValueError("PDF host not in company allowlist")
                event["robots"] = client.policy(c["url"])
                if not event["robots"]["allowed"]:
                    event["result"] = "robots_skipped"
                    continue
                old = history.get(c["url"], [])
                previous = old[-1] if old else None
                headers = {}
                if previous:
                    local = root / previous["saved_path"]
                    valid = local.exists() and hashlib.sha256(local.read_bytes()).hexdigest() == previous["sha256"]
                    if valid and previous.get("etag"):
                        headers["If-None-Match"] = previous["etag"]
                    elif valid and previous.get("last_modified"):
                        headers["If-Modified-Since"] = previous["last_modified"]
                status, response_headers, body = client.fetch(c["url"], headers)
                event.update(http_status=status, conditional_request=bool(headers))
                if status == 304:
                    if not previous or not headers:
                        raise ValueError("Unexpected 304 without a valid local version")
                    event.update(result="not_modified_304", sha256=previous["sha256"], saved_path=previous["saved_path"], bytes=0)
                else:
                    digest, relative = persist_pdf(body, root)
                    metadata = {k.lower(): v for k, v in response_headers.items()}
                    event.update(result="same_content_200" if previous and previous["sha256"] == digest else "downloaded_new_content", sha256=digest, saved_path=relative, bytes=len(body), etag=metadata.get("etag"), last_modified=metadata.get("last-modified"))
                    reader = PdfReader(root / relative)
                    texts = [p.extract_text() or "" for p in reader.pages[:12]]
                    event.update(pdf_pages=len(reader.pages), sampled_pages=len(texts), sampled_text_pages=sum(len(t) > 100 for t in texts))
                    textdir = root / "text" / digest
                    textdir.mkdir(parents=True, exist_ok=True)
                    for i, content in enumerate(texts, 1):
                        (textdir / f"page-{i:03}.txt").write_text(content, encoding="utf-8")
                    if not previous or previous["sha256"] != digest:
                        history.setdefault(c["url"], []).append({k: event[k] for k in ("sha256", "saved_path", "checked_at", "etag", "last_modified", "pdf_pages", "sampled_pages", "sampled_text_pages")})
                event["versions_for_url"] = len(history.get(c["url"], []))
            except Exception as e:
                event.update(result="error", error=str(e))
            finally:
                run["downloads"].append(event)
            print(source["company"], c["period_candidate"], event["result"], flush=True)
        print(source["company"], "catalogs", len(seen), "PDF candidates", len(all_candidates), "eligible", len(eligible), flush=True)
    run.update(finished_at=utc(), robots=[{k: v for k, v in item.items() if k != "text"} for item in client.policies.values()], requests=client.requests)
    for filename, payload in [("run-" + stamp + ".json", run), ("history.json", history), ("latest.json", run)]:
        (root / filename).write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"run_id": stamp, "catalogs": len(run["catalogs"]), "downloads": len(run["downloads"]), "results": [d["result"] for d in run["downloads"]]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
