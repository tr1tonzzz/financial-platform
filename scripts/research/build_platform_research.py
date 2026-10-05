"""Write the broadened platform research and learning plan, dated 2026-10-03.

These are research/design documents, not evidence of completed application work.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'docs/research-platform'


def write(name, content):
    path = OUT / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + '\n', encoding='utf-8')


IDEAS = [
    {
        'id': 'a1-suc-khoe-doanh-nghiep', 'name': 'Phân tích sức khỏe tài chính doanh nghiệp',
        'scores': [4, 4, 5, 5, 5],
        'problem': 'Người học hoặc người phân tích cần so sánh lợi nhuận, tiền và cấu trúc tài chính của doanh nghiệp nhưng phải đọc nhiều PDF khác bố cục và kiểm tra ý nghĩa từng số. Người dùng chọn công ty và kỳ, xem xu hướng, công thức, mức đủ dữ liệu và mở đúng vị trí nguồn.',
        'data': 'BCTC năm chính thức, metadata doanh nghiệp và ngành. Khảo sát trước đã tải 15 PDF của 5 công ty; mới đối chiếu sáu chỉ tiêu trên hai báo cáo. Doanh thu thuần, tài sản ngắn hạn và nợ ngắn hạn là ba trường bổ sung phải xác minh ở pilot. Không cần cổ tức hoặc giá thị trường để hoàn thành lõi.',
        'mvp': 'Pilot 3 công ty × 2 năm; mục tiêu project 10 công ty × 2023–2025, chín chỉ tiêu, ba nhóm phân tích, hàng đợi duyệt và dashboard. Các mục tiêu chỉ đạt sau kiểm tra nguồn và công sức, không dựa vào số file tải được.',
        'evaluation': 'So sánh text-only với OCR có xử lý cột, đo đúng số/đơn vị/kỳ/scope, độ phủ, phút sửa, khả năng chạy lại. Ba case phải truy được từ chart về số gốc. Kết quả trước và sau người duyệt được báo cáo riêng.',
        'risk': 'PDF scan, đổi mã dòng, nhầm cột, thiếu năm và khác cơ sở kế toán. Hạn chế ngành ngân hàng/bảo hiểm; không tạo điểm sức khỏe tổng hợp hoặc xác suất phá sản khi chưa kiểm định.',
        'graduate': 'Ưu tiên phát triển hỏi đáp số liệu có dẫn nguồn và phép tính kiểm chứng trên dataset đã duyệt; hoặc nghiên cứu phát hiện bất thường/phiên bản như một hướng thay thế. Không buộc triển khai mọi nhánh.',
        'finance': 'Cần hiểu ba BCTC, tài sản = nợ phải trả + vốn chủ, số dư tại thời điểm và dòng trong kỳ, doanh thu khác lợi nhuận, lợi nhuận khác tiền. Chín trường lõi: doanh thu thuần, LNST tổng, CFO, tiền và tương đương tiền, tài sản, nợ phải trả, VCSH, tài sản ngắn hạn, nợ ngắn hạn. Biên LNST = LNST/doanh thu; nợ/tài sản; current ratio = tài sản ngắn hạn/nợ ngắn hạn; CFO/LNST khi LNST dương. So cùng kỳ, scope và ngành; missing không phải 0. Bài tập: lấy hai năm một công ty, tính ba tỷ số bằng tay và giải thích thay đổi, chưa kết luận mua/bán cổ phiếu.',
        'it': 'Python xử lý file/HTTP/JSON; pdfplumber với PDF text, Poppler và OCR cho scan; pandas chuẩn hóa; SQLite lưu documents, facts, reviews, runs; Streamlit làm giao diện đọc và duyệt. Module chỉ số độc lập giao diện, dùng Decimal hoặc số nguyên cho tiền và phân biệt dữ liệu gốc/dẫn xuất. Khóa hash và transaction giúp chạy lại không nhân bản. Kiểm thử sai đơn vị, âm ngoặc, thiếu mẫu số, nhầm kỳ và chỉnh sửa có lịch sử. Bài tập: viết một hàm chuẩn hóa số, ba ca kiểm thử và một truy vấn tìm giá trị chưa duyệt.',
        'sources': '[Khảo sát dữ liệu thật](../../../research-recent-data/README.md); [SEC hướng dẫn BCTC](https://www.sec.gov/about/reports-publications/beginners-guide-financial-statements); [pandas](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html).'
    },
    {
        'id': 'a2-bctc-co-tuc', 'name': 'Quan hệ BCTC và cổ tức', 'scores': [4, 3, 4, 4, 5],
        'problem': 'Người theo dõi cổ tức cần biết mức chi trả được lợi nhuận và dòng tiền hỗ trợ thế nào. Ghép BCTC với thông báo quyền thành chuỗi sự kiện có mốc công bố và năm lợi nhuận.',
        'data': 'BCTC cộng thông báo cổ tức tiền mặt từ VSDC/IR. Đã tải bốn thông báo cho hai công ty, không phải lịch sử đủ toàn cửa sổ. Cần kiểm tra đề xuất, thông báo chính thức, điều chỉnh và xác nhận thực hiện.',
        'mvp': 'Một module trên nền dữ liệu A1: timeline cổ tức, DPS theo thành phần năm lợi nhuận và vài case lợi nhuận–tiền. Nếu chọn làm đề tài chính, phải dành thêm công sức độ phủ sự kiện và thiết kế nhãn.',
        'evaluation': 'Đúng ticker, tiền/cổ phiếu, DPS, năm lợi nhuận, ngày; tỷ lệ sự kiện có nguồn và cửa sổ đủ. Đánh giá dự báo chỉ sau gate nhãn và chia thời gian.',
        'risk': 'Nhãn năm 2026 chưa trưởng thành cho cửa sổ 12 tháng; không tìm thấy không nghĩa không trả. Nhiều ngày thanh toán chỉ là lịch. Hướng cũ mạnh về ngữ nghĩa nhưng nặng đối với người mới.',
        'graduate': 'Có thể là nghiên cứu duy trì/cắt giảm cổ tức trên dữ liệu trưởng thành; cần baseline và nhãn công bố hoặc thực trả được chọn rõ.',
        'finance': 'DPS là đồng/cổ phiếu; tỷ lệ mệnh giá khác yield theo giá thị trường. Ngày công bố, chốt quyền, lịch trả và thực trả khác nhau. Năm lợi nhuận khác năm trả tiền. Một thông báo VNM đã đọc gộp 350 đồng thuộc 2024 với 2.500 đồng thuộc 2025. LNST tổng hợp nhất không tự là tiền có thể chia ở công ty mẹ. Bài tập: tách một thông báo thành hai thành phần, giải thích vì sao chưa được gán nhãn tiền đã trả.',
        'it': 'Adapter HTML theo trường mã chứng khoán, tách phần thông báo khỏi tin liên quan, lưu notice ID và bảng event_components; phát hiện trùng route, điều chỉnh và hủy. Dựng coverage ledger theo công ty–cửa sổ; trạng thái unknown/censored. Point-in-time join chống dùng dữ liệu tương lai. Kiểm thử một event nhiều năm và một sự kiện sửa lịch. Pipeline A1 tái sử dụng, nhưng dataset sự kiện và bộ chấm phải xây riêng.',
        'sources': '[Khảo sát VSDC và nhãn](../../../research-recent-data/03-ky-tai-chinh-co-tuc-va-nhan.md); [thiết kế nhánh cổ tức](../../../research-design.md).'
    },
    {
        'id': 'a3-rui-ro-danh-muc', 'name': 'Phân tích rủi ro và hiệu quả danh mục', 'scores': [2, 2, 4, 5, 2],
        'problem': 'Người dùng muốn kiểm tra một danh mục giả định biến động và sụt giảm ra sao, so với nắm giữ đơn giản. Đầu ra là phân tích dữ liệu lịch sử và mô phỏng có giả định.',
        'data': 'Giá cuối ngày, lịch giao dịch, giá điều chỉnh, sự kiện doanh nghiệp và benchmark. Đã đọc README chính thức Vnstock; chưa chạy tải hay xác nhận độ phủ 2025–2026. Thư viện kết nối nguồn thứ ba và giấy phép phần mềm không cấp quyền dữ liệu nguồn.',
        'mvp': 'CSV giá có nguồn cho 5–10 mã; kiểm tra dữ liệu, tính returns, volatility, drawdown và so sánh equal-weight với buy-and-hold. Không giao dịch thật hoặc dự báo giá làm lõi.',
        'evaluation': 'Đối chiếu return/drawdown với ví dụ tính tay; backtest không nhìn tương lai, có phí giả định, kiểm tra dữ liệu điều chỉnh. Chia train/test theo thời gian nếu chọn tham số chiến lược.',
        'risk': 'Nguồn giá, điều chỉnh chia tách/cổ tức, survivorship bias, phí và thống kê khó hơn nền hiện tại. Chưa có benchmark nguồn thật trong repo.',
        'graduate': 'Tối ưu danh mục có ràng buộc hoặc phân tích rủi ro ngoài mẫu, sau khi giải quyết nguồn và phương pháp; vẫn là nhánh độc lập với quan hệ BCTC–cổ tức.',
        'finance': 'Return đơn giản = P_t/P_(t-1) − 1; volatility đo biến động chứ không đồng nghĩa mọi rủi ro. Drawdown là giảm từ đỉnh lịch sử. Sharpe cần quy ước lợi suất phi rủi ro và kỳ; chi phí làm giảm kết quả. Cổ tức/chia tách đòi hỏi giá hoặc total return phù hợp. Bài tập: tính drawdown trên chuỗi 100, 110, 99, 105 và giải thích vì sao số cổ phiếu/điều chỉnh ảnh hưởng so sánh.',
        'it': 'Pipeline time-series, lịch phiên, missing/corporate actions; vector hóa pandas, mô-đun backtest, cấu hình phí và snapshot giá. Split/purge dữ liệu và chống dùng giá tương lai để ra quyết định quá khứ. Lưu trade log để tái tính equity curve. Bài tập: viết backtest equal-weight có phí, kiểm thử một ngày thiếu giá và một mã vào/ra danh mục. Không cần LSTM để thể hiện giá trị IT.',
        'sources': '[README chính thức Vnstock](https://github.com/thinh-vu/vnstock). Thông tin ở đây là khảo sát tài liệu, chưa phải thử tải giá.'
    },
    {
        'id': 'a4-tai-chinh-ca-nhan', 'name': 'Quản lý thu chi và ngân sách cá nhân', 'scores': [5, 4, 4, 3, 1],
        'problem': 'Người dùng muốn hiểu tiền vào/ra, khoản chi định kỳ và khả năng đạt mục tiêu tiết kiệm. Đây là lĩnh vực tài chính khác BCTC doanh nghiệp.',
        'data': 'CSV do người dùng tự xuất hoặc tự nhập; nhãn chi tiêu tự chấm. Có thể dùng dữ liệu giả lập có gắn nhãn để kiểm thử, nhưng không coi là dữ liệu người dùng thật hoặc bằng chứng phân loại tốt. Chưa có dataset thực của người dùng trong repo.',
        'mvp': 'Import một định dạng CSV, chống giao dịch trùng, chỉnh nhóm chi, báo cáo dòng tiền và ngân sách tháng. Không tích hợp tài khoản ngân hàng khi chưa có đường truy cập chính thức.',
        'evaluation': 'Đúng số dư/tổng nhóm, xử lý hoàn tiền/chuyển khoản nội bộ; độ chính xác phân nhóm trên giao dịch thật được phép dùng; thời gian người dùng sửa và khả năng xóa/export dữ liệu.',
        'risk': 'Thuận lợi học phần mềm nhưng dễ chỉ thành CRUD nếu không làm import, reconciliation, phân loại và đánh giá. Tái sử dụng dữ liệu/crawler doanh nghiệp trước đây ít.',
        'graduate': 'Phân loại giao dịch tiếng Việt, nhận diện khoản định kỳ, dự toán dòng tiền cá nhân có đánh giá người dùng. Cần tập giao dịch thật phù hợp và bảo vệ dữ liệu.',
        'finance': 'Thu nhập khác chuyển tiền giữa tài khoản; chi tiêu khác trả nợ gốc; hoàn tiền phải giảm chi đúng nhóm. Ngân sách là kế hoạch, actual là đã phát sinh, variance = actual − budget theo quy ước dấu. Dòng tiền tuần có thể thiếu dù tháng dư vì thời điểm thu/chi khác nhau. Bài tập: phân loại 20 giao dịch tự tạo gồm chuyển nội bộ và hoàn tiền, tính ngân sách còn lại, ghi rõ đây là dữ liệu kiểm thử.',
        'it': 'Parser CSV cấu hình cột, transaction hash, phân nhóm bằng luật trước ML, UI chỉnh nhãn và audit trail. SQLite và mã hóa/đường lưu phù hợp nếu chứa dữ liệu cá nhân; không commit raw giao dịch riêng tư. Có workflow delete/export, kiểm thử nhập lại cùng CSV và hoàn tiền. Phân loại ML cần gold độc lập; đo macro-F1 và công sức chỉnh nhóm chứ không chỉ demo biểu đồ.',
        'sources': '[CFPB spending tracker](https://www.consumerfinance.gov/archive/blog/track-your-spending-with-this-easy-tool/). Nguồn này giải thích nhu cầu theo dõi chi, không cung cấp dataset người dùng cho project.'
    },
    {
        'id': 'a5-dong-tien-doanh-nghiep-nho', 'name': 'Theo dõi công nợ và mô phỏng dòng tiền doanh nghiệp nhỏ', 'scores': [2, 3, 4, 4, 1],
        'problem': 'Doanh nghiệp nhỏ có doanh thu nhưng thiếu tiền khi khách trả chậm. Hệ thống dự kiến thu/chi từ hóa đơn, khoản đến hạn và điều kiện thanh toán.',
        'data': 'Hóa đơn, khoản phải thu/phải trả, lịch thanh toán và số dư ngân hàng do đơn vị hợp tác cung cấp. Đã đọc tài liệu sản phẩm Odoo; chưa có đơn vị hoặc dữ liệu thật. BCTC niêm yết công khai không thay thế được giao dịch/đến hạn nội bộ.',
        'mvp': 'CSV invoices/payments, aging công nợ và mô phỏng 8–13 tuần theo kịch bản trả đúng hạn/chậm; cho sửa giả định. Hệ thống theo dõi thanh toán một phần, không xây toàn bộ phần mềm kế toán.',
        'evaluation': 'Đối chiếu số dư và aging, kiểm thử thanh toán một phần/quá hạn, đo sai số dự toán trên lịch sử khi có dữ liệu thật. Dữ liệu mô phỏng chỉ xác minh thuật toán/kịch bản.',
        'risk': 'Thiếu dữ liệu hợp tác là blocker lớn; OCR hóa đơn và chuẩn hóa nghiệp vụ có thể vượt thời gian. Không tuyên bố chính xác dự báo từ dữ liệu giả lập.',
        'graduate': 'Đánh giá mô hình ngày thanh toán hoặc tối ưu kịch bản thu/chi nếu có doanh nghiệp cung cấp lịch sử đủ dài và yêu cầu thực.',
        'finance': 'Accrual revenue không phải thu tiền; receivable aging tính theo ngày đến hạn và ngày snapshot. Thanh toán một phần giảm outstanding chứ không xóa hóa đơn. Dòng tiền dự kiến = số dư đầu kỳ + thu dự kiến − chi dự kiến. Bài tập: một hóa đơn 10 triệu thu 4 triệu, còn 6 triệu quá hạn; lập hai kịch bản ngày thu còn lại, không gọi kịch bản là dự báo đã kiểm định.',
        'it': 'Schema invoice/payment/allocation, validation CSV, giao dịch nhiều khoản thanh toán, engine mô phỏng theo ngày/tuần và quản lý scenario. Có data lineage, chống trùng, kiểm thử timeline và snapshot. Bài tập: unit test hai payment cho một invoice và một khoản đến hạn chuyển qua tuần sau. OCR hóa đơn là mở rộng riêng, không trộn vào pilot khi chưa có dữ liệu.',
        'sources': '[Odoo reporting](https://www.odoo.com/documentation/19.0/applications/finance/accounting/reporting.html), tìm kiếm đọc được mục cash flow/short-term forecast; web open trực tiếp có lúc lỗi. Đây là bằng chứng nhu cầu/chức năng đã có, không phải nguồn dataset.'
    },
    {
        'id': 'a6-hoi-dap-tai-lieu', 'name': 'Hỏi đáp tài liệu tài chính có bằng chứng và phép tính', 'scores': [4, 2, 5, 5, 4],
        'problem': 'Người đọc hỏi doanh thu, dòng tiền hoặc thay đổi qua năm và cần câu trả lời đúng tài liệu/cột, có phép tính kiểm tra được. Bài toán chính là truy xuất và suy luận số, không phải chatbot trò chuyện chung.',
        'data': 'BCTC, bảng chuẩn hóa, câu hỏi/đáp án và chương trình tính. FinQA và TAT-QA là nghiên cứu benchmark đã đọc; không tự coi dữ liệu tiếng Anh là gold tiếng Việt/VAS. Cần bộ câu hỏi riêng do người hiểu nguồn chấm.',
        'mvp': 'Tra cứu và trả lời theo mẫu trên bảng đã duyệt, có công thức và nguồn. Nếu chọn làm đề tài chính phải dựng evaluation retrieval/numerical answer; RAG/LLM đầu-cuối chưa thích hợp làm nghĩa vụ 13 tuần của người mới.',
        'evaluation': 'Đúng kỳ/scope/số/công thức, nguồn trích đúng, recall retrieval và tỷ lệ từ chối khi thiếu dữ liệu. So lookup/template baseline với RAG và RAG + calculator trên holdout; đo chi phí và độ trễ.',
        'risk': 'Sai OCR lan sang đáp án; tài liệu rất giống nhau khác kỳ, hallucinatory citation và chi phí API. Một chatbot demo chưa chứng minh đóng góp.',
        'graduate': 'Nhánh ưu tiên sau A1: công cụ tính số có schema, retrieval theo kỳ/scope và bộ đánh giá tiếng Việt. A1 cung cấp dữ liệu đúng, nguồn và kiểm định để nghiên cứu này có nền.',
        'finance': 'Câu hỏi phải nêu kỳ, scope, đơn vị và metric; “tăng bao nhiêu” có thể là chênh lệch tuyệt đối hoặc phần trăm. Mẫu số âm/0 và dữ liệu điều chỉnh cần quy tắc riêng. LNST công ty mẹ khác LNST tổng. Bài tập: viết 10 câu hỏi có đáp án tính tay, một câu thiếu số và một câu nhầm kỳ phải từ chối. Kiến thức A1 cần nắm trước khi xây hỏi đáp.',
        'it': 'Index metadata + văn bản/bảng, retrieval lọc document/period/scope, function/tool gọi calculator có kiểm soát, trả citation locator. Tránh cho model tự tính hoặc chạy code tùy ý. Gold giữ câu hỏi, câu trả lời, operand, nguồn và phép tính; tách train/dev/test theo tài liệu. Bài tập: một hàm answer_growth chỉ nhận facts đã duyệt và trả phép tính + IDs, kiểm thử không đủ hai năm.',
        'sources': '[FinQA](https://aclanthology.org/2021.emnlp-main.300/); [TAT-QA](https://aclanthology.org/2021.acl-long.254/).'
    },
    {
        'id': 'a7-du-lieu-vi-mo', 'name': 'Nền tảng dữ liệu và so sánh chỉ tiêu vĩ mô', 'scores': [5, 3, 4, 4, 2],
        'problem': 'Người nghiên cứu cần dữ liệu GDP/lạm phát và so sánh quốc gia/chuỗi năm với đơn vị, metadata và thời điểm snapshot rõ. Bài toán này khác dữ liệu doanh nghiệp và cổ tức.',
        'data': 'World Bank Indicators API, mã chỉ tiêu và metadata. Đã thử một request GDP Việt Nam 2020–2025: HTTP 200, sáu dòng có giá trị; chưa thử toàn bộ chỉ tiêu hoặc vintage công bố ban đầu. Dữ liệu năm không đồng nghĩa có dữ liệu quý mới.',
        'mvp': '3–5 chỉ tiêu, Việt Nam và 2–3 quốc gia so sánh, cache, chuẩn hóa units/missing, biểu đồ và CSV. Phân tích mô tả, không dự báo vĩ mô làm nghĩa vụ.',
        'evaluation': 'Đối chiếu giá trị API, handling null và đơn vị, consistency cập nhật, độ trễ và tính tái lập. Phải có chức năng metadata/phiên bản để mạnh hơn dashboard đơn giản.',
        'risk': 'Dữ liệu bị sửa sau công bố; ít điểm năm không đủ ML. Độ mới và tần suất phụ thuộc từng chỉ tiêu. Câu hỏi ứng dụng có thể mờ hơn phân tích doanh nghiệp.',
        'graduate': 'Nghiên cứu data revision hoặc event-aligned macro/company analysis khi có nhiều nguồn và vintage. Không suy quan hệ nhân quả từ tương quan GDP–giá.',
        'finance': 'GDP danh nghĩa khác thực, USD khác nội tệ, CPI level khác inflation rate. Tăng trưởng phần trăm khác tăng tuyệt đối; năm cơ sở và thay đổi định nghĩa ảnh hưởng so sánh. Không nối chỉ tiêu năm với hàng ngày bằng forward-fill rồi coi là quan sát mới. Bài tập: đọc metadata ba chỉ tiêu, giải thích đơn vị và vì sao không thể cộng chúng trực tiếp.',
        'it': 'HTTP JSON client, paging, cache, schema country/indicator/observation/vintage, kiểm tra null và units; pandas time series; dashboard lọc quốc gia/chỉ tiêu. Bài tập: tải GDP, lưu snapshot hash và nhập lại idempotent. Request đã chạy là bằng chứng khả thi nhỏ, không phải hạ tầng production hoặc dataset realtime.',
        'sources': '[World Bank API documentation](https://datahelpdesk.worldbank.org/knowledgebase/articles/889392-about-the-indicators-api-documentation); [GDP API đã thử](https://api.worldbank.org/v2/country/VN/indicator/NY.GDP.MKTP.CD?date=2020:2025&format=json).'
    },
]


def main():
    for idea in IDEAS:
        base = 'ideas/' + idea['id']
        write(base + '/01-y-tuong-va-kha-thi.md', f"""# {idea['name']}

