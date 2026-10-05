# I5 — Kỹ thuật IT: SQL, truy xuất và RAG có bằng chứng

Ngày: 03/10/2026. Thiết kế mở rộng sau MVP.

## 1. Kiến trúc đề xuất

```text
câu hỏi → xác định intent/company/period/scope/basis/as_of
  → query templates đọc facts/metrics/events
  → tìm đoạn giải thích đúng metadata
  → calculation service nếu đủ đầu vào
  → evidence bundle
  → template hoặc LLM diễn giải
  → kiểm tra claims/citations → câu trả lời + nguồn
```

Intent số liệu đi qua SQL có cấu trúc, không để vector search đoán số. LLM không được tự chạy SQL tùy ý; dùng query templates/structured arguments với schema validation và truy vấn đọc.

## 2. Corpus và chunk

Corpus gồm văn bản nguồn có quyền dùng phù hợp, thuyết minh đã lấy, facts và tài liệu giải thích đã duyệt. Chunk theo đoạn/bảng có tiêu đề, năm, company, scope/basis, available_at, page/bbox và hash/version. Bảng nên giữ nhãn/đơn vị/cột cùng nhau; chia theo số ký tự thuần có thể tách số khỏi ý nghĩa.

Filter metadata trước retrieval: company/period/scope/basis và available_at≤as_of nếu câu hỏi lịch sử. Cần chuẩn hóa ticker/alias và kiểm tra trùng tên. Không dùng văn bản đính chính mới để trả “đã biết gì tại cutoff cũ”.

## 3. Baseline tìm kiếm và nhánh RAG

Baseline: SQL + câu template; tìm kiếm lexical cho thuyết minh. [PostgreSQL full text search](https://www.postgresql.org/docs/current/textsearch-intro.html) là một lựa chọn sẵn trong database; cần benchmark tiếng Việt, không mặc định stemming/chia từ phù hợp.

Sau đó mới thử embeddings và kết hợp lexical/dense với reranking trên corpus này. Chưa chọn provider/model/vector database vì chưa có benchmark/chi phí thực tế. Ở quy mô nhỏ có thể lưu chỉ mục local hoặc trong database hiện có.

RAG lấy ý tưởng truy xuất trước khi sinh từ [Lewis et al.](https://arxiv.org/abs/2005.11401); pipeline SQL và bộ kiểm tra tài chính là thiết kế riêng của đề tài, không là kiến trúc đã được bài gốc xác nhận.

## 4. Evidence bundle và output contract

```json
{
  "snapshot_id": "...",
  "as_of": "...",
  "facts": [{"fact_id": "...", "metric": "...", "value_vnd": "...", "status": "reviewed"}],
  "calculations": [{"formula_version": "...", "input_fact_ids": ["..."]}],
  "citations": [{"document_id": "...", "page_pdf": 1, "locator": "...", "hash": "..."}],
  "missing_reasons": []
}
```

Đây là schema minh họa, không là dữ liệu thực. Response chia câu trả lời thành claims và citation_ids. Resolver kiểm tra citation tồn tại và trỏ đúng evidence; số/đơn vị đối chiếu với bundle. Không chỉ kiểm tra “có link” vì link đúng trang vẫn có thể không hỗ trợ phát biểu.

## 5. Kiểm tra văn bản và từ chối

Số và công thức được kiểm tra bằng code; scope/year/state kiểm tra đối chiếu metadata; phát biểu diễn giải cần rubric người chấm. Tài liệu truy xuất là dữ liệu, không là chỉ dẫn điều khiển; bỏ qua đoạn yêu cầu sửa prompt/chạy lệnh trong nguồn.

Nguồn xung đột → trình bày hai căn cứ hoặc yêu cầu rõ; missing → nêu thiếu; unsupported forecast → không sinh xác suất. Log retrieval IDs, bundle, model/prompt version và latencies để phân tích lỗi.

## 6. Kỹ năng cần học và vận hành

Information retrieval, metadata filtering, embeddings, chunking bảng, structured output, deterministic calculations và claim-level evaluation. Cache theo snapshot/as_of/query/version, không theo text câu hỏi đơn độc vì dữ liệu có thể đổi.

Ngân sách token/độ trễ được đo ở benchmark; chưa có chi phí tiền dự kiến. Không cần fine-tuning hoặc agent tự chủ trước khi baseline tra cứu chứng minh thiếu chức năng.
