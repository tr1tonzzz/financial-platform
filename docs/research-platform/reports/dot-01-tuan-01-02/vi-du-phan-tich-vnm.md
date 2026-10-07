# Phụ lục báo cáo 1 — Phân tích sơ bộ Vinamilk quý I/2026

Ngày cập nhật: **06/10/2026**. Đây là ví dụ chính hiện tại của [báo cáo 1](bao-cao-01.md), thay mẫu DHG trước đó. Phụ lục giữ số VND gốc để kiểm bảng làm tròn, không phải bộ đáp án được kiểm độc lập.

## 1. Nguồn và cách lấy số

[BCTC hợp nhất Vinamilk quý I/2026](https://d8um25gjecm9v.cloudfront.net/cms/20260429_VNM_BCTC_DA_SOAT_XET_Q1_2026_HOP_NHAT_VN_d44326741a.pdf), từ [danh mục doanh nghiệp](https://www.vinamilk.com.vn/investor/reports/financial), công bố 29/04/2026. KPMG soát xét, trang PDF 5–6; báo cáo gồm 71 trang. Phạm vi Công ty CP Sữa Việt Nam và các công ty con, đơn vị VND, giai đoạn ba tháng kết thúc 31/03/2026 và cột ba tháng kết thúc 31/03/2025 **đã phân loại lại**. Không dùng LNST thuộc chủ sở hữu công ty mẹ thay tổng LNST hợp nhất.

[Thử nghiệm công cụ](thu-nghiem-cong-cu.md) đã chạy crawler/PDF/OCR ba trang: sáu ô LNST/CFO/chi cổ tức khớp nguồn. Cầu nối dưới đây được đọc thủ công từ **PDF 13/trang in 12**, rồi cộng bằng Python; chưa tự động trích toàn bộ. Bảng tham chiếu [JSON](../../../research-profit-cash-dividend/evidence/case-vnm-q1-2026.json) giữ số và trạng thái kiểm. SHA-256 PDF: `aa9e9d9a18fbbf05cc23c35b71a5dbae7a0a858a81727ff2e0d1c8ad047cb451`.

## 2. Ba chỉ tiêu đối chiếu

| Chỉ tiêu, VND | Q1/2025 — đã phân loại lại | Q1/2026 | Trang PDF / trang in |
|---|---:|---:|---|
| Tổng LNST hợp nhất | 1.587.273.268.054 | 2.458.221.002.532 | 12 / 11 |
| CFO, dòng 20 | -124.187.023.735 | 269.326.997.516 | 13 / 12 |
| Tiền chi trả cổ tức, dòng 36 | -1.044.977.722.500 | -55.837.540 | 14 / 13 |

- LNST tăng `(2.458.221.002.532 / 1.587.273.268.054 − 1) × 100% ≈ 54,87%`.
- CFO tăng tuyệt đối `269.326.997.516 − (−124.187.023.735) = 393.514.021.251 VND`; kỳ trước âm nên không dùng tăng trưởng phần trăm.
- CFO/LNST: Q1/2026 ≈ **0,109562 lần**; cột Q1/2025 ≈ **−0,078239 lần**.
- Chi cổ tức Q1/2026 có độ lớn **55.837.540 VND ≈ 55,838 triệu**, cột Q1/2025 **1.044.977.722.500 VND ≈ 1.044,978 tỷ**. Không nhầm đơn vị.

## 3. Cầu nối từ LNTT tới CFO, số VND gốc

| Mã trong hồ sơ | Nhãn khoản mục | Q1/2025 — đã phân loại lại | Q1/2026 |
|---|---|---:|---:|
| 01 | Lợi nhuận kế toán trước thuế | 1.951.296.195.523 | 3.014.396.468.576 |
| 02a | Khấu hao và phân bổ | 511.791.212.722 | 537.336.950.720 |
| 02b | Phân bổ lợi thế thương mại | 60.819.781.207 | 60.819.781.207 |
| 03 | Các khoản dự phòng | 2.485.756.955 | -16.770.329.348 |
| 04 | Lỗ chênh lệch tỷ giá đánh giá lại | 4.698.502.109 | 12.172.815.226 |
| 05a | Thu nhập cổ tức, lãi tiền gửi và lãi/lỗ đầu tư khác | -326.600.970.096 | -340.884.346.057 |
| 05b | Lãi từ công ty liên kết, liên doanh | -16.189.054.400 | -48.459.806.269 |
| 06 | Chi phí đi vay | 75.155.207.673 | 118.301.437.284 |
| 09 | Biến động các khoản phải thu | 916.055.229.563 | -127.949.065.402 |
| 10 | Biến động tồn kho và tài sản sinh học | -1.409.385.906.048 | -1.036.622.597.598 |
| 11 | Biến động phải trả và nợ phải trả khác | -429.866.370.661 | 327.879.637.282 |
| 12 | Biến động chi phí chờ phân bổ | -61.949.344.633 | -126.150.419.127 |
| 14 | Chi phí đi vay đã trả | -58.880.104.706 | -80.973.790.732 |
| 15 | Thuế thu nhập doanh nghiệp đã nộp | -931.863.109.189 | -1.579.997.498.166 |
| 17 | Tiền chi khác cho hoạt động kinh doanh | -411.754.049.754 | -443.772.240.080 |

Hậu tố `a/b` phân biệt hai nhãn cùng mã 02 hoặc 05 trên nguồn; không phải mã chính thức mới. Không loại dòng chỉ vì trùng mã. Dòng 08 là tổng trung gian, không cộng thêm vào cầu nối. Dòng 12 cột 2025 được đọc lại từ ảnh gốc là −61.949.344.633 VND; OCR gốc đọc sai thành −61.940.344.633, nên nếu dùng trực tiếp sẽ lệch tổng +9 triệu đồng. Giữ OCR gốc, dùng số đã đối chiếu trong cầu nối.

| Kiểm tra, VND | Q1/2025 | Q1/2026 |
|---|---:|---:|
| LNTT + điều chỉnh, khớp dòng 08 | 2.263.456.631.693 | 3.336.912.971.339 |
| Tổng các dòng thành phần, khớp dòng 20 | −124.187.023.735 | 269.326.997.516 |
| Residual = tổng − CFO báo cáo | **0** | **0** |

Đóng góp vào ΔCFO (tỷ đồng, làm tròn): LNTT **+1.063,100**; điều chỉnh **+10,356**; vốn lưu động **+22,304**; đi vay đã trả/thuế/chi khác **−702,246**; tổng **+393,514**. Tổng bảng làm tròn có thể lệch 0,001 tỷ; phép cộng kiểm dùng VND gốc.

Chi thuế đóng góp **−648,134 tỷ** vào ΔCFO. Phải thu **−1.044,004 tỷ**, tồn kho/tài sản sinh học **+372,763 tỷ**, phải trả/nợ khác **+757,746 tỷ**, chi phí chờ phân bổ **−64,201 tỷ** tạo phần vốn lưu động ròng **+22,304 tỷ**. Đây là đóng góp số học, chưa chứng minh chính sách bán hàng, lịch mua hay nguyên nhân nộp thuế. Không đồng nhất thuế nộp với chi phí thuế.

## 4. Diễn giải và liên hệ cổ tức

LNST và CFO cùng cải thiện, nhưng CFO Q1/2026 nhỏ so với LNST. Cầu nối chỉ ra phần tăng lợi nhuận trước thuế được bù trừ đáng kể bởi chi tiền, trong đó có thuế đã nộp; người đọc cần tiếp tục xem thuyết minh và nhiều kỳ trước khi kết luận chất lượng lợi nhuận.

Chi cổ tức trong quý giảm mạnh về độ lớn không đủ kết luận doanh nghiệp hạ mức cổ tức theo năm lợi nhuận. Chưa xác định khoản nhỏ Q1/2026 thuộc đợt/năm lợi nhuận nào. [Thông báo VSDC năm 2025](https://vsdc.vn/vi/ad1/187729) là ví dụ tách 350 đồng lợi nhuận 2024 và 2.500 đồng lợi nhuận 2025 trong mức 2.850 đồng/cổ phiếu, lịch trả 24/10/2025; không dùng lịch đó làm bằng chứng thực chi Q1/2026.

Không tính tỷ lệ CFO/chi cổ tức quý với mẫu số rất nhỏ để suy tính bền vững. Cần lịch sử thông báo, đối chiếu thực trả, phân biệt phạm vi hợp nhất và nghĩa vụ cổ tức công ty mẹ. Mẫu quý này chỉ minh họa báo cáo 1; pilot năm 2023–2025 và đánh giá độc lập vẫn là công việc tiếp theo.

## 5. Hồ sơ đối chiếu cổ tức bổ sung

Để kiểm ý nghĩa của việc liên kết dữ liệu, rà có mục tiêu thêm ba thông báo VSDC và thuyết minh cổ tức của chính báo cáo Vinamilk. Đây là hồ sơ ghép thủ công một số sự kiện, **chưa phải lịch sử đầy đủ hoặc đối soát giao dịch**.

| Nguồn thông báo | Thành phần theo năm lợi nhuận | Lịch thanh toán | Đối chiếu với BCTC quý |
|---|---|---|---|
| [VSDC, 10/12/2024](https://vsdc.vn/vi/ad/177392) | Tạm ứng đợt 2 năm **2024**, 500 đồng/cổ phiếu | **28/02/2025**, trong Q1/2025 | Là ứng viên giải thích dòng chi 1.044,978 tỷ ở cột Q1/2025; thông báo xác nhận năm/lịch, chưa chứng minh toàn bộ dòng hợp nhất chỉ thuộc đợt này |
| [VSDC, 02/10/2025](https://vsdc.vn/vi/ad1/187729) | 350 đồng cho **2024** và 2.500 đồng cho **2025** | **24/10/2025**, ngoài Q1/2026 | Phải tách hai thành phần; không gán cả 2.850 đồng cho năm 2025 hoặc ghép thành chi Q1/2026 |
| [VSDC, 17/06/2026](https://vsdc.vn/vi/ad/197038) | Phần còn lại năm **2025**, 1.850 đồng/cổ phiếu | **17/07/2026**, ngoài Q1/2026 | Sự kiện bổ sung khi nghiên cứu ngày 06/10/2026, không phải thông tin đã biết cuối Q1 hoặc bằng chứng đã chi trong Q1 |

[Thuyết minh V.23, PDF 60/trang in 59](https://d8um25gjecm9v.cloudfront.net/cms/20260429_VNM_BCTC_DA_SOAT_XET_Q1_2026_HOP_NHAT_VN_d44326741a.pdf#page=60) ghi ĐHĐCĐ ngày **22/04/2026** phê duyệt mức cổ tức năm 2025 là **4.350 đồng/cổ phiếu**. Hai thành phần năm 2025 được chọn ở trên cộng `2.500 + 1.850 = 4.350`, **khớp mức phê duyệt**; phần 350 đồng thuộc năm 2024 được loại khỏi tổng năm 2025. Nếu gán toàn bộ thông báo tháng 10/2025 cho năm 2025 rồi cộng 1.850 đồng, tổng sai thành **4.700 đồng**, cao hơn 350 đồng/cổ phiếu. Đây là một phép kiểm thực cho quy tắc chuẩn hóa năm lợi nhuận; khớp tổng không thay thế việc rà mọi bản sửa hoặc xác nhận thực trả.

Có hai đầu ra tách biệt: **chính sách theo năm lợi nhuận** có mức 2025 được phê duyệt 4.350 đồng/cổ phiếu; **dòng tiền thực chi theo kỳ** ghi 55,838 triệu đồng ở Q1/2026. Vì vậy, khoản chi quý nhỏ không đủ kết luận doanh nghiệp cắt cổ tức năm 2025. Tuy nhiên, chưa xác định khoản 55.837.540 VND thuộc đợt nào hoặc chủ thể nào trong phạm vi hợp nhất; hệ thống phải để **chưa ghép được**, không tự gán.

Mốc phê duyệt 22/04/2026 nằm **sau cuối quý** và đã được trình bày trong báo cáo phát hành 29/04/2026; thông báo tháng 6 còn muộn hơn. Ví dụ này dùng góc nhìn nghiên cứu hồi cứu ngày 06/10/2026. Nếu phân tích thông tin có sẵn tại 31/03/2026, phải loại các nguồn công bố sau ngày đó. Lịch trả là bằng chứng kế hoạch thực hiện quyền, BCLCTT là bằng chứng chi gộp; chưa có chứng từ để xác nhận từng giao dịch.

**Vấn đề đề tài giải quyết:** dữ liệu tài chính đơn lẻ không chứa đủ năm lợi nhuận/lịch đợt; thông báo đơn lẻ không mô tả đủ dòng tiền kinh doanh hay thực chi gộp. Thu thập cả hai, tách thành phần, lưu ngày công bố và kiểm tổng giúp người đọc tránh diễn giải sai chính sách, đồng thời biết trường hợp nào còn thiếu bằng chứng. Việc ghép theo năm không làm cho cổ tức và CFO trở thành quan hệ nhân quả, cũng không đủ để dự báo cổ tức.


Bằng chứng và trạng thái ghép được lưu tại [JSON ca VNM](../../../research-profit-cash-dividend/evidence/case-vnm-q1-2026.json), mục `dividend_context`. Các trang thuyết minh bổ sung được đọc thủ công; không gộp vào kết quả thử OCR sáu ô trước đó.