Khảo sát và đề xuất ngày 03/10/2026. Trạng thái: thiết kế/đánh giá khả thi, không phải chức năng ứng dụng đã hoàn thành.

## Bài toán và người dùng

{idea['problem']}

## Dữ liệu và bằng chứng khả thi

{idea['data']}

## MVP nếu chọn hướng này

{idea['mvp']}

## Đóng góp IT và cách đánh giá

{idea['evaluation']}

## Điểm khó cần xử lý

{idea['risk']}

## Liên thông lên đồ án tốt nghiệp

{idea['graduate']}

## Tài liệu đi kèm

[Kiến thức tài chính](02-kien-thuc-tai-chinh.md); [kỹ thuật IT](03-ky-thuat-it.md). Nguồn: {idea['sources']}
""")
        write(base + '/02-kien-thuc-tai-chinh.md', f"# Kiến thức tài chính cho {idea['name'].lower()}\n\n{idea['finance']}\n\nHọc bằng một ví dụ tính tay trước, sau đó viết lại bằng Python và ghi điều kiện áp dụng. Không xem kết quả số là kết luận đầu tư hoặc xác suất rủi ro nếu chưa có thiết kế kiểm định.\n\nNguồn học/nghiên cứu: {idea['sources']}")
        write(base + '/03-ky-thuat-it.md', f"# Kỹ thuật IT cho {idea['name'].lower()}\n\n{idea['it']}\n\nĐầu ra cần giữ: source code module, dữ liệu đầu vào có nguồn, cấu hình, test phù hợp, log chạy và hạn chế. Đọc được dữ liệu hoặc gọi được thư viện không thay thế đánh giá đúng/sai trên bộ mẫu.\n\nNguồn và hồ sơ: {idea['sources']}")

    weights = [.30, .25, .20, .15, .10]
    rows=[]
    for idea in IDEAS:
        total=sum(a*b for a,b in zip(idea['scores'],weights))
        rows.append(f"| [{idea['name']}](ideas/{idea['id']}/01-y-tuong-va-kha-thi.md) | " + ' | '.join(map(str,idea['scores'])) + f" | {total:.2f} |")
    write('01-so-sanh-va-quyet-dinh.md', """# So sánh hướng của nền tảng tài chính

