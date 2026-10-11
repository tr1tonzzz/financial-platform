"""Đọc lớp chữ PDF và xác định trang cần OCR."""
import argparse
import json
from pathlib import Path

from pypdf import PdfReader


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, nargs="?", default=Path("output"))
    root = parser.parse_args().output.resolve()
    reader = PdfReader(root / "sample.pdf")
    pages = []
    # Đánh số từ 1 để khớp số trang PDF trong báo cáo.
    for number, page in enumerate(reader.pages, 1):
        error = None
        try:
            # pypdf có thể trả None; chuyển thành chuỗi rỗng để lưu và đếm ký tự.
            text = page.extract_text() or ""
        except Exception as exception:
            text = ""
            error = str(exception)
        (root / f"page-{number}-pdf.txt").write_text(text, encoding="utf-8")
        item = {"pdf_page": number, "text_chars": len(text), "has_text": bool(text.strip())}
        if error:
            item["error"] = error
        pages.append(item)
    targets = (12, 13, 14)
    if len(pages) < max(targets):
        raise RuntimeError("Sample PDF does not contain all target pages 12, 13, 14.")
    # Danh sách Python bắt đầu từ 0 nên trang PDF N được tra tại vị trí N-1.
    needed = [page for page in targets if not pages[page - 1]["has_text"]]
    result = {"pdf_pages": len(pages), "pages": pages, "target_pages": list(targets),
              "ocr_pages": needed}
    (root / "pdf-probe.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(f"PDF pages: {len(pages)}; pages with text: {sum(item['has_text'] for item in pages)}")
    print(f"Target pages needing OCR: {needed}" if needed else "Target pages have text. Skip render/OCR and run extract_numbers.py.")


if __name__ == "__main__":
    main()
