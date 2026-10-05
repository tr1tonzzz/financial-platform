# 02 — Cơ sở nghiên cứu và sổ nguồn

**Trạng thái cập nhật05/10/2026:** hướng kết hợp đã được tích hợp vào [SRS v3.1](../research-platform/22-srs-dac-ta-yeu-cau-phan-mem.md), CR-PCD-01/mục15, theo yêu cầu cập nhật tài liệu của người thực hiện. Tối thiểu một ca cầu nối là nghĩa vụ dự thảo; E05/E10 và ca thêm có điều kiện. Nội dung đề xuất ngày04/10 bên dưới là cơ sở nghiên cứu; các câu “chưa tích hợp/chờ change record” mô tả trạng thái lúc đó, được thay bởi SRS v3.1. Chưa có phê duyệt giảng viên hoặc kiểm thử ứng dụng đã chạy. Kế hoạch/checklist v3 là lịch triển khai duy nhất; bảng tuần/giờ trong hồ sơ nghiên cứu là phương án trước tích hợp.

Ngày đọc: **04/10/2026**. Ưu tiên nguồn gốc: nhà xuất bản/tác giả, doanh nghiệp, VSDC, cơ quan công bố văn bản. Phạm vi là rà soát có mục tiêu phục vụ thiết kế, chưa phải systematic literature review hoặc tái lập kinh tế lượng.

## 1. Cơ sở lựa chọn

