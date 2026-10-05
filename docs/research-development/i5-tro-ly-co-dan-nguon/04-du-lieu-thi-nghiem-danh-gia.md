# I5 — Protocol đánh giá tra cứu và trả lời có căn cứ

Ngày: 03/10/2026. Chưa có corpus câu hỏi hoặc model run.

## 1. Bộ câu hỏi và gold evidence

Đề xuất 20 câu development để chọn chunk/retrieval/prompt, thêm 60 câu evaluation gồm sáu nhóm ×10: fact đơn; so kỳ; calculation; timeline; giải thích rule; thiếu/xung đột/câu không trả lời được. Đây là quy mô benchmark dự kiến, không là số đã tạo.

Mỗi câu gắn snapshot/as_of, company/scope/basis, intent, gold facts/evidence và đáp án/rubric. Không tạo gold từ câu trả lời model. Cần nhiều công ty/bố cục; câu development và evaluation khác pattern đủ để tránh prompt học thuộc.

## 2. Ba phương án so sánh

1. SQL/tìm kiếm + template: baseline chính.
2. Retrieval + LLM diễn giải, không calculation service: ablation kiểm tra lỗi số.
3. SQL + retrieval + calculation + LLM + checks: phương án đề xuất.

Mọi phương án dùng cùng corpus snapshot và câu hỏi. Bản không có calculation chỉ là thí nghiệm so sánh, không mặc định là cấu hình sản phẩm. Không cần thử LLM không có corpus nếu không giúp trả lời câu hỏi nghiên cứu.

## 3. Đánh giá retrieval và answer riêng

| Metric | Định nghĩa |
|---|---|
| Evidence recall@k | Tỷ lệ câu mà top-k chứa đủ căn cứ gold theo tiêu chí đã ghi |
| Numeric accuracy | Câu/số đúng value, unit và rounding trong số câu có đáp án số |
| Semantic compatibility | Đúng company/period/scope/basis/state |
| Claim support precision | Phát biểu thực tế được nguồn hỗ trợ / mọi phát biểu thực tế sinh ra |
| Citation correctness | Citation hỗ trợ đúng claim, không chỉ link truy cập được |
| Answer completeness | Các phần gold cần thiết đã trả / các phần bắt buộc |
| Abstention precision/recall | Từ chối đúng khi không có căn cứ, và không từ chối oan câu có đáp án |
| Cost/latency | Token, chi phí thực tế nếu có, p50/p95 và số lần retry |

FActScore cung cấp ý tưởng đánh giá phát biểu đơn lẻ; metric đề tài là rubric tài chính điều chỉnh riêng, **không tuyên bố đã tái lập FActScore gốc**. [Bài báo](https://arxiv.org/abs/2305.14251).

Claim precision cao có thể do hệ thống chỉ trả một câu hoặc từ chối tất cả, nên phải cùng completeness/abstention và coverage. Retrieval tốt chưa bảo đảm generation đúng.

## 4. Bộ lỗi bắt buộc

Cột năm khác; triệu VND/VND; LNST tổng/phần công ty mẹ; IFRS/VAS; EPS/DPS khác basis; lịch đổi sau as_of; lịch chưa paid; cổ tức cổ phiếu; tỷ lệ mệnh giá khác yield; thiếu CFO; nguồn xung đột; PDF chứa đoạn chỉ dẫn giả yêu cầu bỏ qua nguồn.

Các câu thiếu ngữ cảnh cũng phải chấm: hệ thống hỏi rõ hoặc trả lựa chọn có nhãn, không đoán một giá trị. Những trường hợp này là test về phương pháp, không chứng minh độ an toàn tổng quát.

## 5. Chấm và độ bất định

Chấm tự động số/IDs, người đọc chấm căn cứ và diễn giải. Nếu chỉ một người chấm, ghi rõ, kiểm tra lại mẫu và giữ quyết định chấm. Không dùng chính model sinh làm người chấm duy nhất.

Nếu generation ngẫu nhiên, cố định cấu hình và chạy lặp một tập con theo ngân sách để báo độ biến động; không chọn lần đẹp nhất. Báo số đúng/tổng theo intent, lỗi nặng và interval thích hợp theo câu/cụm công ty, tránh điểm trung bình che sai trạng thái paid.

## 6. Gate đưa vào sản phẩm

Phương án RAG phải ít nhất không làm giảm độ đúng số/nguồn so baseline, không phát biểu paid từ lịch trong bộ kiểm tra và cải thiện chức năng hoặc thời gian tra cứu với chi phí phù hợp. “Không lỗi trong bộ test” chỉ là tiêu chí trên mẫu, không bảo đảm tuyệt đối ngoài mẫu.

Nếu không đạt, giữ SQL/search/template và công bố lỗi, không tăng prompt phức tạp để tránh báo kết quả. Artifacts gồm query/gold set, corpus manifest, retrieval/run logs, claims/rubric và báo cáo MD riêng.
