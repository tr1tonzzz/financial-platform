# N1 — Kiến thức tài chính cần dùng

Đọc cùng [đề xuất](01-de-xuat-nghien-cuu.md) và [protocol](04-du-lieu-thi-nghiem-danh-gia.md). Công thức dưới đây là định nghĩa phân tích đề xuất; kiểm tra chính sách và phương pháp trình bày của từng báo cáo.

## 1. Lợi nhuận, dồn tích và CFO

Lợi nhuận ghi nhận và tiền thu/chi có thể khác thời điểm. [IAS 7 overview](https://www.ifrs.org/issued-standards/list-of-standards/ias-7-statement-of-cash-flows.html/) mô tả phương pháp gián tiếp điều chỉnh lợi nhuận cho các khoản phi tiền, dồn tích và khoản thuộc hoạt động khác. Không giả định dòng khởi đầu CFO luôn là LNST: báo cáo có thể bắt đầu từ lợi nhuận trước thuế và tiếp tục điều chỉnh.

`CFO / LNST` chỉ tính khi LNST > 0 và hai số cùng kỳ/phạm vi. Giá trị thấp là dấu hiệu cần đọc sâu; giá trị âm/lớn do mẫu số nhỏ phải giải thích. Không gọi tỷ số này là xác suất cắt cổ tức hoặc bằng chứng gian lận.

## 2. Cầu nối CFO

Đề xuất biểu diễn:

```text
CFO = lợi_nhuận_khởi_đầu + tổng_các_dòng_điều_chỉnh_có_dấu
residual = CFO_công_bố - CFO_tái_dựng
```

Các dòng có thể gồm khấu hao, lãi/lỗ thuộc đầu tư, lãi vay được điều chỉnh, thay đổi vốn lưu động, lãi vay thực trả, thuế thực trả và khoản khác. Đọc dấu tiền vào/ra theo dòng gốc, không dựa vào từ “tăng” mà bỏ dấu. Không cộng cả dòng tổng và các dòng thành phần của chính tổng đó.

Biến động phải thu/tồn kho/phải trả trên bảng cân đối có thể bị ảnh hưởng bởi mua bán công ty, tỷ giá, tái phân loại hoặc dự phòng. Vì vậy không ép biến động số dư bằng dòng điều chỉnh CFO. `residual` phải hiện rõ với lý do chưa giải thích.

## 3. Vốn lưu động và kỳ thu tiền

Chỉ số mô tả đề xuất cho năm đủ dữ liệu:

| Chỉ số | Công thức | Điều kiện |
|---|---|---|
| DSO gần đúng | Phải thu thương mại bình quân / doanh thu thuần × số ngày kỳ | Chưa có doanh thu bán chịu thì ghi dùng doanh thu thuần thay thế |
| DIO | Tồn kho bình quân / giá vốn × số ngày kỳ | Giá vốn dương, phạm vi tồn kho phù hợp |
| DPO gần đúng | Phải trả người bán bình quân / giá vốn × số ngày kỳ | Giá vốn chỉ là proxy; mẫu chuẩn cần số mua hàng chưa chắc có |
| Chu kỳ tiền gần đúng | DSO + DIO − DPO | Chỉ so sánh khi proxy và ngành tương thích |

Bình quân cần đầu và cuối kỳ. Thiếu số đầu kỳ không tự thay bằng số cuối kỳ; bỏ chỉ số hoặc ghi rõ biến thể khác. Dùng số ngày thực tế của kỳ. Kết quả là proxy, không phải tuổi nợ thực tế của từng hóa đơn.

## 4. Liên hệ với cổ tức

Dòng tiền yếu có thể đi cùng tăng trưởng hoặc chu kỳ hoạt động, không chỉ suy giảm. Cổ tức còn chịu ảnh hưởng tiền tích lũy, đầu tư, tài trợ và quyết định chính sách. Case phải đối chiếu nhiều năm, giải thích phần vốn lưu động và dẫn nguồn sự kiện cổ tức.

Các nghiên cứu B01/B02 ở [sổ nguồn](../02-tai-lieu-va-co-so-lua-chon.md) không được tái lập chỉ bằng các công thức này. Mô hình dồn tích chuyên sâu đòi hỏi thiết kế và mẫu riêng; chưa nằm trong N1 ở mức case.
