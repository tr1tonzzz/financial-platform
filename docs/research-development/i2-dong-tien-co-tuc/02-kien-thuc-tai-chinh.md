# I2 — Kiến thức tài chính: lợi nhuận, dòng tiền và dư địa cổ tức

Ngày: 03/10/2026. Đây là kiến thức và định nghĩa nghiên cứu, chưa là kết luận doanh nghiệp cụ thể.

## 1. Lợi nhuận khác tiền

Lợi nhuận theo kế toán dồn tích có thể ghi nhận trước thu tiền. CFO chịu ảnh hưởng thu/chi kinh doanh và vốn lưu động; khấu hao giảm lợi nhuận nhưng không phải chi tiền cùng kỳ. CFO thấp có thể do tăng trưởng phải thu/tồn kho hoặc yếu thu hồi tiền; cần thuyết minh, không tự gán gian lận.

Một proxy mô tả là `(LNST-CFO)/A_avg`, khi có tài sản bình quân tương thích. Đây là chênh lệch lợi nhuận–dòng tiền giản lược; không đồng nhất với mô hình discretionary accruals hay bộ phát hiện gian lận. Không đưa proxy này vào MVP trước khi có lý do ngoài CFO/LNST.

## 2. Chỉ số lõi và ý nghĩa

| Chỉ số | Ý nghĩa nghiên cứu | Hạn chế |
|---|---|---|
| CFO/LNST | Mức dòng tiền so lợi nhuận dương | Nổ khi lợi nhuận gần 0; không dùng LNST âm |
| CFO/A_end | Khả năng tạo tiền so quy mô cuối kỳ | Khác chỉ số dùng tài sản bình quân |
| L/A_end | Nghĩa vụ phải trả so tài sản | Không đo riêng nợ vay/chi phí lãi |
| Cash/A_end | Vùng đệm tiền tại cuối năm | Một ảnh chụp thời điểm, có thể mùa vụ/hạn chế sử dụng |
| Cash/L | Tiền so toàn bộ nghĩa vụ | Không phải cash ratio thanh khoản chuẩn dùng nợ ngắn hạn |
| L/E | Đòn bẩy theo vốn dương | Không diễn giải tỷ số âm khi vốn âm như ít nợ |

Nếu CFO âm và LNST dương, hai tín hiệu CFO<0 và CFO/LNST<0,5 cùng nói một vấn đề; kiểm tra bỏ bớt để tránh đếm quá mạnh.

## 3. Payout và coverage

`Payout = DPS theo năm lợi nhuận / EPS tương thích`, EPS>0. EPS cần xét cơ sở cổ phiếu bình quân/điều chỉnh và phần lợi nhuận dùng cho EPS; DPS dùng cổ phiếu được hưởng quyền từng đợt. Không thay EPS bằng LNST tổng hợp nhất chia số cổ phiếu cuối năm nếu không kiểm tra.

`Cash coverage = CFO / dividends_paid`, mẫu số là số tiền đã trả cùng kỳ/phạm vi. Giữ riêng cổ tức công ty mẹ và cổ tức công ty con cho cổ đông không kiểm soát. Nếu ước tính `Σ(DPS_event × shares_entitled_event)`, ghi rõ estimated, không trộn với dòng tiền thực trả BCTC.

Coverage >1 chưa bảo đảm duy trì: tiền còn cần đầu tư, trả nợ, nghĩa vụ khác. Coverage<1 một năm chưa chứng minh mất khả năng trả: có thể dùng dự trữ hợp lệ. Cần xem chuỗi nhiều năm và thuyết minh.

## 4. CapEx, FCFE và phần mở rộng

Theo khung [Damodaran](https://pages.stern.nyu.edu/~adamodar/pdfiles/acf3E/book/ch11.pdf), đánh giá dư địa tiền cho cổ đông cần tính nhu cầu tái đầu tư và dòng tiền nợ. Công thức đề xuất dưới đây phải thống nhất cách phân loại thực tế:

```text
Net borrowing = tiền vay mới − tiền trả gốc
Cash after CapEx = CFO − CapEx_cash
FCFE_approx = CFO − CapEx_cash + Net borrowing
Cash gap = CFO − CapEx_cash − dividends_paid
```

Chỉ gọi FCFE xấp xỉ khi CFO đã bao gồm các khoản thuế/lãi phù hợp; cần xét tiền thuê, mua doanh nghiệp, khoản bất thường và cơ sở kế toán. “Tiền chi mua tài sản cố định/vô hình/sinh học” là phạm vi CapEx phải ghi rõ; không lấy toàn bộ dòng tiền đầu tư âm làm CapEx vì có thể gồm gửi tiền/mua khoản đầu tư.

Vay mới làm FCFE_approx tăng nhưng có thể giảm tính bền vững lâu dài. Cash gap chưa gồm tất cả dòng tài trợ và thay đổi tiền; không dùng nó làm đẳng thức tiền cuối kỳ.

## 5. Bảng mở rộng kiến thức → dữ liệu cần thêm

| Kiến thức | Đầu vào thêm | Câu hỏi trả lời |
|---|---|---|
| Chất lượng lợi nhuận | Phải thu, tồn kho, doanh thu, thuyết minh | Vì sao lãi chưa biến thành tiền? |
| FCFE và tái đầu tư | CapEx tiền, vay mới, trả gốc, thuê | Còn bao nhiêu tiền sau đầu tư/tài trợ? |
| Khả năng trả lãi | Lãi vay/chi tiền lãi, EBIT hoặc CFO | Áp lực phục vụ nợ có tăng? |
| Phân phối của công ty mẹ | Báo cáo riêng, lợi nhuận giữ lại, nghị quyết | Hợp nhất có phản ánh pháp nhân chi cổ tức? |

Đây là dữ liệu mở rộng có điều kiện; không suy quyền phân phối lợi nhuận hợp pháp chỉ từ tỷ số hợp nhất. Kiểm tra quy định áp dụng đúng kỳ nếu nghiên cứu vấn đề pháp lý.

## 6. Bài tập để sử dụng

Với số giả định LNST=100, CFO=40, CapEx=60, cổ tức thực trả=50 cùng kỳ/phạm vi: CFO/LNST=0,4; coverage=0,8; cash after CapEx=−20; cash gap=−70. Bài tập minh họa công thức, không là số của công ty thật hay bằng chứng nhãn reduced. Tiếp theo cần kiểm tra nguồn tiền tài trợ và số dư tiền, không tự kết luận doanh nghiệp cắt cổ tức.
