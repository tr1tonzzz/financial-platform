# I5 — Nghiên cứu trợ lý tra cứu tài chính có dẫn nguồn

Ngày: 03/10/2026. P2, sau MVP. Chưa triển khai hoặc thử LLM.

## 1. Vấn đề và đề xuất

Người đọc muốn hỏi “CFO năm 2024 ở đâu?”, “Vì sao có cảnh báo?” hoặc “Đợt này thuộc năm lợi nhuận nào?”. Giao diện tìm kiếm truyền thống đáp ứng nhiều câu hỏi; LLM có thể hỗ trợ diễn đạt, nhưng dễ nhầm phạm vi, đơn vị hoặc biến lịch thành thực trả.

Đề xuất bắt đầu với **SQL/tìm kiếm có nguồn**, sau đó so với RAG giới hạn trên corpus đã duyệt. Mọi số và phép tính lấy từ facts/analytics; mô hình chỉ diễn giải bằng chứng được cung cấp. Đây là mở rộng sản phẩm, không làm giảm ưu tiên dữ liệu của MVP.

## 2. Câu hỏi nghiên cứu

- I5-RQ1: RAG cải thiện tỷ lệ trả lời đúng có căn cứ so với tìm kiếm/template không?
- I5-RQ2: bao nhiêu phát biểu sai kỳ, scope/basis, đơn vị hoặc trạng thái cổ tức?
- I5-RQ3: hệ thống biết từ chối khi nguồn thiếu/xung đột ở mức nào?
- I5-RQ4: lợi ích tra cứu có tương xứng độ trễ và chi phí vận hành không?

Nguồn phương pháp: [Lewis et al., RAG](https://arxiv.org/abs/2005.11401), [Min et al., FActScore](https://arxiv.org/abs/2305.14251). Đã đọc abstract/metadata, chưa tái lập và chưa chứng minh hiệu quả tiếng Việt.

## 3. Những câu hỏi được hỗ trợ

Tra cứu fact/kỳ/phạm vi; giải thích ratio và rule đã tính; xem timeline/quyền; so hai năm có cơ sở tương thích; hỏi định nghĩa tài chính trong tài liệu đã duyệt. Câu hỏi thiếu công ty/năm hoặc mơ hồ về hợp nhất/riêng cần làm rõ hoặc trả các lựa chọn có nhãn.

Không suy điều kiện chia lợi nhuận hợp pháp, không khẳng định paid nếu chỉ có lịch, không tự tính chỉ số thiếu đầu vào. Câu hỏi xác suất dùng kết quả mô hình đã đánh giá với version, không bịa phần trăm.

## 4. Phụ thuộc dữ liệu và đóng góp

Cần facts I1, metric I2, events I3, rule/model report I4 và bộ nguồn retrievable. Không có nền dữ liệu thì dừng ở tra cứu tài liệu, ghi chưa trả lời được số liệu.

Đóng góp là pipeline chọn bằng chứng đúng thời điểm/ngữ nghĩa và benchmark trả lời tiếng Việt ở cấp phát biểu. Không gọi ghép vector database với LLM là mô hình mới. Chưa có benchmark tài chính Việt Nam để tuyên bố vượt sản phẩm khác.

## 5. Sản phẩm và gate

Corpus manifest; query set/gold evidence; baseline SQL/template/search; retrieval/RAG specification; citation resolver; evaluation/error report; UI mở nguồn. Chỉ thêm RAG nếu precision phát biểu và nguồn không kém baseline, có lợi ích rõ và chi phí phù hợp.

Không chèn I5 vào lịch 13 tuần nếu ảnh hưởng nghiệm thu. Sẽ cần một kế hoạch thực hiện riêng sau khi đo công sức, thay vì ước lượng giờ chưa có căn cứ.

## 6. Hồ sơ cần đọc

[Kiến thức tài chính/diễn giải](02-kien-thuc-tai-chinh.md), [IT SQL và RAG](03-ky-thuat-it.md), [benchmark hỏi đáp](04-du-lieu-thi-nghiem-danh-gia.md), M02/M03/T12/T13 trong [sổ nguồn](../02-so-tai-lieu-tham-khao.md).
