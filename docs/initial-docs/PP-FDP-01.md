# Kế hoạch dự án BCTC–cổ tức Việt Nam

> **Trạng thái 03/10/2026 — hồ sơ khảo sát trước.** Project hiện hành tập trung thu thập, kiểm định và phân tích lợi nhuận–dòng tiền–cổ tức tiền mặt. Xem [SRS hiện hành](../research-platform/02-de-tai-va-srs.md) và [phương pháp thống nhất](../research-platform/11-phuong-phap-thu-thap-va-xu-ly.md). Các ngưỡng cảnh báo, dự báo, scope và lịch cũ bên dưới chỉ để tham khảo; không là yêu cầu MVP hiện hành.

Phiên bản 2.0 — 03/10/2026. Tham chiếu: [SRS](SRS-FDP-01.md), [SDD](SDD-FDP-01.md), [TP](TP-FDP-01.md).

## 1. Mục tiêu và nguồn lực

Một sinh viên thực hiện MVP trong 13 tuần, đồng thời học các môn khác. Giả định lập kế hoạch là 10–12 giờ/tuần, khoảng 130–156 giờ; phải điều chỉnh sau khi đo công sức pilot.

Ưu tiên thời gian: khoảng 60% thu thập/chuẩn hóa/kiểm định; 25% phân tích và báo cáo; 15% API, demo và tích hợp. AI hỗ trợ viết code, nhưng người thực hiện phải đọc, kiểm tra và giải thích được logic dữ liệu.

## 2. Kế hoạch 13 tuần

| Tuần | Công việc | Bằng chứng hoàn thành |
|---|---|---|
| 1 | Chọn 10 công ty pilot, khảo sát nguồn và tải mẫu | Sổ nguồn có URL thật, loại PDF, ngày công bố; danh sách loại mẫu |
| 2 | Crawler khám phá và lưu raw | URL → PDF/HTML, hash, log, retry; thử chạy lại |
| 3 | Parser cho 6 chỉ tiêu, 3–5 báo cáo | Các giá trị có kỳ, đơn vị, phạm vi và trang |
| 4 | Chuẩn hóa, validation và bộ đối chiếu | Facts VND; bảng lỗi; mẫu kiểm tra độc lập |
| 5 | Thu thập cổ tức pilot | Các đợt DPS, lịch dự kiến, nguồn và trạng thái |
| 6 | Chuỗi hoàn chỉnh một công ty | Bản gốc → facts/sự kiện → chỉ số → API/demo có nguồn |
| 7 | Mở rộng 20–30 công ty; đo công sức | Độ phủ, lỗi, phút review mỗi báo cáo; quyết định tăng quy mô |
| 8 | Chốt 30 công ty hoặc mở lên 60–80 | Dataset snapshot; bảng mẫu có/không đủ điều kiện |
| 9 | Phân tích phân bố, xu hướng, quan hệ và nhóm | Bảng kết quả, biểu đồ, kiểm tra dữ liệu thiếu |
| 10 | Điểm quy tắc, đánh giá và 3 case study | Baseline, bảng cảnh báo đúng/sai; nguồn cho từng case |
| 11 | Hoàn thiện API/dashboard; ML nếu còn đủ điều kiện | Ba màn hình dùng dữ liệu thật; ML chỉ khi không ảnh hưởng nghiệm thu |
| 12 | Kiểm thử, tái lập và báo cáo | Kết quả TP, manifest, hướng dẫn chạy; bản báo cáo |
| 13 | Buffer, sửa lỗi và bảo vệ | Demo dự phòng từ snapshot, slide và các giới hạn |

Nếu chỉ có 12 tuần, gộp viết báo cáo vào các tuần trước và bỏ phần ML; không cắt bước kiểm định dữ liệu.

## 3. Mốc quyết định

| Mốc | Điều kiện | Khi chưa đạt |
|---|---|---|
| Cuối tuần 2 | Tải được ít nhất 10 tài liệu thật từ một nguồn | Thu hẹp nguồn; dùng IR có cùng cấu trúc để tiếp tục pilot |
| Cuối tuần 4 | Trích xuất và đối chiếu được 6 chỉ tiêu | Giới hạn PDF có text; ghi tỷ lệ loại scan; giảm quy mô |
| Cuối tuần 6 | Có chuỗi hoàn chỉnh một công ty | Cắt UI nâng cao, nguồn thứ hai và ML |
| Cuối tuần 8 | Dataset tối thiểu 30 công ty, có bảng độ phủ | Không tăng công ty; tập trung sửa dữ liệu, báo cáo phạm vi thực đạt |
| Cuối tuần 10 | Có phân tích, quy tắc và 3 case study | Chốt phân tích mô tả nếu nhãn chưa đủ; ghi RQ3 chưa kết luận |

Không dùng dữ liệu giả để thay thế chỉ tiêu nghiệm thu dữ liệu thật.

## 4. Quyết định tăng số công ty

Đo số phút tải, trích xuất, review một báo cáo và tỷ lệ file cần sửa tay. Với 60–80 công ty × 5 năm, có khoảng 300–400 BCTC trước khi tính thông báo cổ tức.

Chỉ tăng quy mô nếu khối lượng còn lại, ước lượng bằng số file × thời gian xử lý/review đã đo, nằm trong quỹ giờ thực tế và vẫn còn 20% dự phòng. Tránh chọn toàn công ty dễ lấy dữ liệu rồi suy rộng ra toàn thị trường; ghi rõ tiêu chí mẫu.

## 5. Rủi ro và xử lý

| Rủi ro | Biện pháp | Phần giảm trước |
|---|---|---|
| Nguồn khó crawl hoặc thiếu lịch sử | Pilot sớm, lưu raw, một adapter/nguồn | Nguồn thứ hai |
| PDF scan, bảng lỗi | Đo tỷ lệ, review mẫu, ưu tiên text | OCR tổng quát |
| Thiếu bằng chứng đã trả | Giữ scheduled/unknown; chọn biến kết quả phù hợp | Dự báo tiền thực trả |
| Nhãn ít hoặc mất cân bằng | Chốt phân tích mô tả, baseline và độ bất định | ML phức tạp |
| Thiếu EPS/cổ phiếu được hưởng | Dùng chỉ số lõi, không tính ratio thiếu đầu vào | Payout/coverage |
| UI chiếm thời gian | Ba màn hình tối thiểu | Quản trị, so sánh tùy biến |
| Kết quả quan hệ yếu | Báo cáo trung thực cùng khoảng tin cậy | Không thay nhãn để làm đẹp kết quả |

## 6. Bộ sản phẩm phải nộp

- Dataset có nguồn và manifest; từ điển dữ liệu.
- Pipeline tự thu thập và chuẩn hóa; hướng dẫn tái lập.
- Báo cáo độ phủ, độ chính xác trước/sau review và công sức thủ công.
- Phân tích quan hệ BCTC–cổ tức, điểm cảnh báo và 3 case study.
- API/dashboard đọc snapshot thật.
- Báo cáo kiểm thử, đề cương phương pháp, slide và demo.
- Nếu có ML: baseline, cách chia theo thời gian, kết quả và giới hạn.

## 7. Quản lý thay đổi

Khi đổi nguồn, khoảng năm, số công ty, định nghĩa nhãn hoặc quy tắc, cập nhật SRS và sổ quyết định. Sau tuần 8 đóng băng snapshot đánh giá; mọi sửa dữ liệu tạo phiên bản mới để kiểm tra tác động.
