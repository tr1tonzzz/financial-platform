# Hỏi đáp tài liệu tài chính có bằng chứng và phép tính

Khảo sát và đề xuất ngày 03/10/2026. Trạng thái: thiết kế/đánh giá khả thi, không phải chức năng ứng dụng đã hoàn thành.

## Bài toán và người dùng

Người đọc hỏi doanh thu, dòng tiền hoặc thay đổi qua năm và cần câu trả lời đúng tài liệu/cột, có phép tính kiểm tra được. Bài toán chính là truy xuất và suy luận số, không phải chatbot trò chuyện chung.

## Dữ liệu và bằng chứng khả thi

BCTC, bảng chuẩn hóa, câu hỏi/đáp án và chương trình tính. FinQA và TAT-QA là nghiên cứu benchmark đã đọc; không tự coi dữ liệu tiếng Anh là gold tiếng Việt/VAS. Cần bộ câu hỏi riêng do người hiểu nguồn chấm.

## MVP nếu chọn hướng này

Tra cứu và trả lời theo mẫu trên bảng đã duyệt, có công thức và nguồn. Nếu chọn làm đề tài chính phải dựng evaluation retrieval/numerical answer; RAG/LLM đầu-cuối chưa thích hợp làm nghĩa vụ 13 tuần của người mới.

## Đóng góp IT và cách đánh giá

Đúng kỳ/scope/số/công thức, nguồn trích đúng, recall retrieval và tỷ lệ từ chối khi thiếu dữ liệu. So lookup/template baseline với RAG và RAG + calculator trên holdout; đo chi phí và độ trễ.

## Điểm khó cần xử lý

Sai OCR lan sang đáp án; tài liệu rất giống nhau khác kỳ, hallucinatory citation và chi phí API. Một chatbot demo chưa chứng minh đóng góp.

## Liên thông lên đồ án tốt nghiệp

Nhánh ưu tiên sau A1: công cụ tính số có schema, retrieval theo kỳ/scope và bộ đánh giá tiếng Việt. A1 cung cấp dữ liệu đúng, nguồn và kiểm định để nghiên cứu này có nền.

## Tài liệu đi kèm

[Kiến thức tài chính](02-kien-thuc-tai-chinh.md); [kỹ thuật IT](03-ky-thuat-it.md). Nguồn: [FinQA](https://aclanthology.org/2021.emnlp-main.300/); [TAT-QA](https://aclanthology.org/2021.acl-long.254/).
