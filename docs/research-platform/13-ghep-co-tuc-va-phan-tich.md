# Ghép sự kiện cổ tức và phân tích mối quan hệ

## Cầu nối lợi nhuận tiền và lớp đối chiếu cổ tức

SRS v3.1 thêm tối thiểu một ca cầu nối LNTT→CFO, trình bày LNST riêng. CFO tính=start+Σleaves, residual=CFO báo cáo−CFO tính; không cộng subtotal hai lần, không biến residual thành nguyên nhân kinh tế. Hai năm chỉ phân rã delta khi tương thích kỳ/scope/mapping/source version. Missing trả status+reason; residual0 không đủ chứng minh đầy đủ dòng.

Góc bắt buộc: LNST/CFO năm t đối chiếu DPS thuộc profit_year=t tại as_of; timeline công bố/record/lịch trả riêng. Góc thực chi tùy chọn: CFO và dòng chi cho chủ sở hữu cùng kỳ/scope, không gán dòng này về profit_year. Góc thông tin tại cutoff để nghiên cứu sau. Không tính CFO/DPS khác đơn vị; không suy nguồn tài trợ hoặc khả năng trả cổ tức từ đối chiếu mô tả. [Quy tắc và điều kiện](../research-profit-cash-dividend/03-nghiep-vu-va-tu-dien.md).

Quy tắc project ngày 03/10/2026. Đích là **cổ tức tiền mặt được công bố theo năm lợi nhuận**, phân tích lịch sử mô tả. Nhãn dự báo hoặc tiền thực trả thuộc protocol tương lai khác.

## 1 Hai lớp nhìn dữ liệu

Bảng doanh nghiệp–năm dùng profit_year để ghép BCTC và components cổ tức. Timeline dùng published_at/record_date/scheduled_payment_date để thấy diễn biến công bố. Một thành phần thuộc 2025 có thể công bố năm 2026; không mâu thuẫn và không được đổi năm lợi nhuận để chart đẹp.

Hindsight snapshot cho phép nhìn BCTC đầy đủ và những thông báo phát sinh sau năm lợi nhuận, nhưng phải ghi as_of và tính đầy đủ. Không diễn giải phân tích hồi cứu này như dự đoán tại thời điểm trước thông báo.

## 2 Identity và vòng đời

1. Resolve issuer/ticker/ISIN với nguồn; thiếu mapping để review.
2. Canonical notice ID dedup các route của cùng thông báo. Các nơi đăng cùng đợt là source references, không hai payments.
3. Event components tách đúng năm và đợt. Nếu nguồn có tổng DPS, tổng components phải khớp theo đơn vị/tolerance.
4. Review amendment/cancellation theo đối tượng và field: sửa lịch thay lịch trên active view, giữ DPS; sửa DPS thay component đang có hiệu lực; nội dung hành chính không tự đổi DPS. Hủy thông báo/quyền/ngày đăng ký làm đối tượng thực hiện đó không còn active, lưu bản cũ và relation; không đồng nghĩa hủy mọi quyết định cổ tức hoặc annual DPS = 0. Cần rà bản thay thế và giữ coverage partial/unknown nếu còn nghi vấn. Phương án cổ tức chỉ bị loại khỏi aggregate tương ứng khi có bằng chứng hủy đúng đối tượng đó.
5. Hai notices ticker/ngày/DPS giống chỉ là duplicate candidate; không auto xóa vì có thể hai đợt hợp lệ. Không dùng hash HTML làm event identity vì sidebar có thể đổi.
6. Nghị quyết phê duyệt và thông báo quyền cùng nội dung có vai trò khác, không cộng cả hai vào DPS.

Annual selection ưu tiên FY audited của scope đã chọn; reviewed interim tách khỏi series năm. Restated comparative giữ source version, không ghi đè fact cũ. Mọi aggregate lưu operand/component IDs.

## 3 Tổng hợp DPS có điều kiện

observed_dps = tổng components tiền mặt active, đã duyệt, rõ profit_year và cùng share basis. Đây là tổng phần đã quan sát.

annual_announced_dps chỉ được công bố như đầy đủ khi coverage ledger được review complete_as_of_snapshot: đã rà nguồn phù hợp và trang/filter liên quan, đối chiếu quyết định/năm/đợt còn lại và amendments, không còn đợt/nguồn thiếu đã biết. Ghi reviewer/evidence/as_of; nếu còn nghi vấn giữ partial/unknown.

