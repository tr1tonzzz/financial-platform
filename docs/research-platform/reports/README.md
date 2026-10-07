# Báo cáo và các bản tài liệu tham khảo

## Báo cáo 1 đang soạn bằng Markdown

Đã bổ sung [cơ sở học thuật và giá trị sử dụng](dot-01-tuan-01-02/co-so-hoc-thuat-va-gia-tri-su-dung.md): vì sao cần liên kết BCTC–cổ tức, 10 nghiên cứu có nguồn, câu hỏi người dùng và cách đánh giá ích lợi. [Thử nghiệm công cụ](dot-01-tuan-01-02/thu-nghiem-cong-cu.md) ghi kết quả crawler/PDF/OCR thực tế; tách bằng chứng kỹ thuật với lợi ích sản phẩm chưa đo.

Theo yêu cầu ngày **05/10/2026**, [báo cáo 1](dot-01-tuan-01-02/bao-cao-01.md) tập trung vào bối cảnh đề tài, vấn đề cần giải quyết, hướng project và các chức năng đề xuất. [Phụ lục Vinamilk](dot-01-tuan-01-02/vi-du-phan-tich-vnm.md) minh họa sơ bộ từ BCTC hợp nhất đã soát xét quý I/2026 (thay mẫu ngày 06/10/2026). Giai đoạn này chỉ cập nhật Markdown; chưa cần Word, slide hoặc PDF. Báo cáo chưa là xác nhận hoàn thành tuần 1–2 hay ứng dụng đã triển khai.

## SRS và các bản xuất đã có

Cập nhật **05/10/2026**. [SRS-FAP-01 v3.1 Word](SRS-FAP-01-v3.1.docx) được sinh từ [Markdown nguồn](../22-srs-dac-ta-yeu-cau-phan-mem.md), tích hợp hướng kết hợp và cầu nối CFO: 73 yêu cầu nền + 10 E, 31 TC + 11 P. Chưa ghi nhận giảng viên phê duyệt hoặc test ứng dụng pass. Tái tạo bằng `scripts/research/build_srs_docx.py`, sau đó render/kiểm bố cục. Kế hoạch/checklist v3 là đầu mối thực hiện.

## Các bản xuất trước cập nhật

- [SRS Word v3.0](SRS-FAP-01-v3.0.docx): baseline ngày 04/10, chưa có cầu nối theo ca.
- [Báo cáo đề xuất Word](bao-cao-de-xuat.docx) và [slide](de-xuat-project.pptx): bản xuất cũ trước cập nhật SRS/hướng kết hợp, chỉ tham khảo lịch sử, chưa dùng như proposal hiện hành.
- [JSON nội dung đề xuất](noi-dung-de-xuat.json): nguồn bản xuất cũ, chưa đồng bộ cầu nối và ngân sách mới.

Hồ sơ A1 ở [snapshot](../history/a1-2026-10-03.zip). Nội dung trao đổi hiện hành dùng [SRS v3.1](../22-srs-dac-ta-yeu-cau-phan-mem.md), [nhu cầu](../02-de-tai-va-srs.md) và [đề cương kết hợp](../../research-profit-cash-dividend/09-de-cuong-trao-doi-voi-giang-vien.md). Báo cáo tiến độ thật tạo theo [nhịp hai tuần](../07-bao-cao-hang-tuan.md); chưa làm thì ghi pending, không tạo tiến độ giả.

**Cập nhật mẫu thử 06/10/2026:** [phụ lục công cụ báo cáo 1](dot-01-tuan-01-02/thu-nghiem-cong-cu.md) dùng BCTC hợp nhất quý I/2026 Vinamilk, đã chạy crawler/PDF/OCR ba trang và đối chiếu sáu ô. Ví dụ phân tích chính cũng đổi sang Vinamilk quý I/2026, có cầu nối thủ công kiểm tổng.
