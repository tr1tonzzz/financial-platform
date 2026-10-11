"""Chuyển các trang cần OCR thành ảnh PNG bằng Poppler."""
import argparse
import json
from pathlib import Path
import subprocess


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, nargs="?", default=Path("output"))
    parser.add_argument("--pdftoppm", default="pdftoppm", help="Executable name or absolute path")
    args = parser.parse_args()
    root = args.output.resolve()
    pdf = root / "sample.pdf"
    if not pdf.is_file():
        raise FileNotFoundError("Run download_sample.py first: sample.pdf is missing.")
    probe = json.loads((root / "pdf-probe.json").read_text(encoding="utf-8"))
    if not probe["ocr_pages"]:
        print("PDF text is available. No pages need rendering.")
        return
    for page in probe["ocr_pages"]:
        # -f/-l chọn một trang, -r đặt 220 DPI, -singlefile giữ tên ảnh không thêm số.
        subprocess.run([args.pdftoppm, "-f", str(page), "-l", str(page),
                        "-r", "220", "-singlefile", "-png", str(pdf),
                        str(root / f"page-{page}")], check=True)
        print(f"Rendered: page-{page}.png")


if __name__ == "__main__":
    main()
