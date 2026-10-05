"""Validate weekly planning coverage and build Markdown from the shared JSON."""
import re


def build(plan, base):
    srs=(base/'22-srs-dac-ta-yeu-cau-phan-mem.md').read_text(encoding='utf-8')
    req=set(re.findall(r'^\*\*((?:FR|BR|DR|IR|NFR|E)\d{2})\b',srs,re.M))
    tc=set(re.findall(r'^\| (TC\d{2}) —',srs,re.M)) | set(re.findall(r'\bP\d{2}\b',srs.split('\n## 15.',1)[1]))
    assert [w['n'] for w in plan['weeks']]==list(range(1,14))
    assert {r for w in plan['weeks'] for r in w['requirements']}==req
    assert {t for w in plan['weeks'] for t in w['tests']}==tc
    assert len(req)==83 and len(tc)==42
    total=0
    for w in plan['weeks']:
        assert len(w['tasks'])==6 and len(w['sessions'])==5
        assert all(n<w['n'] for n in w['depends'])
        assert w['inputs'] and w['outputs'] and w['done']
        assert sum(w['hours'].values())==11+w['hours']['extension']
        session_hours=[float(re.search(r'B\d:\s*([\d.,]+)\s*h',s).group(1).replace(',','.')) for s in w['sessions']]
        assert sum(session_hours)+w['hours']['buffer']==11+w['hours']['extension'],(w['n'],session_hours)
        total+=sum(w['hours'].values())
        for ref in w['refs']:assert ref in plan['refs']
    for _,target in plan['refs'].values():assert (base/target).exists(),target
    assert total==167
    intro='''# Kế hoạch thực hiện 13 tuần — v3 theo SRS v3.1

Cập nhật 05/10/2026 theo hướng lợi nhuận→chuyển thành tiền→đối chiếu cổ tức. CR-PCD-01/mục15 SRS thêm cầu nối LNTT→CFO tối thiểu một ca, mục tiêu1–3 theo gate; 83 mã yêu cầu/42 tình huống dự kiến. Giữ 78 việc, bổ sung tiêu chí cầu nối trong việc WNN-05. E05/E10 chỉ áp dụng khi có quyết định kích hoạt.

Quỹ nền143 giờ + cầu nối tối thiểu24 giờ =167 giờ dự toán (12–15giờ/tuần tùy tuần), chưa được người thực hiện xác nhận. Nghiên cứu ước lượng24–40 giờ;24 là mức thấp phải đo lại G4. Nếu thời gian thực chỉ10–12giờ/tuần thì cần phân bổ lại/lùi hạn hoặc CR giảm phạm vi, không coi quỹ mới nằm trong143giờ. Ưu tiên một ca trước mở5–8 doanh nghiệp; không đồng thời mở mọi chiều sâu. B5 là giờ thêm, không lấy dự phòng nền. Phần giả định nền bên dưới được giữ để đối chiếu.

Cập nhật 04/10/2026. Một người, 10–12 giờ/tuần; cơ sở 11 giờ × 13 = 143 giờ gồm học, code, kiểm, báo cáo và dự phòng. Tuần tính từ ngày bắt đầu thật, chưa mặc định đủ 13 tuần học kỳ. Các đầu ra là mục tiêu tương lai, không phải tiến độ đã đạt.

Nguồn đồng bộ: [SRS v3.0](22-srs-dac-ta-yeu-cau-phan-mem.md) → [JSON kế hoạch](checklist-13-tuan.json) → tài liệu này và [checklist HTML](checklist-13-tuan.html). Đọc [hướng dẫn bắt đầu/mẫu minh chứng](23-bat-dau-va-minh-chung-thuc-hien.md) trước buổi 1. Tài liệu 02 giữ P/US/PF/AN; kế hoạch 16 tuần/A1 cũ không áp dụng.

## 1. Kết quả rà soát và cách dùng

Bản trước có khung tuần/nhịp báo cáo nhưng thiếu phân bổ SRS, output paths, replay mọi kết quả, restore, benchmark và local safety; còn quy tắc/hướng tốt nghiệp cũ. V2 bổ sung các phần này, làm rõ freeze holdout trước đo. Version/cache nền làm từ tuần 2, tuần 10 hoàn thiện replay.

Mỗi tuần có đầu vào/phụ thuộc, 6 việc WNN-01…WNN-06, đầu ra, TC và tiêu chí xong. Làm theo thứ tự; ghi giờ/bằng chứng/lỗi cuối tuần. Phụ thuộc chưa đạt thì task liên quan pending, có thể làm việc độc lập. Báo cáo thật ở tuần 2/4/6/8/10/12; tuần 13 tổng kết theo mẫu trường. Không tạo bảy bộ tiến độ giả.

**Môi trường đã kiểm:** Python/venv hiện có 3.14.7, SRS chọn 3.12. Tuần 1 chuẩn bị interpreter/.venv-fap riêng hoặc xử lý CR trước freeze, không xóa venv cũ. src chưa có MVP, prototype chưa thu đủ 2023–2025. Module/file đầu ra dưới đây là vị trí dự kiến cần tạo khi làm.

## 2. Gate và ngân sách mở rộng

| Mốc | Điều kiện / quyết định | Khi chưa đạt |
|---|---|---|
| G2 cuối tuần 2 | Một issuer: danh mục→raw→candidate→review, rà discovery hai loại | Thử IR thay thế, ghi lỗi/assisted, xử lý tuần 3; assisted không pass FR04 |
| G4 cuối tuần 4 | Pilot 9 báo cáo/54 targets có ledger/review, effort và quyết định mẫu | Giữ 3 issuers, không mặc định mở 24 báo cáo |
| G8 đầu tuần 8 | Freeze scope/gold/split/config/hash, backup trước baseline | Chưa freeze thì chưa đo độc lập; ghi giới hạn |
| G11 cuối tuần 11 | Feature freeze, yêu cầu/TC có trạng thái và lỗi ưu tiên | Chỉ sửa lỗi/minh chứng; M chưa đạt cần sửa hoặc CR được chấp nhận |
| Cuối tuần 13 | Clean setup/bundle/replay/restore, báo cáo/deck/app thống nhất | Không gọi hoàn tất phép chưa chạy |

G4 ước lượng effort tăng thêm = BCTC thêm × phút xử lý/review + notices thêm × phút/notice + sửa adapter + rà coverage. Dùng mức cao đã quan sát. Quỹ dữ liệu mở rộng tối đa 6 giờ tuần 7 + ≤2 giờ dự phòng tuần 8 trước G8; không lấy giờ baseline/report/restore tăng mẫu. Vượt quỹ hoặc discovery còn lỗi thì giữ pilot. Giảm nghĩa vụ M cần CR, không tự đổi status thành pass.

TBD01 rubric/hạn/phê duyệt: tuần 1–2; TBD02 issuer/scope/nguồn/policy: trước G4; TBD03 gold/holdout/checker: trước G8; TBD04 máy/dependencies/ngưỡng: trước benchmark tuần 11; TBD05 mapping/basis/tolerance: trong pilot trước duyệt; TBD06 walkthrough/effort: thiết kế trước đo, kiểm tuần 5/12. Ghi decisions thật, chưa có phản hồi thì pending.

## 3. Tổng quan và giờ

Cột giờ: học / code / kiểm / báo cáo / dự phòng. Phát sinh phải ghi giờ thật và phân bổ lại tại gate.

| Tuần | Trọng tâm | Phụ thuộc | Giờ H/C/K/B/D | Báo cáo |
|---|---|---|---|---|
'''
    intro=intro.replace('SRS v3.0','SRS v3.1').replace('Kế hoạch phủ 73 yêu cầu và 31 TC','Kế hoạch phủ 83 mã yêu cầu và 42 tình huống').replace('V2 bổ sung','V3 kế thừa').replace('6 việc','6 việc').replace('Checklist v2','Checklist v3')
    parts=[intro]
    for w in plan['weeks']:
        h='/'.join(str(w['hours'][k]).replace('.',',') for k in ['learn','build','test','report','buffer'])+f" +{w['hours']['extension']} cầu nối"
        report='Cuối' if w['n']==13 else f"Đợt {w['n']//2}" if w['n']%2==0 else 'Nhật ký'
        parts.append(f"| {w['n']} | {w['title']} | {','.join(map(str,w['depends'])) or 'Không'} | {h} | {report} |\n")
    parts.append('\n## 4. Công việc và tiêu chí từng tuần\n')
    for w in plan['weeks']:
        parts.append(f"\n### Tuần {w['n']:02d} — {w['title']}\n\n**Học đúng task:** {w['learn']}\n\n**Đích tuần:** {w['goal']}\n\n**Đầu vào:** {' '.join(w['inputs'])}\n\n**Việc thực hiện:**\n")
        for i,task in enumerate(w['tasks']):parts.append(f"\n- **W{w['n']:02d}-{i+1:02d}:** {task}")
        parts.append('\n\n**Nhịp buổi đề xuất** (cộng giờ dự phòng của tuần):\n')
        for s in w['sessions']:parts.append(f'\n- {s}')
        parts.append('\n\n**Đầu ra phải lưu** (từ repo, tạo khi làm):\n')
        for output in w['outputs']:parts.append(f'\n- {output}')
        parts.append(f"\n\n**Yêu cầu SRS:** {', '.join(w['requirements'])}.\n\n**Kiểm chứng:** {', '.join(w['tests'])}; dùng input/expected mục 10 và 15 SRS, lưu actual/evidence.\n\n**Xong khi:** {w['done']}\n")
        if w['gate']:parts.append(f"\n**Gate:** {w['gate']}\n")
    parts.append('''
## 5. Thiếu thời gian và xử lý vướng

167 giờ (143 nền + 24 cầu nối) là dự toán, chưa chứng minh mọi adapter/layout làm kịp. Lỗi quá một buổi phải lưu raw/run, thu nhỏ một tài liệu, ghi giờ/decision. Giữ review/provenance/missing/lifecycle/snapshot/restore; giảm issuers trước khi bỏ lõi. Assisted không thay discovery trong nghiệm thu. Không có case mong đợi thì chọn case thật khác.

Nếu chỉ còn 8–10 tuần với 10–12 giờ/tuần: tuần 1 gộp môi trường/đọc/discovery; tuần 2–3 pilot/extract/store/review/G4; tuần 4 analytics/lifecycle; tuần 5 gold/freeze; tuần 6 đo/cases; tuần 7 snapshot/restore/local checks; tuần 8 nghiệm thu/report/package; tuần 9–10 nếu có là buffer. Chỉ 3 issuers, không mở 5–8. Giữ TC bắt buộc áp dụng, tính lại giờ/CR trước nhận lịch ngắn. Dưới 8 tuần hoặc <6–7 giờ/tuần cần lập ngân sách theo hạn thật, chưa cam kết lịch này khả thi.

## 6. Theo dõi và mở rộng

Kế hoạch phủ 73 yêu cầu và 31 TC; phân bổ tuần không phải pass. Kiểm khi module xong, hồi quy khi rule/input/store đổi. Tuần 11–13 tổng hợp status với bằng chứng, không suy từ tick. Mẫu hồ sơ ở [23](23-bat-dau-va-minh-chung-thuc-hien.md).

Đồ án ưu tiên version/impact; project giữ lineage làm nền, chưa bắt buộc semantic diff engine đầy đủ. Predictor tùy chọn sau gate riêng, không task 13 tuần. [Báo cáo hai tuần](07-bao-cao-hang-tuan.md), [lộ trình học](05-lo-trinh-hoc.md) và [tài chính](18-nhap-mon-tai-chinh-cho-du-an.md) đi cùng kế hoạch.

Checklist v2 giữ bản lưu v1, chuyển start/notes, không tự áp tick vì tiêu chí đã đổi. Nguồn là JSON, sửa rồi chạy build_weekly_checklist.py để sinh Markdown/HTML. Bản trước trong history/before-srs-v3-plan-2026-10-04-*. Các đường dẫn/module dự kiến chưa phải artifact đã xây.
''')
    output=''.join(parts).replace('Kế hoạch phủ 73 yêu cầu và 31 TC','Kế hoạch phủ 83 mã yêu cầu và 42 tình huống').replace('Checklist v2 giữ bản lưu v1','Checklist v3 giữ bản lưu v1/v2').replace('Bản trước trong history/before-srs-v3-plan-2026-10-04-*','Bản trước trong history/before-pcd-v3.1-2026-10-05')
    (base/'04-ke-hoach-13-tuan.md').write_text(output,encoding='utf-8')
    return {'version':plan['version'],'weeks':13,'tasks':78,'hours':total,'requirements':len(req),'test_cases':len(tc),'coverage':'passed'}
