"""Parse four saved VSDC notices; development examples, not market coverage.

Usage: python extract_recent_dividend_examples.py <evidence-dir> <output-json>
Scheduled payment is never promoted to confirmed payment by this script.
"""
import hashlib
import json
import re
import sys
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path


class Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.hidden = 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.hidden += 1
        if tag in ("p", "div", "tr", "td", "br", "h1", "h2", "h3", "li"):
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.hidden = max(0, self.hidden - 1)
        if tag in ("p", "div", "tr", "td", "h1", "h2", "h3", "li"):
            self.parts.append("\n")

    def handle_data(self, data):
        if not self.hidden:
            self.parts.append(data)


SAMPLES = [
    ("vnm-dividend-2025", "VNM", "https://vsdc.vn/vi/ad1/197038"),
    ("vnm-dividend-2025-mixed", "VNM", "https://vsdc.vn/vi/ad1/187729"),
    ("dhg-dividend-2025-final", "DHG", "https://vsdc.vn/vi/ad1/199544"),
    ("dhg-dividend-2025-first", "DHG", "https://vsdc.vn/ad/195056"),
]


def required(pattern, text):
    match = re.search(pattern, text, re.I)
    if not match:
        raise ValueError(f"Missing field: {pattern}")
    return match.group(1)


def iso_date(value):
    return datetime.strptime(value, "%d/%m/%Y").date().isoformat()


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    evidence, output = Path(sys.argv[1]), Path(sys.argv[2])
    manifest = {r["id"]: r for r in json.loads((evidence / "manifest.json").read_text(encoding="utf-8"))}
    events = []
    amount_pattern = r"(?:được nhận|nhận được)\s+([\d.]+)\s+đồng"
    for identifier, expected_ticker, url in SAMPLES:
        raw = (evidence / (identifier + ".html")).read_bytes()
        parser = Text()
        parser.feed(raw.decode("utf-8"))
        lines = [" ".join(line.split()) for line in "".join(parser.parts).splitlines() if line.strip()]
        start = next(i for i, line in enumerate(lines) if line.startswith(expected_ticker + ":"))
        stop = next(i for i in range(start + 1, len(lines)) if lines[i] == "Tin cùng tổ chức")
        lines = lines[start:stop]
        text = "\n".join(lines)
        ticker = required(r"Mã chứng khoán:\s*(\w+)", text)
        if ticker != expected_ticker or "bằng tiền" not in text:
            raise ValueError("Wrong ticker or unsupported non-cash notice")
        amounts = re.findall(amount_pattern, text, re.I)
        total = int(amounts[0].replace(".", ""))
        components = []
        if len(amounts) > 1:
            for line in lines:
                amount = re.search(amount_pattern, line, re.I)
                year = re.search(r"(?:năm\s*|/)(20\d{2})", line, re.I)
                if amount and year:
                    components.append({"profit_year": int(year.group(1)), "dps_vnd": int(amount.group(1).replace(".", ""))})
        else:
            components = [{"profit_year": int(required(r"(20\d{2})", lines[0])), "dps_vnd": total}]
        if not components or sum(c["dps_vnd"] for c in components) != total:
            raise ValueError("Year-component reconciliation failed")
        updated = required(r"Cập nhật ngày\s*(\d{1,2}/\d{1,2}/\d{4}\s*-\s*\d{2}:\d{2}:\d{2})", text)
        events.append({
            "id": identifier, "ticker": ticker, "source_url": url,
            "source_sha256": hashlib.sha256(raw).hexdigest(),
            "retrieved_at": manifest[identifier]["retrieved_at"],
            "title": lines[0], "event_kind": "cash_dividend_notice",
            "published_at_as_displayed": updated,
            "published_date": iso_date(updated.split(" - ")[0]),
            "displayed_timezone": None,
            "record_date": iso_date(required(r"Ngày đăng ký cuối cùng:\s*(\d{1,2}/\d{1,2}/\d{4})", text)),
            "scheduled_payment_date": iso_date(required(r"Ngày thanh toán:\s*(\d{1,2}/\d{1,2}/\d{4})", text)),
            "par_value_vnd": int(required(r"Mệnh giá:\s*([\d.]+)\s*đồng", text).replace(".", "")),
            "total_dps_vnd": total, "profit_year_components": components,
            "paid_status": "scheduled", "confirmed_paid_at": None,
            "source_locator": "Main notice before Tin cùng tổ chức; table labels and payment bullets",
            "review_status": "checked_against_official_notice_text_by_same_agent",
            "warning": "Not an independent benchmark; not a complete annual dividend history or proof of actual payment.",
        })
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(events, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"notices": len(events), "components": sum(len(e["profit_year_components"]) for e in events), "all_scheduled": all(e["paid_status"] == "scheduled" for e in events)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
