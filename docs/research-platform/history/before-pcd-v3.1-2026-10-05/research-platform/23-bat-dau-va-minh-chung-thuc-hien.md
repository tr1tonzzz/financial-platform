# Bắt đầu và lưu minh chứng thực hiện

04/10/2026 • Dùng cùng [kế hoạch v2](04-ke-hoach-13-tuan.md), [checklist](checklist-13-tuan.html) và [SRS v3.0](22-srs-dac-ta-yeu-cau-phan-mem.md). Đây là hướng dẫn công việc, chưa phải tiến độ đã đạt.

## 1. Buổi đầu tiên

Phần đọc và phân tích cơ bản: dùng [bộ tài liệu/bài tập tuần 1](24-tai-lieu-va-bai-tap-tuan-01.md), có link chính thức, vị trí bảng BCTC mẫu và khung trao đổi với giảng viên.

1. Chọn ngày bắt đầu thật trong checklist, kiểm hạn môn học và quỹ 10–12 giờ/tuần; đọc tuần 1 và các gate.
2. Kiểm môi trường/Git bằng lệnh dưới đây. Repository có nhiều thay đổi; không reset hoặc chạy script sinh nghiên cứu cũ để ghi đè tài liệu.
3. Chuẩn bị Python 3.12 và `.venv-fap` riêng theo SRS. Máy và `venv` hiện là 3.14.7, chưa thấy 3.12 qua launcher. Giữ `venv` cũ; nếu chọn 3.14 thì CR/kiểm dependencies/cập nhật SRS trước freeze.
4. Mở một BCTC năm kiểm toán, tìm sáu chỉ tiêu và ghi kỳ/scope/unit/trang/locator; đọc một notice và tách profit_year/lịch trả. Mẫu VNM nhiều năm thuộc development.
5. Ghi `execution/week-01.md`, nguồn/lệnh/giờ thực và phần còn pending. Chỉ tick việc có đầu ra và tự giải thích được.

Repository có prototype/scripts nghiên cứu, `src` chưa có MVP. Collector hiện chỉ chọn FY2025/H1-2026, tối đa 1–3 trang và 1–3 PDF/doanh nghiệp; chưa thu đủ 2023–2025 và chưa có discovery notice hoàn chỉnh. Tuần 2 phải mở config và adapter; không coi prototype đã đáp ứng SRS.

### Lệnh đang có

Chạy PowerShell tại workspace:

```powershell
Set-Location 'C:\Users\admin\Documents\GitHub\financial-analysis-platform'
py -0p
git status --short
```

Sau khi interpreter 3.12 có sẵn:

```powershell
py -3.12 --version
py -3.12 -m venv .venv-fap
& '.\.venv-fap\Scripts\python.exe' -m pip install -r '.\scripts\research\requirements-crawl.txt'
& '.\.venv-fap\Scripts\python.exe' -m unittest discover -s '.\scripts\research' -p 'test_crawl_official_reports.py'
```

Không cần activate khi dùng đường dẫn interpreter. Nếu `py -3.12` chưa có thì chuẩn bị interpreter trước nhóm lệnh này. Lưu phiên bản/kết quả thật vào `execution/environment.md`; dependencies crawler chưa là lock đầy đủ cho app.

Tuần 2 xem CLI và chạy thử nhỏ sau khi rà policy:

```powershell
& '.\.venv-fap\Scripts\python.exe' '.\scripts\research\crawl_official_reports.py' --help
& '.\.venv-fap\Scripts\python.exe' '.\scripts\research\crawl_official_reports.py' '.\data-sets\fap\prototype-smoke' --companies DHG --max-pages 1 --max-pdfs-per-company 1
```

Smoke còn filter cũ, không thu đủ pilot hoặc crawl notice. Policy-skip/lỗi giữ log, không gọi pass. CLI mới được tài liệu hóa sau khi xây. Chưa có lệnh chạy Streamlit MVP hôm nay.

## 2. Nơi lưu dự kiến

Các vị trí sau tương đối từ repo, bạn tạo khi làm; không coi module/file đã có chỉ vì kế hoạch nêu tên.

| Vị trí | Nội dung |
|---|---|
| `config/pilot.json` | Issuer/year/scope/source/window/as_of có version; prototype chưa tự đọc config này |
| `src/fap/`, `tests/` | Module và fixtures tạo dần; giữ regression crawler hiện tại |
| `data-sets/fap/raw/`, `runs/` | Raw bất biến, source/hash/version, run config/errors/effort |
| `data-sets/fap/pilot/`, `staging/`, `store/` | Expected/gold tay, candidates/issues, SQLite/review |
| `data-sets/fap/evaluation/` | Development/holdout/gold/baselines/metrics/tests; synthetic benchmark tách khỏi case thật |
| `data-sets/fap/snapshots/`, `backup/` | Gói tái lập và backup; SQLite dùng backup API hoặc dừng ghi |
| `docs/research-platform/execution/` | Environment/schema/decisions, nhật ký/requirement status/cases |
| `docs/research-platform/reports/` | Sáu đợt tiến độ và tổng kết từ kết quả thật |

