# Nghiên cứu GitHub: chức năng hỗ trợ thẩm định đầu tư cổ tức

**Tiếp nối:** [nghiên cứu triển khai ba chức năng và GitHub bổ sung](../research-dividend-functions/README.md) đã thêm3 repo (tổng12), thiết kế/khả thi và CR-DIV-02 trong SRS3.2. G01/G02/G03 ở đợt này được ánh xạ sang D01–D12; không đếm ý tưởng làm sâu thành chức năng mới độc lập.

Ngày khảo sát: **11/10/2026**. Thực hiện theo yêu cầu nghiên cứu các dự án tương tự để bổ sung ý tưởng chức năng, dựa trên góp ý giảng viên. Đã khảo sát **9 repository**, lấy phiên bản commit cụ thể, đọc README, các phần mã liên quan, một số test và phản hồi người dùng. **Chưa cài/chạy các ứng dụng, chưa kiểm chứng hiệu quả đầu tư hoặc thu thập đủ dữ liệu mới cho FAP.**

## Kết quả nên dùng ngay

Đề nghị hướng sản phẩm: **hỗ trợ thẩm định cơ sở của cổ tức tiền mặt và lựa chọn doanh nghiệp cần nghiên cứu tiếp bằng bằng chứng tài chính**. GitHub cung cấp các mẫu tác vụ và cách triển khai; không chứng minh chiến lược nào có lợi nhuận tốt hơn.

Ba việc bổ sung đáng ưu tiên:

1. **Phân tích dòng tiền sau chi đầu tư và chi cổ tức thực tế**: trả lời “CFO có đủ bao phủ hai khoản chi này trong kỳ không, và phần chênh lệch cần tra soát ở đâu?”. Đây là chiều phân tích mới rõ nhất so với sáu chỉ tiêu hiện tại; cần thêm dữ liệu và gate thu nguồn.
2. **Kiểm soát tính so sánh của lịch sử cổ tức khi số cổ phiếu thay đổi**: giải thích vì sao DPS giảm chưa chắc khoản tiền của vị thế nắm giữ ban đầu giảm. Giữ tiền mặt là đối tượng phân tích nhưng theo dõi sự kiện cổ phiếu tối thiểu để tránh sai kết luận.
3. **Sàng lọc doanh nghiệp kèm hồ sơ thẩm định và lý do**: đưa kết quả tới tác vụ “đọc doanh nghiệp nào trước, vì sao, còn thiếu gì”, thay vì chỉ hiển thị bảng/biểu đồ. Tái sử dụng phần lớn SRS; đây là đào sâu hành vi hỗ trợ quyết định, không nên khai báo toàn bộ như chức năng mới.

