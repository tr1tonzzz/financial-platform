# Ghi nhớ khi chuẩn bị trao đổi với giảng viên

Cập nhật ngày 09/10/2026 theo góp ý người thực hiện sau buổi trao đổi với thầy.
Áp dụng khi chuẩn bị báo cáo, slide, nội dung demo và buổi trao đổi tiếp theo của project.

- Không cần phân tích lại tổng quan đề tài. Đi vào phân rã các use case (UC) nhỏ, cụ thể.
- Slide ngắn, đúng trọng tâm, chỉ ghi thông tin cần đọc nhất. Tránh lặp ý giữa các mục và các slide.
- Tập trung vào code và các thực nghiệm đã thực hiện được thay vì lý thuyết suông. Phân biệt rõ phần đã chạy với phần mới đề xuất.
- Nêu ý tưởng thực hiện để trao đổi với thầy.

Khi trình bày một UC, ưu tiên làm rõ đầu vào, các bước xử lý, đầu ra và minh chứng từ code/thực nghiệm. Đây là cách triển khai góp ý về phân rã UC, không phải yêu cầu chức năng mới hay thay đổi phạm vi SRS.

## Góp ý giảng viên được người thực hiện bổ sung ngày 11/10/2026

Ngày 11/10 là ngày ghi nhận trong project; chưa xác định ngày chính xác của buổi trình bày.

- Kiểm chứng PaddleOCR so với Tesseract trên tài liệu của project. Nhận xét Paddle đọc tốt hơn là giả thuyết cần thực nghiệm, chưa là kết luận. Người thực hiện sau đó đã chốt chuyển OCR chính sang PaddleOCR ngày 11/10/2026; tiếp tục triển khai lựa chọn này, không xin lại quyền chuyển. Tesseract giữ làm đối chứng; không đổi tên minh chứng cũ thành Paddle.
- Giải thích rõ lý do giới hạn phân tích ở cổ tức tiền mặt và tác động của việc loại cổ tức bằng cổ phiếu. Nghiên cứu ảnh hưởng của biến động số lượng cổ phiếu tới DPS/EPS và tính so sánh; không mặc định có thể bỏ toàn bộ sự kiện cổ phiếu.
- Ưu tiên nghiên cứu sâu chức năng hỗ trợ quyết định đầu tư cổ tức: người dùng cần quyết định gì, hệ thống cung cấp phân tích nào, cần dữ liệu gì, và đo chất lượng quyết định ra sao. Tự động tổng hợp dữ liệu là nền tảng, chưa đủ để chứng minh giá trị đầu tư.
- Dùng thuật ngữ nghiệp vụ chính xác: phân biệt tra cứu nguồn, truy xuất chứng từ nguồn, đối chiếu số liệu và tra soát sai lệch. Không thay máy móc mọi cụm “mở nguồn” thành “tra soát”.
- Đẩy nhanh tiến độ bằng các UC nhỏ có đầu ra chạy được và minh chứng; ưu tiên chức năng có giá trị sử dụng, hạn chế mở rộng mẫu hoặc soạn lại tổng quan.
- Luôn phân biệt dữ kiện đã kiểm chứng, giả thuyết nghiên cứu, chức năng đề xuất và chức năng đã triển khai. Đề xuất chức năng mới cần ghi tác động tới SRS, dữ liệu và công sức trước khi tích hợp.

Kế hoạch nghiên cứu và tiêu chí hoàn thành: [phản hồi góp ý và kế hoạch nghiên cứu 11/10/2026](docs/research-platform/26-ke-hoach-nghien-cuu-sau-gop-y-giang-vien.md).

## Quyết định chức năng của người thực hiện ngày 11/10/2026

