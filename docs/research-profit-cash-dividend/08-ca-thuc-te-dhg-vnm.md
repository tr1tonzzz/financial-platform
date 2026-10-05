# 08 — Ca thực tế: kiểm chứng khả năng kết hợp

**Trạng thái cập nhật05/10/2026:** hướng kết hợp đã được tích hợp vào [SRS v3.1](../research-platform/22-srs-dac-ta-yeu-cau-phan-mem.md), CR-PCD-01/mục15, theo yêu cầu cập nhật tài liệu của người thực hiện. Tối thiểu một ca cầu nối là nghĩa vụ dự thảo; E05/E10 và ca thêm có điều kiện. Nội dung đề xuất ngày04/10 bên dưới là cơ sở nghiên cứu; các câu “chưa tích hợp/chờ change record” mô tả trạng thái lúc đó, được thay bởi SRS v3.1. Chưa có phê duyệt giảng viên hoặc kiểm thử ứng dụng đã chạy. Kế hoạch/checklist v3 là lịch triển khai duy nhất; bảng tuần/giờ trong hồ sơ nghiên cứu là phương án trước tích hợp.

## 1. Nguồn và cách kiểm tra

DHG: [BCTC kiểm toán 2025](https://dhgpharma.com.vn/sites/default/files/2026-03/DHG-Audited-FS-2025-VN.pdf), trang PDF10–11, trang in8–9. Đã mở lại ảnh hai trang trong kho khảo sát và chép các dòng cần thiết; hash PDF được kiểm tra bằng [script](../../scripts/research/verify_profit_cash_dividend.py). Đây là kiểm tra thủ công bởi cùng người nghiên cứu, không đánh giá OCR độc lập. Cột2024 là số so sánh trình bày trong báo cáo2025, không được coi là thông tin đã biết tại cuối2024.

Số bên dưới làm tròn tỷ đồng để đọc; [JSON bằng VND](evidence/case-dhg-2025.json) giữ số chính xác. Phạm vi giữ đúng BCTC Công ty Cổ phần Dược Hậu Giang trên hai trang nguồn; không tự gán nhãn hợp nhất.

## 2. Lợi nhuận và CFO cho hai tín hiệu khác nhau

| Chỉ tiêu | 2024 so sánh | 2025 | Biến động |
|---|---:|---:|---:|
| LNST, tỷ đồng | 778,920 | 852,354 | +9,43% |
| CFO, tỷ đồng | 1.317,583 | 1.212,968 | −7,94% |
| CFO/LNST, lần | 1,692 | 1,423 | Giảm |

Nếu chỉ nhìn LNST sẽ bỏ qua biến động tạo tiền. Nếu chỉ nhìn CFO/LNST vẫn chưa biết khoản nào đóng góp. Đây là tác vụ mà extension giải quyết, chưa phải kết luận chất lượng lợi nhuận xấu.

## 3. Cầu nối và phân rã biến động

| Nhóm theo các dòng nguồn | 2024, tỷ đồng | 2025, tỷ đồng | Đóng góp vào ΔCFO |
|---|---:|---:|---:|
| LNTT | 904,485 | 986,599 | +82,115 |
| Điều chỉnh dòng 02–06 | 60,779 | 64,554 | +3,775 |
| Vốn lưu động dòng 09–12 | 517,633 | 344,523 | −173,110 |
| Dòng tiền khác trong HĐKD14,15,17 | −165,313 | −182,708 | −17,395 |
| CFO | 1.317,583 | 1.212,968 | −104,616 |

Phép cộng bằng VND khớp CFO cả hai cột, residual0. Trong nhóm vốn lưu động, thay đổi đóng góp của dòng tồn kho khoảng−334,305 tỷ, phải thu−160,044 tỷ và phải trả+311,437 tỷ. Vì vậy, chỉ nói “CFO giảm vì lợi nhuận giảm” là không phù hợp với ca này. Các con số cho biết phân rã theo báo cáo; nguyên nhân vận hành phía sau cần đọc thuyết minh/giải trình.

Trong quá trình chép tay, một giá trị cột so sánh ở dòng phải trả bị nhập sai một chữ số; kiểm tra tổng phát hiện không khớp. Đối chiếu lại ảnh/OCR đã sửa đúng thành−21.510.218.626 VND. Ca này minh họa ích lợi của kiểm tra số học, đồng thời cho thấy nhập tay cũng cần kiểm soát. Dữ liệu giao cuối là bản đã sửa; script vẫn kiểm tra từng tổng.

## 4. Đối chiếu với tiền chi cho chủ sở hữu

Dòng 36 của BCLCTT2025 ghi cổ tức/lợi nhuận đã trả cho chủ sở hữu khoảng1.307,461 tỷ đồng. CFO chia độ lớn dòng này khoảng0,928 lần. Nhãn đúng là **bao phủ dòng chi cho chủ sở hữu trong kỳ theo BCLCTT**. Không gán dòng 36 thành cổ tức từ lợi nhuận2025 và không dùng tỷ số để kết luận mất khả năng chi trả.

Đây cũng không chứng minh nguồn riêng tài trợ cổ tức. BCLCTT còn dòng đầu tư/tài chính; muốn diễn giải cụ thể phải có nguồn bổ sung. Extension có thể trình bày góc thực chi riêng, còn annual DPS theo profit_year phải lấy từ bộ sự kiện đã rà đầy đủ.

## 5. VNM: một thông báo có hai năm lợi nhuận

[Thông báo ngày 02/10/2025](https://vsdc.vn/vi/ad1/187729) có tổng2.850 đồng/cp:350 thuộc phần còn lại2024 và2.500 thuộc tạm ứng đợt1/2025; lịch thanh toán24/10/2025. [Thông báo17/06/2026](https://vsdc.vn/vi/ad1/197038) nêu phần còn lại2025 là1.850 đồng/cp, lịch17/07/2026.

Thiết kế phải tạo component riêng theo năm. Từ hai văn bản này có thể ghi nhận các component đã quan sát; chưa đủ để khẳng định đã rà tất cả đợt, basis và sửa/hủy của cả năm. Lịch công bố không là chứng từ thực trả. Không lấy năm 2026 của thông báo thứ hai để ghép số cổ tức đó với CFO2026.

## 6. Điều ca thực chứng minh và chưa chứng minh

Đã chứng minh có thể lấy một báo cáo thật để tạo cầu nối kiểm tra được; câu hỏi lợi nhuận tăng/CFO giảm có dữ liệu hỗ trợ; sự kiện cổ tức cần mô hình nhiều năm. Chưa chứng minh trích bridge tự động, coverage nhiều doanh nghiệp, tác dụng tiết kiệm thời gian với người dùng hoặc quan hệ thống kê giữa CFO và cổ tức.

DHG và VNM ở đây minh họa hai vấn đề bổ sung. Không ghép CFO của DHG với cổ tức VNM để tạo một quan sát nghiên cứu. Để hoàn thành một case end-to-end cho một issuer, cần tiếp tục rà toàn bộ lịch sử sự kiện và context đúng của chính issuer đó.