Nếu có thay đổi share basis và chưa có adjustment được duyệt: không cộng raw DPS khác basis thành annual total hoặc tính tăng trưởng. Hiển thị các đợt raw trên timeline. Nếu explicit nguồn xác nhận không chia tiền mặt cho năm: declared_zero riêng, không suy từ absence hoặc timeout.

Dashboard luôn hiển thị observed/annual đủ khác nhau. Pending tài liệu hoặc notice không gán số 0 và không bị ẩn khỏi bảng chất lượng.

## 4 Phân tích MVP

| Phân tích | Công thức/cách làm | Điều kiện |
|---|---|---|
| Lợi nhuận và CFO | Hai đường theo năm, cùng đơn vị/scope | Đủ fact đã review |
| CFO/LNST | CFO / LNST tổng | LNST >0; <=0 trả trạng thái riêng |
| Tiền/tài sản | Cash / assets | Assets >0, cùng instant/scope |
| Nợ phải trả/tài sản | Liabilities / assets | Không gọi là tỷ lệ nợ vay |
| Mức và chênh lệch DPS | DPS_t, DPS_t−DPS_(t−1) | Annual đủ/comparable |
| Tăng trưởng DPS | (DPS_t−DPS_(t−1))/DPS_(t−1) | Năm trước >0, basis tương thích |
| Biến động lợi nhuận | Mức/chênh lệch, growth khi nền >0 | Không chia nền âm/0 thành growth bình thường |
| Quan hệ mô tả | Scatter, Spearman trên tập hợp lệ | Công bố n/missing/scope/selection |

Không tính “coverage tiền trả” bằng CFO VND / DPS VND/cổ phiếu. Phải có tổng khoản chi cùng scope/khoảng thời gian được kiểm chứng, nếu muốn bổ sung phép đó. Dòng tiền cổ tức trả trong năm có thể thuộc năm lợi nhuận khác.

Số tiền tuyệt đối giữa doanh nghiệp khác quy mô dễ nhiễu; ưu tiên xu hướng trong từng doanh nghiệp và tỷ số phù hợp. Tương quan gộp chỉ thăm dò trên cohort cùng scope; dữ liệu lặp theo công ty và ngành/năm gây phụ thuộc. Với ba năm, tương quan từng công ty quá ít để diễn giải mạnh. Không chọn outliers hoặc missing để tăng hệ số.

Theo AN07 trong [SRS v2.1](02-de-tai-va-srs.md), UI không xuất hệ số khi có <3 cặp hợp lệ hoặc một biến hằng; trả lý do và n. Đây là điều kiện hiển thị của sản phẩm, không phải ngưỡng đảm bảo tin cậy thống kê. Mẫu từ 3 cặp trở lên vẫn phải giữ giới hạn mẫu nhỏ/phụ thuộc; tên biến, cohort, filters, snapshot và phần loại luôn đi cùng kết quả.

[Spearman của SciPy](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.spearmanr.html) là tài liệu hàm; không coi p-value mẫu nhỏ/lặp theo công ty là kiểm định độc lập đáng tin. MVP báo n, biểu đồ và giới hạn; không cần hồi quy nhiều biến với 15–24 quan sát.

## 5 Ba case để trình bày

Lợi nhuận tăng nhưng CFO yếu; cổ tức duy trì trong khi lợi nhuận/dòng tiền giảm; một công bố gộp nhiều năm hoặc sửa lịch làm tổng sai nếu xử lý đơn giản. Chọn case theo dữ liệu thật đủ nguồn, không đặt tên doanh nghiệp trước rồi tự dựng kết quả.

Mỗi case gồm facts, operands, period/scope, active components, coverage, snapshot và câu diễn giải có giới hạn. Không kết luận bền vững, gian lận hoặc chắc chắn cắt giảm chỉ từ tỷ số.

## 6 Nối lên dự đoán

**Cập nhật ngày 04/10/2026:** đồ án ưu tiên đối chiếu phiên bản/ảnh hưởng, xem [nghiên cứu lần hai](20-nghien-cuu-lan-hai-va-chot-de-tai.md). Dự đoán bên dưới là phương án tùy chọn.

Project chưa tạo nhãn cut/maintain theo ngưỡng 30%, window 12 tháng hoặc cảnh báo 0–4. Tốt nghiệp phải chọn một mục tiêu rõ, cutoff feature trước outcome, nhãn trưởng thành/độ phủ và share adjustment. Xem [hướng tốt nghiệp](09-lien-thong-tot-nghiep.md); không kế thừa mặc định protocol dự báo cũ.
