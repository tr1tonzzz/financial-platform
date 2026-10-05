# Bản chốt ý tưởng đề tài

> **Hồ sơ phương án BCTC–cổ tức trước khi mở rộng nền tảng, 03/10/2026.** Giữ nội dung để tham khảo nhánh A2/lịch sử. Định hướng triển khai hiện hành: [bộ tài liệu mới](../research-platform/02-de-tai-va-srs.md). Yêu cầu của phương án này không đồng thời là nghĩa vụ MVP mới.


Ngày: **03/10/2026**. Kết luận đề xuất hiện hành, đồng nhất với [SRS v2.0](../initial-docs/SRS-FDP-01.md). Phần mở rộng ở [trang so sánh](README.md) không tự trở thành yêu cầu nghiệm thu.

## 1. Tên đề tài đang chốt

**Hệ thống thu thập, chuẩn hóa và phân tích dữ liệu BCTC–cổ tức tiền mặt Việt Nam để đánh giá khả năng duy trì cổ tức và nghiên cứu cảnh báo sớm rủi ro cắt giảm.**

Tên ngắn dùng khi trao đổi: **Nền tảng dữ liệu BCTC–cổ tức Việt Nam có truy vết**. Đây là tên gọi tắt, không phải một đề tài thứ hai.

## 2. Ý tưởng trong một đoạn

Tự xây dựng dữ liệu từ BCTC đã kiểm toán và công bố cổ tức của doanh nghiệp phi tài chính Việt Nam; giữ nguồn gốc, kỳ, đơn vị, phạm vi báo cáo và ngày thông tin khả dụng. Trên dữ liệu đã kiểm tra, nghiên cứu lợi nhuận, dòng tiền kinh doanh, tiền mặt và áp lực nợ liên hệ thế nào với việc duy trì hoặc giảm cổ tức tiền mặt. Hệ thống trình bày xu hướng, các trường hợp ngoại lệ và tín hiệu cảnh báo theo quy tắc, kèm số liệu và tài liệu gốc. Mô hình dự báo chỉ bổ sung khi dữ liệu đáp ứng điều kiện đánh giá.

## 3. Bài toán người dùng

Người theo dõi doanh nghiệp thấy công ty có lãi và công bố cổ tức, nhưng cần biết nguồn tiền có hỗ trợ mức chi trả hay không. Câu trả lời yêu cầu nối hai loại công bố, kiểm tra ý nghĩa số liệu và đọc đúng thời điểm. Một thông báo lịch thanh toán chưa chứng minh khoản tiền đã trả; tổng nợ phải trả chưa phải số nợ vay.

Luồng sản phẩm: chọn công ty → xem BCTC và sự kiện cổ tức cùng nguồn → đọc chỉ số và mức đầy đủ → xem tín hiệu cùng lý do → mở báo cáo gốc để kiểm chứng. Điểm cảnh báo là tín hiệu nghiên cứu có giải thích; chỉ có xác suất khi một mô hình đã được đánh giá và hiệu chỉnh phù hợp.

## 4. Ba đóng góp cần chứng minh

| Đóng góp | Bằng chứng cần nộp |
|---|---|
| Dataset BCTC–cổ tức tự thu thập, có truy vết | Manifest, từ điển, bản gốc/hash, độ phủ, quy tắc nối sự kiện và phiên bản |
| Pipeline chuẩn hóa có kiểm định | Gold đối chiếu độc lập; độ đúng trước/sau review, thời gian xử lý, lỗi và khả năng chạy lại |
| Phân tích tài chính có thể kiểm chứng | Thống kê trên mẫu hợp lệ, ít nhất ba case có nguồn, quy tắc cảnh báo và đánh giá baseline nếu nhãn đủ |

Đóng góp khác biệt nằm ở tổ hợp nguồn Việt Nam, cách ghép sự kiện theo thời điểm và đánh giá minh bạch. Chưa chứng minh đây là phương pháp mới trên thế giới hoặc nghiên cứu đầu tiên tại Việt Nam. [Sổ nguồn](02-tai-lieu-va-co-so-lua-chon.md) đã ghi các nghiên cứu liên quan tồn tại.

