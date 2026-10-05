# Kế hoạch kiểm thử và đánh giá dữ liệu BCTC–cổ tức Việt Nam

> **Trạng thái 03/10/2026 — hồ sơ khảo sát trước.** Project hiện hành tập trung thu thập, kiểm định và phân tích lợi nhuận–dòng tiền–cổ tức tiền mặt. Xem [SRS hiện hành](../research-platform/02-de-tai-va-srs.md) và [phương pháp thống nhất](../research-platform/11-phuong-phap-thu-thap-va-xu-ly.md). Các ngưỡng cảnh báo, dự báo, scope và lịch cũ bên dưới chỉ để tham khảo; không là yêu cầu MVP hiện hành.

Phiên bản 2.0 — 03/10/2026. Mục tiêu là chứng minh dữ liệu đúng, có nguồn, không dùng thông tin tương lai và kết quả phân tích tái lập được.

## 1. Hai lớp bằng chứng

Kiểm thử logic dùng fixture nhỏ cho các trường hợp lỗi có chủ đích. Đánh giá thực nghiệm dùng tài liệu thật và bảng đối chiếu được đọc thủ công. Hai lớp được báo cáo riêng; fixture không chứng minh crawler đang hoạt động trên nguồn thực.

## 2. Bộ đối chiếu

Tối thiểu 20 BCTC từ ít nhất 10 công ty, rải qua năm và kiểu bảng, gồm đơn vị khác nhau, số âm và cột so sánh. Ghi trước giá trị, metric, kỳ, đơn vị, phạm vi và trang bằng chứng.

Tách mẫu dùng phát triển mapping khỏi mẫu đánh giá cuối. Người thực hiện có thể tự đọc lại nhưng phải ghi rằng chưa có người chấm độc lập; kiểm tra lại ngẫu nhiên sau một khoảng thời gian. Thêm ít nhất 20 thông báo cổ tức gồm tạm ứng, đổi lịch, cổ phiếu và thông báo dự kiến.

## 3. Ma trận kiểm thử

| Mã | Liên kết yêu cầu | Tình huống | Kết quả mong đợi |
|---|---|---|---|
| VN-TC-01 | FR-01, 02 | Crawl một công ty có tài liệu | Metadata và URL tài liệu thật được lưu |
| VN-TC-02 | FR-02, 03 | Timeout, lỗi HTTP, tải lại | Retry hữu hạn, log lỗi, không lưu file hỏng |
| VN-TC-03 | FR-03 | Chạy hai lần cùng dữ liệu | Không nhân bản facts và sự kiện |
| VN-TC-04 | FR-03, 08 | Bản đính chính cùng kỳ | Giữ bản cũ; snapshot quá khứ không lấy bản công bố sau cutoff |
| VN-TC-05 | FR-04, 05 | Đơn vị VND/nghìn/triệu, ngoặc âm | Số chuẩn đúng dấu và hệ số |
| VN-TC-06 | FR-04, 05 | Năm hiện tại và cột so sánh | Lấy đúng giá trị và period_end |
| VN-TC-07 | FR-05 | Báo cáo riêng/hợp nhất | Không ghép lẫn phạm vi |
| VN-TC-08 | FR-06 | Tài sản không cân đối hoặc đơn vị thiếu | Gắn lỗi; không xuất bản như fact đã duyệt |
| VN-TC-09 | FR-06 | Sửa tay | Có bằng chứng, giá trị cũ/mới, lý do |
| VN-TC-10 | FR-07 | Tỷ lệ cổ tức và mệnh giá nguồn | DPS đúng; thiếu mệnh giá trả unknown |
| VN-TC-11 | FR-07 | Đề xuất, lịch dự kiến và đổi lịch | Không tự coi là đã trả; đổi lịch không cộng hai lần |
| VN-TC-12 | FR-08 | Chưa đủ 12 tháng kết quả | Label censored, không đưa vào train/test |
| VN-TC-13 | FR-08 | Thiếu sự kiện và độ phủ chưa xác minh | Label unknown, không gán bằng 0 |
| VN-TC-14 | FR-08 | Ngày công bố thiếu hoặc không chính xác | Loại khỏi mẫu dự báo theo thời điểm |
| VN-TC-15 | FR-09, 10 | LNST/vốn bằng 0 hoặc âm | Không chia sai; trạng thái đặc biệt có giải thích |
| VN-TC-16 | FR-10 | Thiếu đầu vào | Không đủ dữ liệu, không rủi ro thấp mặc định |
| VN-TC-17 | FR-11 | API truy nguồn một chỉ tiêu | Tìm lại đúng PDF/HTML và vị trí |
| VN-TC-18 | FR-12 | Chạy lại từ raw và cấu hình cố định | Dataset và kết quả trùng trong dung sai được khai báo |
| VN-TC-19 | FR-09 | 3 case study | Số liệu, ngày và kết luận kiểm tra được từ nguồn |
| VN-TC-20 | FR-13 | Chia dữ liệu dự báo | Train chỉ chứa mẫu có outcome_end trước mốc validation/test |

FR trong bảng là mã VN-FR tương ứng tại SRS.

## 4. Đo chất lượng

- Độ chính xác kết hợp: số ô trích đúng cả giá trị, đơn vị, kỳ và phạm vi / tổng ô đối chiếu.
- Precision trích xuất: số ứng viên đúng / tổng ứng viên trích; recall: số facts mục tiêu tìm đúng / tổng facts có trong mẫu.
- Độ phủ: ô facts đủ điều kiện / ô dự kiến của tập công ty–năm đã chốt. Báo cáo riêng tỷ lệ tải và tỷ lệ có báo cáo nguồn.
- Tỷ lệ provenance đầy đủ; lỗi theo loại; phút review mỗi báo cáo.
- Công bố trước và sau sửa thủ công; không chỉ báo cáo dữ liệu sạch sau review.
- Ngưỡng mục tiêu: độ chính xác kết hợp ≥95%, độ phủ lõi ≥80%, truy vết 100%. Đây là mục tiêu chưa được đo.

## 5. Đánh giá phân tích và dự báo

Theo [đề cương nghiên cứu](../research-design.md): phân bố và tương quan, so sánh nhóm, baseline và rule score. Quan sát lặp theo công ty phải được tính đến khi đánh giá độ bất định; không coi mọi firm-year độc lập.

Nếu triển khai ML, báo cáo precision/recall/F1, PR-AUC khi đủ hai lớp, confusion matrix; xác suất thêm Brier/calibration. Báo cáo cả số mẫu, số ca giảm cổ tức và khoảng bất định. Tập một lớp hoặc quá ít ca thì ghi không thể đánh giá chỉ số tương ứng.

## 6. Hồ sơ kết quả

Mỗi lần đánh giá lưu: mã test, snapshot, phiên bản parser/quy tắc, đầu vào, kết quả mong đợi/thực tế, pass/fail, log và lỗi còn mở. Bản này là kế hoạch, chưa có test nào được tuyên bố pass.

Trước demo chạy toàn bộ test bắt buộc, kiểm tra 3 case study từ tài liệu gốc và chạy lại snapshot dự phòng. Chỉ nghiệm thu sau khi giới hạn dữ liệu và phạm vi thực đạt đã được ghi rõ.
