# 01 — Đề xuất kết hợp và đánh giá tính khả thi

**Trạng thái cập nhật05/10/2026:** hướng kết hợp đã được tích hợp vào [SRS v3.1](../research-platform/22-srs-dac-ta-yeu-cau-phan-mem.md), CR-PCD-01/mục15, theo yêu cầu cập nhật tài liệu của người thực hiện. Tối thiểu một ca cầu nối là nghĩa vụ dự thảo; E05/E10 và ca thêm có điều kiện. Nội dung đề xuất ngày04/10 bên dưới là cơ sở nghiên cứu; các câu “chưa tích hợp/chờ change record” mô tả trạng thái lúc đó, được thay bởi SRS v3.1. Chưa có phê duyệt giảng viên hoặc kiểm thử ứng dụng đã chạy. Kế hoạch/checklist v3 là lịch triển khai duy nhất; bảng tuần/giờ trong hồ sơ nghiên cứu là phương án trước tích hợp.

## 1. Kết luận và cách hiểu tên đề tài

Tên đề tài người dùng đưa ra phù hợp cho một project hệ thống thông tin/phân tích dữ liệu: “thu thập, chuẩn hóa” là năng lực kỹ thuật; “phân tích lợi nhuận, dòng tiền kinh doanh” là nghiệp vụ; “trong mối liên hệ với cổ tức tiền mặt” là bối cảnh sử dụng. Có thể giữ nguyên tên. Trong đề cương phải ghi rõ doanh nghiệp **phi tài chính**, dữ liệu **năm**, phân tích **mô tả và đối chiếu**, cùng phạm vi mẫu.

Nên kết hợp theo câu chuyện: **doanh nghiệp tạo lợi nhuận thế nào → lợi nhuận chuyển thành dòng tiền ra sao → chính sách cổ tức công bố có diễn biến gì trong bối cảnh đó?** Câu chuyện đủ thống nhất để dùng chung kho dữ liệu và giao diện. Không suy ra rằng toàn bộ tiền cổ tức được tài trợ trực tiếp bởi CFO của đúng năm lợi nhuận.

Mức khuyến nghị là kết hợp vừa phải: giữ sáu chỉ tiêu lõi và lifecycle cổ tức, thêm cầu nối từ lợi nhuận trước thuế đến CFO ở 1–3 ca; giữ phân tích nguồn lợi nhuận theo từng khoản thuyết minh là mở rộng. Nếu triển khai tất cả thuyết minh, toàn bộ công ty mẹ–con, vốn lưu động và dự báo ngay, công sức vượt nền project hiện tại.

## 2. Nhu cầu và câu hỏi có thể trả lời

Người dùng giả định là sinh viên, người nghiên cứu và người đọc BCTC cần kiểm tra lịch sử doanh nghiệp. Chưa có khảo sát nhu cầu/sẵn sàng trả phí. Nhu cầu thực tế cần kiểm chứng bằng tác vụ, không bằng số tính năng.

| Câu hỏi | Dữ liệu | Kết quả hữu ích |
|---|---|---|
| LNST tăng nhưng CFO có tăng không? | LNST, CFO cùng scope/kỳ/version | Đồ thị và chênh lệch có điều kiện |
| Vì sao CFO khác lợi nhuận? | LNTT và các dòng điều chỉnh của BCLCTT gián tiếp | Cầu nối, nhóm đóng góp và residual |
| Cổ tức thuộc năm nào, công bố và dự kiến trả lúc nào? | Thông báo, components, các mốc ngày | Tổng theo năm lợi nhuận và timeline riêng |
| LNST/CFO giảm nhưng mức cổ tức vẫn giữ/tăng? | Chuỗi tài chính, DPS tương thích và đủ coverage | Danh sách ca cần đọc sâu, không nhãn mất an toàn |
| Nếu số liệu được sửa, kết luận có đổi? | Phiên bản, snapshot, operands | Truy nguồn/tái lập; impact engine để tốt nghiệp |

## 3. Kết hợp ba nhánh trước như thế nào?

| Nhánh | Vai trò trong đề tài | Quyết định |
|---|---|---|
| Thu thập và truy vết BCTC/cổ tức hiện hành | Nền dùng chung, bắt buộc | Tái sử dụng thiết kế, tiếp tục hoàn thiện prototype |
| N1 — Lợi nhuận chuyển thành tiền | Chiều sâu phân tích | Thêm module cầu nối theo ca, tự động cộng và kiểm tra sau duyệt |
| I2 — Dòng tiền và cổ tức | Câu hỏi ứng dụng | Phân tích lịch sử theo năm lợi nhuận; timeline là góc nhìn khác |
| N3 — Riêng và hợp nhất | Kiểm soát cách diễn giải | Luôn lưu scope; thêm báo cáo riêng cho ca cần thiết, không nhân đôi toàn bộ dataset |
| N4 — Phiên bản BCTC | Tái lập và mở rộng tốt nghiệp | Giữ versions từ đầu; semantic diff mở rộng sau |

## 4. Bằng chứng về khả thi

