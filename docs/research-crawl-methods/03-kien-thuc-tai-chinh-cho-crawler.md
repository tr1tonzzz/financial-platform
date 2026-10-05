# Kiến thức tài chính cần hiểu để thu đúng BCTC

> **Trạng thái 03/10/2026 — hồ sơ thử nghiệm thu thập.** Project hiện hành tập trung thu thập, kiểm định và phân tích lợi nhuận–dòng tiền–cổ tức tiền mặt. Xem [SRS hiện hành](../research-platform/02-de-tai-va-srs.md) và [phương pháp thống nhất](../research-platform/11-phuong-phap-thu-thap-va-xu-ly.md). Các ngưỡng cảnh báo, dự báo, scope và lịch cũ bên dưới chỉ để tham khảo; không là yêu cầu MVP hiện hành.

Tài liệu này giúp thiết kế metadata và tránh trộn số; không dùng crawler để đưa khuyến nghị mua/bán.

## 1. Ba báo cáo và thuyết minh

Bảng cân đối kế toán cho biết tài sản, nợ phải trả, vốn chủ sở hữu **tại một thời điểm**. Báo cáo kết quả kinh doanh ghi doanh thu và lợi nhuận **trong một khoảng thời gian**. Báo cáo lưu chuyển tiền tệ ghi dòng tiền kinh doanh, đầu tư, tài trợ **trong một khoảng thời gian**. Thuyết minh giúp xác nhận đơn vị, chính sách, cấu trúc các khoản và thay đổi số so sánh.

Vì vậy chín trường không nằm trên cùng một trang; phải thu BCTC đủ bộ thay vì một PDF “tổng quan kinh doanh”. Không đồng nhất CFO với lợi nhuận hay biến động tiền cuối kỳ. Nợ phải trả bao gồm cả công nợ, thuế và nghĩa vụ khác, không đồng nghĩa tổng nợ vay có lãi.

| Trường schema | Tìm ở đâu? | Loại kỳ cần lưu |
|---|---|---|
| revenue_net | Kết quả kinh doanh: doanh thu thuần | duration |
| net_income_total | Kết quả kinh doanh: LNST tổng | duration; không thay bằng phần cổ đông công ty mẹ |
| cfo | Lưu chuyển tiền tệ: tiền thuần từ HĐKD | duration; trực tiếp/gián tiếp đều cần đúng dòng tổng |
| cash_equivalents | Cân đối: tiền và tương đương tiền | instant |
| total_assets | Cân đối: tổng tài sản | instant |
| total_liabilities | Cân đối: nợ phải trả tổng | instant |
| total_equity | Cân đối: VCSH tổng | instant; không bỏ lợi ích không kiểm soát khi thuộc tổng |
| current_assets | Cân đối: tài sản ngắn hạn | instant |
| current_liabilities | Cân đối: nợ ngắn hạn | instant |

## 2. Năm, quý và bán niên

File năm 2025 có thể công bố năm 2026; kỳ báo cáo không được lấy từ thời điểm tải. Với năm tài chính khác năm dương lịch, phải lưu ngày bắt đầu/kết thúc thật trong PDF, không áp đặt 01/01–31/12.

BCTC quý II có thể chứa cả cột quý II và lũy kế sáu tháng. BCTC bán niên có số tại 30/06 và số lũy kế 01/01–30/06. Hai tài liệu cùng thời điểm có thể khác mức soát xét và số điều chỉnh; không coi chúng như hai kỳ độc lập. Không so doanh thu sáu tháng với doanh thu cả năm mà bỏ nhãn khác khoảng kỳ. Muốn so tăng trưởng H1/2026, cần H1/2025 cùng phạm vi/cơ sở; FY2025 chưa thay thế được.

MVP giữ một series báo cáo năm; báo cáo 2026 là series/case cập nhật riêng. Chỉ ghép khi UI và engine kiểm tra rõ `period_kind`, `period_start`, `period_end`, `as_of_date`.

## 3. Hợp nhất, riêng lẻ và assurance

Hợp nhất mô tả nhóm doanh nghiệp sau xử lý giao dịch nội bộ; riêng lẻ/công ty mẹ mô tả một pháp nhân. Có doanh nghiệp công bố báo cáo cấp doanh nghiệp, không phải cứ không có chữ “hợp nhất” là parser được tự gán hợp nhất. DHG năm 2025 trong khảo sát trước được xác nhận là báo cáo cấp doanh nghiệp/riêng, do đó không dùng chung cơ sở so sánh hợp nhất với HPG/HPA.

“Kiểm toán”, “soát xét”, “chưa soát xét” phải có trường riêng. Bản tiếng Anh là biến thể ngôn ngữ, không tự động có nghĩa IFRS hoặc là một quan sát mới. Ngày ký ý kiến của đơn vị kiểm toán không thay ngày công bố trên website.

## 4. Đơn vị, dấu và cột

VND, nghìn VND, triệu VND tạo chênh lệch hệ số 1.000 hoặc 1.000.000. Lưu `raw_value`, `raw_unit`, `scale`, giá trị chuẩn và vị trí dòng/header chứng minh đơn vị. Dấu chấm/phẩy có thể là phân nhóm hoặc thập phân; số trong ngoặc thường biểu thị âm nhưng vẫn phải xác nhận cách trình bày của tài liệu.

Một dòng thường có mã số, số thuyết minh, cột kỳ hiện tại, cột kỳ trước. “Lấy số đầu tiên trong dòng” sẽ nhầm mã số; “lấy số cuối” có thể lấy kỳ trước. Parser cần hiểu header và tọa độ cột. Dấu gạch/ô trống phải giữ trạng thái riêng, không mặc định mọi thiếu dữ liệu là 0.

## 5. Đính chính và số so sánh

Giữ riêng báo cáo kỳ trước đã công bố và số so sánh được trình bày lại ở báo cáo mới. Hai số khác nhau chưa chứng minh crawler sai hoặc doanh nghiệp gian lận. Lưu `document_version`, `comparative/restated` và review reason; UI giải thích snapshot nào đang dùng. Đây là lý do cần provenance và lịch sử phiên bản trước khi vẽ xu hướng.
