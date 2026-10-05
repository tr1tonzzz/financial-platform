# N2 — Dữ liệu và đánh giá kịch bản

Protocol đề xuất, chưa chạy. [Đề xuất](01-de-xuat-nghien-cuu.md), [công thức](02-kien-thuc-tai-chinh.md).

## 1. Case và nguồn

Chọn một doanh nghiệp phi tài chính có BCTC kiểm toán đầy đủ, dòng đầu tư/tài trợ rõ, thông báo cổ tức và số cổ phiếu hưởng quyền nếu cần tính tổng tiền. Ghi nhận khoản hạn chế sử dụng tiền và cách báo cáo lãi/thuế/cổ tức. Nếu không thể phân loại, không phát hành kết quả scenario như đã kiểm chứng.

Giữ hai bộ riêng: dữ liệu lịch sử dùng kiểm tra cân đối, và giả định tương lai dùng mô phỏng. Chi thực tế khác lịch dự kiến; không tạo dữ liệu “đã trả” bằng cách dùng ngày thông báo thanh toán làm xác nhận.

## 2. Kiểm tra số học trước mô phỏng

Với dữ liệu lịch sử, trước hết đối chiếu tiền đầu/cuối kỳ bằng CFO, CFI, CFF và ảnh hưởng tỷ giá/các khoản được báo cáo. Sau đó phân rã các dòng thành phần dùng trong engine. Nếu không khớp, lưu residual và nguồn thiếu; không chỉnh `other_net_cash` thành khoản bù vô danh để làm sai số bằng 0.

Độc lập tính lại ít nhất một case trên bảng đối chiếu thủ công từ raw. Kiểm tra đổi đơn vị, lãi/thuế đã trong CFO, CapEx, vay mới và cổ tức. Gold không lấy từ cùng hàm tính engine.

## 3. Ma trận thí nghiệm đề xuất

- Một scenario cơ sở với các giả định ghi rõ.
- CFO dương giảm theo ba mức do người nghiên cứu định trước; CFO âm dùng giảm tuyệt đối.
- Thay riêng CapEx, nợ gốc và cổ tức để đọc mức nhạy cảm.
- Một case thiếu dữ liệu để kiểm tra từ chối/hiện kết quả có điều kiện.

Chưa ấn định các mức giảm là cú sốc kinh tế thực tế; cần nguồn hoặc ghi là mức minh họa. Không chọn kịch bản chỉ vì nó tạo ra thiếu hụt lớn và câu chuyện hấp dẫn.

## 4. Tiêu chí đánh giá

Độ đúng phép tính và phân loại; số input có nguồn/giả định/thiếu; thời gian kiểm tra; khả năng chạy lại; độ đúng phát biểu theo output. Đo tỷ lệ câu trả lời biết giới hạn khi thay đổi dữ liệu hoặc giả định. Ngưỡng nghiệm thu chỉ chốt sau case thử, không coi chúng là kết quả đã đạt.

Không đánh giá scenario như mô hình dự báo bằng accuracy cắt giảm cổ tức. Kiểm tra cân đối lịch sử không chứng minh dự báo tương lai đúng. Nếu muốn dự báo, cần một thiết kế khác với inputs khả dụng tại thời điểm dự báo và kết quả tương lai độc lập.

## 5. Artifact cần nộp khi thực hiện

Phiếu dữ liệu nguồn, bảng phân loại dòng tiền, bảng kiểm tra lịch sử, scenario JSON/CSV, bảng nhạy cảm, báo cáo giả định và lỗi. N2 chỉ được thêm vào demo sau khi các inputs và cân đối được duyệt; chưa tính vào phạm vi MVP.
