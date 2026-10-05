# Workspace nghiên cứu bằng AI agents

## Nguồn context bắt buộc

Mỗi agent đọc [chỉ mục tài liệu](../README.md), [SRS](../initial-docs/SRS-FDP-01.md), [đề cương](../research-design.md) và tài liệu chuyên môn liên quan trong bộ mới.

Đề tài là BCTC–cổ tức tiền mặt Việt Nam. Mục tiêu MVP 13 tuần, pilot 10 công ty, tối thiểu 30, mở rộng 60–80 có điều kiện. Bỏ mọi giả định triển khai ngoài bộ hiện hành.

## Workflow tiết kiệm quota

Chạy lần lượt từng agent, mỗi lượt một câu hỏi hẹp và đầu ra file Markdown. Đọc lại kết quả trước khi chạy lượt sau. Đây là hướng dẫn vận hành; chưa cài bộ chạy agent tự động.

Mỗi phát biểu về nguồn phải có URL, ngày kiểm tra, cách kiểm tra và trạng thái. Phân biệt thiết kế đề xuất, thông tin đã đọc và kết quả đã chạy. Không tự điền số đo hay trích dẫn.

## Prompt chung

```text
Bạn nghiên cứu đề tài BCTC–cổ tức tiền mặt Việt Nam.
Đọc docs/README.md, docs/initial-docs/SRS-FDP-01.md và docs/research-design.md.
Đề tài tập trung thu thập/chuẩn hóa/kiểm định dữ liệu và phân tích quan hệ.
MVP 13 tuần, pilot 10 công ty, tối thiểu 30; mục tiêu 60–80 có điều kiện.
Viết tiếng Việt có dấu. Ghi rõ đề xuất, bằng chứng, điều chưa kiểm chứng,
ảnh hưởng phạm vi và bước tiếp theo. Không tuyên bố đã crawl nếu chưa chạy.
```

## Nhiệm vụ từng agent

| Agent | Nghiên cứu | File đầu ra |
|---|---|---|
| Nguồn dữ liệu | Crawl được gì, PDF text/scan, lịch hay thực trả, metadata, công sức pilot | docs/agent-research/01-data-source-feasibility.md |
| Phương pháp tài chính | Giả thuyết, ratio, phạm vi hợp nhất/riêng, nhãn và độ nhạy | docs/agent-research/02-finance-research-design.md |
| Kiến trúc | Adapter, schema, nguồn truy vết, ngày khả dụng, dedupe, kiểm định | docs/agent-research/03-technical-architecture.md |
| Phạm vi | Ước lượng giờ từ pilot, gate tăng công ty/ML và phần cần cắt | docs/agent-research/04-scope-and-risk-review.md |
| Tổng hợp | Giải quyết mâu thuẫn, đề xuất cập nhật SRS/đề cương/SDD/PP/TP | docs/agent-research/05-final-synthesis.md |

Agent nguồn phải thử ít nhất một tài liệu khi có công cụ truy cập; nếu chỉ đọc trang web thì ghi rõ chưa kiểm chứng tải/parser. Agent tài chính cần dẫn nguồn học thuật đã đọc và không gọi tương quan là nhân quả.

Agent kiến trúc dùng thiết kế SDD như baseline, không thêm hạ tầng nếu chưa chứng minh nhu cầu. Agent phạm vi giữ quỹ giờ học song song và 20% dự phòng. Agent tổng hợp không ghi đè quy định chính khi chưa nêu bằng chứng và lý do thay đổi.

## Prompt cho mỗi lượt

```text
Thực hiện nhiệm vụ của agent [tên] trong bảng trên.
Đọc context bắt buộc và file chuyên môn liên quan.
Kiểm tra các giả định chưa chắc chắn; ghi URL và ngày kiểm tra cho bằng chứng.
Đầu ra gồm: kết luận, bằng chứng, đề xuất, giới hạn, thay đổi cần thiết, bước tiếp.
Ghi vào file đầu ra của agent. Cập nhật sources-ledger cho nguồn đã kiểm tra.
```

Sau các lượt, kiểm tra sources-ledger và decisions; cập nhật tài liệu chính khi quyết định được chốt. Ưu tiên pilot nguồn và nhãn trước khi đào sâu ML.


