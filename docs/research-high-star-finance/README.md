# Nghiên cứu GitHub: chức năng phục vụ người theo dõi tài chính và đầu tư

Ngày **11/10/2026**. Khảo sát **36 repository hợp lệ**, trong đó **25 repo ≥3.000 sao**, **12 repo ≥10.000 sao**. Đọc README của 35 repo và các tệp triển khai chọn lọc của **17 repo**; stocknear/frontend không có README ở commit đã lưu, được khảo sát qua mã giao diện. Đã lưu **87 tệp**, commit cố định và SHA-256. Đây là nghiên cứu tài liệu/mã, chưa cài hoặc chạy các nền tảng nguồn.

**Kết luận:** giữ nền tảng dữ liệu tài chính doanh nghiệp làm hướng chính. Đưa việc khai thác, phân tích, so sánh và tiếp tục theo dõi doanh nghiệp thành chức năng cho người dùng. Thu thập/chuẩn hóa/duyệt là nền hỗ trợ. Theo yêu cầu người thực hiện, **loại A04 và các chức năng sàng lọc liên quan**; danh sách theo dõi do người dùng tự chọn vẫn có ích.

## 1. Cấu trúc chức năng đề xuất

**Nghiên cứu tiếp sau bản vẽ:** [kiểm sâu 12 repo chọn lọc/32 tệp mã](../research-investor-support/README.md) và [đánh giá chiều sâu hỗ trợ người đầu tư](../research-platform/37-danh-gia-muc-do-ho-tro-nha-dau-tu.md). Đây là phần kế thừa khảo sát này, không cộng thành 48 repo; các gói bổ sung chưa thành phạm vi bắt buộc.

| Nhóm UC lớn | Phân rã chức năng nhỏ | Giải quyết việc gì? |
|---|---|---|
| **Khai thác dữ liệu tài chính doanh nghiệp** | Tra cứu doanh nghiệp; bảng nhiều kỳ; chọn/xuất chỉ tiêu; định nghĩa/nguồn; độ đầy đủ/phiên bản; thu–chuẩn hóa–duyệt ở phía vận hành | Có dữ liệu sử dụng được mà không tự nhập lại PDF |
| **Phân tích dữ liệu tài chính** | Biểu đồ xu hướng; tăng trưởng/biên lợi nhuận; cơ cấu tài sản/nguồn vốn; lợi nhuận–CFO; cầu nối; DuPont; cùng kỳ/kế hoạch; lưu nhận xét | Hiểu tình hình và các khoản giải thích biến động |
| **So sánh tài chính doanh nghiệp** | Bảng/biểu đồ nhiều doanh nghiệp tự chọn; so tỷ số/cơ cấu/xu hướng; benchmark ngành khi đủ mẫu | Đối chiếu doanh nghiệp mình quan tâm trên cùng cơ sở |
| **Theo dõi doanh nghiệp và sự kiện** | Danh sách tự chọn; công bố mới; lịch có nguồn; trước/sau dữ liệu sửa; mở lại lần phân tích | Theo dõi liên tục sau lần phân tích đầu |
| **Phân tích cổ tức** | Lịch sử/biểu đồ; chính sách–quyền–lịch trả; tiền sau CAPEX/phân phối; basis cổ phiếu; payout đúng chủ thể; nhận xét có bằng chứng | Đọc đúng cổ tức và đặt trong bối cảnh tài chính |
| **Theo dõi danh mục đầu tư — mở rộng** | Giao dịch/vị thế; giá vốn/lãi lỗ; phân bổ; hiệu quả/benchmark; thu nhập cổ tức dự kiến và thực nhận | Theo dõi kết quả của chính khoản đầu tư |
| **Mô phỏng kịch bản và định giá — mở rộng** | Kịch bản dòng tiền; lưu giả định; DCF/DDM; bảng độ nhạy | Hiểu kết quả phụ thuộc giả định nào |

[Tài liệu yêu cầu chức năng riêng](../research-platform/27-yeu-cau-chuc-nang-va-vi-du.md) phân rã 38 chức năng nhỏ, giải thích mục đích, ví dụ và phần cần thêm dữ liệu. Biểu đồ thuộc UC tương ứng, không tạo UC lớn riêng.

## 2. Những ý tưởng bổ sung đáng nghiên cứu nhất