Ngày 03/10/2026. Việc rà soát trước đã thu hẹp nền tảng thành BCTC–cổ tức quá sớm. Lần này coi quan hệ BCTC–cổ tức là một trong bảy hướng, không lấy nó làm ràng buộc bắt buộc.

## Tiêu chí theo hoàn cảnh của người thực hiện

Chấm 1–5, cao là thuận lợi: dữ liệu 30%, độ vừa sức khi học 25%, đóng góp IT 20%, khả năng liên thông tốt nghiệp 15%, tận dụng công việc hiện tại 10%. Đây là phán đoán thiết kế của người nghiên cứu, không phải kết quả khảo sát người dùng, thí nghiệm hay ý kiến phê duyệt của thầy. Một tiêu chí thay đổi có thể đổi thứ hạng.

| Hướng | Dữ liệu | Vừa sức | IT | Tốt nghiệp | Tái sử dụng | Điểm có trọng số |
|---|---:|---:|---:|---:|---:|---:|
""" + '\n'.join(rows) + """

## Quyết định đề xuất

Chọn A1 làm project: **Nền tảng phân tích sức khỏe tài chính doanh nghiệp Việt Nam từ BCTC với dữ liệu có truy vết và kiểm định chất lượng**. Cổ tức trở thành module tùy chọn, không là điều kiện hoàn thành lõi. Tên đăng ký chính thức còn cần đối chiếu rubric và trao đổi với thầy; không có bằng chứng thầy đã đồng ý.

