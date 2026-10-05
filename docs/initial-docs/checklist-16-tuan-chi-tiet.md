# Checklist MVP BCTC–cổ tức Việt Nam — 13 tuần

> **Trạng thái 03/10/2026 — hồ sơ khảo sát trước.** Project hiện hành tập trung thu thập, kiểm định và phân tích lợi nhuận–dòng tiền–cổ tức tiền mặt. Xem [SRS hiện hành](../research-platform/02-de-tai-va-srs.md) và [phương pháp thống nhất](../research-platform/11-phuong-phap-thu-thap-va-xu-ly.md). Các ngưỡng cảnh báo, dự báo, scope và lịch cũ bên dưới chỉ để tham khảo; không là yêu cầu MVP hiện hành.

Tên file được giữ để tương thích liên kết. Checklist dựa trên [SRS](SRS-FDP-01.md), [PP](PP-FDP-01.md), [TP](TP-FDP-01.md).

## Tuần 1–2: Pilot và thu thập

- [ ] Chốt câu hỏi nghiên cứu, 10 công ty phi tài chính và tiêu chí chọn/loại.
- [ ] Lưu URL nguồn thật và ghi trạng thái đã kiểm tra/chưa kiểm tra.
- [ ] Tải tối thiểu 10 tài liệu gốc, xác định PDF text/scan.
- [ ] Lưu ngày công bố, ngày tải, hash, loại báo cáo và trạng thái lỗi.
- [ ] Thử chạy lại, không tạo bản trùng.
- [ ] Quyết định nguồn chính dựa trên bằng chứng pilot.

## Tuần 3–4: Trích xuất và kiểm định

- [ ] Trích 6 chỉ tiêu lõi, đúng năm và cột.
- [ ] Chuẩn hóa VND, số âm, phạm vi riêng/hợp nhất.
- [ ] Lưu trang PDF/locator và số/nhãn/đơn vị gốc.
- [ ] Kiểm tra đẳng thức tài sản và trường thiếu.
- [ ] Xây bộ đối chiếu tách khỏi mẫu phát triển parser.
- [ ] Đo chính xác trước/sau review; lưu lịch sử sửa.

## Tuần 5–6: Cổ tức và chuỗi hoàn chỉnh

- [ ] Lấy DPS, loại cổ tức và các ngày có nguồn.
- [ ] Phân biệt lịch dự kiến, thực trả, hủy/đổi lịch.
- [ ] Không đếm hai lần thông báo cùng sự kiện.
- [ ] Có chuỗi PDF → facts/sự kiện → chỉ số → demo cho một công ty.
- [ ] Chốt biến kết quả là thực hiện hay công bố theo bằng chứng có được.

## Tuần 7–8: Dataset

- [ ] Đạt tối thiểu 30 công ty trong phạm vi đã chốt hoặc báo cáo phần chưa đạt.
- [ ] Đo phút review/báo cáo; quyết định có mở lên 60–80 hay không.
- [ ] Lưu snapshot, manifest và từ điển dữ liệu.
- [ ] Tạo cutoff và cửa sổ kết quả; gán unknown/censored đúng.
- [ ] Báo cáo độ phủ, mẫu số, loại mẫu và sai lệch chọn mẫu.

## Tuần 9–10: Phân tích

- [ ] Phân bố, xu hướng LNST/CFO/DPS và dữ liệu thiếu.
- [ ] Tương quan và so sánh nhóm với giới hạn rõ ràng.
- [ ] Rule score có phiên bản, lý do và kiểm tra độ nhạy.
- [ ] Baseline được đánh giá cùng mẫu.
- [ ] Ít nhất 3 case study truy lại được nguồn.
- [ ] Quyết định ML theo gate trong đề cương, ghi số mẫu/số ca thực tế.

## Tuần 11–13: Hoàn thiện

- [ ] API/dashboard dùng dữ liệu thật và có nguồn.
- [ ] Các test bắt buộc tại TP có kết quả.
- [ ] Chạy lại snapshot từ raw; có demo dự phòng.
- [ ] Báo cáo đóng góp, công sức thủ công và giới hạn dự báo.
- [ ] Slide tập trung dữ liệu và phân tích; luyện trả lời về nhãn và leakage.
