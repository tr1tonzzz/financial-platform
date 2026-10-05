# Sổ nguồn và bằng chứng

Đọc/đối chiếu ngày 03/10/2026. Đã đọc, đã thử và thiết kế tương lai được phân biệt. Nguồn học quốc tế không thay chuẩn/pháp luật Việt Nam.

| Nguồn | Vai trò | Trạng thái |
|---|---|---|
| [Crawler nghiên cứu](../research-crawl-methods/README.md) và [JSON](../research-crawl-methods/crawl-evidence.json) | BCTC official discovery, hash, 304 | 8 PDF/4 issuer, 13 test; source policy unknown ở 4 PDF; development |
| [Khảo sát gần hiện tại](../research-recent-data/README.md) | PDF/OCR và sự kiện mẫu | Chưa dataset lịch sử đầy đủ/holdout độc lập |
| [VSDC VNM nhiều năm](https://vsdc.vn/vi/ad1/187729) | Event components và năm lợi nhuận | Nội dung chính đối chiếu lại; không payment confirmation |
| [VSDC VNM phần còn lại 2025](https://vsdc.vn/vi/ad1/197038) | Notice tiền mặt | Mẫu đã trích, chưa closure năm |
| [VSDC DHG đợt 1](https://vsdc.vn/ad/195056), [đợt cuối](https://vsdc.vn/vi/ad1/199544) | Các đợt và lịch thanh toán | Mẫu đã trích; ghi scheduled, không suy paid |
| [HPG IR](https://www.hoaphat.com.vn/quan-he-co-dong/bao-cao-tai-chinh), [DHG IR](https://dhgpharma.com.vn/vi/bao-cao-tai-chinh), [VHC IR](https://www.vinhhoan.com/investors-2/), [HPA IR](https://nongnghiep.hoaphat.com.vn/quan-he-co-dong/bao-cao-tai-chinh) | Danh mục PDF | Đã thử discovery; không tất cả doanh nghiệp nằm trong cohort cuối |
| [HTTP RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html#name-conditional-requests), [robots RFC 9309](https://www.rfc-editor.org/rfc/rfc9309.html) | Update/policy | GET/304 đã thử; robots parser pilot chưa đầy đủ RFC |
| [pdfplumber](https://github.com/jsvine/pdfplumber), [Tesseract](https://github.com/tesseract-ocr/tesseract) | Text/bbox và OCR baseline | Đã có probe; confidence không là accuracy |
| [SciPy Spearman](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.spearmanr.html) | Tương quan mô tả | Đã đọc docs; chưa chạy tương quan dataset project |
| [Python](https://docs.python.org/3.12/tutorial/), [pandas](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html), [SQLite](https://www.sqlite.org/lang.html), [Streamlit](https://docs.streamlit.io/get-started/fundamentals) | Học/stack | Nền đã chọn; app cần triển khai |
| [SEC beginner guide](https://www.sec.gov/about/reports-publications/beginners-guide-financial-statements) | Học cơ chế BCTC | Tham khảo kiến thức, không hướng dẫn pháp luật Việt Nam |
| [Scrapy files](https://docs.scrapy.org/en/latest/topics/media-pipeline.html), [Playwright downloads](https://playwright.dev/python/docs/downloads) | Phương án mở rộng | Nghiên cứu, chưa chạy trong collector mới |

Các khảo sát World Bank/FinQA/TAT-QA/Vnstock thuộc ý tưởng trước, giữ trong [snapshot A1](history/a1-2026-10-03.zip) và ideas; không là dependency đề tài hiện hành.

Chưa có rubric/hạn thực, teacher approval, event discovery lịch sử đầy đủ, dataset sáu fields + components toàn cohort hoặc benchmark/model. Sổ nguồn phải cập nhật bằng artifact thật, không ghi “đã xác minh” từ kế hoạch hoặc kết quả tìm kiếm alone.