Nguồn trực tiếp cho hướng trên: [mô hình bao phủ tiền của FinanceToolkit](https://github.com/JerBouma/FinanceToolkit/blob/37ed6f01465b4bfb6718b07e1d65826734f53337/financetoolkit/ratios/solvency_model.py#L267), [xử lý cơ sở cổ phiếu của Dividend CLI](https://github.com/Santhosh-004/dividend-cli/blob/7c6033b11db694eb101d2b27217441c7184e9c4f/dividend_calculator/utils.py#L173), [bộ lọc cấu hình của dividend-low-vol-tracker](https://github.com/aspirin188/dividend-low-vol-tracker/blob/7ca601f6bb3f9f3411bfce3f70b80a6708e93ea1/server/services/scorer.py#L179). Các đề nghị cho FAP là **suy luận thiết kế có điều chỉnh**, không sao chép nguyên quy tắc nguồn.

## Hồ sơ đọc theo nhu cầu

- [Khảo sát từng dự án và đánh giá mã](01-khao-sat-du-an-va-bang-chung.md): dự án giải quyết nhu cầu gì, đã thấy gì trong code, điểm học được và điểm không nên kế thừa.
- [Danh mục yêu cầu chức năng ứng viên](02-yeu-cau-chuc-nang-de-xuat.md): 10 ý tưởng với đầu vào, xử lý, đầu ra, ví dụ, tiêu chí và quan hệ SRS.
- [Lựa chọn ưu tiên và kế hoạch kiểm chứng](03-uu-tien-va-thuc-nghiem.md): một luồng demo ưu tiên, dữ liệu cần bổ sung, gate và thí nghiệm.
- [Sổ nguồn](sources.md), [danh sách tệp đã lấy](source-files.json), thư mục `evidence/`: commit, đường dẫn và bản mã đã đọc để kiểm tra lại.
- [Ca số học minh họa](illustrative-cases.json): tính độc lập trên số giả lập; không phải kết quả chạy repository hoặc số doanh nghiệp thật.

## Bản đồ dự án → nhu cầu → ứng dụng cho FAP

| Dự án | Nhóm nhu cầu được quan sát | Ý tưởng chuyển sang FAP | Mức thích hợp |
|---|---|---|---|
| FinanceToolkit | Tính và kiểm tra chỉ tiêu tài chính bằng công thức minh bạch | Bao phủ chi đầu tư + cổ tức, hiện operands/điều kiện áp dụng | Cao; phải bổ sung dòng tiền chi |
| Dividend CLI | Phân tích lịch sử cổ tức, tăng/giảm và tác động chia tách | Chuỗi DPS so sánh được, khoản thu trên vị thế gốc, lọc tiêu chí | Cao; đổi từ cơ sở năm lịch sang năm lợi nhuận khi phù hợp |
| dividend-low-vol-tracker | Sàng lọc cổ phiếu theo nhiều điều kiện | Bộ lọc có lý do và trạng thái đủ/thiếu bằng chứng | Cao cho tác vụ; chưa kế thừa điểm/ngưỡng |
| SALARY-2045 | Theo dõi mục tiêu thu nhập, cổ tức theo tháng và từng khoản nắm giữ | Ước tính khoản thu theo quyền đã công bố, kịch bản thu nhập | Trung bình; cần vị thế, quyền, không tự kéo dài lịch sử thành dự báo |
| Ghostfolio | Quản lý danh mục, thu nhập, quy tắc kiểm tra | Danh sách theo dõi, phân rã nguồn thu và cảnh báo giải thích được | Trung bình; FAP chưa có sổ giao dịch |
| Portfolio Performance | Ghi nhận cổ tức thực nhận, phí/thuế và hiệu suất | Tách công bố, quyền và thực nhận; đối soát khoản thu | Trung bình; mở rộng danh mục là phạm vi riêng |
| OpenBB | Mô hình dữ liệu tài chính và lịch cổ tức nhiều nguồn | Tách ngày công bố/GDKHQ/đăng ký cuối cùng/thanh toán và trạng thái | Cao cho hợp đồng dữ liệu; không là tính năng đầu tư tự thân |
| vnstock | Truy xuất BCTC/thông tin doanh nghiệp Việt Nam | Khảo sát nguồn phụ để đối chiếu và kiểm tính khả thi dữ liệu mới | Cao cho nguồn; không chứng minh hồ sơ phân tích đã có |
| dividend_analysis | Phân tích yield–payout và so sánh theo ngành trong notebook | Mặt bằng so sánh và câu hỏi về cổ tức cao | Tham khảo phương pháp; không dùng cách điền thiếu/xếp hạng làm kết luận |

## Nhu cầu thực tế có dấu vết từ người dùng

Trong [Ghostfolio Discussion #5867](https://github.com/ghostfolio/ghostfolio/discussions/5867), người dùng yêu cầu phân rã thu nhập theo chứng khoán, ngày nhận và năm; các phản hồi còn đề cập thu nhập theo vị thế, lịch trả và yield on cost. Đây là bằng chứng một nhóm người sử dụng muốn **hiểu cơ cấu thu nhập**, không chỉ biết tổng thu.

[Ghostfolio Issue #2126](https://github.com/ghostfolio/ghostfolio/issues/2126) phản ánh nhầm ex-date/payment date và ghép khoản thu của nhiều tài khoản. [Portfolio Performance PR #1879](https://github.com/portfolio-performance/portfolio/pull/1879) sửa việc cộng các tỷ suất riêng thay vì dùng cơ sở vốn tổng; [PR #1897](https://github.com/portfolio-performance/portfolio/pull/1897) thêm phí cho giao dịch cổ tức. Đây là tình huống lịch sử có ích để thiết kế test; không suy phiên bản hiện tại vẫn có cùng lỗi.

Mức chứng cứ: phản hồi công khai chứng minh nhu cầu/điểm vướng của những người đó. Chưa phải khảo sát đại diện nhà đầu tư Việt Nam, chưa chứng minh nhu cầu trả phí, cũng chưa chứng minh lợi ích của FAP.

## Các phát hiện làm thay đổi cách thiết kế

**Không lấy điểm an toàn có sẵn làm kết luận.** SALARY-2045 gọi công thức là heuristic và phân bổ lại trọng số khi thiếu yếu tố. Dividend CLI chấm lịch sử ổn định/tăng trưởng, khác việc kiểm khả năng tạo tiền. Do đó FAP nên hiển thị từng chiều phân tích và mức đầy đủ chứng cứ trước khi nghiên cứu điểm tổng. [Mã SALARY](https://github.com/GavrielP1/SALARY-2045/blob/806cdaa821c7a4eb04a0f1bc7cf59c0a30314e0a/app.py#L258), [mã Dividend CLI](https://github.com/Santhosh-004/dividend-cli/blob/7c6033b11db694eb101d2b27217441c7184e9c4f/dividend_calculator/utils.py#L115).

**Thiếu dữ liệu phải thành trạng thái nghiệp vụ.** Có nhánh lọc trong dividend-low-vol-tracker cho phép qua khi thiếu tăng trưởng lợi nhuận/CFO; notebook dividend_analysis điền yield/payout bằng trung bình ngành. Những cách này không phù hợp để FAP trình bày như dữ kiện doanh nghiệp đã xác minh. [Bộ lọc](https://github.com/aspirin188/dividend-low-vol-tracker/blob/7ca601f6bb3f9f3411bfce3f70b80a6708e93ea1/server/services/scorer.py#L301), [notebook](https://github.com/hsteffens/dividend_analysis/blob/53469d0da4127402f500af5ef5ea6c8a44a5ce9c/Analytic%20Dividend%20Analysis.ipynb).

**Cần biết công thức thật trong code.** FinanceToolkit có `CFO / (|CAPEX| + |dividends|)`. Tên tỷ số không thay việc kiểm dấu, kỳ, scope, nghĩa dòng chi và mẫu số. Số dư `CFO − CAPEX − cổ tức` âm cho thấy CFO kỳ này chưa bao phủ hai khoản chi; không tự chứng minh doanh nghiệp vay để trả cổ tức hoặc sắp cắt cổ tức. [Hàm nguồn](https://github.com/JerBouma/FinanceToolkit/blob/37ed6f01465b4bfb6718b07e1d65826734f53337/financetoolkit/ratios/solvency_model.py#L267).

**Nguồn chuẩn hóa phụ không thay chứng từ gốc.** vnstock có nhánh `dropna` biến NaN thành 0 rồi bỏ cột toàn 0. Cần kiểm đầu ra/phương án giữ thiếu khi dùng nguồn này; không kết luận mọi API đều biến thiếu thành 0. [Mã xử lý](https://github.com/thinh-vu/vnstock/blob/88825be3f9aab729362e6fca178eb6e9ae4d3f88/vnstock/explorer/vci/financial.py#L519).

## Phạm vi khảo sát và giới hạn

Tìm theo các nhóm dividend screener, dividend growth, dividend portfolio, fundamental analysis và dữ liệu cổ phiếu Việt Nam; chọn dự án có mã công khai và liên quan đến một tác vụ cụ thể. Không dùng star để chứng minh chất lượng, không chọn theo độ nổi tiếng đơn thuần, không bao quát mọi dự án GitHub. Có dự án mới, dự án notebook và nền tảng lớn; mức trưởng thành không đồng nhất.

Tệp lấy qua GitHub API/raw được cố định bằng commit; một yêu cầu lấy `vnstock/LICENSE` thất bại 404 và đã tìm được `LICENSE.md`. Giấy phép GitHub API báo `NOASSERTION` cho vnstock/OpenBB không có nghĩa không có giấy phép. vnstock hiện tự mô tả source-available với giấy phép riêng; một dự án không thấy giấy phép trong inventory. Hồ sơ này nghiên cứu chức năng; chưa tích hợp hay phân phối lại code nguồn.

Đây là nghiên cứu thiết kế dựa trên nguồn và đọc mã, không phải kiểm thử chạy chín hệ thống. Ca minh họa kiểm số học độc lập chỉ làm rõ tác động nghiệp vụ. Chưa sửa SRS hoặc cam kết các chức năng ứng viên thành nghĩa vụ triển khai.
