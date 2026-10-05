# Nền tảng dữ liệu và so sánh chỉ tiêu vĩ mô

Khảo sát và đề xuất ngày 03/10/2026. Trạng thái: thiết kế/đánh giá khả thi, không phải chức năng ứng dụng đã hoàn thành.

## Bài toán và người dùng

Người nghiên cứu cần dữ liệu GDP/lạm phát và so sánh quốc gia/chuỗi năm với đơn vị, metadata và thời điểm snapshot rõ. Bài toán này khác dữ liệu doanh nghiệp và cổ tức.

## Dữ liệu và bằng chứng khả thi

World Bank Indicators API, mã chỉ tiêu và metadata. Đã thử một request GDP Việt Nam 2020–2025: HTTP 200, sáu dòng có giá trị; chưa thử toàn bộ chỉ tiêu hoặc vintage công bố ban đầu. Dữ liệu năm không đồng nghĩa có dữ liệu quý mới.

## MVP nếu chọn hướng này

3–5 chỉ tiêu, Việt Nam và 2–3 quốc gia so sánh, cache, chuẩn hóa units/missing, biểu đồ và CSV. Phân tích mô tả, không dự báo vĩ mô làm nghĩa vụ.

## Đóng góp IT và cách đánh giá

Đối chiếu giá trị API, handling null và đơn vị, consistency cập nhật, độ trễ và tính tái lập. Phải có chức năng metadata/phiên bản để mạnh hơn dashboard đơn giản.

## Điểm khó cần xử lý

Dữ liệu bị sửa sau công bố; ít điểm năm không đủ ML. Độ mới và tần suất phụ thuộc từng chỉ tiêu. Câu hỏi ứng dụng có thể mờ hơn phân tích doanh nghiệp.

## Liên thông lên đồ án tốt nghiệp

Nghiên cứu data revision hoặc event-aligned macro/company analysis khi có nhiều nguồn và vintage. Không suy quan hệ nhân quả từ tương quan GDP–giá.

## Tài liệu đi kèm

[Kiến thức tài chính](02-kien-thuc-tai-chinh.md); [kỹ thuật IT](03-ky-thuat-it.md). Nguồn: [World Bank API documentation](https://datahelpdesk.worldbank.org/knowledgebase/articles/889392-about-the-indicators-api-documentation); [GDP API đã thử](https://api.worldbank.org/v2/country/VN/indicator/NY.GDP.MKTP.CD?date=2020:2025&format=json).