1. **Biên lợi nhuận và cơ cấu BCTC:** biết lợi nhuận đổi vì doanh thu/biên, biết tài sản và nguồn vốn chuyển dịch thế nào. Chọn thêm doanh thu và một nhóm dòng có mục đích; chưa cần toàn bộ tỷ số của toolkit.
2. **DuPont:** hiểu ROE tăng nhờ biên lợi nhuận, vòng quay tài sản hay hệ số vốn. Cần số dư bình quân và phạm vi lợi nhuận/vốn phù hợp. [FinanceToolkit — triển khai DuPont](https://github.com/JerBouma/FinanceToolkit/blob/37ed6f01465b4bfb6718b07e1d65826734f53337/financetoolkit/models/dupont_model.py#L10).
3. **Công bố mới và lịch doanh nghiệp:** theo dõi BCTC, nghị quyết, quyền cổ tức của công ty mình chọn. Nguồn công bố ở Việt Nam phải được nối riêng. [AKShare — truy vấn công bố](https://github.com/akfamily/akshare/blob/fac1e50ebf9b907960d6aab4c3df658559689f39/akshare/stock_feature/stock_disclosure_cninfo.py#L129).
4. **Cùng kỳ và kế hoạch–thực hiện:** theo dõi tiến độ mục tiêu doanh nghiệp công bố. stocknear có giao diện earnings guidance; việc chuyển sang kế hoạch Việt Nam là đề xuất của nghiên cứu này, cần dữ liệu kế hoạch riêng. [stocknear — giao diện guidance](https://github.com/stocknear/frontend/blob/a97f990ea2567303de88279ed020c4f16f4ddbbd/src/lib/components/EarningsGuidance.svelte#L129).
5. **Thu nhập cổ tức thực nhận của danh mục:** biết tháng nào nhận tiền và cổ phiếu nào đóng góp; khác với biểu đồ DPS của doanh nghiệp. Cần vị thế/đủ quyền/tiền thực nhận. [Ghostfolio — tổng hợp cổ tức theo kỳ](https://github.com/ghostfolio/ghostfolio/blob/8fa4f6a6739afee82461b3aa48f47dfa6a396dc8/apps/api/src/app/portfolio/portfolio.service.ts#L458), [Wealthfolio — tổng hợp thu nhập](https://github.com/wealthfolio/wealthfolio/blob/ace5c5243d890f22cf68118ed74986cac8f4cb17/crates/core/src/portfolio/income/income_service.rs#L76).
6. **Kịch bản dòng tiền rồi độ nhạy định giá:** thử CFO/CAPEX/phân phối trước vì dùng lại G02; DCF/DDM để sau khi đủ dữ liệu. Không sao chép ngưỡng mặc định nước ngoài. [Fincept — sensitivity và scenario](https://github.com/Fincept-Corporation/FinceptTerminal/blob/3f444cb7ab712d85a57d270d5edd6e7a2ef50d55/fincept-qt/scripts/Analytics/corporateFinance/valuation/dcf_model.py#L409).

## 3. Chọn hướng thực hiện

**Ưu tiên đầu:** chọn A/B → xem bảng và biểu đồ lợi nhuận/CFO → so tỷ số cùng cơ sở → chọn số để kiểm nguồn → lưu/xuất. Kế tiếp thêm biên lợi nhuận/cơ cấu theo câu hỏi, cầu nối/G02/G03 và theo dõi công bố. Danh mục và định giá là hướng mở rộng có điều kiện, không tự thêm toàn bộ vào MVP.

Người dùng chọn doanh nghiệp để so sánh hoặc theo dõi. Không bổ sung bộ tìm mã đạt ngưỡng, nhóm pass/fail/unknown, điểm an toàn cổ tức hay xếp hạng tự động. Các thư viện ML/backtest/giao dịch nhiều sao được khảo sát để xác định ranh giới, không làm mục tiêu phát triển cho đề tài này.

Việc chọn chức năng là suy luận thiết kế từ các dự án nguồn và nhu cầu người thực hiện; chưa có phỏng vấn độc lập hoặc thực nghiệm chứng minh cải thiện lợi nhuận đầu tư. Mức sao chỉ giúp ưu tiên tìm hiểu. Repo dữ liệu Mỹ/Trung Quốc/Hàn Quốc không tự cung cấp dữ liệu Việt Nam; ý tưởng giao diện/công thức có thể chuyển thể, adapter/định nghĩa/chất lượng nguồn cần kiểm riêng.

## 4. Bộ tài liệu và quyết định liên quan

- [Khảo sát 36 repository: sao, loại, bài học và mức bằng chứng](01-khao-sat-repository.md).
- [Minh chứng mã tại commit cố định và chuyển thể cho Việt Nam](02-minh-chung-ma-va-bai-hoc.md).
- [Tính khả thi, dữ liệu, thứ tự và tiêu chí hoàn thành](03-kha-thi-va-thu-tu-thuc-hien.md).
- [Danh mục UC lớn → nhỏ, mục đích và ví dụ](../research-platform/27-yeu-cau-chuc-nang-va-vi-du.md).
- [SRS v3.3 — CR-AN-03 tại mục 18](../research-platform/22-srs-dac-ta-yeu-cau-phan-mem.md): rút FR29/FR30/D09/D10; còn 91 yêu cầu hoạt động và 51 tình huống dự kiến. Các mở rộng mới vẫn là ứng viên.
- [Danh sách metadata và tệp bằng chứng](evidence/repository-survey.json); [phương thức thu nguồn](../../scripts/research/fetch_high_star_finance_research.py).
