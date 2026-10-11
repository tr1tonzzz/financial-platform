# G01 — Sàng lọc và lập hồ sơ thẩm định cổ tức có giải thích

**Lịch sử nghiên cứu trước CR-AN-03:** phần sàng lọc/criteria/pass-fail-unknown G01 và BUC04 cũ đã loại theo yêu cầu người thực hiện ngày11/10/2026. Chỉ kế thừa lưu nhận xét/câu hỏi/bằng chứng và snapshot. [SRS v3.3/mục18](../research-platform/22-srs-dac-ta-yeu-cau-phan-mem.md) và [danh mục UC v2.0](../research-platform/27-yeu-cau-chuc-nang-va-vi-du.md) là nguồn hiện hành; prototype cũ giữ làm bằng chứng lịch sử.

Thuộc BUC04/BUC05; D09–D12. Nhu cầu thực tế: chọn doanh nghiệp nào cần đọc trước, biết vì sao được chọn, xem bằng chứng và lưu vấn đề chưa giải quyết. Giá trị được đo bằng độ chính xác nhận diện vấn đề và công sức thẩm định; không đo bằng số dashboard hay tự tuyên bố tăng lợi nhuận đầu tư.

## Đầu vào và ngôn ngữ tiêu chí

Tập doanh nghiệp phi tài chính đã có trong pilot; snapshot/as_of; cửa sổ năm; scope; facts/DPS/basis/coverage; danh sách tiêu chí do người dùng xác nhận. G02/G03 là đầu vào tùy chọn: nếu tiêu chí không dùng chúng thì không bắt buộc có hai trường bổ sung. Ngành và giá/yield chưa bắt buộc.

`screen_definition`: id/version/name, universe_ids, years, scope_policy, as_of_policy, conditions[{metric_id, operator, threshold, period_window, missing_policy}], created_by/time. Operator bản đầu chỉ `>=`, `<=`, `>`, `<`, `==` trên metric có registry; không nhận biểu thức Python/SQL tùy ý. Threshold được lưu Decimal và units. Bộ tiêu chí minh họa ghi là tiêu chí thử nghiệm, không chuẩn chất lượng tài chính đã được xác lập.

Ví dụ tiêu chí: CFO dương ở các năm đủ dữ liệu; CFO/LNST đạt mức người dùng đặt; không có giảm DPS năm trên basis tương thích; CFO sau CAPEX/phân phối không âm nếu có G02. Điều kiện xu hướng cần từng năm kế tiếp, không nối qua năm thiếu. “CFO giảm trong khi DPS giữ/tăng” là điều kiện tìm vấn đề, không mặc định là điều kiện chọn mua.

## Logic ba trạng thái

Mỗi điều kiện trả `pass`, `fail`, `unknown` với value/threshold/operands/reason. Missing, annual DPS partial, cross-scope, basis unresolved hoặc metric not_applicable không được pass. AND: có fail → kết quả không đạt, vẫn liệt kê điều kiện unknown; không fail nhưng có unknown → chưa đủ cơ sở; tất cả pass → đạt theo bộ tiêu chí. Không được biến trạng thái không đạt thành hồ sơ đầy đủ khi có điều kiện unknown. Bản đầu chỉ hỗ trợ AND; OR cần ngữ nghĩa riêng và test trước khi thêm.

Hệ thống luôn xuất số doanh nghiệp trong tập, số ở từng nhóm, excluded và lý do. Người dùng có thể xếp theo trạng thái/công việc cần làm, nhưng không có điểm tổng trọng số hoặc “cổ phiếu tốt nhất”. Chọn đọc trước vì có vấn đề quan trọng khác với được đánh giá tốt. Ba doanh nghiệp pilot chưa đủ để đánh giá bộ lọc toàn thị trường hoặc benchmark ngành.

## Hồ sơ thẩm định hoàn chỉnh

