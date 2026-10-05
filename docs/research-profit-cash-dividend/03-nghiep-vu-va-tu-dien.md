# 03 — Nghiệp vụ tài chính, từ điển và quy tắc phân tích

**Trạng thái cập nhật05/10/2026:** hướng kết hợp đã được tích hợp vào [SRS v3.1](../research-platform/22-srs-dac-ta-yeu-cau-phan-mem.md), CR-PCD-01/mục15, theo yêu cầu cập nhật tài liệu của người thực hiện. Tối thiểu một ca cầu nối là nghĩa vụ dự thảo; E05/E10 và ca thêm có điều kiện. Nội dung đề xuất ngày04/10 bên dưới là cơ sở nghiên cứu; các câu “chưa tích hợp/chờ change record” mô tả trạng thái lúc đó, được thay bởi SRS v3.1. Chưa có phê duyệt giảng viên hoặc kiểm thử ứng dụng đã chạy. Kế hoạch/checklist v3 là lịch triển khai duy nhất; bảng tuần/giờ trong hồ sơ nghiên cứu là phương án trước tích hợp.

Thiết kế đề xuất ngày 04/10/2026. Giữ quy tắc [SRS hiện hành](../research-platform/22-srs-dac-ta-yeu-cau-phan-mem.md); extension chỉ hoạt động khi đủ đầu vào và được duyệt.

## 1. Ba khái niệm cần tách

**Lợi nhuận** ghi nhận doanh thu/chi phí theo kỳ kế toán; bán chịu có thể tạo doanh thu trước khi thu tiền. **CFO** là lưu chuyển tiền thuần từ hoạt động kinh doanh, không phải số tiền cuối kỳ hay tất cả dòng tiền. **Cổ tức tiền mặt** là phân phối cho cổ đông: có mức/chính sách công bố, các đợt thực hiện quyền, lịch dự kiến và bằng chứng đã chi; các lớp không tương đương.

CFO dương không đồng nghĩa toàn bộ có thể trả cổ tức: doanh nghiệp còn đầu tư, trả nợ, duy trì thanh khoản. CFO âm một kỳ không chứng minh gian lận hoặc chắc chắn cắt cổ tức. Tiền hợp nhất không tự là tiền công ty mẹ có thể sử dụng. Muốn đánh giá điều kiện pháp lý phân phối phải có nghiên cứu pháp lý và BCTC pháp nhân phù hợp; MVP không đưa kết luận này.

## 2. Từ điển dữ liệu

| Mã | Nghĩa/đơn vị | Grain và quy tắc |
|---|---|---|
| net_income_total | Tổng LNST, VND | Report–period–scope–version; dùng với CFO cùng scope |
| cfo | Lưu chuyển tiền thuần HĐKD, VND | Flow trong cả kỳ, giữ dấu âm |
| cash_equivalents | Tiền và tương đương tiền, VND | Stock tại cuối kỳ; không gộp tiền gửi khác nếu chưa phân loại |
| total_assets | Tổng tài sản, VND | Cuối kỳ; mẫu số phải dương |
| total_liabilities | Tổng nợ phải trả, VND | Không tự gọi toàn bộ là nợ vay |
| total_equity | Tổng vốn chủ sở hữu, VND | Giữ giá trị âm nếu báo cáo có |
| profit_before_tax | Lợi nhuận trước thuế, VND | Điểm xuất phát cầu nối nếu báo cáo gián tiếp dùng LNTT |
| bridge_item | Một dòng điều chỉnh, VND có dấu | Report–period–scope–line; có raw label/code/locator/group |
| bridge_subtotal | Dòng tổng trung gian | Dùng kiểm tra, không cộng cùng children |
| owner_distributions_paid | Dòng tiền cổ tức/lợi nhuận đã chi cho chủ sở hữu | Kỳ thực chi của BCLCTT; giữ phạm vi đúng nhãn, chưa mặc định chỉ cổ đông công ty mẹ |
| dividend_component | Phần của một đợt theo năm lợi nhuận | Issuer–security–event–component–revision |
| dps_vnd | Cổ tức tiền mặt/cổ phiếu, VND/cp | Phân biệt gross theo thông báo với net người nhận; không dùng thuế cá nhân để đổi số nguồn |
| profit_year | Năm lợi nhuận theo văn bản | Unknown khi không rõ; khác năm record/payment/publication |
| share_basis | Cơ sở cổ phiếu/quyền | Lưu loại cổ phần, mệnh giá, hiệu lực và quan hệ corporate action |
| coverage | Phạm vi nguồn đã rà tại as_of | complete_as_of/partial/unknown/declared_zero/not_applicable |

Sáu dòng đầu là lõi; các trường sau là extension/cấu trúc sự kiện đã nêu rõ. Không lấy LNST thuộc cổ đông mẹ thay tổng LNST để chia với CFO toàn tập đoàn. Khi nghiên cứu payout cho cổ đông mẹ cần chỉ tiêu lợi nhuận thuộc chủ sở hữu tương ứng và định nghĩa riêng.

## 3. Công thức lõi và điều kiện

| Chỉ tiêu | Công thức | Trường hợp không công bố số |
|---|---|---|
| Chênh lệch tuyệt đối | X(t)−X(t−1) | Thiếu dữ liệu, lệch scope/kỳ/basis |
| Tăng trưởng | X(t)/X(t−1)−1 | Nền≤0: trả lý do, vẫn cho xem chênh lệch tuyệt đối |
| Chuyển lợi nhuận thành tiền | CFO/LNST | LNST≤0 hoặc operands không tương thích |
| Khoảng cách lợi nhuận–tiền | LNST−CFO, VND | Thiếu operands; không đặt tên “dồn tích bất thường” |
| CFO/tài sản cuối kỳ | CFO/A_end | A_end≤0; ghi rõ không phải mẫu số tài sản bình quân |
| Tiền/tài sản; nợ phải trả/tài sản | Cash/A_end; L/A_end | A_end≤0 hoặc khác scope |
| DPS theo năm lợi nhuận | Tổng active components của cùng FY/security/basis | Nếu coverage chưa đủ chỉ hiển thị observed subtotal, annual=null |
| DPS growth | DPS(t)/DPS(t−1)−1 | Annual thiếu/partial/basis chưa tương thích hoặc nền≤0 |

