# Tài liệu và bài tập tuần 1 để trao đổi với giảng viên

**Đồng bộ hướng kết hợp 05/10/2026:** theo [SRS v3.1](22-srs-dac-ta-yeu-cau-phan-mem.md), học/triển khai thêm cầu nối LNTT→CFO cho ít nhất một ca, mục tiêu 1–3 sau gate. Đọc [nghiệp vụ](../research-profit-cash-dividend/03-nghiep-vu-va-tu-dien.md) và [ca DHG/VNM](../research-profit-cash-dividend/08-ca-thuc-te-dhg-vnm.md). Minh chứng cần reviewed rows/nguồn, residual/completeness, replay và giờ nhập–duyệt; ghi LNST cạnh LNTT, cổ tức theo profit_year riêng lịch trả. Tuần2 đọc mẫu, tuần4 đo effort, tuần6 cầu nối, tuần8 freeze, tuần10 replay, tuần12–13 kết quả/demo; chưa làm thì ghi pending/not_run. Nhịp báo cáo hai tuần giữ nguyên; theo kế hoạch v3 cho giờ và tiêu chí mới.

Ngày rà nguồn: 04/10/2026. Gắn với W01-02 đến W01-06 của [kế hoạch](04-ke-hoach-13-tuan.md); phần môi trường làm theo [hướng dẫn bắt đầu](23-bat-dau-va-minh-chung-thuc-hien.md).

Tuần 1 cần giải thích được bài toán, đọc tay một BCTC và một sự kiện cổ tức, thiết kế dữ liệu có nguồn. Chưa cần kết luận về toàn thị trường, xây mô hình dự báo hoặc đọc hết các chuẩn mực. Đây là tài liệu học và mẫu đối chiếu do trợ lý chuẩn bị; không chứng minh sinh viên đã làm xong tuần 1.

## 1. Bộ đọc ưu tiên

