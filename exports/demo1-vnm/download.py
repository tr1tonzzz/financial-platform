"""Tải HTML danh mục và PDF mẫu từ hai URL cố định."""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import time
from urllib.request import Request, urlopen

CATALOG_URL = "https://www.vinamilk.com.vn/investor/reports/financial"
PDF_URL = "https://d8um25gjecm9v.cloudfront.net/cms/20260429_VNM_BCTC_DA_SOAT_XET_Q1_2026_HOP_NHAT_VN_d44326741a.pdf"


def utc():
    return datetime.now(timezone.utc).isoformat()


def download(url, log):
    event = {"url": url, "started_at": utc()}
    # Dùng đồng hồ đơn điệu để đo thời gian tải, tránh ảnh hưởng khi giờ hệ thống đổi.
    started = time.monotonic()
    try:
        request = Request(url, headers={"User-Agent": "VNM-OCR-Demo/1.0"})
        with urlopen(request, timeout=30) as response:
            body = response.read()
            event.update(status=response.status, final_url=response.geturl(),
                         bytes=len(body), content_type=response.headers.get("Content-Type"))
            return body
    except Exception as error:
        event.update(error=str(error), status=getattr(error, "code", None))
        raise
    finally:
        # Ghi nhật ký request kể cả khi tải lỗi.
        event.update(finished_at=utc(), seconds=round(time.monotonic() - started, 3))
        log["requests"].append(event)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    # Tham số thư mục có thể bỏ qua; mặc định lưu vào output.
    parser.add_argument("output", type=Path, nargs="?", default=Path("output"))
    root = parser.parse_args().output.resolve()
    root.mkdir(parents=True, exist_ok=True)
    log = {"started_at": utc(), "catalog_url": CATALOG_URL,
           "pdf_url": PDF_URL, "requests": []}
    try:
        print("Downloading catalog HTML...")
        (root / "catalog.html").write_bytes(download(CATALOG_URL, log))
        print("Downloading sample PDF...")
        body = download(PDF_URL, log)
        # Kiểm chữ ký đầu file để không lưu trang HTML báo lỗi thành PDF.
        if not body.startswith(b"%PDF-"):
            raise RuntimeError("The response is not a PDF.")
        (root / "sample.pdf").write_bytes(body)
        log.update(pdf_path="sample.pdf", pdf_bytes=len(body))
    except Exception as error:
        log["error"] = str(error)
        raise
    finally:
        log["finished_at"] = utc()
        (root / "source-probe.json").write_text(
            json.dumps(log, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Downloaded files: {root}")


if __name__ == "__main__":
    main()