- Người dùng chính là người theo dõi tài chính doanh nghiệp và người đầu tư; người vận hành dữ liệu là vai trò hỗ trợ.
- Loại chức năng “Tìm và khám phá trường hợp cần chú ý” (A04), bộ sàng lọc/criteria/pass-fail-unknown; không đưa trở lại dưới tên cảnh báo. Danh sách theo dõi và nhóm so sánh là doanh nghiệp do người dùng tự chọn.
- Tổ chức yêu cầu theo UC lớn → UC/chức năng nhỏ; biểu đồ/tỷ số/phân rã nằm trong UC phân tích tương ứng. Thu/trích/chuẩn hóa/duyệt là nền dữ liệu.
- Danh mục sản phẩm: [yêu cầu chức năng v2.0](docs/research-platform/27-yeu-cau-chuc-nang-va-vi-du.md); quyết định phạm vi: [SRS v3.3/mục18](docs/research-platform/22-srs-dac-ta-yeu-cau-phan-mem.md). Ý tưởng danh mục/định giá chưa tự thuộc MVP.
- Ưu tiên thực hiện mới nhất: UC-F01/02/03/05 trước, UC-F04 sau; đây là số UC trong danh mục sản phẩm, không đổi số BUC của SRS. Làm theo lát cắt có đầu ra sử dụng được, không đợi hoàn thành toàn bộ chức năng nhỏ của mỗi nhóm. [Kế hoạch và tiến độ có bằng chứng](docs/research-platform/28-ke-hoach-thuc-hien-uc-1-2-3-5.md), [dữ liệu cần thu](docs/research-platform/29-du-lieu-can-thu-thap-cho-uc-1-2-3-5.md).
- Phạm vi chính đã chốt: HPG, VNM, FPT, BCTC năm 2023–2025, ưu tiên hợp nhất; 9 báo cáo đích/54 ô lõi. Stack web giữ React/TypeScript + FastAPI/Python 3.12 + PostgreSQL; SQLAlchemy/Alembic cho persistence, pandas cho phân tích, OCR chính chuyển PaddleOCR/PaddlePaddle CPU; khóa package/model sau smoke test. [Quyết định](docs/research-platform/31-chot-pham-vi-va-stack-paddleocr.md), [manifest](config/pilot-scope.json). Chốt công nghệ không đồng nghĩa đã cài/chạy hoặc kiểm chứng chất lượng.
- Hạn mới người thực hiện cung cấp: còn 10 tuần; 4–5 tuần tới phải thể hiện cơ bản UC-F01/02/03. [Kế hoạch 10 tuần v6](docs/research-platform/32-ke-hoach-10-tuan-tiep-theo.md), [checklist HTML](docs/research-platform/checklist-10-tuan-v4.html) thay kế hoạch 13 tuần cho công việc tiếp theo. Tuần 1 tính từ mốc hiện tại, ngày bắt đầu chọn trong HTML; quỹ giờ thực chưa xác nhận. UC-5 tuần 6–8; UC-4 tuần 9 chỉ sau gate core ổn định.
- Điều chỉnh tiếp: kế hoạch hiện **v6** (giữ tên file HTML/JSON v4 để URL tiếp tục hoạt động). Tuần 1 gộp thay Paddle vào pipeline đã thử và triển khai UC-1 cơ bản, không dành tuần riêng kiểm lại công cụ. Tuần 2 củng cố UC-1/mở nhiều kỳ. Mỗi tuần có gợi ý Word/slide/demo theo kết quả thực; không tự tạo file Word/slide hoặc báo cáo đã chạy. [Chi tiết tuần này](docs/research-platform/33-ke-hoach-chi-tiet-tuan-01.md).
- Căn cứ Báo cáo 2 do người thực hiện cung cấp: giữ sáu metrics nền; thực nghiệm cũ chỉ là LNST/CFO/tiền chi cổ tức × hai cột kỳ, không phải đã thử đủ sáu metrics nền hoặc Paddle. [Định nghĩa và hợp đồng dữ liệu](docs/research-platform/35-dac-ta-metrics-tu-bao-cao-02.md), [tuần 2 chi tiết](docs/research-platform/34-ke-hoach-chi-tiet-tuan-02.md). Tuần 2 ưu tiên ba năm một công ty (18 targets), chưa bắt buộc đủ chín PDF; targets khác số đã duyệt. CAPEX/cầu nối/khoản phân phối thu theo ca ở giai đoạn sau.

- Quyết định tiếp ngày 11/10/2026: giữ web React + FastAPI + PostgreSQL thay pilot Streamlit/SQLite; kế hoạch hiện v6, vẫn tên HTML/JSON v4. Tuần 1/2 dự toán 24/22 giờ, tổng 195 giờ; chưa là quỹ giờ xác nhận. Có frontend/API/schema/migration, không chỉ script. Khóa lưu v6 riêng, giữ bản v5/v4 gốc và nhật ký/giờ khi chuyển; tick thay đổi cần kiểm lại.
