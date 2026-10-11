# Workspace tuần 1

Toàn bộ code và hồ sơ thực hiện tuần 1 được gom tại đây theo yêu cầu người thực hiện. Mẫu chính là **Vinamilk 2025, PaddleOCR CPU**; HPG nhập tay trước đó giữ riêng là lịch sử, không tính thành kết quả Paddle.

| Thư mục | Nội dung |
|---|---|
| `scripts/` | Thu nguồn, chạy Paddle, xác minh ngữ cảnh, parser, test và ledger |
| `docs/` | [Nhật ký VNM 2025](docs/vnm-2025.md), [môi trường](docs/environment.md), nhật ký HPG cũ và evidence nhỏ |
| `data/vnm-2025/` | PDF gốc/hash, HTML nguồn, ảnh render, raw OCR, log và CSV sáu candidate |
| `data/` | Ledger 9 báo cáo/54 targets và hồ sơ HPG lịch sử |
| `config/` | Snapshot manifest, package lock và model hash |

Chạy từ **root repository**, dùng môi trường `.venv-paddle/` đã cài:

```powershell
.venv-paddle/Scripts/python.exe workspace/week1/scripts/verify_vnm_paddle_context.py
.venv-paddle/Scripts/python.exe workspace/week1/scripts/extract_vnm_paddle_facts.py
.venv-paddle/Scripts/python.exe workspace/week1/scripts/test_extract_vnm_paddle_facts.py
python workspace/week1/scripts/build_pilot_ledger.py
```

Lệnh tải nguồn và OCR đầy đủ nằm trong nhật ký. Chạy lại tải nguồn sẽ thay metadata thu nguồn bằng phiên mới; không cần tải/OCR lại chỉ vì di chuyển thư mục.

Môi trường Python `.venv-paddle/`, bootstrap `.tools/` và cache model Paddle vẫn là runtime dùng chung ngoài workspace; di chuyển virtualenv có thể làm hỏng đường dẫn môi trường. Ảnh Q1 dùng smoke là input kế thừa ở `exports/demo1-vnm/output/page-12.png`. Các tài liệu kế hoạch chung ở `docs/research-platform/` và manifest chính ở `config/` vẫn thuộc project; hồ sơ thực hiện và code mới chỉ nằm ở đây.

`relocation-map.json` ghi đường dẫn cũ → mới. Log OCR gốc giữ nguyên commands/timings để bảo toàn lịch sử; đường dẫn trong log có thể là đường dẫn trước khi di chuyển. Parser và metadata hiện hành dùng vị trí mới. [CSV](data/vnm-2025/reference-facts.csv) có sáu candidate chờ duyệt, 0 fact đã duyệt; chưa hoàn thành web/API/DB hoặc toàn bộ tuần 1.

`data/` được Git-ignore vì chứa PDF/ảnh/raw OCR; cần sao lưu riêng. Code, nhật ký, config và evidence nhỏ có thể theo dõi bằng Git.