`data-sets/` được Git ignore nên commit code không sao lưu dữ liệu; backup tại gate là bắt buộc. Khi tạo `.venv-fap`, bổ sung ignore cho thư mục này; không commit venv/secrets, không xóa môi trường cũ.

## 3. Mẫu scope và hồ sơ

Mẫu để bạn tạo file, chưa là dữ liệu thu sẵn:

```json
{
  "schema_version": 1,
  "scope_version": "pilot-draft-01",
  "srs_version": "3.0",
  "status": "draft",
  "issuer_candidates": ["HPG", "DHG", "VHC"],
  "fiscal_years": [2023, 2024, 2025],
  "scope_preference": "consolidated",
  "financial_targets": ["net_income_total", "cfo", "cash_equivalents", "total_assets", "total_liabilities", "total_equity"],
  "as_of": null,
  "sources": [],
  "source_window": null,
  "unresolved": ["issuer/scope confirmation", "source/policy", "actual as_of/window", "rubric/deadline"]
}
```

Ba mã là ứng viên từ prototype, cần xác nhận nguồn lịch sử/notice/scope. Notice có thể công bố ở năm khác năm lợi nhuận; cửa sổ rà không được cắt máy móc theo 2023–2025. Có 9 report targets không chứng minh đã công bố/tải đủ.

`expected-reports.csv`: `scope_version,issuer_id,ticker,fiscal_year,scope_expected,source_status,url,raw_version,review_status,reason`.

`expected-targets.csv`: `scope_version,issuer_id,fiscal_year,scope_expected,metric_key,status,reason,source_version`. Pilot 54 dòng gồm missing; downloaded khác extracted/reviewed/correct.

`gold-financial.csv`: `artifact_version,issuer_id,metric_key,raw_text,raw_unit,value_vnd,period_start,period_end,scope,page,locator,status,annotator,checker,checked_at`. Chưa có checker độc lập ghi self_check.

`gold-events.json`: source/notice versions, identity/relations, components/profit_year/DPS/basis, ngày/độ chính xác/timezone, policy/execution, coverage/as_of/window, locator và người đối chiếu. Routes/bản dịch/revisions cùng lineage thuộc cùng split.

`test-results.csv`:

```text
tc_id,srs_version,method,input_manifest,code_version,config_version,expected,actual,status,evidence_path,checked_by,checked_at,notes
```

`execution/requirements-status.csv`:

```text
requirement_id,srs_version,status,tc_ids,evidence_path,run_id,checked_at,notes
```

Status: `not_run`, `pass`, `fail`, `blocked`, `superseded_with_CR`. Ban đầu chưa chạy. Một requirement có nhiều TC chỉ pass khi các điều kiện áp dụng đã kiểm; BR được kiểm qua FR/DR và TC liên quan. Script kiểm kế hoạch không xác nhận app pass 31 TC.

Nhật ký:

```markdown
# Tuần NN — ngày thực tế
SRS version / scope version:
Việc WNN-01…WNN-06 dự kiến và thực đạt:
Giờ học / code / kiểm / báo cáo / phát sinh:
File/run/commit/source thật:
TC: input + expected + actual + status + evidence:
Nguồn thiếu / lỗi / review:
Một công thức tự tính và một hàm/truy vấn tự giải thích:
Quyết định/CR thật và ba việc tiếp:
```

`execution/decisions.md`: ngày/gate/TBD/CR_id, quyết định/người/lý do, yêu cầu/TC/scope bị ảnh hưởng, giờ còn lại/phiên bản. Chưa có phản hồi thì pending; đổi nghĩa vụ nghiệm thu cần người có thẩm quyền tương ứng chấp nhận.

## 4. Tick việc và bản lưu cũ

Tick khi có đầu ra, input/source/config/version, phép đối chiếu, nhật ký và tự giải thích được. Tick việc khác pass TC/nghiệm thu. Vướng quá một buổi thì giữ raw/run, thu nhỏ một tài liệu, ghi giờ/lỗi; không bỏ blocking hoặc đổi missing thành 0.

Checklist v2 có 78 việc/13 tuần. Tick v1 không tự áp sang v2 vì tiêu chí đã đổi; giữ bản lưu v1, chuyển start/notes, bạn đối chiếu minh chứng rồi tick lại. JSON v2 khôi phục tick/notes/start, JSON v1 chỉ chuyển start/notes. Xuất JSON để sao lưu/chuyển máy.

Nguồn kế hoạch là JSON; chạy `scripts/research/build_weekly_checklist.py` để sinh Markdown04/HTML. Script kiểm giờ, mã SRS/TC, phụ thuộc và links, không xác nhận việc đã xong.
