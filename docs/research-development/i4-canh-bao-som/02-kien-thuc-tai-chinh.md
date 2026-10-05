# I4 — Kiến thức tài chính: tín hiệu, nhãn và rủi ro diễn giải

Ngày: 03/10/2026. Bám định nghĩa hiện hành; mọi threshold là tham số nghiên cứu.

## 1. Đích dự báo phải đo được

Hai đích hợp lệ nhưng khác nhau: giảm cổ tức tiền đã có bằng chứng thực trả; giảm mức tiền mặt được công bố. Chọn sau pilot I3. Không trộn đích trong train hoặc dùng tên “cắt tiền đã trả” cho dữ liệu lịch.

Chỉ nghiên cứu sự giảm trên doanh nghiệp có past_dps>0 ở cửa sổ trước. Doanh nghiệp vốn không trả không tự trở thành ca omitted. Cổ tức đặc biệt hoặc thay đổi cơ sở cổ phiếu cần gắn cờ.

## 2. Quy tắc nhãn

```text
past_window   = (cutoff−12 tháng, cutoff]
future_window = (cutoff, cutoff+12 tháng]
reduction     = 1 − future_dps / past_dps
```

Nếu outcome chưa khép: censored. Nếu độ phủ hoặc khả năng so sánh chưa đủ: unknown. Sau đó mới xét past_dps>0: future_dps=0 và coverage complete → omitted; future_dps>0 và reduction≥0,30 → reduced; còn lại → maintained. Ca không có past_dps dương là not_eligible cho bài toán cắt giảm.

Thứ tự trên giúp omitted không bị lẫn reduced dù reduction=100%. Có thể gộp reduced/omitted thành lớp dương, vẫn giữ subtype. Ngưỡng 30% bám đề cương; kiểm tra 10/20/30% đã chốt trước test, không chọn threshold label theo điểm test.

## 3. Tín hiệu tài chính

| Tín hiệu trong đề cương | Lý do xem xét | Vì sao có thể cảnh báo sai |
|---|---|---|
| CFO<0 | Kinh doanh tiêu hao tiền | Chu kỳ đầu tư/vốn lưu động hoặc dự trữ tiền |
| CFO/LNST<0,5 khi LNST>0 | Lợi nhuận chưa chuyển thành tiền tương xứng | Thời điểm thu tiền, LNST gần 0 hoặc thu nhập bất thường |
| L/A tăng >10 điểm % | Nghĩa vụ tương đối tăng | Mở rộng tài sản, khoản phải trả không chịu lãi |
| Cash/A giảm >5 điểm % | Vùng đệm tiền giảm | Chuyển tiền sang đầu tư ngắn hạn hoặc dùng tiền có kế hoạch |

Một điểm mỗi tín hiệu; giảm/thiếu đầu vào không cộng 0. Bản score chính cần đầy đủ và domain hợp lệ; khi CFO/LNST không áp dụng do lỗ, hiển thị trạng thái và không gọi score đầy đủ. Có thể thiết kế phiên bản riêng cho doanh nghiệp lỗ, nhưng phải ghi rule_version và đánh giá riêng.

## 4. Mùa vụ và lựa chọn mốc

BCTC năm thường công bố sau cuối kỳ, trong khi cổ tức có thể có kỳ tạm ứng và kỳ cuối khác nhau. So hai cửa sổ 12 tháng giảm lệch lịch nhưng không xóa hoàn toàn khác biệt mùa vụ hoặc việc một lịch bị đẩy qua biên.

Một khoản trả chuyển sang tháng 13 có thể tạo reduced/omitted cửa sổ 12 tháng dù chính sách năm không giảm. Giải thích đúng target theo cửa sổ; có thể nghiên cứu độ nhạy cửa sổ dài hơn ở phân tích bổ sung, không sửa nhãn âm thầm.

## 5. Cảnh báo khác xác suất và nhân quả

Score cao nghĩa nhiều điều kiện quy tắc xảy ra; không suy xác suất 75% từ điểm 3/4. Logistic có xác suất ước lượng của target trên mẫu, không là bảo đảm tương lai. Hệ số CFO có thể phản ánh yếu tố ngành hoặc chính sách chưa thu thập.

Theo [hướng dẫn calibration](https://scikit-learn.org/stable/modules/calibration.html), cần kiểm tra tỷ lệ thực tế theo nhóm xác suất. Brier tốt hơn có thể do khả năng phân biệt, không chỉ calibration; dùng cùng reliability diagram và số mẫu.

## 6. Các nhóm cần báo riêng

LNST≤0, vốn≤0, cơ sở cổ phiếu thay đổi, cổ tức đặc biệt, phạm vi riêng/hợp nhất, basis khác và không đủ audit. Không loại những nhóm này khỏi báo cáo coverage; chỉ loại đúng phần ratio/forecast không hợp lệ và ghi lý do.
