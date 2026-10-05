# N2 — Kỹ thuật IT cho engine kịch bản

Thiết kế đề xuất, chưa có code. [Tài chính](02-kien-thuc-tai-chinh.md), [protocol](04-du-lieu-thi-nghiem-danh-gia.md).

## 1. Schema scenario

Mỗi scenario lưu ID, công ty/pháp nhân, phạm vi báo cáo, kỳ cơ sở, khoảng mô phỏng, snapshot dữ liệu, phiên bản công thức, tác giả và thời điểm tạo. Mỗi input có giá trị/đơn vị, loại `observed` hoặc `assumed`, fact nguồn hoặc lý do giả định, trạng thái duyệt và ngày khả dụng.

Mức cổ tức gồm loại `announced`, `confirmed_paid` hoặc `hypothetical`; tham chiếu sự kiện và cơ sở số cổ phiếu. Không cho input thiếu mặc định thành 0. Unknown hạn chế tiền phải hiển thị trước kết quả, dù người dùng chủ động chọn một giả định để mô phỏng.

## 2. Engine tính xác định

Thực hiện hàm nhận inputs đã kiểm tra và trả cân đối tiền, headroom, bảng đóng góp và các giả định. Dùng decimal/numeric; đổi đơn vị tại lớp chuẩn hóa. Không lấy dữ liệu live thay snapshot mà không thay version scenario.

Tạo bảng phân loại dòng tiền độc quyền: mỗi khoản nguồn chỉ được đưa vào một hạng, với dấu và phép điều chỉnh rõ. Cảnh báo khi lãi/thuế/cổ tức hoặc khoản vốn lưu động bị đưa vào cả CFO và dòng chi riêng. Đây là kiểm tra quy tắc, không cần huấn luyện mô hình.

## 3. Bảng nhạy cảm

Sinh lưới các giá trị CFO và CapEx hoặc cổ tức theo khoảng người dùng chọn; các khoảng là giả định. Giữ các input khác cố định và lưu danh sách tham số thay đổi. Với CFO âm/0, từ chối chế độ “giảm phần trăm CFO” hoặc chuyển sang giảm tuyệt đối có thông báo.

Output API gồm `scenario_status`, `currency`, `period`, `cash_end`, `headroom`, `cashflow_components`, `assumptions`, `source_refs` và `limitations`. UI hiển thị nguồn lịch sử và giả định cạnh nhau, cùng nhãn “kịch bản theo giả định”.

## 4. Tái lập và kiểm tra

Export JSON/CSV gồm inputs, facts nguồn, công thức và kết quả. Chạy lại cùng snapshot/version phải cho cùng số. Kiểm tra dấu, đơn vị, không đếm hai lần, input thiếu và tính đơn điệu theo giả định: giữ các khoản khác cố định, tăng cổ tức làm giảm tiền cuối kỳ tương ứng.

Khả năng tải CSV/API kế thừa pipeline; không cần thêm hệ thống phân tán. Tài liệu [PostgreSQL numeric](https://www.postgresql.org/docs/current/datatype-numeric.html) và [constraints](https://www.postgresql.org/docs/current/ddl-constraints.html) là nguồn kỹ thuật tham khảo; schema này là thiết kế project chưa được benchmark.
