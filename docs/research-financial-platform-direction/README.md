# Hướng nền tảng dữ liệu tài chính — kết luận được kế thừa

Nghiên cứu ngày 11/10/2026. **Cập nhật theo yêu cầu mới nhất:** bỏ A04 “Tìm và khám phá trường hợp cần chú ý”. Cấu trúc hiện hành nằm trong [danh mục UC lớn→nhỏ v2.0](../research-platform/27-yeu-cau-chuc-nang-va-vi-du.md); [nghiên cứu36 repo ưu tiên sao cao](../research-high-star-finance/README.md) bổ sung ý tưởng và nguồn. [SRS v3.3/mục18](../research-platform/22-srs-dac-ta-yeu-cau-phan-mem.md) rút các nghĩa vụ sàng lọc.

## 1. Hướng nền tảng dữ liệu có bị lệch không?

Có nguy cơ lệch trong cách tổ chức chức năng nếu trải nghiệm chính chỉ là tải PDF, duyệt số và nhận vài tỷ số. Thu thập/chuẩn hóa/kiểm tra là nền hỗ trợ. Trải nghiệm của người theo dõi tài chính/đầu tư cần là khai thác dữ liệu → phân tích → so sánh → theo dõi tiếp, với cổ tức là ứng dụng cụ thể trên nền ấy.

| Nhóm chức năng lớn | Các năng lực nhỏ kế thừa từ đợt này |
|---|---|
| Khai thác dữ liệu doanh nghiệp | A01 chọn dữ liệu/kỳ/chỉ tiêu, xem thiếu và nguồn, xuất dữ liệu |
| Phân tích dữ liệu tài chính | A02 bảng/biểu đồ xu hướng; A05 cầu nối/phân rã; A08 lưu góc nhìn và nhận xét |
| So sánh tài chính doanh nghiệp | A03 bảng/biểu đồ đối chiếu doanh nghiệp do người dùng chọn |
| Theo dõi doanh nghiệp/sự kiện | A07 danh sách tự chọn, dữ liệu trước/sau cập nhật |
| Phân tích cổ tức | A06 lịch sử DPS, đợt quyền, cơ sở cổ phiếu; G02/G03 và hồ sơ D11/D12 |

Các mã A là năng lực phân rã, không phải UC lớn riêng. A04 không còn trong danh mục. Các ý tưởng mới về DuPont, kế hoạch, danh mục và định giá được ghi tại bộ nghiên cứu mới, có điều kiện dữ liệu/phạm vi.

## 2. Biểu đồ và phân tích

Có yêu cầu xu hướng LNST/CFO, tỷ số tiền/nợ phải trả/tài sản, lịch cổ tức và nguồn; chưa có giao diện hoàn chỉnh đã chạy. FR29/FR30 về bộ lọc trường hợp/scatter/Spearman đã rút. Điều cần thực hiện tiếp là bảng/biểu đồ cùng bộ chọn, so sánh cùng cơ sở, chọn số để xem nguồn và lưu lần phân tích.

[CFA Institute — Financial Analysis Techniques](https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/financial-analysis-techniques) mô tả so sánh theo thời gian/giữa doanh nghiệp và diễn giải. Sáu trường lõi đủ một số tác vụ, chưa đủ phân tích toàn diện: biên cần doanh thu, thanh khoản cần ngắn hạn, cầu nối cần dòng điều chỉnh.

## 3. Bằng chứng đợt này và tài liệu kế thừa

Đợt này ban đầu bổ sung5 repo và đọc lại FinanceToolkit, lưu32 tệp tại6inventory; chỉ đọc nguồn, chưa chạy dự án. Danh mục17 repo của các đợt trước là mốc lịch sử; không cộng máy móc với36 repo mới khảo sát vì có repo được đọc lại/tên đổi.

- [Bằng chứng mã và bài học](01-bang-chung-va-bai-hoc.md), [sổ nguồn](sources.md).
- [Các năng lực phân tích còn giữ và điều kiện dữ liệu](02-chuc-nang-phan-tich-va-kha-thi.md).
- [Nghiên cứu mở rộng mới](../research-high-star-finance/README.md), [khả thi/thứ tự](../research-high-star-finance/03-kha-thi-va-thu-tu-thuc-hien.md).
- [Yêu cầu chức năng v2.0](../research-platform/27-yeu-cau-chuc-nang-va-vi-du.md).
- [Snapshot văn bản trước khi loại A04](../research-platform/history/before-user-removal-2026-10-11.zip).

Ưu tiên hiện hành: chọn A/B → xem bảng/biểu đồ → so tỷ số → kiểm nguồn → lưu/xuất, rồi phân tích sâu/cổ tức và theo dõi công bố. Ngân sách/checklist cũ là baseline; chưa cam kết toàn danh mục trong 13 tuần. Kết luận lựa chọn chức năng là suy luận thiết kế, chưa chứng minh cải thiện lợi nhuận đầu tư.
