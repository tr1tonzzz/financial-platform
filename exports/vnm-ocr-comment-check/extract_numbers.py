"""Trích LNST, CFO và tiền chi cổ tức từ văn bản PDF hoặc OCR."""
import argparse
import json
from pathlib import Path
import re
import unicodedata

FIELDS = [
    ("net_income", 12, "loi nhuan sau thue"),
    ("cfo", 13, "luu chuyen tien thuan tu hoat dong"),
    ("cash_dividends_paid", 14, "tien chi tra co tuc"),
]


def fold(text):
    # NFD tách dấu khỏi chữ; bỏ dấu và đổi đ thành d để tìm nhãn dòng.
    return "".join(c for c in unicodedata.normalize("NFD", text.lower())
                   if not unicodedata.combining(c)).replace("đ", "d")


def extract(root):
    result = {"unit": "VND", "Q1/2026": {}, "Q1/2025": {}}
    probe = json.loads((root / "pdf-probe.json").read_text(encoding="utf-8"))
    for key, page, label in FIELDS:
        # Dùng văn bản OCR chỉ cho các trang được read_pdf.py đánh dấu cần OCR.
        suffix = "ocr" if page in probe["ocr_pages"] else "pdf"
        lines = (root / f"page-{page}-{suffix}.txt").read_text(encoding="utf-8").splitlines()
        values = []
        for index, line in enumerate(lines):
            if label in fold(line):
                # Lấy thêm dòng sau vì OCR có thể tách nhãn và số thành hai dòng.
                window = " ".join(lines[index:index + 2])
                # Tìm số có dấu chấm phân nhóm và dấu âm dạng ngoặc, ví dụ (124.187.023.735).
                tokens = re.findall(r"\(?\d{1,3}(?:\.\d{3}){2,}\)?", window)
                # Bỏ dấu chấm, đổi ngoặc thành dấu âm, lấy hai cột 2026 và 2025.
                values = [(-1 if token.startswith("(") else 1)
                          * int(token.strip("()").replace(".", ""))
                          for token in tokens[:2]]
                break
        for index, quarter in enumerate(("Q1/2026", "Q1/2025")):
            # Thiếu số thì giữ None, khi ghi JSON sẽ thành null.
            result[quarter][key] = values[index] if index < len(values) else None
    (root / "data.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, nargs="?", default=Path("output"))
    extract(parser.parse_args().output.resolve())
