# Nhật ký lỗi và giới hạn nghiên cứu

> **Trạng thái 03/10/2026 — hồ sơ thử nghiệm thu thập.** Project hiện hành tập trung thu thập, kiểm định và phân tích lợi nhuận–dòng tiền–cổ tức tiền mặt. Xem [SRS hiện hành](../research-platform/02-de-tai-va-srs.md) và [phương pháp thống nhất](../research-platform/11-phuong-phap-thu-thap-va-xu-ly.md). Các ngưỡng cảnh báo, dự báo, scope và lịch cũ bên dưới chỉ để tham khảo; không là yêu cầu MVP hiện hành.

## Lỗi có bằng chứng đã sửa

**Nhầm bán niên 2025 thành năm 2025.** Classifier ban đầu nhìn token 2025, chọn file VHC “first half 2025”; khi mở trang hai HPG còn chọn nhầm báo cáo kết thúc 30.06.2025. Đã sửa thứ tự marker quý/bán niên/ngày kết thúc trước năm; thêm regression tests. Hai run cuối trong thư mục `verified` đã chọn đúng tám link mục tiêu. Các file ngoài mục tiêu ở thư mục cha giữ làm raw phát triển, không cộng coverage cuối.

**Loại nhầm bundle chứa BCTC.** Filename HPG H1/2026 có “và giải trình” nhưng anchor là BCTC hợp nhất soát xét; dùng filename alone sẽ loại mất BCTC thật. Đã ưu tiên tiêu đề anchor để phân biệt bundle với thư giải trình. Vẫn cần kiểm tra nội dung và phạm vi trang trước trích số.

**Phân trang sắp chuỗi và trang gốc khác nhau.** DHG page=0, HPG/HPA page đầu=1; trang 13 không được đứng trước trang 2 theo thứ tự chuỗi. Đã lấy chỉ số nguyên, chỉ theo link cùng path có số lớn hơn trang đang đọc và giới hạn page budget.

## Chưa giải quyết hoặc chưa thực nghiệm

| Vấn đề | Trạng thái / cách xử lý dự kiến |
|---|---|
| Robots host file Hòa Phát trả 403 | Không xác định policy; research probe có cờ/ghi log; mặc định skip; cần xác minh trước lịch chạy thường xuyên |
| Classifier chưa bao phủ mọi tên báo cáo | Candidate + kiểm tra header; cần holdout nguồn/layout/kỳ khác |
| HPA FY2025 anchor chưa nêu assurance | Trang bìa đã xác nhận kiểm toán; chưa có metadata extraction tự động từ scan |
| Publication date VHC không có trong context chọn | Giữ null; Last-Modified là trường HTTP khác |
| pypdf text 12 trang đầu đều ít/không text | Cần OCR; chưa chứng minh toàn tài liệu scan hoặc chín trường đều lấy đúng |
| HNX Python TLS từng lỗi CA | Curl Schannel từng hoạt động với TLS xác thực; adapter mới chưa tích hợp; không hạ kiểm tra certificate |
| Vinamilk chọn năm động, HOSE, RSS/sitemap | Chưa chạy end-to-end trong prototype mới; chỉ là hướng kiểm tra tiếp |
| Parser robots không đầy đủ RFC | Ghi rõ giới hạn; dùng parser chuẩn/test mở rộng khi thành collector |
| Redirect/auth/CAPTCHA | Không xử lý/vượt; ghi lỗi, chọn nguồn thay thế hoặc nhập có provenance |
| Retry-After dạng HTTP-date, retry network timeout | Chưa có đầy đủ parser/retry; thêm nếu pilot cần |
| Crash/concurrency/history JSON | Không là service bền vững; chuyển SQLite/transaction/resume trong MVP |
| Bản sửa đổi BCTC thật | Chưa xảy ra trong cửa sổ quan sát; chỉ có test offline nội dung thay đổi |

Không dùng “tám link đúng sau sửa” để tuyên bố classifier đạt accuracy 100%: đây là tập phát triển. Không có dữ liệu thị trường đầy đủ hoặc kỳ chưa công bố trong lần thử này. Mọi phần chưa làm được chuyển thành task đo/triển khai cụ thể, không đổi thành kết quả đã đạt.