| Thứ tự | Tài liệu và nơi mở | Phần cần đọc | Thời gian dự kiến | Đầu ra tự viết |
|---|---|---|---|---|
| 1 | [Nhập môn tài chính trong project](18-nhap-mon-tai-chinh-cho-du-an.md) | Lợi nhuận, tài sản, dòng tiền, cổ tức và sáu chỉ tiêu | 30 phút | Một trang giải thích bằng lời của mình |
| 2 | [SEC — Beginners’ Guide to Financial Statements](https://www.sec.gov/about/reports-publications/beginners-guide-financial-statements) | Balance Sheets, Income Statements, Cash Flow Statements và Footnotes | 25 phút | Phân biệt số tại thời điểm và số trong một kỳ |
| 3 | [VAS 24 — Báo cáo lưu chuyển tiền tệ, trong Quyết định 165/2002/QĐ-BTC](https://vbpl.vn/botaichinh/Pages/vbpq-toanvan.aspx?ItemID=21394) | Tìm “Chuẩn mực số 24”; đọc định nghĩa tiền/tương đương tiền, ba nhóm dòng tiền và phương pháp gián tiếp | 30 phút | Giải thích vì sao LNST khác CFO |
| 4 | [DHG — trang công bố BCTC kiểm toán năm 2024](https://dhgpharma.com.vn/vi/co-dong/10253-bao-cao-tai-chinh-kiem-toan-nam-2024-va-giai-trinh-chenh-lech), [PDF gốc](https://dhgpharma.com.vn/sites/default/files/2025-03/DHG-Audited-FS-2024-VN.pdf) | Ý kiến kiểm toán, bảng cân đối, kết quả kinh doanh, lưu chuyển tiền tệ và chính sách tiền | 60 phút | Bảng số liệu kèm đơn vị/kỳ/trang/nhãn gốc |
| 5 | [VSDC — DHG tạm ứng cổ tức năm 2024](https://www.vsd.vn/vi/ad1/177453) | Năm lợi nhuận, tỷ lệ, đồng/cổ phiếu, ngày đăng ký cuối cùng và lịch thanh toán | 15 phút | Một bản ghi sự kiện có nguồn |
| 6 | [VSDC — DHG trả cổ tức bằng tiền năm 2024](https://www.vsd.vn/vi/ad1/182731) | Đối chiếu với đợt tạm ứng, giữ hai đợt riêng | 15 phút | Minh họa năm công bố khác năm lợi nhuận |
| 7 | [Từ điển tài chính của project](12-kien-thuc-tai-chinh-va-tu-dien.md) và [SRS v3.1](22-srs-dac-ta-yeu-cau-phan-mem.md) | Sáu metric keys, phạm vi báo cáo, thiếu dữ liệu, nguồn và quy tắc cổ tức | 30 phút | Nối kiến thức tài chính với trường dữ liệu hệ thống |

Tổng khoảng 3 giờ 25 phút, gồm đọc và ghi chú ban đầu; bài tập/viết báo cáo dùng quỹ làm và báo cáo trong tuần, không cộng thành một lịch học riêng.

SEC dùng để học cấu trúc, không phải mẫu biểu pháp lý Việt Nam. VAS và chính sách kế toán ngay trong BCTC là căn cứ khi đọc dữ liệu mẫu. Trang VAS/VSDC có lúc trả lỗi khi truy cập tự động; giữ link gốc, thử mở bằng trình duyệt và ghi tình trạng nếu chưa đọc được. Không ghi đã đọc chỉ vì có link.

## 2. Đọc thêm khi cần, chưa bắt buộc

- [IFRS Foundation — IAS 7](https://www.ifrs.org/issued-standards/list-of-standards/ias-7-statement-of-cash-flows/): phần About để hiểu ba nhóm dòng tiền và cách điều chỉnh lợi nhuận theo phương pháp gián tiếp. Không tự áp quy tắc IFRS lên BCTC VAS.
- [BCTC hợp nhất kiểm toán HPG năm 2024](https://file.hoaphat.com.vn/hoaphat-com-vn/2025/03/bao-cao-tai-chinh-hop-nhat-nam-2024-da-kiem-toan-1.pdf), [danh mục chính thức](https://www.hoaphat.com.vn/quan-he-co-dong/bao-cao-tai-chinh): đối chiếu cách trình bày hợp nhất với báo cáo của Công ty DHG. Chưa nhập số HPG từ tài liệu này trong bộ bài tập.
- [Thông tư 200/2014/TT-BTC trên cổng đăng ký kinh doanh](https://dangkykinhdoanh.gov.vn/vn/pages/ChiTietVanBan.aspx?vID=26993): tra cứu nền mẫu biểu cho giai đoạn lịch sử, đối chiếu chính sách công bố của từng báo cáo; không cần đọc toàn bộ.
- [Thông tư 99/2025/TT-BTC — Công báo](https://congbao.chinhphu.vn/van-ban/thong-tu-so-99-2025-tt-btc-46529.htm), [giải đáp của Bộ Tài chính về thời điểm áp dụng](https://portal.mof.gov.vn/hoidapcstc/home/cthoidap/159102): nguồn cập nhật khi mở rộng sang năm tài chính bắt đầu từ hoặc sau 01/01/2026. Không mô tả TT200 là chế độ hiện hành cho mọi năm.
- [Python 3.12 Tutorial](https://docs.python.org/3.12/tutorial/): mục 3–5 và 7.2; chỉ học đủ để tự viết dict/list và lưu một bản ghi JSON có nguồn.

## 3. Những khái niệm phải tự giải thích

| Khái niệm | Cách hiểu để dùng trong đề tài | Sai sót cần tránh |
|---|---|---|
| Bảng cân đối | Tài sản, nợ phải trả và vốn chủ sở hữu tại một ngày | Ghép số cuối năm với lợi nhuận quý rồi gọi tỷ số năm |
| Báo cáo kết quả kinh doanh | Doanh thu/chi phí/lợi nhuận của một kỳ | Nhầm LNST với doanh thu hoặc lợi nhuận chưa phân phối |
| Báo cáo lưu chuyển tiền tệ | Biến động tiền phân theo kinh doanh, đầu tư và tài chính | Nhầm CFO với biến động tiền toàn năm |
| Thuyết minh | Giải thích chính sách, cấu phần và chi tiết số liệu | Bỏ qua nhãn, đơn vị và phạm vi |

Khung đọc cấu trúc dựa trên [hướng dẫn SEC](https://www.sec.gov/about/reports-publications/beginners-guide-financial-statements). Lợi nhuận và tiền có thể khác do khoản chưa thu/chi, khấu hao và biến động vốn lưu động; tham khảo [VAS 24](https://vbpl.vn/botaichinh/Pages/vbpq-toanvan.aspx?ItemID=21394) và [IAS 7](https://www.ifrs.org/issued-standards/list-of-standards/ias-7-statement-of-cash-flows/).

Quy ước hệ thống lấy từ SRS: không tìm thấy dữ liệu thì ghi missing; nợ phải trả không đồng nghĩa nợ vay; báo cáo công ty và hợp nhất phải có scope riêng. Cổ tức theo phần trăm mệnh giá không phải lợi suất theo giá thị trường. LNST cả tập đoàn và LNST thuộc cổ đông công ty mẹ là hai chỉ tiêu cần phân biệt.

## 4. Bài tập BCTC thật: DHG năm 2024

Đã tải bản PDF gốc tại `data-sets/fap/week-01-reading/DHG-Audited-FS-2024-VN.pdf`. Bản này 47 trang, dạng ảnh. Bảng dưới do trợ lý đọc trực quan; bạn phải mở lại và tự đối chiếu trước khi dùng làm minh chứng cá nhân. Chưa phải gold độc lập hoặc kết quả trích xuất tự động.

Vị trí: trang in 4–5/PDF 7–8 là kiểm toán; trang in 6–7/PDF 9–10 là cân đối; trang in 8/PDF 11 là kết quả kinh doanh; trang in 9–10/PDF 12–13 là lưu chuyển tiền; trang in 11–12/PDF 14–15 là cơ sở trình bày/chính sách.

| Chỉ tiêu đối chiếu | Số 2024, VND | Mã | Trang in / PDF |
|---|---:|---|---|
| Tổng tài sản | 5.959.243.276.265 | 270 | 6 / 9 |
| Nợ phải trả | 1.864.488.178.296 | 300 | 7 / 10 |
| Vốn chủ sở hữu | 4.094.755.097.969 | 400 | 7 / 10 |
| LNST | 778.920.119.960 | 60 | 8 / 11 |
| CFO | 1.317.583.405.328 | 20 | 9 / 12 |
| Tiền tại cuối kỳ | 62.857.547.612 | 70 | 10 / 13 |

Nguồn số và vị trí: [BCTC DHG 2024](https://dhgpharma.com.vn/sites/default/files/2025-03/DHG-Audited-FS-2024-VN.pdf). Nhãn tiền chỉ ghi “Tiền”, không tự đổi thành “Tiền và tương đương tiền”. Lưu candidate rồi review cách ánh xạ `cash_equivalents`; chưa kết luận tương đương tiền bằng 0. Báo cáo này đứng tên Công ty DHG; không tự gán scope hợp nhất.

Bạn tự làm ba kiểm tra: tài sản trừ nợ và vốn; CFO/LNST khi mẫu số dương; nợ phải trả/tài sản. Ghi toán hạng, công thức, kết quả và nguồn. CFO/LNST là phép so sánh hai đại lượng cả năm; chưa đủ để kết luận doanh nghiệp tốt/xấu hoặc có sai phạm.

## 5. Bài tập sự kiện cổ tức: DHG, năm lợi nhuận 2024

| Nguồn | Năm lợi nhuận | DPS thông báo | Ngày cập nhật trên VSDC | Ngày đăng ký cuối cùng | Lịch thanh toán |
|---|---:|---:|---|---|---|
| [Tạm ứng](https://www.vsd.vn/vi/ad1/177453) | 2024 | 4.000 VND/cổ phiếu, 40% | 11/12/2024 | 25/12/2024 | 14/02/2025 |
| [Đợt tiếp theo](https://www.vsd.vn/vi/ad1/182731) | 2024 | 6.000 VND/cổ phiếu, 60% | 13/05/2025 | 26/05/2025 | 18/06/2025 |

Hai thông báo cho thấy cùng một năm lợi nhuận có thể có nhiều đợt, công bố và thanh toán theo lịch ở năm khác. Tổng hai mức là 10.000 VND/cổ phiếu; chỉ coi đây là tổng của hai thông báo đã đọc. Xác nhận DPS năm còn cần rà độ đầy đủ, sửa đổi/hủy và cơ sở cổ phiếu tương thích. Notice có lịch trả chưa chứng minh đã thực trả. Ngày cập nhật VSDC không tự đồng nhất với ngày doanh nghiệp công bố; `first_seen` phải là thời điểm hệ thống thực sự ghi nhận.

Bản ghi tự viết cần có: issuer/ticker, loại cash, profit_year, component, announced_dps_vnd, tỷ lệ/mệnh giá, published_date và nguồn của ngày đó, record_date, scheduled_payment_date, payment_status, source_url, locator, review_status. Giữ `first_seen` trống nếu chưa có lần thu thập được ghi log.

## 6. Bốn đầu ra cần mang trao đổi với thầy

1. **Tóm tắt bài toán một trang:** người dùng cần xem gì, dữ liệu nằm ở đâu, khó khăn khi ghép, kết quả hệ thống dự kiến cung cấp. Đọc [câu chuyện người dùng](16-y-tuong-va-cau-chuyen-nguoi-dung.md), [nghiên cứu/chốt hướng](20-nghien-cuu-lan-hai-va-chot-de-tai.md) và trích SRS; không tuyên bố đề tài chưa ai làm.
2. **Bảng đọc tay có nguồn:** sáu nhãn trên, kỳ/scope/đơn vị/trang; đánh dấu chỗ cash cần review. Kèm hai dòng sự kiện cổ tức.
3. **Sơ đồ xử lý bằng lời:** nguồn chính thức → lưu bản gốc → trích xuất → chuẩn hóa → kiểm tra/review → ghép theo doanh nghiệp/năm lợi nhuận → phân tích và truy vết. Chỉ mô tả thiết kế, chưa gọi là chức năng đã chạy.
4. **Phạm vi và câu hỏi cần chốt:** 3 doanh nghiệp pilot; đề xuất mục tiêu bản cuối 8 doanh nghiệp × 3 năm, còn phụ thuộc dữ liệu và quỹ giờ. Kế hoạch hiện hành vẫn có gate 5–8, đề xuất 8 chưa tự thay baseline SRS. Nếu thầy yêu cầu nghiên cứu thống kê khái quát thị trường thì cần thiết kế lại mẫu và ngân sách.

Dùng [khung báo cáo tuần 1](reports/tuan-01-khung-trao-doi-voi-thay.md). Lịch báo cáo chính thức hiện là cuối tuần 2; khung tuần 1 phục vụ trao đổi sớm theo yêu cầu của bạn.

## 7. Câu hỏi giảng viên và tiêu chí hoàn thành

- Đồ án được đánh giá chủ yếu về hệ thống dữ liệu hay về kiểm định một giả thuyết tài chính?
- Ba doanh nghiệp pilot và mục tiêu mở rộng tám doanh nghiệp có phù hợp rubric/thời hạn không?
- Có chấp nhận phân tích mô tả, case và đánh giá độ đúng trích xuất làm trọng tâm không?
- Được dùng nguồn công khai và bước review tay có lưu minh chứng ở mức nào?
- Có yêu cầu khảo sát người dùng, mẫu SRS/báo cáo, người kiểm tra gold hoặc hình thức demo riêng không?

Hoàn thành phần phân tích cơ bản khi bạn tự đọc lại nguồn, giải thích được ba báo cáo, phân biệt LNST/CFO và ba loại ngày cổ tức, viết được một bản ghi có provenance, và ghi vấn đề chưa chốt. Mẫu đã chuẩn bị không làm W01 tự động hoàn thành; môi trường, ledger 9 report/54 target, TC01/TC08 và nhật ký vẫn làm theo kế hoạch.

## 8. Hồ sơ nguồn và giới hạn kiểm chứng

[Sổ nguồn JSON tuần 1](execution/week-01-reading-sources.json) ghi URL, phương thức kiểm, hash bản PDF tải về và tình trạng truy cập. PDF mẫu là tài liệu học/development; không đưa cùng lineage vào holdout độc lập sau này. `data-sets/` bị Git ignore: cần giữ bản tải và sao lưu riêng. Bài tập kiểm hai thông báo không chứng minh đã rà toàn bộ lịch sử cổ tức hoặc tải đủ BCTC 2023–2025 của pilot.