A4 dễ lấy dữ liệu kiểm thử và làm phần mềm, nhưng chuyển mạnh khỏi dữ liệu/crawler đã có; nếu thích sản phẩm phục vụ cá nhân hơn, đây là lựa chọn thay thế có thực chất. A7 có đường API đã thử thật và ít OCR, nhưng cần câu hỏi sử dụng rõ và dataset revision để vượt dashboard. A3 có tiềm năng định lượng nhưng nguồn giá và thống kê chưa kiểm chứng. A5 cần dữ liệu nội bộ chưa có. A6 phù hợp giai đoạn tốt nghiệp hơn vì cần nền dữ liệu, đánh giá đáp án và kiến thức NLP/LLM. A2 cần thêm dữ liệu sự kiện và thời gian trưởng thành nhãn.

Nếu bỏ trọng số tái sử dụng và ưu tiên đơn thuần khả năng làm ứng dụng dễ tiếp cận, khoảng cách giữa A1 và A4 thu hẹp. Không diễn giải điểm số là bằng chứng A1 tốt hơn trong mọi bối cảnh.

## Vấn đề đáng nghiên cứu của A1

Làm thế nào trích số đúng kỳ/scope/unit từ BCTC Việt Nam khác layout và scan, giữ bằng chứng, giảm thời gian đối chiếu và phục vụ phân tích có thể kiểm chứng? Đóng góp nằm ở thiết kế và đo lường pipeline, không ở tuyên bố một tỷ số tài chính mới hoặc phát minh OCR.

