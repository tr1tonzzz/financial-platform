"""Build the next ten weeks from one source; no application progress is inferred."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / 'docs/research-platform'


def task(title, acceptance, hours):
    return {'title': title, 'acceptance': acceptance, 'hours': hours}


def week(n, title, uc, inputs, tasks, outputs, done, risk, requirements, tests):
    for i, item in enumerate(tasks, 1):
        item['id'] = f'W{n:02d}-{i:02d}'
    return {'n': n, 'title': title, 'uc': uc, 'inputs': inputs, 'tasks': tasks,
            'outputs': outputs, 'done': done, 'risk': risk,
            'requirements': requirements.split(), 'tests': tests.split(),
            'hours': sum(t['hours'] for t in tasks)}


W = [
week(1, 'UC-1 cơ bản, thay Paddle vào pipeline đã thử', 'UC-1',
 'Tận dụng tải PDF, pypdf và render Poppler đã thử; manifest HPG/VNM/FPT; ảnh VNM Q1/2026 chỉ dùng thử tích hợp OCR, không thay dữ liệu năm.', [
 task('Thay bước Tesseract bằng adapter Paddle trong pipeline có sẵn.', 'Chỉ kiểm lại môi trường cần cho Paddle; dùng ảnh/render cũ, lưu engine/model/version/bbox/text/confidence và log. Không dành một tuần thử lại toàn bộ stack.', 2),
 task('Nối manifest đã chốt vào ledger ứng dụng.', 'Có 9 report targets/54 ô đích với kỳ/scope/status; xác định các tài liệu theo nhóm trước tinh chỉnh parser. Không chọn lại doanh nghiệp.', 1),
 task('Chọn một BCTC năm hợp nhất và đọc sáu ô tham chiếu.', 'Ưu tiên PDF FY2025 của HPG đã thu nếu còn tệp/hash đúng; nếu chọn VNM/FPT thì xác nhận nguồn. Có nhãn/cột/đơn vị/trang; quý 2026 không thay báo cáo năm.', 2),
 task('Dựng FastAPI, schema PostgreSQL và luồng candidate→duyệt.', 'Có migration SQLAlchemy/Alembic, API truy vấn/review, NUMERIC và audit trong transaction; một báo cáo tạo sáu candidates hoặc lý do thiếu; chỉ số reviewed được cung cấp.', 10),
 task('Dựng web React/TypeScript gọi FastAPI: bảng, duyệt, nguồn và CSV.', 'Có loading/error/empty; chọn mã/năm và xem nguồn từng ô; API trả số tiền dạng chuỗi chính xác, export từ backend; browser không kết nối trực tiếp DB.', 7),
 task('Kiểm luồng, lưu minh chứng và soạn phần Word/slide tuần 1.', 'Có run thật, ảnh bảng/nguồn và bảng lỗi; ghi mức tự động/assisted và giờ thực; slide demo UC-1, không trình bày lại tổng quan đề tài.', 2),
 ], ['Paddle adapter và lock sau khi chạy qua, tái sử dụng render/download', 'Một BCTC năm + sáu ô tham chiếu + DB/candidate/review mẫu', 'Màn hình UC-1, CSV và week-01.md'],
 'Cuối tuần 1 có UC-1 cơ bản cho một BCTC năm; Paddle là thay đổi trong luồng đã thử, không là một đợt nghiên cứu công cụ tách riêng.',
 'Timebox đổi Paddle khoảng 2 giờ ban đầu; nếu chưa chạy, ghi lỗi và xử lý trong giờ dự phòng/core, vẫn làm kho/bảng bằng số duyệt thủ công. Không báo số nhập tay là Paddle đã trích.',
 'FR01 FR03 FR05 FR08 FR10 FR12 IR01 IR02 NFR07 NFR08 DR03 DR04 FR02 FR09 FR11 FR15 FR16 FR17 FR31 DR01 DR02 IR03 IR04', 'TC01 TC02 TC03 TC06 TC08 TC10 TC11 TC23 TC24'),
week(2, 'Củng cố UC-1, mở dữ liệu nhiều kỳ cho UC-2', 'UC-1; chuẩn bị UC-2',
 'UC-1 một báo cáo đã có từ tuần 1; lỗi thực và ledger mẫu chính.', [
 task('Hoàn thiện schema, ràng buộc, transaction và revision từ DB tối thiểu.', 'Không dựng lại từ đầu; Alembic migration, NUMERIC/FK/unique, rollback và revision; pg_dump/pg_restore mẫu DB.', 5),
 task('Mở parser sáu trường cho báo cáo của các mã/kỳ tiếp theo.', 'Dùng fixture development; xử lý nhãn/cột/đơn vị khác mẫu đầu; một ô chưa trích được được giữ missing/ambiguous, không giả tự động.', 4),
 task('Hoàn thiện hàng đợi duyệt và các kiểm tra số liệu.', 'React review gọi API; blocking không publish; warning có lý do; revision conflict HTTP 409, không ghi đè lần duyệt khác.', 5),
 task('Bổ sung ba năm công ty đầu, bảng nhiều kỳ và CSV.', 'React giữ bộ chọn; FastAPI trả coverage/facts, CSV cùng bộ lọc; phân biệt current/comparative/revision và hiện thiếu rõ.', 5),
 task('Kiểm tải lại, raw version và chạy tiếp sau lỗi.', '304/cùng hash không nhân raw; lỗi một file không phá file khác; nhập tay có acquisition_mode=assisted.', 2),
 task('Báo cáo tiến độ đợt 1 và lưu demo UC-1.', 'Demo PDF→candidate→duyệt→bảng→nguồn→CSV; ghi đúng phần tự động/phần thủ công, giờ thực và lỗi.', 1),
 ], ['DB/review đã củng cố và fixture bố cục khác', 'Bảng nhiều kỳ của công ty đầu, CSV và audit', 'week-02.md + ảnh/video ngắn/log chạy'],
 'UC-1 ổn định hơn trên dữ liệu nhiều kỳ; có bộ số đã duyệt để tuần 3 làm UC-2, không đợi kiểm công cụ lại.',
 'Không đợi parser đạt độ chính xác cao ở mọi bố cục. Cho nhập/sửa có nguồn để hoàn thành luồng và đo công sức.',
 'FR02 FR06 FR07 FR09 FR11 FR14 FR15 FR16 FR17 FR18 FR33 FR31 DR01 DR02 DR05 DR06 IR03 IR04 NFR01 NFR03 BR01 BR02 BR03 BR12',
 'TC04 TC05 TC06 TC07 TC10 TC11 TC12 TC23 TC24 TC27'),
week(3, 'UC-2: biểu đồ, tỷ số và lưu phân tích', 'UC-2',
 'Kho số đã duyệt; bổ sung hai năm còn lại của công ty đầu bằng nguồn đúng scope.', [
 task('Viết engine delta/growth, CFO/LNST, tiền/tài sản và nợ phải trả/tài sản.', 'Chỉ dùng reviewed operands; nền tăng trưởng≤0, thiếu năm, assets≤0/cross-scope trả lý do; CFO âm được giữ.', 4),
 task('Dựng bảng và biểu đồ LNST/CFO theo năm.', 'React vẽ từ API phân tích; nhãn/trục/đơn vị, không nối số thiếu; kiểm số chính xác ở bảng bên cạnh biểu đồ.', 5),
 task('Gắn công thức, nguồn và lưu/mở lại lần phân tích.', 'API lưu/mở snapshot PostgreSQL; React mở operands/nguồn; bản dữ liệu mới không đổi snapshot đã lưu.', 5),
 task('Xuất bảng và nhận xét cùng bối cảnh.', 'CSV/JSON có nguồn/phiên bản, null/status; roundtrip mở lại không mất tiếng Việt/dấu âm.', 2),
 task('Kiểm ca thiếu và mẫu số không hợp lệ.', 'Có expected/actual cho các ca biên; số giả định chỉ làm fixture, tách khỏi case doanh nghiệp.', 1),
 task('Demo câu hỏi lợi nhuận tăng có đi cùng CFO không.', 'Ghi một nhận xét từ dữ liệu thật, ít nhất hai số nguồn và giới hạn; lưu giờ thực.', 1),
 ], ['Màn hình phân tích công ty đầu qua 2023–2025', 'engine + fixture công thức và snapshot mẫu', 'week-03.md'],
 'UC-2 có bảng/biểu đồ và tỷ số thực dùng được; mở lại đúng bối cảnh. Chưa bắt buộc DuPont/doanh thu/biên lợi nhuận.',
 'Nếu chưa đủ ba năm: hiển thị phần đã duyệt, ghi missing. Không dùng quý 2026 để thay năm 2025.',
 'FR25 FR26 FR27 FR32 FR34 FR35 BR11 DR08 NFR02 NFR05', 'TC18 TC19 TC21 TC23 TC24 TC25'),
week(4, 'UC-3 và demo cơ bản ba UC đầu', 'UC-1/2/3',
 'UC-1/2 dùng được; số đã duyệt của doanh nghiệp thứ hai, tối thiểu một năm trùng với công ty đầu.', [
 task('Thu và duyệt dữ liệu doanh nghiệp thứ hai.', 'Ít nhất một năm chung, sáu trường có số đã duyệt hoặc lý do thiếu; giữ scope cùng cơ sở.', 4),
 task('Viết truy vấn và engine so sánh doanh nghiệp tự chọn.', 'Chọn hai mã/kỳ; chuẩn hóa đơn vị; tái dùng công thức UC-2; khác scope hoặc thiếu operand không tạo so sánh giả.', 4),
 task('Dựng bảng/biểu đồ cạnh nhau và giải thích giới hạn.', 'React gọi API compare, đối chiếu LNST/CFO/tỷ số và nguồn; không xếp hạng/sàng lọc hay gọi nhóm khác ngành là benchmark ngành.', 4),
 task('Nối luồng tra cứu→phân tích→so sánh→lưu/xuất.', 'React điều hướng ba UC, dùng chung bộ chọn và API; error/empty/loading không làm hiện dữ liệu kỳ cũ.', 3),
 task('Chạy và ghi demo mốc 4 tuần; báo cáo đợt 2.', 'Ba tác vụ đi hết luồng, có file/run và dữ liệu thật; ghi phần assisted và danh sách lỗi; chưa tuyên bố nghiệm thu tất cả SRS.', 2),
 task('Dự phòng sửa lỗi chặn demo.', 'Ưu tiên nguồn/đơn vị/bộ chọn/số sai; không thêm giao diện nâng cao hoặc chỉ tiêu ngoài lát cắt.', 1),
 ], ['Ứng dụng demo UC-1/2/3', 'demo-week-04.md với kịch bản và kết quả', 'ảnh/CSV/snapshot của nhóm so sánh'],
 '**Mốc bắt buộc:** cuối tuần 4 demo cơ bản UC-1/2/3; UC-1 truy số/nguồn, UC-2 có biểu đồ/tỷ số, UC-3 so ít nhất hai công ty.',
 'Nếu nguồn thứ hai chậm: ưu tiên nhập số đã đối chiếu thủ công có provenance, báo assisted. Nếu luồng còn lỗi, chuyển tuần 5 sửa ba UC đầu trước cổ tức.',
 'FR32 FR31 IR03 NFR05 BR01', 'TC07 TC18 TC19 TC21 TC23'),
week(5, 'Hoàn thiện ba công ty, kiểm chất lượng ba UC đầu', 'UC-1/2/3',
 'Demo tuần 4 và danh sách lỗi; ledger chín báo cáo chính.', [
 task('Thu/xác nhận chín BCTC HPG/VNM/FPT 2023–2025 và rà 54 targets.', 'Mọi target có trạng thái; cố gắng đủ số nhưng thiếu phải có lý do và báo độ đầy đủ chưa đạt; kiểm bản sửa/phạm vi FPT.', 6),
 task('Sửa parser theo lỗi thật trên tập phát triển.', 'Lưu fixture/layout và lỗi trước–sau; không xem/chỉnh theo tập kiểm đã giữ riêng.', 3),
 task('Mở so sánh cả ba mã và chuỗi nhiều năm.', 'Bảng/biểu đồ hiển thị đúng số/thiếu; không đổi kỳ hoặc scope âm thầm; nguồn từng ô truy được.', 3),
 task('Freeze tập kiểm OCR/trích số và đo thử công sức.', '20–30 trang mục tiêu từ nhiều bố cục; ghi số trang/ô thực và lineage. Nếu chưa đủ mẫu, báo cỡ mẫu nhỏ thay vì nhân bản trang.', 3),
 task('Sửa lỗi và rà yêu cầu cho UC-1/2/3.', 'Lập ma trận đã chạy/chưa chạy, các chức năng bổ sung F03 có tiêu chí riêng; không tự pass yêu cầu SRS bằng tick.', 3),
 task('Chốt demo mốc 5 tuần và cập nhật kế hoạch bằng giờ thực.', 'Cả ba mã chọn được; phân tích/so sánh ổn định trên phần số đã duyệt; báo đủ/thiếu dữ liệu tách khỏi đủ chức năng.', 2),
 ], ['ledger chín reports/54 ô đã rà và báo cáo coverage', 'freeze-manifest.json + extraction-error-log.csv', 'demo-week-05.md và requirement-status.csv'],
 '**Mốc cam kết triển khai:** tuần 5 có bản cơ bản ba UC đầu cho HPG/VNM/FPT; lỗi dữ liệu/nguồn còn lại phải được công bố, không giả hoàn tất.',
 'Không mở thêm doanh nghiệp, doanh thu/DuPont hoặc benchmark ngành. Nếu chưa đạt, ưu tiên sửa và giảm phần UC-4 tùy chọn.',
 'FR36 DR07 NFR10', 'TC01 TC07 TC12 TC26'),
week(6, 'UC-5: thông báo và lịch sử cổ tức', 'UC-5',
 'Kho ba công ty; nguồn IR/VSDC và notice mẫu lịch sử để phát triển.', [
 task('Viết một adapter tự phát hiện notice theo doanh nghiệp/cửa sổ.', 'Có log từ catalog/search chính thức tới notice thật của mẫu; seed từng URL đếm assisted, không đạt FR04.', 5),
 task('Trích và duyệt notice/components.', 'Tách đúng năm lợi nhuận/đợt, loại quyền, DPS, ngày; notice hỗn hợp không đẩy toàn bộ vào năm đăng.', 3),
 task('Làm liên kết trùng, sửa và hủy đúng đối tượng.', 'Giữ old/current; sửa amount không cộng hai lần; hủy record notice không tự hủy chính sách/annual DPS.', 4),
 task('Lập coverage từng mã/năm và tổng DPS có điều kiện.', 'Không tìm thấy khác 0; partial/unknown khác complete_as_of; chặn cộng khi basis chưa rõ.', 3),
 task('Dựng timeline/bảng cổ tức và nguồn.', 'Tách lịch trả với xác nhận thực trả; FY2025 có thể có thông báo 2026; ngày đã qua không tự thành paid.', 2),
 task('Báo cáo đợt 3 và ca notice hỗn hợp/sửa.', 'Một hồ sơ từ nguồn tới màn hình; ghi số notice đã rà, tự động/assisted và các mục unresolved.', 1),
 ], ['notices/components/relations và coverage ledger', 'màn hình lịch sử cổ tức có trạng thái', 'week-06.md + fixture vòng đời'],
 'UC-5 đọc được lịch sử quan sát, không giả đầy đủ; có discovery notice thật hoặc FR04 được báo chưa đạt.',
 'Nếu nguồn chặn: thử nguồn IR chính thức phù hợp; thu thủ công để demo nhưng báo thiếu FR04, không tự đổi nghĩa vụ nghiệm thu.',
 'FR04 FR13 FR19 FR20 FR21 FR22 FR23 FR24 FR28 BR04 BR05 BR06 BR07 BR08 BR09 BR10 DR04 DR07',
 'TC02 TC08 TC09 TC13 TC14 TC15 TC16 TC17 TC20'),
week(7, 'UC-5: cơ sở tiền mặt và cầu nối CFO theo ca', 'UC-2/5',
 'Một BCTC của HPG/VNM/FPT có operands G02/cầu nối đọc được; không dùng DHG thay case nghiệm thu chính.', [
 task('Đọc/duyệt CAPEX và khoản phân phối chủ sở hữu cho một ca.', 'Cùng kỳ/scope/unit với CFO; lưu nhãn nguồn và loại khoản chi gộp/tách; không abs mọi dòng đầu tư.', 4),
 task('Làm cầu nối LNTT→CFO từ các dòng cấu thành.', 'Một ca thật; leaf chỉ cộng một lần, subtotal chỉ kiểm; có residual/tolerance và nguồn từng dòng. Hai kỳ chỉ thêm khi đủ.', 6),
 task('Ghép hàm bao phủ CFO−CAPEX và các khoản chi.', 'Có công thức/operands/điều kiện; CFO âm giữ dấu; chi=0 chặn tỷ số; không gọi kết quả là FCFE.', 4),
 task('Dựng biểu đồ cầu nối và bảng bao phủ có nguồn.', 'Người dùng hiểu khoản nào đóng góp CFO và khoản chi được bao phủ thế nào; khoản gộp không hiện thành cổ tức thường đã tách.', 3),
 task('Kiểm thiếu/sai dấu/sai kỳ và snapshot kết quả.', 'Ca thiếu trả lý do; fixture tách ca thật; xuất/mở lại giữ operand/formula version.', 2),
 task('Ghi nhận xét đầu tư có căn cứ và giới hạn.', 'Lưu câu hỏi cần đọc thêm với số/nguồn; không suy khả năng trả cổ tức tương lai từ một tỷ số.', 1),
 ], ['bridge-lines.csv và cầu nối có residual', 'G02 case có operands và định nghĩa khoản chi', 'week-07.md + snapshot'],
 'Ít nhất một ca mẫu chính có cầu nối và bao phủ chạy được; không ép khớp bằng dòng bù. Nhiều ca/E05/E10 chỉ khi đủ thời gian và quyết định kích hoạt.',
 'Nếu không đủ dòng phân rã: ghi unresolved và tiếp tục đọc một báo cáo khác trong ba mã; không dùng sáu số tổng để dựng phân rã giả.',
 'E01 E02 E03 E04 E05 E06 E07 E08 E09 E10 D01 D02 D03 D04 D11',
 'P01 P02 P03 P04 P05 P06 P07 P08 P09 P10 P11 TC-D01 TC-D02 TC-D03 TC-D04 TC-D11'),
week(8, 'UC-5: basis DPS, hồ sơ lưu và đo OCR', 'UC-5',
 'Ledger sự kiện, ca tiền mặt/cầu nối, tập kiểm đã freeze tuần 5.', [
 task('Thu/duyệt sự kiện vốn cần cho HPG/FPT và trạng thái basis VNM.', 'Loại/tỷ lệ/ngày hiệu lực có nguồn; không suy ngày basis từ ngày record hoặc coi mọi phát hành là split.', 5),
 task('Ghép điều chỉnh DPS và chặn khi chưa đủ cơ sở.', 'Giữ DPS gốc; chỉ chain hợp lệ; unsupported/unresolved/tương lai bị chặn; chưa đủ dữ liệu vẫn là đầu ra hợp lệ có lý do.', 3),
 task('Dựng lịch sử cổ tức và biểu đồ có trạng thái so sánh.', 'Annual/growth chỉ khi coverage và basis đủ; không cộng cổ tức cổ phiếu vào thu nhập tiền mặt.', 3),
 task('Lưu hồ sơ nhận xét/câu hỏi, xuất và replay offline.', 'Bối cảnh/nguồn/version/checksum đầy đủ; sửa dữ liệu không thay snapshot cũ; gói hỏng báo lỗi.', 3),
 task('Đo Paddle/Tesseract và B0/B1/B2 trên tập kiểm đã giữ.', 'Cùng trang/ô; ghi đúng/sai/thiếu metric-value-unit-period-scope và thời gian/công sức; chỉ có một người thì ghi tự kiểm.', 4),
 task('Báo cáo đợt 4 và freeze chức năng ưu tiên.', 'Demo UC-1/2/3/5; bảng actual/pass/fail/not_run; kết quả OCR không khẳng định tăng lợi nhuận đầu tư.', 2),
 ], ['corporate-action ledger và raw/reference DPS', 'dossier + export/replay bundle', 'ocr-evaluation.csv, report-week-08.md'],
 'Bốn UC ưu tiên có luồng dùng được, kể cả trạng thái chưa đủ dữ liệu; công bố phần chưa đạt SRS. Freeze feature trước tuần 9.',
 'Không đủ basis thì chặn điều chỉnh; không dựng số giả để demo. Nếu core còn lỗi, tuần 9 không làm UC-4.',
 'D05 D06 D07 D08 D11 D12 FR34 FR35 FR36 NFR02 NFR10',
 'TC-D05 TC-D06 TC-D07 TC-D08 TC-D11 TC-D12 TC16 TC20 TC24 TC25 TC26'),
week(9, 'Ổn định hệ thống; UC-4 có điều kiện', 'Kiểm hệ thống; UC-4 sau gate',
 'Feature freeze tuần 8; ma trận các yêu cầu còn thiếu và bộ demo bốn UC.', [
 task('Rà toàn bộ yêu cầu/ca kiểm hiện hành và sửa lỗi trọng yếu.', '91 mã/51 TC có owner/mốc/status/evidence; yêu cầu chưa đạt giữ fail/not_run hoặc có CR, không đổi thành pass.', 3),
 task('Backup/restore DB, raw, config và snapshots vào thư mục sạch.', 'pg_dump/pg_restore cùng raw/config/migration; hash/revision khớp và replay snapshot; không copy data directory đang chạy làm backup.', 5),
 task('Đo hiệu năng và kiểm an toàn local theo SRS.', 'TC30 đúng bộ tải chuẩn, TC31 localhost/path/HTML/log; dữ liệu tạo kiểm tải ghi synthetic, không tính thành mẫu nghiên cứu mới.', 3),
 task('Nếu gate đạt: danh sách theo dõi và công bố mới tối thiểu.', 'Doanh nghiệp tự chọn; xem cập nhật/old-new và mở phân tích. Không sàng lọc hoặc cảnh báo tiêu chí. Nếu core lỗi, dành giờ sửa core và ghi UC-4 hoãn.', 3),
 task('Walkthrough tác vụ với người dùng hoặc ghi rõ tự đánh giá.', 'Đo tìm số/nguồn, LNST–CFO, so sánh và cổ tức; giờ/lỗi đọc PDF thủ công làm đối chứng tác vụ.', 2),
 task('Nhật ký tuần và danh sách lỗi cuối.', 'Chốt lỗi phải sửa trước nộp, dữ liệu nào chưa đủ và UC-4 có làm/hoãn; không thêm hướng ML/định giá.', 1),
 ], ['restore-check.json và yêu cầu/TC có bằng chứng', 'performance/local-check logs + walkthrough.md', 'UC-4 tối thiểu hoặc quyết định hoãn có lý do'],
 'Luồng ưu tiên ổn định và restore/replay kiểm được. UC-4 không được lấy giờ sửa lỗi dữ liệu/tính toán để kịp thêm tính năng.',
 'TC30 là kiểm tải khác bộ pilot chín báo cáo; nếu chưa đủ bộ theo SRS phải ghi chưa đạt, hoặc lập CR phù hợp, không báo phép đo chín PDF là TC30 pass.',
 'FR38 IR05 NFR03 NFR04 NFR06 NFR09 NFR05 NFR10', 'TC05 TC11 TC25 TC27 TC29 TC30 TC31'),
week(10, 'Nghiệm thu thử, đóng gói và báo cáo cuối', 'UC-1/2/3/5 và phần UC-4 đã làm',
 'Ứng dụng freeze, hồ sơ đo, danh sách lỗi, raw/DB và snapshots.', [
 task('Sửa lỗi chặn sử dụng và chạy lại các ca bị ảnh hưởng.', 'Số/nguồn đúng, không mất audit/snapshot; không mở thêm chức năng.', 4),
 task('Chạy từ môi trường sạch theo README.', 'Khôi phục dependency/model/config, có hướng dẫn nguồn/model offline nếu cần; một người khác hoặc tự chạy mới ghi rõ.', 3),
 task('Xuất ba case thật của mẫu chính.', 'Mỗi case có số/nguồn/phạm vi/coverage/giới hạn và câu hỏi người dùng; không bắt buộc cả ba đều ra kết quả điều chỉnh DPS.', 3),
 task('Tổng hợp đánh giá và ma trận nghiệm thu.', 'Tách tự động/review/assisted, số đếm/tỷ lệ/giờ; tất cả M được báo pass/fail/not_run hoặc CR, không gọi hoàn tất nếu còn thiếu.', 3),
 task('Viết báo cáo cuối và chuẩn bị demo ngắn theo UC.', 'Phân rã đầu vào→xử lý→đầu ra→minh chứng; ít lý thuyết tổng quan; báo giới hạn và chức năng đề xuất tách đã chạy.', 4),
 task('Đóng gói, sao lưu và kiểm tệp nộp cuối.', 'MD/app/evidence thống nhất; có danh sách file/hash và bản lưu tiến độ; dự phòng lỗi nộp.', 1),
 ], ['release bundle + README + backup', 'ba case và acceptance-status.csv', 'báo cáo cuối Markdown, kịch bản demo; bản xuất theo yêu cầu trường khi cần'],
 'Bộ bàn giao chạy/tái lập được và báo đúng phần đã đạt/chưa đạt. Không dùng số tick checklist làm tỷ lệ chất lượng đồ án.',
 'Nếu còn yêu cầu M chưa đạt, báo thiếu và hướng xử lý/CR cho thầy; không tự giảm yêu cầu hoặc hứa đầy đủ.',
 'FR37 FR38 FR36 IR05 NFR01 NFR02 NFR09 NFR10', 'TC23 TC24 TC25 TC26 TC28 TC29'),
]


REPORTS = {
1: {
 'word': ['UC-1 nhỏ: một BCTC năm, sáu trường kế thừa bảng dữ liệu Báo cáo 2, kỳ/scope. Mẫu thử cũ là ba dòng × hai cột; tải/đọc/render được tái sử dụng, chỉ thay engine OCR.', 'Luồng đã ghép: text/Paddle→candidate→duyệt→PostgreSQL→bảng/nguồn/CSV. Gắn ảnh bảng, một ô nguồn và log engine.', 'Bảng số ô đúng/sai/thiếu trước và sau duyệt nếu đã đo; lỗi còn lại, phần nhập tay và ba việc tuần 2. Chưa đo thì ghi chưa đo.'],
 'slides': ['UC-1 tuần này: một báo cáo vào, bảng sáu chỉ tiêu có nguồn ra.', 'Một sơ đồ ngắn: pipeline cũ giữ lại, bước OCR đổi Paddle.', 'Ảnh hoặc demo trực tiếp bảng→ô số→trang nguồn→CSV.', 'Kết quả đã chạy, lỗi cần xử lý và đầu ra tuần 2.'],
 'demo': 'Chọn báo cáo năm→xem một ô đã duyệt→mở trang/cột nguồn→xuất CSV; chỉ vị trí Paddle trong run log.',
 'ask': 'Luồng khai thác này đã đủ cơ bản cho UC-1 chưa; cần ưu tiên cải thiện trích số hay cách tra cứu nguồn?'},
2: {
 'word': ['Phần cải thiện so tuần 1: bố cục/kỳ nào đã xử lý; bảng ledger số báo cáo/ô đã duyệt và còn thiếu. Rà 18 targets của ba năm công ty đầu, không đồng nhất targets với số hợp lệ.', 'Một ca sai cột/đơn vị hoặc bản sửa: candidate→issue→sửa/duyệt→audit; kiểm chạy lại không nhân dữ liệu.', 'Bảng nhiều kỳ công ty đầu, định nghĩa sáu metrics từ Báo cáo 2 và dữ liệu dùng cho UC-2. Gộp tuần 1 vào báo cáo hai tuần; phần tự động và assisted ghi riêng.'],
 'slides': ['UC-1 từ một báo cáo sang nhiều kỳ: kết quả tăng thêm.', 'Một lỗi dữ liệu thật và cách xử lý có audit.', 'Demo bảng nhiều kỳ→nguồn→xuất dữ liệu.', 'Coverage hiện tại và kế hoạch biểu đồ/tỷ số tuần 3.'],
 'demo': 'Mở bảng ba năm; sửa một candidate có nguồn, kiểm bản trước/sau; chạy lại không nhân bản.',
 'ask': 'Định nghĩa sáu trường, cách hiển thị thiếu và phạm vi báo cáo đã phù hợp chưa?'},
3: {
 'word': ['Câu hỏi người dùng: lợi nhuận tăng có đi cùng CFO không? Nêu kỳ/scope và các số đã duyệt.', 'Đầu vào→công thức có điều kiện→bảng/biểu đồ; một ca mẫu số 0/âm hoặc thiếu năm và cách hiển thị.', 'Một nhận xét từ số thật, nguồn operands, snapshot mở lại và giới hạn diễn giải; chuẩn bị dữ liệu so sánh.'],
 'slides': ['UC-2 trả lời câu hỏi LNST–CFO của công ty nào/kỳ nào.', 'Biểu đồ thực tế và nhận xét ngắn gắn hai số.', 'Một tỷ số: công thức, nguồn và điều kiện không tính.', 'Demo lưu/mở lại; bước tiếp theo là so sánh công ty.'],
 'demo': 'Chọn công ty/giai đoạn→xem biểu đồ→mở công thức/nguồn CFO-LNST→lưu và mở lại nhận xét.',
 'ask': 'Bảng/biểu đồ đã giúp đọc biến động rõ chưa; nên phân rã khoản nào khi CFO thay đổi?'},
4: {
 'word': ['Mốc demo ba UC: bảng từng UC gồm input, xử lý, output và đường dẫn minh chứng thực chạy.', 'Ca so sánh hai công ty cùng kỳ/scope: số tuyệt đối, tỷ số, biểu đồ và một trường hợp không đủ cơ sở.', 'Kết quả walkthrough, phần tự động/assisted, lỗi còn lại; tuần 5 mở HPG/VNM/FPT. So sánh khác ngành chưa là benchmark.'],
 'slides': ['Mốc tuần 4: những phần UC-1/2/3 đã chạy.', 'UC-1/2: bảng có nguồn và biểu đồ một công ty.', 'UC-3: bảng/biểu đồ hai công ty, cùng kỳ/phạm vi.', 'Demo liên thông ba UC và lỗi cần sửa ở tuần 5.'],
 'demo': 'Tra cứu một số→phân tích xu hướng→chọn công ty thứ hai→so sánh→nguồn→lưu/xuất.',
 'ask': 'Ba UC đầu đã thể hiện đúng hướng nền tảng dữ liệu hỗ trợ phân tích chưa; thao tác nào cần đơn giản hơn?'},
5: {
 'word': ['Ma trận HPG/VNM/FPT×2023–2025: chín reports/54 targets, số đã duyệt/thiếu và lý do; không chỉ báo số PDF tải được.', 'Các lỗi parser/bộ chọn/phạm vi đã sửa từ demo tuần 4; minh chứng so sánh ba công ty.', 'Giờ thu/duyệt thực, tập kiểm giữ riêng và quyết định giữ phạm vi; dữ liệu còn thiếu ảnh hưởng chỉ tiêu nào.'],
 'slides': ['Ba công ty đã dùng được ở mức nào: bảng coverage.', 'Một thay đổi quan trọng so demo tuần 4.', 'Demo nhóm ba mã và chỉ rõ dữ liệu thiếu.', 'Điều kiện chuyển sang cổ tức; không mở thêm phạm vi.'],
 'demo': 'Chuyển HPG/VNM/FPT và năm; so sánh nhóm; mở một số/thiếu có lý do; lưu cấu hình.',
 'ask': 'Phần core đã đủ để ưu tiên hồ sơ cổ tức chưa; cần sửa lỗi nào trước khi thêm UC-5?'},
6: {
 'word': ['Câu hỏi UC-5: mỗi khoản cổ tức thuộc năm lợi nhuận nào, ở trạng thái nào? Nêu nguồn và cửa sổ đã tra cứu.', 'Một notice hỗn hợp hoặc bản sửa: tách components/quan hệ old-current; phân biệt lịch trả và đã trả.', 'Timeline và coverage; annual DPS được tính/chặn thế nào; thiếu discovery FR04 hoặc phần assisted báo riêng.'],
 'slides': ['UC-5: lịch sử cổ tức cần đọc theo năm lợi nhuận.', 'Một thông báo→components và trạng thái có nguồn.', 'Demo timeline/lịch sử và một ca sửa/hủy.', 'Dữ liệu chưa đủ và kế hoạch phân tích cơ sở tiền mặt.'],
 'demo': 'Mở notice→thành phần theo năm→bản sửa nếu có→timeline; hiện nguyên nhân annual chưa được tính.',
 'ask': 'Cách phân biệt công bố/lịch trả/thực chi và độ đầy đủ lịch sử đã rõ chưa?'},
7: {
 'word': ['Ca thật trong ba mã: LNTT, các dòng cầu nối và CFO; nguồn từng dòng, subtotal/leaf và residual.', 'CFO−CAPEX−khoản chi: định nghĩa khoản chi, công thức, scope và số tiền; nguồn gộp phải gọi đúng tên.', 'Nhận xét/câu hỏi người dùng từ kết quả, giới hạn không suy FCFE hay cổ tức tương lai; điều kiện thiếu operands.'],
 'slides': ['Vấn đề ca thật: lợi nhuận và tiền thay đổi ra sao.', 'Biểu đồ cầu nối CFO với khoản đóng góp chính.', 'Bảng bao phủ khoản chi, công thức và nhãn khoản chi.', 'Demo truy nguồn; điều kết quả cho phép và chưa cho phép kết luận.'],
 'demo': 'Chọn ca→cầu nối CFO→một dòng nguồn→bao phủ→operands→lưu câu hỏi đọc thêm.',
 'ask': 'Cách giải thích cơ sở tiền mặt của khoản phân phối đã đúng nghiệp vụ và hữu ích chưa?'},
8: {
 'word': ['Sự kiện vốn và basis DPS: DPS gốc/chuỗi tham chiếu được phép tính, nguồn ngày hiệu lực, ca bị chặn.', 'Kết quả OCR cùng tập trang/ô: đúng/sai/thiếu, nhầm cột/đơn vị, thời gian; B0/B1/B2 và tự/độc lập kiểm khai rõ.', 'Hồ sơ UC-5 xuất/replay, ma trận bốn UC ưu tiên, phần còn thiếu và quyết định feature freeze.'],
 'slides': ['Vì sao vẫn giữ sự kiện cổ phiếu trong phân tích tiền mặt.', 'DPS gốc/tham chiếu hoặc lý do chặn từ một ca có nguồn.', 'Kết quả Paddle–Tesseract bằng số đếm và giới hạn mẫu.', 'Demo hồ sơ cổ tức lưu/mở lại; trạng thái core trước tuần 9.'],
 'demo': 'Xem basis của một chuỗi→kết quả hoặc lý do chặn→hồ sơ→export→replay đúng phiên bản.',
 'ask': 'Điều kiện so sánh DPS và thiết kế đo OCR đã đủ thuyết phục; phần nào cần công bố giới hạn rõ hơn?'},
9: {
 'word': ['Kiểm backup→restore→replay: file/hash/revision và kết quả thật; hiệu năng ghi đúng cấu hình/bộ kiểm.', 'Walkthrough tác vụ: thời gian/lỗi với đọc PDF thủ công, người thử và giới hạn mẫu; không khẳng định tăng lợi nhuận đầu tư.', 'UC-4 có làm/hoãn theo gate; nếu làm, mô tả danh sách tự chọn/công bố/old-new; danh sách lỗi trước nộp.'],
 'slides': ['Core ổn định: những kiểm tra đã chạy và còn thiếu.', 'Minh chứng restore/replay hoặc kết quả hiệu năng.', 'Walkthrough và UC-4 tối thiểu nếu đã làm.', 'Các lỗi cuối và quyết định ưu tiên trước nộp.'],
 'demo': 'Restore một gói→mở snapshot; nếu UC-4 đã chạy thì mở cập nhật sang phân tích, nếu chưa thì báo hoãn.',
 'ask': 'Những giới hạn nào cần ghi vào báo cáo cuối; còn lỗi nào chặn nghiệm thu?'},
10: {
 'word': ['Kết quả theo UC: chỉ phần đã chạy, đầu vào/xử lý/đầu ra và ba case HPG/VNM/FPT có bằng chứng.', 'Phương pháp và kết quả kiểm: coverage, OCR, công sức, replay/restore và pass/fail/not_run từng yêu cầu; giả định/tập kiểm riêng.', 'Hướng dẫn chạy, phạm vi/giới hạn, chức năng hoãn và nghiên cứu tốt nghiệp đề xuất; không lặp toàn bộ thư viện khảo sát.'],
 'slides': ['Kết quả sản phẩm và phạm vi đã chốt.', 'Demo UC-1→UC-2→UC-3 trên dữ liệu thật.', 'Demo UC-5: lịch sử, cơ sở tiền mặt/basis và nguồn.', 'Một bảng số đo chính; giới hạn/chưa đạt và hướng tiếp theo.'],
 'demo': 'Kịch bản liền mạch 5–7 phút với dữ liệu đã lưu; có bản backup và ảnh/log thật nếu nguồn mạng không sẵn.',
 'ask': 'Xác nhận kết quả, phạm vi chưa đạt và phần nên phát triển tiếp; không tự ghi đã được thầy phê duyệt.'},
}


def build():
    for w in W:
        w['reporting'] = REPORTS[w['n']]
    plan = {'version': 6, 'id': 'fap-hpg-vnm-fpt-next-10weeks-v6', 'updated': '2026-10-11',
            'legacy': {'version':5,'id':'fap-hpg-vnm-fpt-next-10weeks-v5','retained_task_ids':['W01-01','W01-02','W01-03','W02-02']},
            'legacy_sources': [{'version':5,'id':'fap-hpg-vnm-fpt-next-10weeks-v5','retained_task_ids':['W01-01','W01-02','W01-03','W02-02']},{'version':4,'id':'fap-hpg-vnm-fpt-next-10weeks-v4','retained_task_ids':[]}],
            'srs': 'SRS-FAP-01 v3.3', 'weeks': W,
            'start_date': None, 'start_note': 'Tuần 1 là tuần làm tiếp từ mốc hiện tại; chọn ngày bắt đầu trong HTML. Không phải tuần đầu học kỳ.',
            'user_deadline': 'Còn 10 tuần; trong 4–5 tuần tới phải thể hiện cơ bản UC-1/2/3.',
            'hours_note': '195 giờ dự toán, gồm nghiên cứu đúng task/code/kiểm/ghi báo cáo và dự phòng; khoảng 16–24 giờ mỗi tuần. Người thực hiện chưa cung cấp quỹ giờ thực. Không cộng ngân sách này vào baseline cũ.',
            'baseline': 'Đã thử pipeline Tesseract trên VNM Q1/2026: ba dòng × hai cột, 6/6 ô khớp đối chiếu thủ công. Có crawler và các prototype khác. Chưa có Paddle chạy, ứng dụng hoặc corpus năm đã duyệt hoàn chỉnh.',
            'progress_note': 'Tất cả việc tương lai mặc định chưa đánh dấu; quyết định chọn mẫu/stack đã có không chứng minh việc cài/triển khai đã hoàn thành.',
            'reports': [{'week': n, 'title': title} for n, title in [(2,'UC-1 nguồn→bảng'),(4,'Demo cơ bản UC-1/2/3'),(5,'Mốc kiểm ba công ty'),(6,'Lịch sử và vòng đời cổ tức'),(8,'UC-5 và kết quả OCR'),(10,'Nghiệm thu thử/báo cáo cuối')]],
            'retired': ['FR29','FR30','D09','D10','TC22','TC-D09','TC-D10'],
            'planned_output_root': 'data-sets/fap/execution-v4/ (Git-ignore; cần sao lưu raw/DB riêng)',
            'planned_journal_root': 'docs/research-platform/execution-v4/ (tạo khi làm, không ghi tiến độ giả)',
            'feature_note': 'F03 so sánh nhiều công ty và tương tác biểu đồ là lát cắt sản phẩm đã chọn; ghi tiêu chí bổ sung riêng, không tự coi danh mục 38 chức năng đã thành toàn bộ SRS.',
            'gates': [{'week': n, 'title': title} for n,title in [(1,'UC-1 cơ bản một báo cáo; ghép Paddle'),(2,'UC-1 nhiều kỳ, đủ nền UC-2'),(4,'Demo cơ bản UC-1/2/3'),(5,'Ba công ty, rà chín reports/54 targets'),(8,'Luồng UC-1/2/3/5 và feature freeze'),(9,'UC-4 chỉ khi core ổn định'),(10,'Bàn giao và trạng thái nghiệm thu thật')]]}
    scope = json.loads((ROOT/'config/pilot-scope.json').read_text(encoding='utf-8'))
    assert [x['ticker'] for x in scope['issuers']] == ['HPG','VNM','FPT']
    assert len(W) == 10 and sum(w['hours'] for w in W) == 195
    srs = (BASE/'22-srs-dac-ta-yeu-cau-phan-mem.md').read_text(encoding='utf-8')
    req = set(re.findall(r'^\*\*((?:FR|BR|DR|IR|NFR|E|D)\d{2})\b', srs, re.M))
    mapped = {r for w in W for r in w['requirements']}
    assert req == mapped, ('Requirement coverage', sorted(req-mapped), sorted(mapped-req))
    active_tests = set(re.findall(r'^\| (TC\d{2}) —',srs,re.M)) | set(re.findall(r'^\| (TC-D\d{2}) \|',srs,re.M)) | {f'P{i:02d}' for i in range(1,12)}
    mapped_tests = {t for w in W for t in w['tests']}
    assert active_tests == mapped_tests, ('Test planning coverage', sorted(active_tests-mapped_tests), sorted(mapped_tests-active_tests))
    assert len(req)==91 and len(active_tests)==51
    plan['coverage'] = {'active_requirements': len(req), 'planned_tests': len(active_tests),
                        'status': 'mapped to weeks, not executed or passed',
                        'conditional_note': 'E05/E10 và D có điều kiện: ghi kích hoạt/not_applicable có lý do; không ép có chain/case nhiều kỳ khi thiếu nguồn.'}
    (BASE/'checklist-10-tuan-v4.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    intro = '''# Kế hoạch 10 tuần tiếp theo — HPG, VNM, FPT và PaddleOCR

Cập nhật **11/10/2026**, kế hoạch **v6**, theo hạn còn **10 tuần** do người thực hiện cung cấp. **Tuần 1 ghép Paddle vào pipeline đã thử và làm UC-1 cơ bản; cuối tuần 4 demo UC-1/2/3; tuần 5 hoàn thiện ba doanh nghiệp.** Đây là tuần làm tiếp từ mốc hiện tại, không đếm lại tuần học kỳ. Chi tiết [tuần 1](33-ke-hoach-chi-tiet-tuan-01.md), [tuần 2](34-ke-hoach-chi-tiet-tuan-02.md), [sáu metrics kế thừa Báo cáo 2 và dữ liệu bổ sung](35-dac-ta-metrics-tu-bao-cao-02.md). Quyết định web thay thiết kế pilot: có API, frontend và migration; tăng dự toán, giữ ID task để truy vết, dùng khóa lưu v6 riêng.

Mốc hiện tại: thử công cụ/pipeline Tesseract trên một BCTC VNM quý I/2026, ba dòng × hai cột, 6/6 ô khớp đối chiếu thủ công; có thêm crawler và prototype tính toán. Điều này hỗ trợ tính khả thi ban đầu của pipeline, chưa chứng minh PaddleOCR, trích xuất tổng quát hoặc ứng dụng đã chạy. [Minh chứng công cụ](reports/dot-01-tuan-01-02/thu-nghiem-cong-cu.md).

Phạm vi: **HPG/VNM/FPT, BCTC năm 2023–2025, ưu tiên hợp nhất; chín báo cáo và 54 ô lõi**. [Quyết định stack](31-chot-pham-vi-va-stack-paddleocr.md), [manifest](../../config/pilot-scope.json), [SRS v3.3](22-srs-dac-ta-yeu-cau-phan-mem.md). React/TypeScript + FastAPI/Python 3.12 + PostgreSQL; pandas cho phân tích, PaddleOCR chính, Tesseract đối chứng. Không mở thêm doanh nghiệp, DuPont, ML, danh mục hoặc định giá.

## Cách dùng và ngân sách

[Checklist HTML đánh dấu/lưu tiến độ](checklist-10-tuan-v4.html) và [JSON kế hoạch](checklist-10-tuan-v4.json) được sinh từ cùng nguồn; giữ tên tệp để URL đang mở tiếp tục dùng được, nội dung hiện là v6. Tick phản ánh việc người dùng tự xác nhận; không tự nghiệm thu. Khi chuyển bản lưu v5: giữ ngày/nhật ký/giờ và tick bốn task không đổi W01-01/02/03, W02-02; các task phụ thuộc web/API/DB cần kiểm lại nên chưa chuyển tick. Bản v4 chỉ chuyển ngày/nhật ký/giờ. Bản lưu gốc vẫn giữ nguyên; có thể xuất JSON để đối chiếu.

**195 giờ dự toán**, khoảng **16–24 giờ/tuần**, đã gồm ghi báo cáo và phần dự phòng trong task. Quỹ giờ thực chưa được cung cấp; đây là ước lượng cần kiểm sau tuần 2, không phải cam kết đủ mọi nghĩa vụ trong 195 giờ và không cộng vào baseline 167 giờ/ước lượng 98–150 giờ cũ. Nếu quỹ thấp hơn, ưu tiên lỗi core, giữ demo bằng dữ liệu đã kiểm thủ công và hoãn UC-4; phần tự động chưa đạt vẫn báo chưa đạt. Không tự giảm nghĩa vụ M của SRS.

Mỗi tuần chia 4–5 buổi: đầu tuần chuẩn bị đúng phần cần, tái sử dụng công cụ đã thử; các buổi giữa viết/ghép code; cuối tuần kiểm luồng, lưu bằng chứng và giờ thật. Hạn/ngày cụ thể tính theo ngày bạn chọn trong HTML. Báo cáo định kỳ cuối tuần 2/4/6/8/10, thêm mốc kiểm tuần 5 theo yêu cầu. Mỗi tuần đều có gợi ý Word/slide để ghi kết quả khi làm; tuần lẻ có thể lưu nháp rồi gộp vào đợt hai tuần. Không phải tạo mười bộ Word/slide hoàn chỉnh hoặc báo cáo kết quả chưa chạy.

**Cách soạn:** Word giữ input→xử lý→output, code/run và số đo, khoảng 1–2 trang cho cập nhật tuần, gộp 3–5 trang nếu phù hợp đợt hai tuần. Slide dùng 4 ý cụ thể bên dưới, mỗi slide một ý, ưu tiên bảng/biểu đồ/demo; không lặp tổng quan đề tài hoặc giải thích lại công cụ đã kiểm. Các gợi ý là nội dung cần soạn, chưa tạo file .docx/.pptx.

Nơi lưu đầu ra đề xuất: `data-sets/fap/execution-v4/` cho PDF/ảnh/DB/kết quả, phải sao lưu riêng vì Git-ignore; `docs/research-platform/execution-v4/week-NN.md` cho nhật ký/minh chứng. Đường dẫn là mục tiêu tạo khi thực hiện, chưa có output không được tick.

## Mốc demo 4–5 tuần: thế nào là đủ cơ bản?

| UC | Demo cuối tuần 4 | Bổ sung tuần 5 |
|---|---|---|
| UC-1 | Chọn mã/năm, xem sáu chỉ tiêu đã duyệt hoặc lý do thiếu, truy xuất trang nguồn, xuất CSV; có luồng duyệt/sửa | Chọn được HPG/VNM/FPT; ledger chín báo cáo/54 ô được rà |
| UC-2 | Một công ty có bảng/biểu đồ nhiều kỳ, LNST/CFO, tỷ số có điều kiện; mở số nguồn, lưu nhận xét | Chạy trên phần dữ liệu đã duyệt của ba mã, sửa lỗi bộ chọn/đơn vị/thiếu |
| UC-3 | Chọn ít nhất hai công ty cùng năm/scope; xem bảng/biểu đồ cạnh nhau và tỷ số | So sánh nhóm ba mã, nhiều năm khi đủ nguồn; giải thích khác ngành |

Đây là demo chức năng, chưa là nghiệm thu toàn bộ SRS. Nhập tay/sửa số có nguồn để demo được chấp nhận nhưng phải hiện acquisition/review; không cộng vào độ chính xác tự động hoặc discovery. Chưa đủ dữ liệu phải báo độ đầy đủ chưa đạt, dù màn hình đã chạy.

## Tổng quan tuần

| Tuần | Trọng tâm | Giờ dự toán | Đầu ra chính |
|---|---|---:|---|
'''
    lines = [intro]
    for w in W:
        lines.append(f"| {w['n']} | {w['title']} | {w['hours']} | {w['uc']} |\n")
    lines.append('\n## Công việc chi tiết\n')
    for w in W:
        lines.append(f"\n### Tuần {w['n']:02d} — {w['title']}\n\n**UC:** {w['uc']} · **Giờ dự toán:** {w['hours']}\n\n**Đầu vào:** {w['inputs']}\n\n")
        for t in w['tasks']:
            lines.append(f"- [ ] **{t['id']} — {t['title']}** ({t['hours']} giờ)\n  - Xong khi: {t['acceptance']}\n")
        lines.append('\n**Đầu ra cần lưu:**\n\n'+'\n'.join('- '+o for o in w['outputs'])+'\n')
        lines.append(f"\n**Tiêu chí chuyển mốc:** {w['done']}\n\n**Khi vướng/chậm:** {w['risk']}\n\n**Yêu cầu liên quan:** {', '.join(w['requirements'])}.\n\n**Ca kiểm cần thực hiện:** {', '.join(w['tests'])}. Đây là phân bổ kế hoạch, chưa phải kết quả pass.\n")
        r=w['reporting']
        lines.append('\n**Gợi ý nội dung Word:**\n\n'+'\n'.join(f'{i}. {s}' for i,s in enumerate(r['word'],1))+'\n')
        lines.append('\n**Gợi ý slide ngắn:**\n\n'+'\n'.join(f'{i}. {s}' for i,s in enumerate(r['slides'],1))+'\n')
        lines.append(f"\n**Demo:** {r['demo']}\n\n**Điểm trao đổi với thầy:** {r['ask']}\n")
    lines.append('''
## Đánh giá và kiểm soát phạm vi

Kế hoạch phân bổ 91 yêu cầu hiện hành/51 ca kiểm SRS; không tái đưa FR29/FR30/D09/D10 hoặc sàng lọc dưới tên cảnh báo. Phần bổ sung tương tác biểu đồ/so sánh nhóm F03 có tiêu chí riêng trong tuần 1/4/5, chưa biến toàn danh mục 38 chức năng thành phạm vi nghiệm thu. E05/E10/nhiều ca và các yêu cầu D có điều kiện phải ghi trạng thái kích hoạt/not_applicable có lý do, không mặc định đã đạt.

Freeze lineage trước đo: bản dịch/cột so sánh/bản sửa gần giống không nằm hai phía development/holdout. Cỡ pilot nhỏ thì báo số đếm thật và giới hạn; người tự xây gold phải ghi tự kiểm. Không gọi tập đã chỉnh parser để khớp là tập kiểm độc lập. Đo Paddle–Tesseract trên cùng trang/ô và khai cấu hình; không đổi quyết định OCR thành tuyên bố ưu thế chưa đo.

TC30 yêu cầu bộ tải 24 báo cáo/144 targets/≤200 notices theo SRS, khác mẫu nghiên cứu chín báo cáo. Có thể chuẩn bị bộ kiểm tải riêng nhưng phải ghi nguồn/synthetic, không nhân bản thành corpus nghiên cứu. Không đủ đúng bộ kiểm thì TC30 chưa đạt hoặc cần CR; không báo đo pilot nhỏ là đạt TC30.

Mỗi task chỉ tick khi có đầu ra và bằng chứng đúng tiêu chí. Mỗi TC ghi input/expected/actual, code/config version, pass/fail/not_run, người/ngày và đường dẫn. Nhật ký mỗi tuần: giờ thực, file/run, số đã duyệt/thiếu, lỗi và việc chuyển tuần. Tuần 9 làm UC-4 chỉ khi lỗi core đã xử lý; nếu chưa đạt, dùng giờ đó sửa UC-1/2/3/5 và ghi UC-4 hoãn.

Kết thúc tuần 10: tổng hợp phần đã chạy, phần chưa đạt và dữ liệu chưa đầy đủ. Tất cả yêu cầu M phải có bằng chứng đạt hoặc change record được chấp nhận; checklist/tài liệu không thay nghiệm thu. Trình bày theo UC nhỏ, đầu vào→xử lý→đầu ra→minh chứng; ưu tiên demo và số đo thay tổng quan lý thuyết.
''')
    (BASE/'32-ke-hoach-10-tuan-tiep-theo.md').write_text(''.join(lines),encoding='utf-8')
    template = (ROOT/'scripts/research/templates/checklist-10-tuan-v4.html').read_text(encoding='utf-8')
    html = template.replace('__PLAN__',json.dumps(plan,ensure_ascii=False).replace('</','<\\/'))
    (BASE/'checklist-10-tuan-v4.html').write_text(html,encoding='utf-8')
    print(json.dumps({'weeks':len(W),'tasks':sum(len(w['tasks']) for w in W),'hours':195,
                      'active_requirements_mapped':len(req),'planned_tests_mapped':len(active_tests),
                      'application_tests_executed':False}))


if __name__ == '__main__':
    build()
