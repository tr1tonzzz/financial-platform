# 09 — Đề cương trao đổi với giảng viên

Ngày 04/10/2026 · Bản đề xuất để thảo luận, chưa ghi nhận phê duyệt.

## Tên đề tài

**Xây dựng hệ thống thu thập, chuẩn hóa và phân tích lợi nhuận, dòng tiền kinh doanh trong mối liên hệ với cổ tức tiền mặt của doanh nghiệp niêm yết Việt Nam.**

Giới hạn trong đề cương: doanh nghiệp phi tài chính, BCTC năm kiểm toán 2023–2025 và thông báo cổ tức liên quan tới mốc khảo sát; phân tích mô tả có truy nguồn. Có thể thêm “dữ liệu” trước “lợi nhuận” để tên nhấn mạnh hướng CNTT, nhưng không cần đổi bản chất đề tài.

## Vấn đề đặt ra

Lợi nhuận kế toán không đồng nhất với dòng tiền kinh doanh. Dữ liệu để đối chiếu phân tán trong BCTC và thông báo quyền, có nhiều định dạng, đơn vị, phạm vi và phiên bản. Cổ tức công bố một năm có thể thuộc năm lợi nhuận khác hoặc nhiều năm cùng lúc. Nếu chỉ nối mã cổ phiếu–năm và vẽ biểu đồ, kết quả có thể sai ý nghĩa dù phép tính đúng.

## Mục tiêu

Xây dựng pipeline tự thu thập tài liệu mục tiêu; chuẩn hóa các chỉ tiêu và sự kiện có provenance; kiểm tra/duyệt sai lệch; phân tích biến động LNST–CFO và cầu nối CFO ở các ca đủ dữ liệu; đối chiếu cổ tức theo đúng năm lợi nhuận và timeline; xuất kết quả tái lập.

## Phạm vi và phương pháp

Pilot 3 doanh nghiệp×3 năm; sau gate có thể mở5–8 doanh nghiệp. Sáu chỉ tiêu nền gồm LNST, CFO, tiền/tương đương tiền, tài sản, nợ phải trả, vốn chủ sở hữu. Extension đề xuất là1–3 ca cầu nối gián tiếp, nguồn theo từng dòng và residual. Nghiên cứu gồm rà tài liệu, khảo sát nguồn, xây dựng hệ thống, đánh giá gold/holdout và thử tác vụ người dùng nếu tiếp cận được.

Lợi ích là giả thuyết cần đo: giảm lỗi ghép và hỗ trợ giải thích/kiểm chứng. Không xem số lượng doanh nghiệp nhỏ là đủ chứng minh quy luật toàn thị trường. Không đưa dự báo ML hoặc khuyến nghị đầu tư thành nghĩa vụ project.

## Sản phẩm bàn giao

- Mã nguồn collector, normalizer, validator, event resolver, analysis và giao diện.
- Bộ dữ liệu có manifest, nguồn/phiên bản/coverage, gold và nhật ký đánh giá.
- Dashboard theo doanh nghiệp, cầu nối CFO, lịch sử cổ tức và mở nguồn.
- Báo cáo ba ca theo baseline, trong đó tích hợp cầu nối cho ca qua gate; tài liệu SRS/thiết kế/kế hoạch/kiểm thử cập nhật theo CR được chấp nhận.
- Export/snapshot và hướng dẫn tái lập kết quả.

## Đóng góp và đánh giá

Đóng góp CNTT nằm ở pipeline kiểm chứng được và ngữ nghĩa ghép dữ liệu, không chỉ crawler/dashboard. Đo joint correctness, discovery coverage theo ledger, độ đúng component/cầu nối, provenance, thời gian review và tác vụ. Giữ riêng tự động và hỗ trợ thủ công. Kết quả đọc nguồn DHG/VNM trong [08](08-ca-thuc-te-dhg-vnm.md) là minh chứng khả thi ban đầu, chưa là nghiệm thu app.

## Các điểm cần thống nhất trong buổi trao đổi

| Điểm cần chốt | Đề xuất đem trao đổi |
|---|---|
| Rubric CNTT và yêu cầu AI | Đánh giá pipeline/chất lượng/truy nguồn; AI không mặc định bắt buộc |
| Phạm vi dữ liệu | Phi tài chính, năm 2023–2025, pilot 3; mở theo công sức |
| Chiều sâu tài chính | Cầu nối và case mô tả, không cam kết nhân quả/dự báo |
| Vai trò extension | Nhận CR cho1 ca trước, tăng tới3 ca khi đủ giờ |
| Mức tự động hóa | Tự discovery/tải là lõi; OCR có review, đo rõ nhập tay |
| Phương pháp đánh giá | Gold/holdout và tác vụ người dùng; khai báo nếu tự đánh giá |
| Hướng tốt nghiệp | Chọn một nhánh phiên bản/impact hoặc parser sâu sau project |

## Nội dung trình bày ngắn

Em đề xuất kết hợp theo một chuỗi câu hỏi: doanh nghiệp có lãi như thế nào, phần lợi nhuận đó chuyển thành tiền ra sao, và cổ tức tiền mặt công bố diễn biến thế nào trong bối cảnh đó. Hệ thống sẽ tự thu thập tài liệu, giữ nguồn và phiên bản, chuẩn hóa đúng kỳ/phạm vi, rồi phân tích có truy vết. Phần mở rộng là cầu nối CFO cho một số ca thay vì chỉ hiển thị tỷ số. Em giới hạn pilot 3 doanh nghiệp trong3 năm, mở rộng sau khi đo công sức. Kết quả dự kiến là một hệ thống và bộ dữ liệu có chất lượng đo được; chưa đặt mục tiêu dự báo cổ tức hay giá cổ phiếu.