- Kho dự án đã có prototype discovery/tải PDF và ledger sự kiện; bằng chứng có giới hạn được dẫn trong [04](04-nguon-chuan-hoa-va-chat-luong.md). Nó giảm rủi ro khởi đầu nhưng không chứng minh pipeline hoàn chỉnh.
- Đã đọc lại ảnh BCTC DHG 2025: bảng KQKD và BCLCTT chứa đủ dữ liệu cho một cầu nối số học. [Ca cụ thể và nguồn](08-ca-thuc-te-dhg-vnm.md).
- [Thông báo VNM 02/10/2025](https://vsdc.vn/vi/ad1/187729) gộp phần cổ tức hai năm lợi nhuận. Điều này xác nhận component theo năm là yêu cầu thật, không chỉ tình huống giả lập.
- Nghiên cứu học thuật Việt Nam đã xét lợi nhuận/FCF và chính sách cổ tức; cần kế thừa phương pháp và phân biệt FCF với CFO. Xem [02](02-co-so-nghien-cuu-va-so-nguon.md).

## 5. Ma trận khả thi có điều kiện

| Mặt đánh giá | Nhận định | Điều kiện còn thiếu |
|---|---|---|
| Tính thống nhất nghiệp vụ | Tốt: chung doanh nghiệp, năm và tài liệu | Giữ ranh giới scope, thời điểm, đơn vị |
| Nguồn công khai | Có bằng chứng truy cập nguồn cụ thể | Chưa đủ lịch sử 9 firm-year và cổ tức liên quan |
| Trích số tự động | Có thể làm bán tự động | OCR/layout phải đo trên holdout, review có công sức |
| Cầu nối CFO | Một ca thật có đủ dòng và đối chiếu được | Cần thêm mẫu khác phương pháp/template; không hứa parser tổng quát |
| Thống kê quan hệ | Đủ cho case/mô tả mẫu nhỏ | Không đủ để khẳng định nhân quả hoặc quy luật toàn thị trường |
| Project 13 tuần một người | Hợp lý với scope có gate | Ước lượng phải cập nhật bằng giờ làm thực tế |
| Tính mới | Có hướng đóng góp IT đo được | Chưa chứng minh mới học thuật hoặc khác biệt thương mại độc quyền |

## 6. Phạm vi đề nghị

**P0 – baseline:** 3 doanh nghiệp phi tài chính × 2023–2025, BCTC năm kiểm toán; 6 facts/BCTC; sự kiện cổ tức tiền mặt; review, provenance, dashboard, snapshot. Giữ nghĩa vụ discovery tự động theo SRS v3.0. Số reports có thể vượt 9 nếu cần riêng/hợp nhất hoặc version; không gọi chúng là quan sát độc lập mới.

**P1 – thử kết hợp:** tối thiểu một ca cầu nối kiểm chứng, mục tiêu 1–3 ca nếu quỹ giờ cho phép. Các ca là doanh nghiệp–năm thuộc mẫu; một PDF có cột so sánh không tự thay thế BCTC năm trước khi cần nghiên cứu thông tin tại thời điểm cũ. P1 chưa là yêu cầu nghiệm thu chính thức trước change record.

**P2 – sau gate:** mở 5–8 doanh nghiệp; phân tích riêng công ty mẹ và dòng tiền đã chi cho chủ sở hữu ở ca đủ chứng cứ; phân rã biến động lợi nhuận nếu dữ liệu thuyết minh đủ. Tránh tăng số doanh nghiệp đồng thời với tất cả chiều sâu.

**Ngoài phạm vi:** dự báo giá, khuyến nghị mua bán, cam kết cổ tức bền vững, chấm điểm gian lận, mô hình ML cắt giảm, crawl toàn thị trường và RAG hỏi đáp chung. Những phần này không cần thiết để chứng minh đề tài tốt.

## 7. Tính mới nên phát biểu thế nào?

Đóng góp đề xuất: (1) hợp đồng dữ liệu giữ kỳ/scope/version; (2) ghép sự kiện đa năm và lifecycle vào firm-year có kiểm soát coverage; (3) cầu nối có truy nguồn, phép kiểm tra tổng và phần chưa giải thích; (4) đo tác động của chuẩn hóa/review lên kết quả và thời gian làm tác vụ.

Không phát biểu “lần đầu kết hợp lợi nhuận và cổ tức ở Việt Nam” hoặc “CFO quyết định cổ tức”. [FiinTrade đã mô tả BCTC chuẩn hóa](https://web.fiintrade.vn/nhom-trang-tinh-nang/phan-tich-co-ban/bao-cao-tai-chinh/) và [cổ tức/lịch/dự báo](https://web.fiintrade.vn/nhom-trang-tinh-nang/phan-tich-co-ban/co-tuc-va-du-bao/). Chưa thử sản phẩm nên không khẳng định họ thiếu truy nguồn hay cầu nối.

## 8. Điều kiện ra quyết định

Tiếp tục khi thu được tài liệu mục tiêu, một cầu nối thật có source và residual giải thích được, phép ghép năm cổ tức hoạt động, và công sức dự phóng nằm trong quỹ còn lại. Nếu cầu nối quá tốn công, giữ phân tích LNST–CFO–DPS hiện có và ghi giới hạn. Nếu discovery cổ tức không đạt, đó là thiếu baseline phải xử lý/change record, không được tự đổi thành đề tài chỉ BCTC mà vẫn giữ tuyên bố hoàn thành cổ tức.
