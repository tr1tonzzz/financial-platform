# Sổ tài liệu tham khảo và mức độ kiểm chứng

Ngày truy cập của các mục dưới đây: **03/10/2026**. “Đã đọc” nghĩa là đọc phần được nêu; không mặc định đã đọc toàn văn hay thực nghiệm đã chạy. DOI arXiv là định danh kho bài, không tự chứng minh xuất bản ở tạp chí.

## 1. Nguồn nghiệp vụ và học thuật

| ID | Tài liệu/URL | Nội dung đã đọc và cách kiểm tra | Dùng cho | Giới hạn |
|---|---|---|---|---|
| F01 | Brav, Graham, Harvey, Michaely (2005), *Payout policy in the 21st century*. [PDF tác giả](https://people.duke.edu/~charvey/Research/Published_Papers/P88_Payout_policy_in.pdf); [DOI](https://doi.org/10.1016/j.jfineco.2004.07.004) | Web đọc abstract, introduction, mô tả mẫu; xác nhận metadata tại [Duke](https://scholars.duke.edu/publication/762061) | I2/I4, baseline lịch sử | Chưa đọc toàn bộ bảng/hồi quy; mẫu nước ngoài |
| F02 | Aswath Damodaran, *Applied Corporate Finance*, chương 11. [PDF NYU](https://pages.stern.nyu.edu/~adamodar/pdfiles/acf3E/book/ch11.pdf) | Đọc phần khung phân tích tiền có thể chi và đoạn tổng kết qua text web | I2, FCFE và tái đầu tư | Chưa đọc toàn chương; tài liệu giảng dạy, không phải kiểm định ở Việt Nam |
| F03 | IFRS Foundation, [IAS 7 overview](https://www.ifrs.org/issued-standards/list-of-standards/ias-7-statement-of-cash-flows.html/) | Đọc phần About và lịch sử tiêu chuẩn | I1/I2, học khái niệm dòng tiền | Không coi overview là toàn văn quy định; không áp dụng thay VAS |
| F04 | Chau, A. V. (2023), [FCF và vòng đời với chính sách cổ tức Việt Nam](https://ctujs.ctu.edu.vn/index.php/ctujs/article/view/583); [PDF](https://ctujs.ctu.edu.vn/index.php/ctujs/article/download/583/643/3623); [DOI](https://doi.org/10.22144/ctu.jen.2023.026) | Đọc abstract, introduction, khái niệm vòng đời và Table 1 qua text web; mở PDF 10 trang | I2, nghiên cứu Việt Nam | Chưa rà toàn bộ diagnostics hoặc tái lập; FCF bài này không đồng nhất FCFE |
| F05 | Nguyen Do Quyen, Tran Thi Minh Tram (2016), [Dividend Policy, Financial Leverage and Ownership Structure: Empirical Evidence from Vietnam](https://jiem.ftu.edu.vn/index.php/jiem/article/view/159); [PDF](https://jiem.ftu.edu.vn/index.php/jiem/article/download/159/109/359) | Đọc abstract/metadata; mở PDF 21 trang nhưng chưa đọc toàn văn | I2/I4, nợ và sở hữu | Chưa rà specification/robustness, chưa xác minh DOI, dùng URL tạp chí |
| V01 | Vinamilk, [BCTC hợp nhất IFRS 2024, trích báo cáo thường niên](https://www.vinamilk.com.vn/bao-cao-thuong-nien/bao-cao/2024/doc/en/bctc-ifrs.pdf) | Tải HTTP 200; pdfplumber đọc 3 trang; render và xem cả 3; đối chiếu 6 giá trị | I1, khảo sát parser | Web fetch từng báo 403 nhưng tải local được; chưa xác minh audit/available_at |
| V02 | VSDC, [VNM: cổ tức cuối 2023 và tạm ứng 1/2024](https://www.vsd.vn/vi/ad1/174349) | Đọc nội dung HTML qua web, mệnh giá, phân bổ, ngày quyền/lịch; thời điểm trang 30/08/2024 | I3, sự kiện có nhiều thành phần | Tải local lỗi TLS; không có bằng chứng thực trả |
| V03 | VSDC, [VSH: đổi ngày thanh toán](https://www.vsd.vn/vi/ad/174490) | Đọc thông báo 05/09/2024 qua web: lịch cũ 03/10/2024, mới 19/09/2024 | I3, amendment/dedupe | Chưa đối chiếu toàn chuỗi; chưa xác nhận thực trả |
| M01 | Cynthia Rudin, [Stop Explaining Black Box…](https://arxiv.org/abs/1811.10154) | Đọc abstract và metadata; bản tác giả | I4, ưu tiên mô hình hiểu trực tiếp | Không là bằng chứng logistic hiệu quả trên đề tài |
| M02 | Lewis et al. (2020), [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401), [DOI kho bài](https://doi.org/10.48550/arXiv.2005.11401) | Đọc abstract và metadata, trang ghi NeurIPS 2020 | I5, truy xuất trước khi sinh | Chưa đọc toàn văn, chưa tái lập |
| M03 | Min et al. (2023), [FActScore](https://arxiv.org/abs/2305.14251), [DOI kho bài](https://doi.org/10.48550/arXiv.2305.14251) | Đọc abstract và metadata | I5, kiểm tra phát biểu đơn lẻ | Benchmark gốc khác tài chính Việt Nam |

## 2. Tài liệu kỹ thuật chính thức

| ID | Tài liệu | Phần đã đọc / quyết định thiết kế sử dụng |
|---|---|---|
| T01 | W3C, [PROV-DM](https://www.w3.org/TR/prov-dm/) và [overview](https://www.w3.org/TR/prov-overview/) | Abstract/core concepts: entity, activity, agent; chuyển thành provenance quan hệ cho I1 |
| T02 | [pdfplumber README](https://github.com/jsvine/pdfplumber) | Text, crop, tables, visual debugging; đã dùng đọc/crop trong khảo sát |
| T03 | [Tesseract repository](https://github.com/tesseract-ocr/tesseract) | Vai trò OCR engine; chưa chạy OCR hoặc đo tiếng Việt |
| T04 | PostgreSQL, [numeric types](https://www.postgresql.org/docs/current/datatype-numeric.html) | Kiểu chính xác cho số tiền; NUMERIC/Decimal là đề xuất |
| T05 | PostgreSQL, [constraints](https://www.postgresql.org/docs/current/ddl-constraints.html) | CHECK, UNIQUE, FK; kiểm soát cấu trúc, không chứng minh đúng nghiệp vụ |
| T06 | pandas, [merge_asof](https://pandas.pydata.org/docs/reference/api/pandas.merge_asof.html) | Ghép theo khóa có thứ tự và hướng thời gian; cần lọc scope/basis/metric trước |
| T07 | SciPy, [spearmanr](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.spearmanr.html) | Hệ số hạng, missing/constant input; cảnh báo p-value mẫu nhỏ |
| T08 | scikit-learn, [common pitfalls](https://scikit-learn.org/stable/common_pitfalls.html) | Leakage và preprocessing trong Pipeline |
| T09 | scikit-learn, [TimeSeriesSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html) | Thứ tự thời gian, gap theo mẫu; đề tài cần splitter theo ngày |
| T10 | scikit-learn, [probability calibration](https://scikit-learn.org/stable/modules/calibration.html) | Reliability diagram; Brier phản ánh nhiều thành phần, không chỉ calibration |
| T11 | scikit-learn, [average_precision_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.average_precision_score.html) | AP là tổng có trọng số theo recall; phân biệt với diện tích PR nội suy hình thang |
| T12 | PostgreSQL, [full text search](https://www.postgresql.org/docs/current/textsearch-intro.html) | Baseline tra cứu văn bản của I5; chưa benchmark khả năng tiếng Việt |
| T13 | FastAPI, [response model](https://fastapi.tiangolo.com/tutorial/response-model/) | Khai báo/kiểm tra output schema và metadata nguồn |

Các trang “stable/current” có thể đổi sau ngày truy cập. Khi triển khai phải khóa phiên bản phụ thuộc và ghi runtime thực tế; số phiên bản từ trang web chưa phải phiên bản dự án sử dụng.

## 3. Nguồn phát hiện nhưng chưa đủ bằng chứng

| Nguồn | Trạng thái | Cách dùng hợp lệ |
|---|---|---|
| [FPT annual report 2024](https://fpt.com/-/media/project/fpt-corporation/fpt/ir/general-meetings-of-shareholders/fpt_annual_report_2024.pdf) | Search có nội dung; web mở lỗi; tải local HTTP 404 | Ứng viên cần tìm lại đường dẫn IR; chưa là file đã kiểm tra |
| [HNX: VE4 BCTC 2024](https://www.hnx.vn/vi-vn/m-niem-yet/tin-tuc/Bao%20cao%20tai%20chinh%20nam%202024-549416-1.html) | Search thấy metadata và tên đính kèm; web open lỗi | Chưa kết luận tải được đính kèm hoặc parser hoạt động |
| [REE: danh mục BCTC](https://www.reecorp.com/danh-muc-bao-cao/bao-cao-tai-chinh/page/4/) | Đã đọc trang danh mục, chưa tải file | Ứng viên khám phá tài liệu; chưa đo độ phủ |
| [SDT: đổi lịch thanh toán](https://vsd.vn/vi/ad/159639) | Search trả nội dung; mở trang timeout, tải local lỗi TLS | Đầu mối cần xác minh tiếp; không dùng làm case thực nghiệm đã xác nhận |
| [MacKinlay, Event Studies in Economics and Finance](https://www.bu.edu/econ/files/2011/01/MacKinlay-1996-Event-Studies-in-Economics-and-Finance.pdf) | Mở PDF/đọc đoạn thiết kế nghiên cứu | Tài liệu cho hướng thị trường về sau; không nằm trong năm hồ sơ triển khai |
| [Phan Ngọc Thùy Như, Nguyễn Kim Phước: các yếu tố chính sách cổ tức ngành công nghiệp HOSE](https://journalofscience.ou.edu.vn/index.php/econ-vi/article/view/2061) | Search trả abstract/DOI; web mở trang timeout | Bài cần đọc tiếp; chưa dùng kết quả làm căn cứ |

## 4. Quy tắc bổ sung nguồn

Mỗi nguồn mới ghi ID, tác giả/tổ chức, tiêu đề, năm, URL/DOI, ngày kiểm tra, phần đã đọc, cách truy cập, phát biểu hỗ trợ, hạn chế và hồ sơ sử dụng. Tách thành “search thấy”, “đọc trang”, “tải file”, “trích xuất”, “đối chiếu”, “đánh giá trên mẫu”. Chỉ bước cuối mới hỗ trợ tuyên bố chất lượng tổng quát.
