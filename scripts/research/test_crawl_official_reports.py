"""Offline regression and three-run update tests; no requests to live sites."""
import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from pypdf import PdfWriter

import crawl_official_reports as crawler


class ClassificationTests(unittest.TestCase):
    def test_half_year_is_not_annual_even_when_year_matches(self):
        for title in ["VHC_Consolidated FS for the first half 2025_VN", "BCTC hợp nhất đã soát xét 30.06.2025", "BCTC hợp nhất 6 tháng 2025"]:
            c = crawler.classify(title, "https://example.test/report.pdf")
            self.assertEqual(c["period_candidate"], "H1-2025")
            self.assertFalse(c["eligible"])

    def test_quarter_before_annual_and_short_year(self):
        for title in ["FY2025-Q3.25-Consolidated-FS-Non-Reviewed-VN", "BCTC hợp nhất Quý IV năm 2025", "BCTC hợp nhất Quý 4/2025"]:
            c = crawler.classify(title, "https://example.test/report.pdf")
            self.assertTrue(c["period_candidate"].startswith("Q"))
            self.assertFalse(c["eligible"])

    def test_upload_year_is_not_report_year(self):
        c = crawler.classify("BCTC hợp nhất năm 2025 sau kiểm toán", "https://example.test/2026/20260327-bctc.pdf")
        self.assertEqual(c["period_candidate"], "FY-2025")
        self.assertTrue(c["eligible"])

    def test_combined_fs_file_can_contain_explanation(self):
        c = crawler.classify("Báo cáo tài chính hợp nhất soát xét 6 tháng 2026", "https://example.test/bctc-6-thang-2026-va-giai-trinh.pdf")
        self.assertTrue(c["eligible"])
        self.assertFalse(crawler.classify("Giải trình BCTC năm 2025", "https://example.test/giai-trinh.pdf")["eligible"])

    def test_overview_and_separate_are_not_target_fs(self):
        for title in ["Tổng quan tình hình kinh doanh Quý II/2026", "BCTC riêng năm 2025 sau kiểm toán", "VHC_Reviewed-Separate-FS_6M2026_VN"]:
            self.assertFalse(crawler.classify(title, "https://example.test/report.pdf")["eligible"])

    def test_language_variants_not_both_selected(self):
        self.assertFalse(crawler.classify("VHC Reviewed Consolidated FS 6M2026 EN", "https://example.test/report_EN.pdf")["eligible"])

    def test_pagination_and_duplicate_download_anchor(self):
        source = next(s for s in crawler.SOURCES if s["company"] == "DHG")
        body = '''<div class="share-holders-body">21 Tháng 3, 2026
        <a href="/report.pdf">BCTC năm 2025 đã kiểm toán</a><a href="/report.pdf">Download</a></div>
        <a href="?page=13">Last</a><a href="?page=1">Next</a><a href="?page=0">1</a>'''.encode()
        candidates, pages = crawler.discover(body, source, source["catalog"])
        self.assertEqual(len(candidates), 1)
        self.assertEqual(candidates[0]["publication_date_evidence"], "21 Tháng 3, 2026")
        self.assertTrue(pages[0].endswith("page=1"))


class TransportAndStorageTests(unittest.TestCase):
    def test_wildcard_pdf_disallow_and_query_disallow(self):
        text = "User-agent: *\nDisallow: /*.pdf$\nDisallow: /*?\nAllow: /public.pdf"
        self.assertFalse(crawler.robots_decision(text, "https://example.test/a/report.pdf")["allowed"])
        self.assertFalse(crawler.robots_decision(text, "https://example.test/catalog?page=2")["allowed"])
        self.assertTrue(crawler.robots_decision(text, "https://example.test/public.pdf")["allowed"])

    def test_unknown_switch_never_overrides_known_disallow(self):
        with tempfile.TemporaryDirectory() as tmp:
            client = crawler.Client(Path(tmp), ["example.test"], allow_unknown=True)
            client.policies["https://example.test"] = {"state": "parsed_pilot_rules", "text": "User-agent: *\nDisallow: /private/"}
            self.assertFalse(client.policy("https://example.test/private/a.pdf")["allowed"])

    def test_html_masquerading_as_pdf_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(ValueError):
                crawler.persist_pdf(b"<html>Access denied</html>", Path(tmp))

    def test_url_host_and_tls_scheme_allowlist(self):
        with tempfile.TemporaryDirectory() as tmp:
            client = crawler.Client(Path(tmp), ["example.test"])
            for url in ["http://example.test/a.pdf", "https://other.test/a.pdf", "https://user:pass@example.test/a.pdf"]:
                with self.assertRaises(ValueError):
                    client.fetch(url)

    def test_content_hash_idempotence_and_corruption_detection(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            digest, relative = crawler.persist_pdf(b"%PDF-fixture", root)
            self.assertEqual(crawler.persist_pdf(b"%PDF-fixture", root)[0], digest)
            self.assertEqual(len(list((root / "pdf").glob("*.pdf"))), 1)
            (root / relative).write_bytes(b"corrupt")
            with self.assertRaises(ValueError):
                crawler.persist_pdf(b"%PDF-fixture", root)

    def test_three_run_history_304_and_changed_content(self):
        def pdf(n):
            writer = PdfWriter()
            for _ in range(n):
                writer.add_blank_page(width=100, height=100)
            out = io.BytesIO()
            writer.write(out)
            return out.getvalue()

        body = '<div class="share-holders-body"><a href="/report.pdf">BCTC năm 2025 đã kiểm toán</a></div>'.encode()
        mode, observed = [0], []

        def fetch(client, url, headers=None):
            if url.endswith("robots.txt"):
                return 200, {}, b"User-agent: *\nAllow: /"
            if url.endswith("report.pdf"):
                observed.append(headers)
                if mode[0] == 1:
                    return 304, {}, b""
                return 200, {"ETag": '"version-' + str(mode[0]) + '"'}, pdf(1 if mode[0] == 0 else 2)
            return 200, {}, body

        with tempfile.TemporaryDirectory() as tmp, patch.object(crawler.Client, "fetch", fetch), contextlib.redirect_stdout(io.StringIO()):
            for i in range(3):
                mode[0] = i
                with patch.object(crawler.sys, "argv", ["crawler", tmp, "--companies", "DHG"]):
                    crawler.main()
            history = json.loads((Path(tmp) / "history.json").read_text())
            versions = history["https://dhgpharma.com.vn/report.pdf"]
            self.assertEqual(len(versions), 2)
            self.assertEqual([v["pdf_pages"] for v in versions], [1, 2])
            self.assertEqual(len(list((Path(tmp) / "pdf").glob("*.pdf"))), 2)
            self.assertEqual(observed[1], {"If-None-Match": '"version-0"'})


if __name__ == "__main__":
    unittest.main()
