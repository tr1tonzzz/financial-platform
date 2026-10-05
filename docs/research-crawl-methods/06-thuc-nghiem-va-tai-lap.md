# Thực nghiệm và cách chạy lại

> **Trạng thái 03/10/2026 — hồ sơ thử nghiệm thu thập.** Project hiện hành tập trung thu thập, kiểm định và phân tích lợi nhuận–dòng tiền–cổ tức tiền mặt. Xem [SRS hiện hành](../research-platform/02-de-tai-va-srs.md) và [phương pháp thống nhất](../research-platform/11-phuong-phap-thu-thap-va-xu-ly.md). Các ngưỡng cảnh báo, dự báo, scope và lịch cũ bên dưới chỉ để tham khảo; không là yêu cầu MVP hiện hành.

## 1. Bộ chạy được báo cáo

Chỉ dùng hai run trong thư mục `data-sets/research-evidence/2026-10-03-crawl-methods/verified/` để tổng hợp kết quả cuối. Các run phát triển ở thư mục cha có lỗi phân loại và hai PDF ngoài mục tiêu; giữ lại làm nhật ký, không cộng vào tám báo cáo đã chốt.

| Lần chạy | UTC bắt đầu/kết thúc | HTML trực tiếp | PDF | History sau chạy |
|---|---|---|---|---|
| Thu mới | 03/10/2026 11:32:28–11:32:53 | 7 trang, 4 nguồn | 8 × HTTP 200; 76.118.458 byte; 423 trang | 8 URL, 8 phiên bản |
| Kiểm tra lại | 03/10/2026 11:33:38–11:33:58 | 7 trang, 4 nguồn | 8 × HTTP 304; 0 byte PDF body | 8 URL, 8 phiên bản |

Giờ Việt Nam = UTC + 7. Hai lần cùng ngày, cùng cấu hình: bốn issuer, tối đa hai trang và hai PDF/công ty, FY2025/H1-2026, ưu tiên không phải riêng lẻ/tiếng Anh. Raw có catalog HTML, robots snapshots đọc được, PDF theo hash, text 12 trang đầu và manifests. [crawl-evidence.json](crawl-evidence.json) là bản bằng chứng gọn đưa vào Git; raw nằm trong `data-sets` bị `.gitignore` loại, vì vậy clone repo chưa có raw sẵn.

HPA là nguồn mới so với bộ khảo sát cũ; trang đầu hai PDF đã được render/đọc ảnh: FY2025 hợp nhất đã kiểm toán, kết thúc 31/12/2025; H1/2026 hợp nhất giữa niên độ đã soát xét, kỳ sáu tháng kết thúc 30/06/2026. Đó là kiểm tra metadata, chưa phải đối chiếu chín giá trị của HPA.

## 2. Chạy trên máy của người thực hiện

Python môi trường project cần `lxml` và `pypdf`; phiên bản đã chạy lưu ở JSON evidence. Tạo virtualenv/cài dependencies theo môi trường của mình; không cần giữ đường dẫn runtime Codex trên máy khác.

```powershell
python -m pip install -r scripts/research/requirements-crawl.txt
python scripts/research/crawl_official_reports.py data-sets/research-evidence/my-crawl --companies DHG,VHC --max-pages 2
python scripts/research/crawl_official_reports.py data-sets/research-evidence/my-crawl --companies DHG,VHC --max-pages 2
python -m unittest discover -s scripts/research -p test_crawl_official_reports.py -v
```

Hai nguồn trên đã có robots đọc được. Để tái lập thử hữu hạn bốn nguồn và ghi nhận cả trường hợp robots host file chưa xác định:

```powershell
python scripts/research/crawl_official_reports.py data-sets/research-evidence/my-four-source-probe --max-pages 2 --allow-unknown-robots
```

Cờ không ghi đè Disallow đã đọc. Không dùng cờ này để mặc định bật lịch khai thác mọi host. Không bật `verify=False`, không dùng `curl -k`, không dùng proxy đổi IP để vượt chặn. Prototype không theo redirect; nếu gặp 301/302 thì xem lại URL danh mục và policy host đích trước khi bổ sung adapter.

Kết quả mạng lần sau có thể khác vì nguồn thay đổi, TLS, timeout hoặc robots. Log lỗi thay vì sửa báo cáo để luôn ghi “thành công”. Output directory mới → thu mới; cùng directory → kiểm tra cập nhật dựa history và file hash.

## 3. Những gì kiểm thử đã chứng minh

**13 test offline pass**: nhầm H1 thành năm; quý và năm rút gọn; năm upload khác năm tài chính; bundle chứa giải trình; loại tổng quan/riêng; loại EN; phân trang và anchor trùng; wildcard robots; cờ unknown không vượt Disallow; response HTML giả PDF; HTTPS/host allowlist; hash/corruption; chuỗi ba lần với 304 và thay nội dung.

Test phiên bản sử dụng PDF fixture tổng hợp một/hai trang, không chứa số tài chính thật. Chưa test trực tiếp việc nguồn thật đính chính, mọi mã retry, phân trang vô hạn, parser RFC đầy đủ, số tài chính hay UI.

## 4. Protocol để đánh giá project thật

Freeze tập expected issuer–period–scope trước khi crawl, không chọn mẫu chỉ từ file tải thành công. Đo riêng:

- Discovery coverage: tài liệu đúng tìm thấy / tài liệu mong đợi đã xác nhận công bố; ghi lý do không tìm thấy.
- Selection precision: link BCTC đúng loại/kỳ/scope / link được chọn, đối chiếu PDF; còn unknown không chấm là đúng.
- Download success: file PDF hợp lệ tải được / link hợp lệ đã thử; tách policy-skip, unavailable, lỗi TLS/HTTP.
- Incremental behavior: URL/phiên bản/blob trước và sau chạy; byte tải, 304, file mới/đổi.
- Field joint correctness: giá trị **và** kỳ/unit/scope/metric đúng / toàn bộ target chín trường, kể cả missing.
- Effort: giây crawl/OCR, phút review/tài liệu, phút sửa adapter khi DOM đổi.

Chia holdout theo tài liệu/layout hoặc nguồn, không chia ngẫu nhiên các dòng của cùng một PDF. Dùng người đối chiếu khác nếu có; nếu tự chấm thì công khai giới hạn. Kết quả 8/8 download trên mẫu phát triển này không là estimate 100% toàn thị trường hoặc accuracy extraction.
