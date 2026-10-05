# Kỹ thuật IT cho nền tảng dữ liệu và so sánh chỉ tiêu vĩ mô

HTTP JSON client, paging, cache, schema country/indicator/observation/vintage, kiểm tra null và units; pandas time series; dashboard lọc quốc gia/chỉ tiêu. Bài tập: tải GDP, lưu snapshot hash và nhập lại idempotent. Request đã chạy là bằng chứng khả thi nhỏ, không phải hạ tầng production hoặc dataset realtime.

Đầu ra cần giữ: source code module, dữ liệu đầu vào có nguồn, cấu hình, test phù hợp, log chạy và hạn chế. Đọc được dữ liệu hoặc gọi được thư viện không thay thế đánh giá đúng/sai trên bộ mẫu.

Nguồn và hồ sơ: [World Bank API documentation](https://datahelpdesk.worldbank.org/knowledgebase/articles/889392-about-the-indicators-api-documentation); [GDP API đã thử](https://api.worldbank.org/v2/country/VN/indicator/NY.GDP.MKTP.CD?date=2020:2025&format=json).