| Thành phần | Nội dung và cách sử dụng |
|---|---|
| Thông tin hồ sơ | Doanh nghiệp, snapshot, as_of, scope, kỳ, bộ tiêu chí/version |
| Kết quả kiểm tra | Theo từng tiêu chí: dữ liệu, công thức, ngưỡng, trạng thái và bằng chứng |
| Luận điểm hệ thống | Rule_id có operands: CFO/DPS khác chiều, G02 thiếu bao phủ, basis unresolved; chỉ mô tả |
| Nhận xét người dùng | Nội dung, author/time, nguồn được tham chiếu; đánh dấu giả thuyết hoặc kết luận có bằng chứng |
| Việc cần tra soát | Đọc khoản đầu tư nào? khoản trả thuộc chủ thể nào? thiếu thông báo nào? trạng thái open/resolved và evidence |
| Bản lưu | JSON/CSV hoặc Markdown đọc được, checksum, refs; replay kết quả tính theo version |

Luồng: chọn bộ tiêu chí → xem ba nhóm → mở một doanh nghiệp → tra soát nguồn từng kết quả → ghi câu hỏi → bổ sung bằng chứng/đánh dấu xử lý → lưu hồ sơ và snapshot. Nếu facts đổi, hồ sơ cũ vẫn giữ bản freeze; chỉ so sánh với hồ sơ hiện hành khi người dùng chủ động tính lại. Phát hiện ảnh hưởng tự động là ý tưởng giai đoạn sau, không giả rằng FR35 replay đã làm được nó.

## Thiết kế để thực hiện

`metric_registry` định nghĩa metric/unit/required facts/eligibility; `screen_service` chỉ gọi metric đã có; `dossier_service` lưu tham chiếu kết quả đã đóng băng và ghi chú. Không viết lại normalization trong screener. Module công thức dùng chung BUC02/03 và UI; mọi kết quả có source refs. Lưu SQLite cho bộ tiêu chí và dossier; JSON cho snapshot để replay offline. UI Streamlit gồm danh sách ba nhóm, bảng giải thích và trang hồ sơ, không cần đổi toàn bộ stack.

Triển khai G01 theo hai mức: (1) criteria hiện có FR29 với trạng thái/giải thích và lưu bộ lọc; (2) bổ sung G02/G03, ghi chú/câu hỏi và xuất dossier. Nghiệm thu chức năng hoàn chỉnh phải có mức 2 theo dữ liệu ca đã chọn; chỉ có bộ lọc là UC phân rã, chưa hoàn thành hồ sơ thẩm định.

## Kiểm chứng giá trị thực tế

TC-D09: lưu/tải/version bộ tiêu chí, invalid operator/unit bị chặn. TC-D10: bảng chân trị AND cho pass/fail/unknown, không bỏ hồ sơ thiếu; condition riêng có nguồn. TC-D11: note và issue nằm trong dossier đúng snapshot, không đổi fact/source; mở lại sau cập nhật còn đúng bản cũ. TC-D12: xuất/replay criteria + results + notes + refs; thay version không âm thầm đổi kết quả.

Thử tác vụ với 3–5 người có kiến thức tài chính cơ bản nếu huy động được, không coi là cỡ mẫu suy rộng. Tác vụ đối chứng: từ cùng tài liệu xác định hồ sơ có (a) CFO chưa bao phủ khoản chi, (b) DPS không so sánh được do basis, (c) thiếu dữ liệu không được kết luận. Chuẩn đáp án cần người độc lập duyệt. Đổi thứ tự/tập ca tương đương để giảm hiệu ứng học; đo thời gian tổng, số lỗi diễn giải, số nguồn tra đúng và điểm tin cậy tự khai. Tiêu chí nghiệm thu an toàn ngữ nghĩa: không hồ sơ unknown nào bị xuất là đạt; mọi lý do đi tới operands/nguồn. Tỷ lệ giảm giờ hoặc tăng độ chính xác là **kết quả phải đo**, chưa đặt bằng chứng bằng một mục tiêu đẹp. Chưa có thử người dùng trong nghiên cứu này.

**Khả thi:** cao cho bộ lọc minh bạch trên pilot, trung bình cho workflow dossier hoàn chỉnh. Ước tính 20–30 giờ bao gồm lưu criteria, UI hồ sơ và tests, với facts/metric services đã có. Một demo có thể dùng dữ liệu nhập/duyệt từ ca thật; không hạ coverage để đủ cả ba nhóm. Khả năng mở rộng thị trường bị giới hạn bởi độ đầy đủ dữ liệu BUC01, chưa bởi thuật toán lọc.