CFO/LNST là tỷ số mô tả, không ngưỡng kết luận chất lượng lợi nhuận. Đối với ba năm, có thể so tổng CFO với tổng LNST nếu chuỗi cùng scope, đầy đủ và tổng LNST dương; không lấy trung bình giản đơn các tỷ số năm. Chưa đưa chỉ tiêu nhiều năm thành nghĩa vụ MVP.

## 4. Cầu nối CFO

Theo phương pháp gián tiếp, chuẩn hóa đúng điểm bắt đầu trong báo cáo. Với mẫu bắt đầu từ LNTT:

`CFO_tính = LNTT + Σ điều chỉnh phi tiền/đầu tư/tài chính + Σ điều chỉnh vốn lưu động + Σ dòng tiền vận hành khác có dấu`.

`Residual = CFO_báo_cáo − CFO_tính`.

Không cộng dòng “lợi nhuận trước thay đổi vốn lưu động” cùng toàn bộ LNTT và các dòng tạo ra tổng đó. Giữ `line_role=leaf/subtotal/total` và quan hệ cha–con; mỗi leaf chỉ được cộng một lần. Các khoản lãi vay, thuế phải theo mẫu, không tự cộng trừ dựa vào tên chung.

Nếu bắt đầu từ LNST, phải thêm cầu nối LNST→LNTT từ **chi phí thuế hiện hành và thuế hoãn lại**, có dấu nguồn, trước khi dùng chuỗi từ LNTT. Không lấy thuế thực nộp làm chi phí thuế để đảo ngược LNST. Giao diện ưu tiên bảng LNST bên cạnh và cầu nối LNTT→CFO được ghi rõ.

Với phương pháp trực tiếp, trình bày nhóm thu–chi theo báo cáo; không tự dựng cầu nối gián tiếp. Với dòng chưa trích được: `missing`, `not_reconciled`, residual nếu tính được phần quan sát; không gọi residual là một nguyên nhân kinh tế. Dữ liệu làm tròn: tolerance theo đơn vị gốc và chính sách cộng sai số, không dùng một ngưỡng tùy ý để che lỗi dấu.

Phân tích biến động giữa hai năm: `ΔCFO = ΔLNTT + ΣΔdòng_điều_chỉnh + Δresidual`. Đây là phân rã số học theo báo cáo. Một dòng đóng góp lớn không tự chứng minh nguyên nhân vận hành; muốn nói hàng tồn kho giảm vì bán tốt phải đọc thuyết minh/giải trình.

## 5. Ba cách nối với cổ tức

| Góc nhìn | Khóa thời gian | Cách đọc đúng |
|---|---|---|
| Chính sách theo lợi nhuận | LNST/CFO FYt ↔ DPS thuộc profit_year=t | So kết quả năm với mức công bố thuộc năm đó; lịch sử tại as_of |
| Dòng tiền thực chi | CFO kỳt ↔ dòng chi chủ sở hữu trong BCLCTT kỳt | So các dòng tiền cùng kỳ/scope; không đổi nhãn thành cổ tức từ lợi nhuận nămt |
| Thông tin sẵn có tại thời điểm | Chỉ nguồn published/available≤cutoff | Dùng nếu nghiên cứu phản ứng/dự báo; phải có cutoff và cửa sổ tương lai đã đóng |

MVP bắt buộc góc thứ nhất và timeline. Góc thứ hai làm theo ca đủ nguồn, góc thứ ba để mở rộng. Không nhập nhằng các góc nhìn vào một cột dividend_year.

**Payout/coverage chỉ mở có điều kiện:** `cash_dividend_amount_for_profit_year / matched_earnings` cần tổng số tiền công bố thuộc năm, cổ phần đủ điều kiện từng đợt và mẫu số lợi nhuận được định nghĩa. `CFO / abs(owner_distributions_paid)` đo bao phủ dòng chi theo BCLCTT khi denominator>0, cùng scope/kỳ; không là “khả năng trả cổ tức tương lai”. Không tính CFO/DPS vì VND và VND/cp khác đơn vị. DPS×cổ phiếu cuối năm không bảo đảm đúng số tiền của các đợt có số cổ phiếu khác nhau. DPS/EPS chỉ tính khi kiểm tra share basis và mục đích chỉ số; bình quân cổ phiếu tính EPS có thể khác số hưởng quyền.

## 6. Quy tắc diễn giải

Cho phép: “LNST tăng, CFO giảm trong hai cột được so sánh; biến động các dòng tồn kho/phải thu đóng góp số học vào thay đổi CFO; cổ tức công bố thuộc năm X có các đợt sau…”. Không cho phép: “doanh nghiệp lấy nợ để trả cổ tức” chỉ vì cùng kỳ có vay và trả cổ tức; tiền có tính thay thế và báo cáo tổng không truy được nguồn tài trợ riêng.

Tỷ lệ công bố trên mệnh giá không là dividend yield theo thị giá. “Chưa thấy thông báo” không là zero. Ngày thanh toán đã qua không tự là paid. Số so sánh được trình bày lại phải lưu version và thời điểm khả dụng.
