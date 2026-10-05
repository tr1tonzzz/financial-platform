# I3 — Kiến thức tài chính: quyền, ngày và mức cổ tức

Ngày: 03/10/2026. Định nghĩa phục vụ dữ liệu nghiên cứu; không thay thế quy định nghiệp vụ áp dụng từng thời kỳ.

## 1. Những ngày khác nhau

| Ngày | Ý nghĩa | Quy tắc dataset |
|---|---|---|
| Ngày nghị quyết/công bố đầu tiên | Quyết định hoặc thông tin doanh nghiệp đưa ra | Phân biệt ngày ký và khả dụng công khai |
| Ngày thông báo VSDC | Công bố quyền qua VSDC | Không mặc định là lần đầu thị trường biết |
| Ngày giao dịch không hưởng quyền | Giao dịch không kèm quyền liên quan | Chỉ lấy khi nguồn xác minh; không tự suy từ record_date |
| Ngày đăng ký cuối cùng | Mốc danh sách người hưởng quyền | Không phải ngày trả tiền |
| Ngày thanh toán dự kiến | Lịch nêu trong thông báo | `scheduled_payment_date` |
| Ngày thực trả xác nhận | Thời điểm thực hiện có bằng chứng | `confirmed_payment_date` với nguồn |

Không áp lịch giao dịch/thanh toán hiện hành để suy ngày lịch sử. Nếu nghiên cứu cần suy ngày quyền, phải xác minh quy định, ngày nghỉ và lịch sàn đúng kỳ; MVP ưu tiên dữ liệu công bố trực tiếp.

## 2. Tỷ lệ trên mệnh giá, DPS và yield

`DPS = tỷ lệ dạng thập phân × mệnh giá`. Ví dụ nguồn nêu mệnh giá 10.000 đồng và tỷ lệ 15% thì DPS=1.500 đồng. Nếu tài liệu chỉ có tỷ lệ, mệnh giá chưa xác minh thì giữ chưa đủ dữ liệu.

Tỷ lệ 15% trên mệnh giá khác dividend yield = DPS/giá cổ phiếu ở ngày xác định. MVP chưa thu giá nên không hiển thị tỷ lệ trên mệnh giá như lợi suất đầu tư.

## 3. Đợt, tạm ứng và năm lợi nhuận

Một năm có nhiều đợt; đợt cuối có thể thanh toán năm sau. Tạm ứng tiền mặt vẫn là loại cash, nhưng chưa tự chứng minh thực hiện. Thành phần profit_year chỉ ghi khi nguồn nêu.

Với lịch gộp nhiều năm, giữ event tổng cho lịch quyền và components cho phân bổ. Tổng components phải bằng cash_dps của event trong dung sai. Cộng theo năm lợi nhuận dùng components; cộng theo cửa sổ lịch dùng event tổng một lần.

Không cộng phần “còn lại” như toàn bộ năm nếu văn bản chỉ nói một đợt. Không trộn cổ tức đặc biệt với cổ tức thông thường khi đánh giá mức đều đặn mà không gắn cờ.

## 4. Lịch công bố và thực trả

Các mức bằng chứng: đề xuất → được duyệt/công bố → lên lịch → điều chỉnh/hủy → xác nhận trả. Một nguồn chỉ ghi lịch không hỗ trợ nhãn paid, kể cả ngày dự kiến đã qua.

Dòng “cổ tức đã trả” trên BCTC có thể chứng minh tổng chi trong năm ở phạm vi báo cáo, nhưng chưa tự xác minh ngày/DPS của từng quyền. Cần đối chiếu số cổ phiếu hưởng quyền, kỳ và phần cổ đông không kiểm soát nếu muốn nối event-level.

## 5. Thay đổi số cổ phiếu

Stock split/cổ tức cổ phiếu/phát hành làm DPS danh nghĩa kém so sánh. Với split có tỷ lệ k, DPS trên cơ sở sau split của khoản trước đó có thể chuẩn hóa bằng chia k khi quyền/cơ sở đã rõ. Phát hành huy động vốn không đơn giản là split; cần chính sách điều chỉnh riêng và thời điểm hưởng quyền.

Không điều chỉnh “15% cổ tức cổ phiếu” thành DPS tiền mặt. Lưu corporate action và basis; không đủ thông tin so sánh thì gán unknown cho nhãn bị ảnh hưởng.

## 6. Hoãn, giảm và bỏ chi

Hoãn là dời lịch muộn; giảm là giảm mức so trên cùng basis; omitted là không có mức đủ điều kiện trong cửa sổ đã xác minh độ phủ. Doanh nghiệp có thể hoãn mà không giảm DPS, hoặc giảm DPS nhưng vẫn trả đúng lịch.

Thông báo đổi ngày sớm hơn không tạo delay dương. Với nhiều amendment, lưu cả lịch gốc và lịch mới để đo “so với lịch gốc” hoặc “so với lịch ngay trước”; không trộn hai định nghĩa.

## 7. Kiến thức cần kiểm tra bằng bài tập

Đọc một chuỗi quyền thật, đánh dấu từng ngày, loại bằng chứng, tổng DPS/components và lịch sửa. Giải thích vì sao source_missing khác omitted. Nguồn học là các thông báo đã đọc V02/V03 trong [sổ nguồn](../02-so-tai-lieu-tham-khao.md); chưa có quy định pháp lý cụ thể được kiểm chứng trong hồ sơ này.