Lợi nhuận đo kết quả theo kế toán dồn tích; CFO phản ánh dòng tiền từ hoạt động kinh doanh. Cầu nối gián tiếp cho phép xem các điều chỉnh giữa hai góc nhìn. [IAS 7, phần About](https://www.ifrs.org/issued-standards/list-of-standards/ias-7-statement-of-cash-flows/) hỗ trợ khái niệm và phân loại, không thay chế độ kế toán áp dụng trong BCTC Việt Nam. Parser phải đọc chuẩn mực/mẫu báo cáo thực tế.

[Brav và cộng sự, 2005](https://people.duke.edu/~charvey/Research/Published_Papers/P88_Payout_policy_in.pdf) là nền tham khảo về quyết định phân phối và động cơ giữ ổn định cổ tức. Trong lượt này chỉ đọc phần mở đầu/abstract có thể truy xuất, không tái lập khảo sát. Dùng để đặt câu hỏi, không chuyển kết luận của thị trường khác thành quy luật Việt Nam.

[Alphonse & Tran, 2014](https://www.ccsenet.org/journal/index.php/ijef/article/view/32728) phân biệt quyết định có chia với mức chia, dùng cách tiếp cận hai bước. Abstract báo quan hệ FCF/tài sản với payout có dấu âm. Bài gợi ý rủi ro chọn mẫu khi chỉ giữ doanh nghiệp chia cổ tức; không cung cấp bằng chứng cho dấu CFO trong dataset đề tài này.

[Chau Anh Vu, 2023](https://ctujs.ctu.edu.vn/index.php/ctujs/article/view/583), mẫu 110 công ty HOSE trong 2014–2020, nghiên cứu FCF và vòng đời với payout. Đã mở PDF, đọc abstract và phần định nghĩa biến/Bảng 1, chưa kiểm tra toàn bộ mô hình. FCF trong bảng dùng EBIT sau thuế, khấu hao, thay đổi vốn lưu động và CAPEX, chia tài sản; **không phải CFO/LNST**. Kế thừa câu hỏi cần phân biệt các nguồn tiền và đặc điểm doanh nghiệp; không sao chép công thức sang tên CFO.

## 2. Khoảng trống áp dụng và phương pháp nghiên cứu

Hồ sơ trước đã có N1/I2 và SRS ba nhóm dữ liệu. Khoảng trống triển khai là tạo một chuỗi kiểm chứng từ PDF/thông báo → số đúng context → phép ghép → giải thích. Đề tài có thể theo hướng xây dựng và đánh giá một hệ thống: xác định tác vụ, thiết kế artifact, thử nguồn thật, đo chất lượng/công sức, đánh giá giới hạn. Tính mới nằm ở đóng góp được đo, không nằm ở việc gọi một tỷ số là “chất lượng lợi nhuận”.

Ba câu hỏi nghiên cứu đề xuất:

- **RQ1:** Pipeline có tạo được dữ liệu LNST/CFO/cổ tức với kỳ, scope, component và provenance đúng; mức lỗi/công sức trước–sau review là bao nhiêu?
- **RQ2:** Thêm cầu nối CFO giúp giải thích đúng và kiểm tra nhanh hơn các ca lệch lợi nhuận–tiền so với chỉ bảng tỷ số không?
- **RQ3:** Quy tắc năm lợi nhuận/coverage/version làm thay đổi bảng mô tả và lựa chọn ca so với ghép đơn giản theo năm thông báo như thế nào?

RQ2 là giả thuyết lợi ích chưa được kiểm chứng. RQ3 đo tác động phương pháp dữ liệu; không phải tác động nhân quả của CFO lên cổ tức. Ba câu hỏi có thể đánh giá với project nhỏ; hồi quy panel cần thiết kế và mẫu riêng.

## 3. Sổ nguồn và mức sử dụng

| ID | Nguồn trực tiếp | Đã đọc/kiểm tra | Dùng cho và giới hạn |
|---|---|---|---|
| R01 | [IAS 7 – IFRS Foundation](https://www.ifrs.org/issued-standards/list-of-standards/ias-7-statement-of-cash-flows/) | Trang tóm tắt chính thức | Khái niệm CFO/trực tiếp/gián tiếp; không xác nhận mọi BCTC VN theo IFRS |
| R02 | [Brav et al., 2005, PDF tác giả](https://people.duke.edu/~charvey/Research/Published_Papers/P88_Payout_policy_in.pdf) | Mở PDF 45 trang, phần đầu; chưa đọc toàn văn | Nền hành vi cổ tức; không là kiểm chứng Việt Nam |
| R03 | [Alphonse & Tran, 2014, DOI 10.5539/ijef.v6n3p16](https://www.ccsenet.org/journal/index.php/ijef/article/view/32728) | Abstract đọc được; download PDF lỗi | Selection và hai quyết định; chưa kiểm tra specification |
| R04 | [Chau Anh Vu, 2023, PDF](https://ctujs.ctu.edu.vn/index.php/ctujs/article/download/583/643/3623) | Abstract, thiết kế biến và Bảng 1 trang in119 | Định nghĩa FCF khác CFO; chưa tái lập hay xác nhận robustness |
| R05 | [VNM – thông báo hỗn hợp 2024/2025](https://vsdc.vn/vi/ad1/187729) | Nội dung chính, tỷ lệ, các ngày | Ca tách component; không chứng minh thực trả/coverage toàn năm |
| R06 | [VNM – phần còn lại 2025](https://vsdc.vn/vi/ad1/197038) | Nội dung chính | Thanh toán dự kiến 2026 cho FY2025; không paid confirmation |
| R07 | [DHG – trang công bố BCTC 2025](https://dhgpharma.com.vn/vi/co-dong/10533-bao-cao-tai-chinh-kiem-toan-nam-2025-va-giai-trinh-chenh-lech) | Trang HTML ngày 21/03/2026 | Xác định tài liệu chính thức |
| R08 | [DHG – BCTC kiểm toán 2025 PDF](https://dhgpharma.com.vn/sites/default/files/2026-03/DHG-Audited-FS-2025-VN.pdf) | PDF lưu từ khảo sát trước; đọc lại ảnh trang PDF10–11, trang in8–9 | Số KQKD/cầu nối/chi cho chủ sở hữu; chưa đọc toàn bộ thuyết minh để phân bổ profit_year cho dòng chi |
| R09 | [Công báo – TT99/2025/TT-BTC](https://congbao.chinhphu.vn/van-ban/thong-tu-so-99-2025-tt-btc-46529/59637.htm) | Trang metadata và danh mục văn bản | Có hiệu lực01/01/2026; báo động version mapping khi mở rộng, chưa đối chiếu mọi phụ lục |
| R10 | [FiinTrade – BCTC](https://web.fiintrade.vn/nhom-trang-tinh-nang/phan-tich-co-ban/bao-cao-tai-chinh/) | Mô tả chức năng | Prior art sản phẩm; chưa dùng thực tế |
| R11 | [FiinTrade – Cổ tức và dự báo](https://web.fiintrade.vn/nhom-trang-tinh-nang/phan-tich-co-ban/co-tuc-va-du-bao/) | Mô tả chức năng | Không tuyên bố dashboard cổ tức là mới |
| L01 | [Khảo sát crawler trong repo](../research-crawl-methods/README.md) | Đọc hồ sơ kết quả, không chạy lại crawler | Khả thi nguồn cụ thể; không kết quả toàn thị trường |
| L02 | [Bốn sự kiện mẫu](../research-recent-data/dividend-event-examples.json) | Đọc grain, fields và review warning | Seed thử nghiệp vụ; chưa complete annual |
| L03 | [OCR kiểm tra sáu trường](../research-recent-data/ocr-core-check.json) | Đọc ledger; xem lại ảnh DHG nêu trên | Development evidence, không gold độc lập |

Đường dẫn danh mục DHG thử ban đầu `/vi/quan-he-co-dong/bao-cao-tai-chinh` không truy cập được qua web tool; đã dùng trang công bố R07 được xác nhận. Không đánh đồng lỗi một route với nguồn DHG không dùng được. Không sử dụng kết quả từ diễn đàn hoặc bản đăng lại làm căn cứ số liệu.

## 4. Điều cần nghiên cứu tiếp

Đọc toàn văn R03 để đối chiếu mẫu/công thức; kiểm tra R04 ở phần lựa chọn mẫu và kiểm định trước nếu muốn dùng mô hình. Đối chiếu văn bản kế toán và mẫu đang áp dụng trên từng report, đặc biệt khi thêm 2026. Phỏng vấn/tác vụ với người dùng để xác nhận RQ2. Rà thêm công trình mới nếu phát biểu tính mới học thuật; hiện không tuyên bố đã bao quát tài liệu đến 2026.
