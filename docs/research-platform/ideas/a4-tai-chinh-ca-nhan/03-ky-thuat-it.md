# Kỹ thuật IT cho quản lý thu chi và ngân sách cá nhân

Parser CSV cấu hình cột, transaction hash, phân nhóm bằng luật trước ML, UI chỉnh nhãn và audit trail. SQLite và mã hóa/đường lưu phù hợp nếu chứa dữ liệu cá nhân; không commit raw giao dịch riêng tư. Có workflow delete/export, kiểm thử nhập lại cùng CSV và hoàn tiền. Phân loại ML cần gold độc lập; đo macro-F1 và công sức chỉnh nhóm chứ không chỉ demo biểu đồ.

Đầu ra cần giữ: source code module, dữ liệu đầu vào có nguồn, cấu hình, test phù hợp, log chạy và hạn chế. Đọc được dữ liệu hoặc gọi được thư viện không thay thế đánh giá đúng/sai trên bộ mẫu.

Nguồn và hồ sơ: [CFPB spending tracker](https://www.consumerfinance.gov/archive/blog/track-your-spending-with-this-easy-tool/). Nguồn này giải thích nhu cầu theo dõi chi, không cung cấp dataset người dùng cho project.
