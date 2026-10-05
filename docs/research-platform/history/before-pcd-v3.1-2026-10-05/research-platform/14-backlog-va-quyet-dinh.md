# Backlog triển khai và sổ quyết định

**D13 — 04/10/2026:** kế hoạch [v2 theo SRS v3.0](04-ke-hoach-13-tuan.md) và [checklist đồng bộ](checklist-13-tuan.html) là backlog chi tiết hiện hành, gồm W01-01…W13-06, toàn bộ73 yêu cầu/31TC, outputs và gates. T01–T08 bên dưới là nhóm định hướng, không thay các việc/tiêu chí mới. Chuẩn bị holdout tuần7, freeze đầu tuần8 trước đo; version/cache từ tuần2, replay tuần10, restore/performance/safety tuần11. [Bắt đầu và mẫu hồ sơ](23-bat-dau-va-minh-chung-thuc-hien.md). Chưa tick tiến độ chỉ vì cập nhật kế hoạch.

## Quyết định đã thống nhất ngày 03/10/2026

| ID | Quyết định | Lý do |
|---|---|---|
| D01 | Một ngách lợi nhuận–CFO–cổ tức tiền mặt | Người thực hiện muốn tập trung và liên thông lên dự đoán |
| D02 | Project phân tích mô tả, predictor để tốt nghiệp | Nền học và dữ liệu chưa đủ cho mô hình |
| D03 | Target là DPS công bố theo profit_year | Nguồn đang có là thông báo/lịch, chưa payment confirmation |
| D04 | Sáu financial targets lõi | Đã có mẫu phát triển; giảm phần ngoài câu hỏi chính |
| D05 | Pilot 3 × 3 năm; gate 5–8 doanh nghiệp | Quỹ 13 tuần, 10–12 giờ/tuần gồm học/report |
| D06 | Python HTTP/lxml, text/OCR, SQLite, Streamlit | Một stack dễ tự giải thích; mở framework khi thật cần |
| D07 | Human review metadata/closure/số có audit | Không giả định crawl và OCR luôn đúng |
| D08 | Hợp nhất ưu tiên, entity tách scope | Không trộn riêng/hợp nhất hoặc suy khả năng chi tiền mẹ từ nhóm |

Đây là quyết định của người thực hiện và phương pháp triển khai; chưa có xác nhận giảng viên/rubric/hạn thực.

## Việc làm tiếp theo theo phụ thuộc

**Quyết định sau nghiên cứu lần hai ngày 04/10/2026:**

| ID | Quyết định | Tác động |
|---|---|---|
| D09 | Giữ tên đề tài, sáu trường và pilot/gate; kiểm định/truy vết và lifecycle là lõi | Không mở project sang chatbot/giá/ML; làm sâu contract và thí nghiệm đã có |
| D10 | Đối chiếu phiên bản/ảnh hưởng là nhánh đồ án ưu tiên | Thay ưu tiên predictor trong hồ sơ trước; dự đoán chỉ còn tùy chọn sau gate |
| D11 | Phân biệt hủy ngày đăng ký/quyền/thông báo với hủy phương án cổ tức | Không suy annual DPS = 0; rà bản thay thế; bổ sung test và coverage |
| D12 | Phân loại thay đổi hành chính/lịch/mức/hiệu lực trước cập nhật | Hash đổi không mặc định số thay đổi; giữ snapshot và audit |

[Báo cáo và tám nhánh đã khảo sát](20-nghien-cuu-lan-hai-va-chot-de-tai.md) · [Sổ nguồn](21-so-nguon-nghien-cuu-lan-hai.md). Đây là quyết định triển khai theo yêu cầu chốt của người thực hiện, không là giảng viên phê duyệt hay tính năng đã xong.

| Thứ tự | Đầu ra | Tiêu chí xong |
|---|---|---|
| T01 | Chọn 3 issuer và source/expected ledger | Đủ nguồn BCTC/sự kiện, scope chính và lý do chọn |
| T02 | Một vertical slice | BCTC + notice thật tới candidates/review/aggregate; đọc được source |
| T03 | Discovery cổ tức | Tự tìm nhiều notice từ trang công khai, giữ tuyến discovery và pagination |
| T04 | Mở collector kỳ 2023–2025 | Bỏ fixed FY2025/H1 filter theo config, giữ regression tests |
| T05 | Pilot 9 BCTC + sự kiện | Sáu target/report, events/components, missing và phút review |
| T06 | SQLite/UI review | Keys/transaction, source/event versions và audit |
| T07 | Dashboard ba case | Chuỗi đủ/comparable, timeline, provenance/export |
| T08 | Holdout và report | Baselines, metrics, giới hạn, Word/slide thống nhất |

T01–T08 là backlog tương lai; không tick hoàn thành bằng việc đã có tài liệu. Chưa cần predictor/API/React hoặc tự tạo lịch gửi thầy. Người thực hiện tự giải thích một module mỗi tuần.

## Gate thu hẹp

Tuần 2: một luồng nguồn tới dữ liệu phải chạy; event discovery thất bại thì thử IR adapter chính thức trước, báo phần assisted riêng. Tuần 4: đo thời gian pilot rồi chốt số issuer, không đổi missing thành 0. Tuần 8: freeze scope/holdout. Tuần 11: feature freeze. Nếu hạn/giờ thực khác giả định, lập lại ngân sách.

## Lịch sử

A1 sức khỏe tài chính là quyết định trước, [snapshot](history/a1-2026-10-03.zip). Các forecast score/threshold từ bộ initial-docs cũ là nghiên cứu lịch sử, không hiện hành. Khi đổi target/scope/nguồn phải ghi ngày, lý do, tác động dữ liệu và cập nhật SRS cùng Word/slide.

## Cập nhật nhịp báo cáo

Ngày 03/10/2026, người thực hiện yêu cầu checklist mỗi tuần và Word/slide hai tuần một lần. Giữ 13 tuần: sáu đợt tuần 2/4/6/8/10/12 và tổng kết tuần 13. Nhật ký tuần là nội bộ; thay nhịp cũ trong tài liệu và proposal. [Bản trước thay nhịp](history/before-biweekly-2026-10-03.zip).
