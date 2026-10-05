# Tổng quan tài liệu và khoảng trống nghiên cứu cần kiểm tra

Ngày: 03/10/2026. Mức độ đã đọc ghi tại [sổ nguồn](02-so-tai-lieu-tham-khao.md). Đây là tổng quan có mục tiêu cho đồ án, chưa phải systematic review.

## 1. Chính sách cổ tức và giới hạn giả thuyết

Brav, Graham, Harvey và Michaely (2005) khảo sát 384 lãnh đạo tài chính, phỏng vấn thêm 23 người. Nghiên cứu nhấn mạnh xu hướng duy trì mức cổ tức và vai trò của tính ổn định lợi nhuận; quyết định tăng cổ tức còn liên quan nhu cầu đầu tư và thanh khoản. Điều này hỗ trợ việc xây baseline lịch sử và xem xét dòng tiền, nhưng không chứng minh ngưỡng CFO/LNST hoặc mức giảm 30% có hiệu lực ở Việt Nam. [Bài báo gốc](https://people.duke.edu/~charvey/Research/Published_Papers/P88_Payout_policy_in.pdf), DOI: [10.1016/j.jfineco.2004.07.004](https://doi.org/10.1016/j.jfineco.2004.07.004).

Tài liệu giảng dạy của Damodaran phân biệt cổ tức đã chi với tiền có thể phân phối sau nhu cầu tái đầu tư và dòng tiền nợ. Suy luận thiết kế của đề tài: CFO dương là một đầu vào, chưa đủ đo toàn bộ dư địa cổ tức; FCFE đòi hỏi dữ liệu mở rộng ngoài sáu chỉ tiêu lõi. [Chương phân tích chính sách cổ tức](https://pages.stern.nyu.edu/~adamodar/pdfiles/acf3E/book/ch11.pdf).

**Khoảng cần kiểm tra:** tín hiệu dòng tiền có bổ sung thông tin cho lịch sử chi trả trong mẫu phi tài chính Việt Nam không? Phải nghiên cứu trên mẫu cụ thể, tránh lấy kết quả khảo sát nước ngoài làm kết quả của đề tài.

## 2. BCTC và ngữ nghĩa tiền mặt

IAS 7 phân biệt hoạt động kinh doanh, đầu tư, tài trợ và yêu cầu giải thích biến động tiền. Dùng như tài liệu học khái niệm; dataset Việt Nam phải giữ cơ sở kế toán thực tế của từng báo cáo, không tự chuyển toàn bộ VAS sang IFRS. [IFRS Foundation: IAS 7](https://www.ifrs.org/issued-standards/list-of-standards/ias-7-statement-of-cash-flows.html/).

Khảo sát nhỏ tìm được PDF IFRS ba trang của Vinamilk, có text nhưng bảng mặc định không nhận diện được. Đây là bằng chứng thao tác đã chạy, trình bày ở [khảo sát](03-khao-sat-nguon-thuc-te.md). Chưa xác minh báo cáo kiểm toán tương ứng và ngày công bố ban đầu nên chưa đưa mẫu này vào cohort dự báo.

**Khoảng cần kiểm tra:** mức độ sai do đơn vị, cột năm, phạm vi và chuẩn mực lớn đến đâu? I1 đo trực tiếp từng nhóm lỗi thay vì chỉ đo độ đúng chữ OCR.

## 3. Cổ tức là dữ liệu sự kiện có phiên bản

Thông báo VNM ngày 30/08/2024 gồm 950 đồng cho năm 2023 và 1.500 đồng tạm ứng năm 2024, cùng lịch thanh toán. Thông báo VSH ngày 05/09/2024 sửa một lịch đã có. Hai cấu trúc này chứng minh cần tách phần phân bổ theo năm và lưu lịch sử điều chỉnh. [VNM](https://www.vsd.vn/vi/ad1/174349), [VSH](https://www.vsd.vn/vi/ad/174490).

Đây là nhận xét từ thông báo đã đọc, không phải bằng chứng tiền đã chuyển đến cổ đông. **Khoảng cần kiểm tra:** bao nhiêu nhãn thay đổi khi đối chiếu phiên bản và phân bổ đúng năm? I3 định nghĩa thí nghiệm này.

## 4. Truy vết và công nghệ trích xuất

W3C PROV-DM cung cấp ba thành phần thích hợp để mô tả một số liệu: thực thể nguồn, hoạt động xử lý và tác nhân chịu trách nhiệm. Đề tài áp dụng ý tưởng này vào bảng quan hệ; chưa cần RDF hoặc cơ sở dữ liệu đồ thị. [PROV-DM](https://www.w3.org/TR/prov-dm/).

pdfplumber cung cấp text, tọa độ và phương tiện kiểm tra bảng, phù hợp làm baseline cho PDF có text. OCR là nhánh riêng khi mất lớp chữ. [Tài liệu pdfplumber](https://github.com/jsvine/pdfplumber), [Tesseract](https://github.com/tesseract-ocr/tesseract).

**Khoảng cần kiểm tra:** parser theo vùng/nhãn cộng review có giảm thời gian làm dữ liệu mà vẫn giữ độ đúng so với đọc tay không? Không gọi việc ghép thư viện là thuật toán mới; đóng góp là quy trình và đánh giá trên tài liệu Việt Nam.

## 5. Đánh giá mô hình theo thời điểm

Hướng dẫn scikit-learn về leakage yêu cầu tách dữ liệu trước khi học phép biến đổi; Pipeline giúp giữ imputation/scaling trong train. TimeSeriesSplit dùng thứ tự mẫu và giả định khoảng cách phù hợp cho so sánh fold. Suy luận cho đề tài: panel doanh nghiệp có ngày công bố khác nhau cần chia theo mốc lịch và kiểm tra outcome_end, không chỉ đặt gap theo số dòng. [Leakage](https://scikit-learn.org/stable/common_pitfalls.html), [TimeSeriesSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html).

Rudin trình bày lý do ưu tiên mô hình có thể hiểu trực tiếp trong những quyết định quan trọng. Đề tài chọn rule score và logistic trước; lời giải thích dễ đọc không thay thế đánh giá ngoài mẫu. [Rudin, bản tác giả trên arXiv](https://arxiv.org/abs/1811.10154).

**Khoảng cần kiểm tra:** tín hiệu có ổn định qua thời gian và có cải thiện so với baseline trên cùng tập nhãn không? Không suy độ đúng từ accuracy của dữ liệu mất cân bằng.

## 6. Trợ lý hỏi đáp và căn cứ trả lời

Lewis và cộng sự kết hợp mô hình sinh với truy xuất nguồn bên ngoài trong RAG. Min và cộng sự đề xuất đánh giá độ đúng bằng các phát biểu đơn lẻ thay vì chấm toàn bộ đoạn văn bằng một nhãn. Chuyển sang đề tài: câu trả lời cần kiểm tra riêng số, kỳ, phạm vi, công thức và trạng thái cổ tức. [RAG](https://arxiv.org/abs/2005.11401), [FActScore](https://arxiv.org/abs/2305.14251).

Chỉ đã đọc abstract và metadata hai bài trên; chưa tái lập thí nghiệm của tác giả. I5 đề xuất benchmark tiếng Việt riêng, không chuyển điểm của tác giả sang sản phẩm.

## 7. Công việc rà soát học thuật tiếp theo

### Nghiên cứu Việt Nam đã đọc được

Chau (2023) nghiên cứu FCF/vòng đời với payout trên 110 công ty HOSE, 2014–2020, bằng FEM/REM/GMM. Nguyen Do Quyen và Tran Thi Minh Tram (2016) xét đòn bẩy/sở hữu ở doanh nghiệp phi tài chính HOSE/HNX, 2010–2015. [CTU](https://ctujs.ctu.edu.vn/index.php/ctujs/article/view/583), [FTU](https://jiem.ftu.edu.vn/index.php/jiem/article/view/159).

Abstract CTU báo dấu dương của nợ với payout, còn FTU báo nợ cao thường chi ít hơn. Chưa đối chiếu toàn bộ định nghĩa/specification nên không coi là mâu thuẫn trực tiếp. [CTU](https://ctujs.ctu.edu.vn/index.php/ctujs/article/view/583), [FTU](https://jiem.ftu.edu.vn/index.php/jiem/article/view/159).

Suy luận thiết kế: không áp một dấu quan hệ nợ cho mọi ngành/kỳ. Đã có nghiên cứu trong nước, nên định vị đóng góp ở dữ liệu có truy vết, sự kiện theo phiên bản và đánh giá theo cutoff; chưa đủ bằng chứng khẳng định tính mới. Hai bài không thay kết quả dự báo cắt giảm 12 tháng của đề tài; chưa tái lập.

### Phần cần tiếp tục rà có hệ thống

Tìm tài liệu thực nghiệm Việt Nam bằng cả hai ngôn ngữ: “chính sách cổ tức dòng tiền doanh nghiệp Việt Nam”, “dividend cuts cash flow Vietnam non-financial firms”, “financial statement extraction Vietnamese PDF”, “point-in-time dividend prediction”. Chọn bài có toàn văn/phương pháp đọc được; ghi nguồn, mẫu, biến phụ thuộc, cách split và yếu tố gây thiên lệch. Loại bài chỉ có tiêu đề khỏi bằng chứng kết luận; giữ trong danh mục cần đọc.

Tiêu chí đọc tiếp: nguồn tác giả/tạp chí/trường; câu hỏi gần RQ1–RQ3; định nghĩa cổ tức rõ; mô tả dữ liệu; đánh giá có kiểm soát thời gian. Chưa đủ bằng chứng để khẳng định khoảng trống nghiên cứu trong nước hoặc ưu thế sản phẩm so với mọi nền tảng hiện có.
