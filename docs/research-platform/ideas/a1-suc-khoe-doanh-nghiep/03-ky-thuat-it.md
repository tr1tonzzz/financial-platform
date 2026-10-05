# Kỹ thuật IT cho phân tích sức khỏe tài chính doanh nghiệp

> **Phương án A1 trước, không còn là scope triển khai.** Kiến thức/pipeline có thể tái sử dụng cho [hướng A2 hiện hành](../../README.md); mức 10 doanh nghiệp/chín chỉ tiêu ở đây là đề xuất cũ.

Python xử lý file/HTTP/JSON; pdfplumber với PDF text, Poppler và OCR cho scan; pandas chuẩn hóa; SQLite lưu documents, facts, reviews, runs; Streamlit làm giao diện đọc và duyệt. Module chỉ số độc lập giao diện, dùng Decimal hoặc số nguyên cho tiền và phân biệt dữ liệu gốc/dẫn xuất. Khóa hash và transaction giúp chạy lại không nhân bản. Kiểm thử sai đơn vị, âm ngoặc, thiếu mẫu số, nhầm kỳ và chỉnh sửa có lịch sử. Bài tập: viết một hàm chuẩn hóa số, ba ca kiểm thử và một truy vấn tìm giá trị chưa duyệt.

Đầu ra cần giữ: source code module, dữ liệu đầu vào có nguồn, cấu hình, test phù hợp, log chạy và hạn chế. Đọc được dữ liệu hoặc gọi được thư viện không thay thế đánh giá đúng/sai trên bộ mẫu.

Nguồn và hồ sơ: [Khảo sát dữ liệu thật](../../../research-recent-data/README.md); [SEC hướng dẫn BCTC](https://www.sec.gov/about/reports-publications/beginners-guide-financial-statements); [pandas](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html).