## Bằng chứng hiện có và phần chưa kiểm chứng

1. Đã tải 15 PDF/5 công ty và bốn HTML cổ tức trong [khảo sát gần hiện tại](../research-recent-data/README.md); VHC gồm hai ngôn ngữ. 12 PDF không có lớp chữ hữu ích theo probe, OCR 10 trang cho bộ tìm dòng 11/12 giá trị khớp ảnh trên mẫu phát triển.
2. Đã đọc tài liệu chính thức của Vnstock, CFPB, Odoo, FinQA/TAT-QA và World Bank. Chưa chạy tải giá, chưa có dữ liệu cá nhân/SME, chưa dựng RAG.
3. World Bank GDP Việt Nam 2020–2025: một request local HTTP 200/sáu giá trị. Không suy ra có đủ dữ liệu vĩ mô quý hiện tại.
4. `src` chưa có file ứng dụng được phát hiện trong lần đọc này. Script nghiên cứu và bộ tài liệu không đồng nghĩa đã có sản phẩm. Kế hoạch tính từ việc dựng một luồng nhỏ chạy thật.
""")
    probe = ROOT / 'data-sets/research-evidence/2026-10-03-platform-options/worldbank-probe.json'
    if probe.exists():
        write('worldbank-probe.json', probe.read_text(encoding='utf-8'))
    print(f'Wrote {len(IDEAS)*3 + 1} research MD files')


if __name__ == '__main__':
    raise SystemExit('Legacy A1 generator disabled: current docs are maintained in docs/research-platform. Do not overwrite the accepted A2 direction.')
