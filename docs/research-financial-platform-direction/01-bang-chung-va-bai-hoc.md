# Bằng chứng nghiên cứu và bài học áp dụng

Ngày kiểm tra: 11/10/2026. Mục tiêu: tìm các tác vụ phân tích hữu ích và cách tổ chức nền tảng dữ liệu; không lấy số lượng tính năng quảng bá làm yêu cầu cho project.

## 1. Phương pháp và mức bằng chứng

- Chọn dự án thể hiện các lớp khác nhau: dữ liệu có cấu trúc, tính toán, khám phá trực quan, đối chiếu và theo dõi.
- Đọc README, cây mã nguồn và các tệp thực hiện chức năng; lưu tệp tại commit cố định. Sáu repository trong đợt này gồm năm nguồn bổ sung và FinanceToolkit đã khảo sát trước.
- Đối chiếu với tài liệu chính thức về phân tích tài chính và thiết kế tương tác.
- Tách **đã thấy trong mã/tài liệu**, **bài học có thể chuyển sang Việt Nam** và **đề xuất của nghiên cứu này**.

Có 32 tệp nguồn/README/license và sáu inventory; mỗi tệp có SHA-256. Không chạy các repository, đo hiệu năng hoặc xác nhận chất lượng dữ liệu của chúng. Việc tìm thấy mã dựng biểu đồ không đồng nghĩa đã kiểm thử biểu đồ đó trong một ứng dụng đang vận hành.

