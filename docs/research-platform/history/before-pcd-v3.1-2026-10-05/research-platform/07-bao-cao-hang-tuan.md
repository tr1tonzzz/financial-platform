# Báo cáo tiến độ hai tuần một lần

**Đồng bộ kế hoạch v2 ngày 04/10/2026:** giữ nhịp2/4/6/8/10/12 và tổng kết13. Nội dung từng đợt lấy từ [checklist v2](checklist-13-tuan.html); cuối tuần11–12 phải có restore, benchmark, local safety và trạng thái yêu cầu/TC có bằng chứng. Đợt9–10 kiểm replay toàn bộ kết quả snapshot. Dùng [mẫu hồ sơ](23-bat-dau-va-minh-chung-thuc-hien.md), không ghi kế hoạch thành pass ứng dụng.

Cập nhật 03/10/2026 theo nhịp người thực hiện yêu cầu. Checklist học/làm vẫn theo từng tuần; báo cáo chính thức Word và slide gộp **hai tuần**. Sáu đợt ở cuối tuần 2, 4, 6, 8, 10, 12; tuần 13 là tổng kết/nộp cuối. Ngày thực tế theo ngày bắt đầu/hạn học kỳ, chưa là lịch gặp đã được thầy xác nhận.

## 1 Nhật ký tuần và bộ báo cáo

Mỗi tuần dành khoảng 30 phút ghi task, file/run/commit, giờ học/làm, lỗi và điều tự giải thích được. Cuối mỗi cặp tuần dành khoảng hai giờ tổng hợp Word, slide và luyện nói; bình quân phần nhật ký/báo cáo khoảng 1,5 giờ/tuần trong ngân sách 11 giờ. Tuần báo cáo có thể dành nhiều giờ hơn, bù từ tuần trước.

Word khoảng **3–5 trang** để giữ chi tiết; slide khoảng **6–8 trang**, nói **8–10 phút** gồm demo ngắn, sau đó trao đổi. Báo cáo cuối theo mẫu trường, không giới hạn như báo cáo tiến độ. Chỉ ghi việc đã chạy/đã hiểu; phản hồi thầy chỉ điền sau buổi gặp thật.

## 2 Khung Word mỗi đợt

1. Thông tin và mục tiêu hai tuần: đề tài, đợt, khoảng ngày; bảng dự kiến/thực đạt và trạng thái.
2. Kết quả có minh chứng: file/run/commit, số thực và mẫu số; phân biệt tự tìm, nhập hỗ trợ, candidate và reviewed.
3. Một phần kỹ thuật trọng tâm: input → xử lý → output, lý do chọn phương pháp, lỗi gặp và kiểm thử. Dùng sơ đồ/bảng có ích, không chụp hàng trang code.
4. Điều đã hiểu: một ví dụ tài chính tự tính/giải thích và một hàm/truy vấn tự viết/sửa; AI hỗ trợ và cách đã kiểm tra.
5. Giới hạn và kế hoạch hai tuần tới: nguyên nhân/ảnh hưởng/biện pháp; tối đa ba đầu ra có tiêu chí xong và điểm cần thầy góp ý.

Gợi ý bố trí: trang đầu mục tiêu/tiến độ; một trang dữ liệu và kỹ thuật; một trang kết quả/kiểm thử và kiến thức; thêm giới hạn/kế hoạch nếu cần. Không kéo dài đủ số trang bằng ảnh.

Ví dụ khi kết quả thực đúng: “Parser tìm được 5/6 trường trên file X; một trường thiếu, chưa đối chiếu độc lập.” Chấm holdout phải báo bộ mẫu, quy tắc và số đúng/sai/thiếu; mẫu phát triển không là accuracy nghiệm thu.

## 3 Khung bảy slide và cách nói

| Slide | Nội dung | Cách nói và minh chứng |
|---|---|---|
| 1 | Mục tiêu và kết quả chính hai tuần | 30–45 giây, nói điều mới chạy được |
| 2 | Tiến độ so kế hoạch | 45–60 giây; task/artifact/trạng thái, không đặt % tùy ý |
| 3 | Dữ liệu/chất lượng hoặc case | Khoảng 60 giây; bảng nhỏ có mẫu số hoặc một biểu đồ |
| 4 | Kỹ thuật trọng tâm | Khoảng 90 giây; input–xử lý–output, lựa chọn và lỗi |
| 5 | Demo/kiểm thử | Khoảng 120 giây; một thành công và một lỗi được xử lý |
| 6 | Kiến thức đã hiểu và giới hạn | 60–90 giây; ví dụ tự giải thích và điều chưa chắc |
| 7 | Hai tuần tới và điểm trao đổi | 45–60 giây; ba đầu ra và câu hỏi cụ thể |

Một slide một ý, không copy đoạn Word lên slide. Speaker notes ghi ý chính, câu mở đầu và nguồn. Trước buổi gặp chạy lại demo, đồng bộ số Word/slide/log và thử nói không nhìn notes. Chuẩn bị fallback cùng snapshot khi app/mạng lỗi.

## 4 Nội dung từng đợt và cách đặt file

[Gợi ý bảy mốc](goi-y-noi-dung-7-dot-bao-cao.md): nguồn → pilot/scope → ứng dụng/sự kiện → đánh giá → phân tích/cập nhật → hoàn thiện → nộp cuối. Đây là mục tiêu trình bày, chưa là các đợt đã hoàn thành.

[Mẫu điền hai tuần](mau-bao-cao-hai-tuan.md) làm dàn ý Word; [nhật ký tuần](mau-bao-cao-tuan.md) giữ ghi chép nội bộ.

Khi có báo cáo thật, đặt trong reports/dot-01-tuan-01-02/ với bao-cao.docx, tien-do.pptx và notes.md; các đợt sau tương tự. Tuần cuối dùng reports/tong-ket-tuan-13/. Không tạo bảy bộ tiến độ giả.

## 5 Chất lượng dữ liệu phải theo dõi

BCTC/notices mong đợi → tự tìm/tải/trích/duyệt; sáu targets/report; components theo năm; coverage/basis; nhập hỗ trợ, lỗi nguồn và phút sửa. Phân biệt DPS công bố, lịch thanh toán và bằng chứng thực trả. Missing không chuyển thành 0.

Sau gặp ghi phản hồi/decision log thật rồi cập nhật backlog. Project chưa có predictor thì không đưa dự đoán vào kết quả. Tên, số đo và scope phải cùng phiên bản giữa SRS, Word, slide và ứng dụng.
