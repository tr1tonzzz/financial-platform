# Kiến thức tài chính cho nền tảng dữ liệu và so sánh chỉ tiêu vĩ mô

GDP danh nghĩa khác thực, USD khác nội tệ, CPI level khác inflation rate. Tăng trưởng phần trăm khác tăng tuyệt đối; năm cơ sở và thay đổi định nghĩa ảnh hưởng so sánh. Không nối chỉ tiêu năm với hàng ngày bằng forward-fill rồi coi là quan sát mới. Bài tập: đọc metadata ba chỉ tiêu, giải thích đơn vị và vì sao không thể cộng chúng trực tiếp.

Học bằng một ví dụ tính tay trước, sau đó viết lại bằng Python và ghi điều kiện áp dụng. Không xem kết quả số là kết luận đầu tư hoặc xác suất rủi ro nếu chưa có thiết kế kiểm định.

Nguồn học/nghiên cứu: [World Bank API documentation](https://datahelpdesk.worldbank.org/knowledgebase/articles/889392-about-the-indicators-api-documentation); [GDP API đã thử](https://api.worldbank.org/v2/country/VN/indicator/NY.GDP.MKTP.CD?date=2020:2025&format=json).