Nhu cầu là các giả thuyết tác vụ có cơ sở nghề nghiệp và sản phẩm tham chiếu; chưa có phỏng vấn người dùng độc lập. [Protocol kiểm chứng](02-chuc-nang-phan-tich-va-kha-thi.md#11-thứ-tự-triển-khai-và-kiểm-chứng-giá-trị-sử-dụng).

## 2. EdgarTools — dữ liệu là đối tượng có thể truy vấn

**Đã kiểm trong mã:** `FactQuery` có lọc năm tài chính, lọc theo thời điểm nộp báo cáo, trả DataFrame và chuyển bảng theo kỳ. [Theo năm — dòng 148](https://github.com/dgunning/edgartools/blob/246010946cdbe588b0397643fb1598a04fe0cad6/edgar/entity/query.py#L148), [as_of — dòng 321](https://github.com/dgunning/edgartools/blob/246010946cdbe588b0397643fb1598a04fe0cad6/edgar/entity/query.py#L321), [DataFrame — dòng 659](https://github.com/dgunning/edgartools/blob/246010946cdbe588b0397643fb1598a04fe0cad6/edgar/entity/query.py#L659), [pivot — dòng 736](https://github.com/dgunning/edgartools/blob/246010946cdbe588b0397643fb1598a04fe0cad6/edgar/entity/query.py#L736). [Company Facts chính thức](https://edgartools.readthedocs.io/en/latest/guides/company-facts/) mô tả các kiểu truy vấn và bảng nhiều kỳ.

**Bài học:** người dùng chọn một chỉ tiêu/giai đoạn để khai thác, không phải chọn PDF rồi mới tự tìm số. Đây là bằng chứng rõ về năng lực dữ liệu cần có trong A01/A02/A08.

**Chuyển sang Việt Nam:** xây facts chuẩn của project từ BCTC đã duyệt; dùng khóa công ty–kỳ–phạm vi–chỉ tiêu–phiên bản. Bộ đọc SEC/XBRL của thư viện không trực tiếp giải quyết các PDF Việt Nam. `as_of` ở mã nguồn dùng `filing_date`; project chỉ cung cấp phân tích tại thời điểm quá khứ nếu có bằng chứng thời gian công bố/khả dụng tương ứng. Không lấy ngày thu thập hiện tại làm ngày công bố quá khứ.

## 3. FinanceDatabase — tìm và chọn tập doanh nghiệp

**Đã kiểm trong mã:** có thao tác lọc theo cột/giá trị, xử lý niêm yết chính và tìm kiếm các hàng dữ liệu. [filter_rows — dòng 76](https://github.com/JerBouma/FinanceDatabase/blob/5583c4ef5d51fa404a65aa4685da60aca69b7538/financedatabase/query_model.py#L76), [primary listings — dòng 92](https://github.com/JerBouma/FinanceDatabase/blob/5583c4ef5d51fa404a65aa4685da60aca69b7538/financedatabase/query_model.py#L92), [search_rows — dòng 161](https://github.com/JerBouma/FinanceDatabase/blob/5583c4ef5d51fa404a65aa4685da60aca69b7538/financedatabase/query_model.py#L161).

**Bài học:** trước khi tính toán, người dùng cần tìm công ty và biết tập dữ liệu mình đang phân tích. A01/A03 cần danh mục có mã định danh ổn định, tên, thông tin niêm yết và phân ngành khi có nguồn.

**Chuyển sang Việt Nam:** bắt đầu danh mục pilot đã xác nhận; bộ lọc ngành chỉ xuất hiện khi đã có phương pháp phân ngành rõ. Không gộp nhầm mã/chủ thể hoặc coi danh mục công cụ tài chính là kho số liệu BCTC. Không xác nhận thư viện có đủ tập doanh nghiệp/số liệu Việt Nam hiện hành.

## 4. FinanceToolkit — nhiều góc nhìn dùng cùng bộ dữ liệu

**Đã kiểm trong mã:** constructor nhận bảng `balance`, `income`, `cash` do người dùng cung cấp; các hàm bảng tài chính có lựa chọn growth/lag và các dòng hiển thị. [Đầu vào — dòng 105](https://github.com/JerBouma/FinanceToolkit/blob/37ed6f01465b4bfb6718b07e1d65826734f53337/financetoolkit/toolkit_controller.py#L105), [bảng cân đối — dòng 4692](https://github.com/JerBouma/FinanceToolkit/blob/37ed6f01465b4bfb6718b07e1d65826734f53337/financetoolkit/toolkit_controller.py#L4692).

**Bài học:** tập dữ liệu và phương pháp chung có thể phục vụ bảng nhiều doanh nghiệp/kỳ, số tuyệt đối và biến động. A01–A03 không cần mỗi màn hình tự thu/chuẩn hóa/tính lại theo một định nghĩa khác.

**Chuyển sang Việt Nam:** giữ từ điển và điều kiện công thức của project. Chưa kiểm việc đưa DataFrame Việt Nam vào thư viện để chạy; cần thử tương thích trước khi chọn làm dependency. Không đưa toàn bộ bộ chỉ tiêu của toolkit vào yêu cầu vì dữ liệu hoặc định nghĩa chưa đủ.

## 5. finagg — chuẩn hóa dữ liệu và đối chiếu ngành

**Đã kiểm trong mã:** module refined annual có truy vấn nhóm ngành theo ticker hoặc SIC/level, giữ kỳ và ngày nộp trong các bảng; lớp chuẩn hóa tính chênh lệch so với trung bình/độ lệch chuẩn ngành. [IndustryAnnual — dòng 42](https://github.com/theOGognf/finagg/blob/614631d8e26bdbb21c1a6e6a3a10972a00e1d24b/src/finagg/sec/feat/_refined/annual.py#L42), [mốc filed — dòng 145](https://github.com/theOGognf/finagg/blob/614631d8e26bdbb21c1a6e6a3a10972a00e1d24b/src/finagg/sec/feat/_refined/annual.py#L145), [chuẩn hóa — dòng 231](https://github.com/theOGognf/finagg/blob/614631d8e26bdbb21c1a6e6a3a10972a00e1d24b/src/finagg/sec/feat/_refined/annual.py#L231).

**Bài học:** so sánh ngành là một bước phát triển của A03 khi tập dữ liệu đủ lớn và đồng nhất, không phải nhãn thêm vào bảng ba doanh nghiệp.

**Chuyển sang Việt Nam:** cần phân ngành, tập mẫu, năm và nguyên tắc so sánh rõ. Mã này có bước điền giá trị thiếu bằng 0 trong các cột đã biến đổi; không áp dụng cách đó cho facts còn thiếu của project. Chuẩn hóa thống kê cũng không tạo ra điểm chất lượng đầu tư đã được kiểm định.

## 6. FinceptTerminal — màn hình phân tích, đối chiếu và theo dõi

**Đã kiểm trong mã:** không chỉ có tiêu đề màn hình. `EquityFinancialsTab_Populate.cpp` dựng các chuỗi doanh thu/lợi nhuận, biên lợi nhuận, tài sản và dòng tiền từ payload tài chính; `EquityPeersTab.cpp` nhận nhóm mã người dùng chọn, gửi yêu cầu và điền bảng; `WatchlistScreen.cpp` nạp các danh sách theo dõi.

- [Biểu đồ doanh thu/lợi nhuận — dòng 324](https://github.com/Fincept-Corporation/FinceptTerminal/blob/3f444cb7ab712d85a57d270d5edd6e7a2ef50d55/fincept-qt/src/screens/equity_research/EquityFinancialsTab_Populate.cpp#L324).
- [Biểu đồ dòng tiền — dòng 511](https://github.com/Fincept-Corporation/FinceptTerminal/blob/3f444cb7ab712d85a57d270d5edd6e7a2ef50d55/fincept-qt/src/screens/equity_research/EquityFinancialsTab_Populate.cpp#L511).
- [Chọn và nhận bảng peers — dòng 143](https://github.com/Fincept-Corporation/FinceptTerminal/blob/3f444cb7ab712d85a57d270d5edd6e7a2ef50d55/fincept-qt/src/screens/equity_research/EquityPeersTab.cpp#L143).
- [Nạp watchlists — dòng 571](https://github.com/Fincept-Corporation/FinceptTerminal/blob/3f444cb7ab712d85a57d270d5edd6e7a2ef50d55/fincept-qt/src/screens/watchlist/WatchlistScreen.cpp#L571).

**Bài học:** một màn hình phân tích cần nhiều góc nhìn liên quan cùng doanh nghiệp; so sánh và theo dõi là tác vụ riêng có đầu ra sử dụng được. Áp dụng A02/A03/A07.

**Chuyển sang Việt Nam:** dựng biểu đồ từ facts đã duyệt của project; bắt đầu nhóm do người dùng chọn. Nguồn mã có nhiều chức năng về thị trường/giao dịch và heuristics đánh màu; không coi đó là chuẩn đánh giá doanh nghiệp Việt Nam. Danh sách theo dõi chứng minh cấu trúc sử dụng lại, chưa chứng minh chức năng tự nhận diện ảnh hưởng khi BCTC thay đổi.

## 7. OpenBB — một không gian phân tích có chung ngữ cảnh

**Đã kiểm trong mã mẫu:** `widgets_grouping.py` dùng cùng tên tham số công ty/năm giữa các vùng hiển thị; có mẫu chọn dòng bảng truyền mã sang góc nhìn khác. `widgets_plotly_chart.py` có chế độ trả biểu đồ hoặc dữ liệu nền. [Shared parameters — dòng 30](https://github.com/OpenBB-finance/backends-for-openbb/blob/a6293707576e16edda8305adda95b07b6a4b968b/getting-started/reference-backend/widgets_grouping.py#L30), [table grouping — dòng 332](https://github.com/OpenBB-finance/backends-for-openbb/blob/a6293707576e16edda8305adda95b07b6a4b968b/getting-started/reference-backend/widgets_grouping.py#L332), [raw toggle — dòng 546](https://github.com/OpenBB-finance/backends-for-openbb/blob/a6293707576e16edda8305adda95b07b6a4b968b/getting-started/reference-backend/widgets_plotly_chart.py#L546).

**Bài học:** các biểu đồ và bảng không nên hoạt động rời nhau; chọn công ty/kỳ ở một nơi cần đổi bối cảnh phân tích thống nhất. A01/A02/A03/A08 dùng nguyên tắc này.

**Chuyển sang Việt Nam:** bắt đầu một trang với bộ lọc chung và bố cục cố định, không cần triển khai nền tảng widget kéo thả. Mẫu backend dùng dữ liệu hard-coded/mock ở các ví dụ đã đọc; đây là bằng chứng thiết kế tương tác, không là hệ thống tự thu BCTC. Tài liệu [tương tác dữ liệu](https://docs.openbb.co/workspace/analysts/widgets/interacting-with-data) và [dashboard](https://docs.openbb.co/workspace/analysts/dashboards) thuộc Workspace, sản phẩm riêng; phân biệt với mã mẫu backend và OpenBB ODP.

## 8. Cơ sở phương pháp: biểu đồ phải phục vụ một quá trình phân tích

### Phân tích tài chính

[CFA Institute — Financial Analysis Techniques](https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/financial-analysis-techniques) là tài liệu nghề nghiệp cho các cách so sánh, dùng tỷ số và biểu đồ. **Suy luận áp dụng:** nền tảng phải giúp người dùng đặt cơ sở so sánh, đọc kết quả cùng bằng chứng và tiếp tục kiểm tra; một màn hình tính toán đơn lẻ chưa hoàn thành tác vụ này.

### Thiết kế khám phá trực quan

[Shneiderman, 1996 — The Eyes Have It](https://api.drum.lib.umd.edu/server/api/core/bitstreams/419fe7fc-d7d8-4929-bdf0-f4a3041455c1/content), báo cáo University of Maryland, đề xuất các tác vụ tổng quan, thu phóng/lọc, xem chi tiết, liên hệ, lịch sử thao tác và trích xuất. **Suy luận áp dụng:** bảng/biểu đồ của project cần có đường đi từ tổng quan đến dữ liệu cụ thể rồi lưu/xuất kết quả. Công trình là nguyên tắc thiết kế tương tác, không nghiên cứu chứng minh hiệu quả đầu tư.

## 9. Các ý tưởng không nên ưu tiên chỉ vì dự án tham chiếu có

| Ý tưởng | Vì sao chưa cần ở bước hiện tại? | Điều kiện để xem xét lại |
|---|---|---|
| Giá realtime, trading terminal, chỉ báo kỹ thuật | Khác trục phân tích BCTC/cổ tức và cần nguồn giá riêng | Có câu hỏi sử dụng cùng phạm vi, nguồn và công sức rõ |
| Điểm sức khỏe/tự xếp hạng đầu tư | Chưa có phương pháp/trọng số được kiểm định | Định nghĩa, kiểm chứng và giới hạn được chứng minh |
| Bình quân ngành cho pilot ba công ty | Nhóm mẫu có thể khác ngành/quy mô/phạm vi | Có danh mục và tập cùng ngành đủ phù hợp |
| AI giải thích mọi biến động | Không thay được dòng nguồn/thuyết minh và kiểm tra con người | Có dữ liệu căn cứ và protocol đo lỗi diễn giải |
| Trình thiết kế dashboard kéo thả | Tốn công hơn bố cục cố định, chưa giải quyết thêm câu hỏi cốt lõi | Người dùng thực sự cần bố trí tùy chỉnh |

Kết quả nghiên cứu hướng về **ít tác vụ nhưng hoàn chỉnh**. Đây không phải đề nghị bỏ các chức năng dữ liệu hiện hành; cần đưa đầu ra của chúng tới việc phân tích và theo dõi.

[Các chức năng và tính khả thi](02-chuc-nang-phan-tich-va-kha-thi.md) · [Sổ nguồn và bản lưu](sources.md).
