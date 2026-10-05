# Kỹ thuật IT cho hỏi đáp tài liệu tài chính có bằng chứng và phép tính

Index metadata + văn bản/bảng, retrieval lọc document/period/scope, function/tool gọi calculator có kiểm soát, trả citation locator. Tránh cho model tự tính hoặc chạy code tùy ý. Gold giữ câu hỏi, câu trả lời, operand, nguồn và phép tính; tách train/dev/test theo tài liệu. Bài tập: một hàm answer_growth chỉ nhận facts đã duyệt và trả phép tính + IDs, kiểm thử không đủ hai năm.

Đầu ra cần giữ: source code module, dữ liệu đầu vào có nguồn, cấu hình, test phù hợp, log chạy và hạn chế. Đọc được dữ liệu hoặc gọi được thư viện không thay thế đánh giá đúng/sai trên bộ mẫu.

Nguồn và hồ sơ: [FinQA](https://aclanthology.org/2021.emnlp-main.300/); [TAT-QA](https://aclanthology.org/2021.acl-long.254/).