## 5. Câu hỏi nghiên cứu giữ nguyên

- **RQ1:** Có thể thu thập và chuẩn hóa sáu chỉ tiêu lõi, nối cổ tức với nguồn, đạt độ đúng và độ phủ đo được không?
- **RQ2:** Nhóm giảm/ngừng và nhóm duy trì cổ tức khác nhau ra sao về lợi nhuận, dòng tiền và nợ trên mẫu có nhãn hợp lệ?
- **RQ3:** Tín hiệu theo quy tắc, và mô hình đơn giản nếu đủ dữ liệu, có giá trị ngoài mẫu so với baseline hiện hành không?

Không chứng minh nhân quả bằng tương quan. Nếu không đủ nhãn, ghi rõ RQ3 chưa đánh giá được; nếu mô hình yếu, báo cáo kết quả yếu thay vì đổi nhãn hoặc chọn mẫu để làm đẹp kết quả.

## 6. Phạm vi và ưu tiên

Giữ kế hoạch 13 tuần, 10–12 giờ/tuần. Pilot 10 công ty; MVP tối thiểu 30, mục tiêu 60–80 có điều kiện. BCTC năm kiểm toán 2020–2024; thêm 2025 khi đủ tài liệu và cửa sổ kết quả. Sáu chỉ tiêu: LNST toàn doanh nghiệp, CFO, tiền và tương đương tiền, tổng tài sản, nợ phải trả, vốn chủ sở hữu. Ưu tiên hợp nhất, phân biệt báo cáo riêng.

**Bắt buộc:** pipeline, dữ liệu, vòng đời cổ tức, truy vết, kiểm định chất lượng, phân tích, quy tắc cảnh báo, API/web tối thiểu và xuất dataset tái lập.

**Ưu tiên nghiên cứu bổ sung:** N1 giải thích lợi nhuận–dòng tiền trong các case, dùng thêm dòng điều chỉnh CFO/vốn lưu động khi có. Không nâng các chỉ tiêu bổ sung thành yêu cầu toàn mẫu.

**Có điều kiện/sau MVP:** ML, mô phỏng N2, phân tích công ty mẹ N3, benchmark phiên bản sâu N4 và trợ lý tra cứu. Khả năng lưu phiên bản cơ bản vẫn thuộc lõi; N4 bổ sung đánh giá ảnh hưởng phiên bản chứ không loại bỏ yêu cầu này.

## 7. Ý tưởng đã ổn và đầy đủ chưa?

**Ổn về cấu trúc đề tài và đủ phạm vi để triển khai. Chưa được xác nhận về dữ liệu và kết quả.** Khoảng trống hiện tại là hoàn thành pilot, lựa chọn nguồn tải ổn định, chốt định nghĩa cổ tức, đo công sức làm sạch và kiểm tra số mẫu hợp lệ. Thêm tính năng trước khi giải quyết các điểm này sẽ không làm đề tài thuyết phục hơn.

Kết luận thực hành: giữ một bài toán chính; làm bằng chứng tốt; dùng N1 để đào sâu ba case nếu dữ liệu cho phép. Chỉ cân nhắc N4 làm đề tài thay thế khi kết quả pilot cho thấy nhãn cổ tức không thể bảo vệ.

## 8. Đoạn giới thiệu dùng trao đổi với giảng viên

> Em dự kiến xây dựng hệ thống tự thu thập và chuẩn hóa BCTC cùng công bố cổ tức tiền mặt của doanh nghiệp Việt Nam. Mỗi số liệu giữ nguồn và thời điểm để kiểm chứng. Từ bộ dữ liệu đó, em phân tích mối liên hệ giữa lợi nhuận, dòng tiền và mức duy trì cổ tức, xây dựng tín hiệu cảnh báo có giải thích và đánh giá chất lượng dữ liệu cùng kết quả phân tích. Em ưu tiên hoàn thành pipeline và các case study; dự báo bằng mô hình chỉ thực hiện nếu pilot cho thấy đủ mẫu và nhãn.

Đây là đoạn đề xuất để người dùng sử dụng, chưa được gửi cho giảng viên và không hàm ý giảng viên đã phê duyệt phạm vi.
