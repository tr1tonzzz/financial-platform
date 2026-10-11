"""Editable SVG mockups and a local walkthrough. All financial values are synthetic."""
from pathlib import Path
from html import escape
import json
import zipfile

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'docs/design-5-uc'
OUT.mkdir(parents=True, exist_ok=True)
TOKENS = {'ink':'#182F39','muted':'#64767E','line':'#DCE5E8','bg':'#F3F6F7',
          'white':'#FFFFFF','brand':'#126B59','pale':'#E6F4EE','blue':'#4168C8',
          'amber':'#865A14','amberbg':'#FFF3DA','red':'#AE453B','nav':'#122F37'}
P=[]
def rect(x,y,w,h,fill='white',r=12,stroke=None):
    P.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{TOKENS.get(fill,fill)}"'+(f' stroke="{TOKENS.get(stroke,stroke)}"' if stroke else '')+'/>')
def text(x,y,s,size=14,color='ink',weight=400,anchor='start'):
    P.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{TOKENS.get(color,color)}" font-weight="{weight}" text-anchor="{anchor}">{escape(str(s))}</text>')
def lines(x,y,items,size=14,color='muted',step=23):
    for i,s in enumerate(items):text(x,y+i*step,s,size,color)
def line(x1,y1,x2,y2,color='line',width=1):
    P.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{TOKENS.get(color,color)}" stroke-width="{width}"/>')
def group(name,target=None):
    P.append(f'<g id="{name}"'+(f' data-screen="{target}" role="button" tabindex="0" aria-label="Mở {target}" style="cursor:pointer"' if target else '')+'>')
def end():P.append('</g>')
def button(x,y,w,label,target=None,primary=False):
    group('action-'+str(len(P)),target);rect(x,y,w,40,'brand' if primary else 'white',8,None if primary else 'line');text(x+w/2,y+26,label,13,'white' if primary else 'ink',600,'middle');end()
def tag(x,y,label,tone='pale',w=None):
    w=w or max(75,len(label)*7+22);rect(x,y,w,26,tone,13);text(x+11,y+18,label,11,'amber' if tone=='amberbg' else 'brand',600)
def card(x,y,w,h,title=None):
    rect(x,y,w,h,'white',12,'line')
    if title:text(x+22,y+32,title,16,weight=600)
def table(x,y,width,headers,rows,colwidths=None,rowheight=48,links=None):
    colwidths=colwidths or [width/len(headers)]*len(headers)
    rect(x,y,width,42,'bg',6)
    for ri,row in enumerate([headers]+rows):
        yy=y+27 if ri==0 else y+42+(ri-1)*rowheight+30
        pos=x
        for ci,value in enumerate(row):
            target=(links or {}).get((ri,ci));group('cell-'+str(len(P)),target)
            text(pos+14,yy,value,12 if ri==0 else 14,'muted' if ri==0 else ('brand' if target else 'ink'),600 if ri==0 or ci==0 else 400)
            end();pos+=colwidths[ci]
        if ri:line(x,y+42+ri*rowheight,x+width,y+42+ri*rowheight)
def filterbar(issuer='HPG · Hòa Phát',period='2023 — 2025',extra='Đơn vị: tỷ đồng'):
    rect(248,202,1156,64,'white',10,'line')
    for x,w,label in [(264,285,issuer),(565,190,period),(771,226,'BCTC năm · Hợp nhất'),(1013,190,extra)]:
        rect(x,214,w,40,'bg',7);text(x+14,239,label,13,weight=500)
    text(1378,239,'Đổi bộ chọn',12,'brand',600,'end')
def shell(key,uc,title,subtitle,detail=False):
    P.clear();P.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="1440" height="1080" viewBox="0 0 1440 1080" aria-label="{escape(title)}"><style>text{{font-family:"Be Vietnam Pro","Segoe UI",Arial,sans-serif}}[data-screen]:hover{{opacity:.8}}</style>')
    group(key)
    rect(0,0,1440,1080,'bg',0);rect(0,0,1440,64,'nav',0)
    rect(24,16,32,32,'brand',8);text(40,39,'F',21,'white',700,'middle');text(70,40,'NỀN TẢNG TÀI CHÍNH',14,'white',600)
    text(1000,39,'HPG / VNM / FPT',12,'#BED1D7');tag(1150,20,'Bản thiết kế',w=112);text(1355,40,'Cá nhân',13,'white')
    rect(0,64,216,1016,'white',0);line(216,64,216,1080)
    text(24,109,'KHÔNG GIAN NGHIÊN CỨU',10,'muted',600)
    names=['Dữ liệu tài chính','Phân tích tài chính','So sánh doanh nghiệp','Theo dõi doanh nghiệp','Phân tích cổ tức']
    for i,name in enumerate(names,1):
        group('nav-'+key+'-'+str(i),'uc'+str(i));rect(12,132+(i-1)*56,192,44,'pale' if uc==i else 'white',8)
        text(27,160+(i-1)*56,f'{i:02}',12,'brand' if uc==i else 'muted',600);text(54,160+(i-1)*56,name,12,'brand' if uc==i else 'ink',600 if uc==i else 400);end()
    line(24,434,192,434);text(24,467,'DỮ LIỆU HỖ TRỢ',10,'muted',600)
    group('review-nav-'+key,'review');text(24,502,'Duyệt và tra soát số liệu',12,'muted');end()
    group('saved-nav-'+key,'saved');text(24,538,'Phân tích đã lưu',12,'muted');end()
    rect(16,893,184,116,'bg',10);lines(30,921,['Mẫu nghiên cứu','3 doanh nghiệp','BCTC năm 2023–2025'],12,step=25)
    text(248,98,('CHI TIẾT' if detail else f'UC-{uc:02}')+'  /  '+names[uc-1],11,'muted',600)
    text(248,145,title,29,weight=600);text(248,176,subtitle,13,'muted')
    line(248,1031,1404,1031);text(248,1058,'DỮ LIỆU MINH HỌA · Số liệu giả định, chưa đối chiếu nguồn doanh nghiệp.',12,'amber',500)
    text(1404,1058,'Thiết kế đề xuất · chưa triển khai',11,'muted',anchor='end')
def finish(key,title,uc,functions):
    end();P.append('</svg>');s=''.join(P);(OUT/f'{key}.svg').write_text(s,encoding='utf-8')
    return {'id':key,'title':title,'uc':uc,'functions':functions,'svg':s,'file':f'{key}.svg'}
screens=[]

shell('uc1',1,'Khai thác dữ liệu tài chính','Chọn doanh nghiệp và kỳ để đọc số liệu đã duyệt, định nghĩa và bằng chứng nguồn.');filterbar()
card(248,290,1156,88);text(270,324,'Hòa Phát',20,weight=600);text(270,350,'HPG · Dữ liệu năm · Hợp nhất',13,'muted');tag(621,309,'17 / 18 ô đã duyệt',w=159);tag(798,309,'1 ô còn thiếu','amberbg',132);button(1216,314,166,'Xuất bộ dữ liệu')
card(248,398,1156,445,'Bảng dữ liệu nhiều kỳ');text(1382,430,'Chọn ô có số để xem nguồn ↗',12,'brand',anchor='end')
table(268,450,1116,['Chỉ tiêu','2023','2024','2025','Tình trạng'],[
 ['Tổng lợi nhuận sau thuế','6.000','9.000','12.000','Đã duyệt'],['CFO','8.000','7.000','16.000','Đã duyệt'],['Tiền & tương đương tiền','12.000','14.000','20.000','Đã duyệt'],['Tổng tài sản','150.000','170.000','200.000','Đã duyệt'],['Tổng nợ phải trả','60.000','70.000','80.000','Đã duyệt'],['Tổng vốn chủ sở hữu','— Chưa có số','100.000','120.000','Thiếu năm 2023']],
 [350,170,170,170,256],links={(2,3):'source',(1,3):'source',(6,1):'review'})
lines(270,812,['Số dư dùng ngày cuối kỳ; LNST và CFO dùng khoảng kỳ cả năm. Ô thiếu khác số 0.'],12)
card(248,863,746,140,'Tài liệu và độ đầy đủ');lines(270,925,['2023: 5/6 ô  •  2024: 6/6 ô  •  2025: 6/6 ô','Bản số được chọn và lịch sử sửa có trong chi tiết từng ô.'],13)
button(1030,879,352,'Đi tới phân tích tài chính','uc2',True);button(1030,935,352,'Duyệt số liệu còn thiếu','review')
screens.append(finish('uc1','UC-1 · Khai thác dữ liệu',1,['F01.1','F01.2','F01.3','F01.4','F01.5','F01.6']))

shell('uc2',2,'Phân tích dữ liệu tài chính','Xem xu hướng, đọc công thức và tìm hiểu những khoản đóng góp vào dòng tiền.');filterbar()
card(248,290,748,394,'Lợi nhuận và dòng tiền kinh doanh');text(270,350,'Tỷ đồng',11,'muted')
for v in [0,5,10,15,20]:
 yy=602-v*10;line(310,yy,958,yy);text(295,yy+4,str(v*1000),10,'muted',anchor='end')
for i,year in enumerate([2023,2024,2025]):text(380+i*250,630,year,12,'muted',anchor='middle')
for vals,col in [([6,9,12],'brand'),([8,7,16],'blue')]:
 points=' '.join(f'{380+i*250},{602-v*10}' for i,v in enumerate(vals));P.append(f'<polyline points="{points}" fill="none" stroke="{TOKENS[col]}" stroke-width="3"/>')
 for i,v in enumerate(vals):P.append(f'<circle cx="{380+i*250}" cy="{602-v*10}" r="5" fill="{TOKENS[col]}"/>')
rect(340,650,18,4,'brand',2);text(370,656,'LNST',12);rect(510,650,18,4,'blue',2);text(540,656,'CFO',12)
card(1016,290,388,394,'Chỉ tiêu năm 2025')
for y,a,b in [(360,'CFO / LNST','1,33 lần'),(436,'Tiền / Tài sản','10,0%'),(512,'Nợ phải trả / Tài sản','40,0%')]:
 text(1038,y,a,13,'muted');text(1368,y+30,b,26,'brand',600,'end')
button(1038,618,344,'Xem công thức và nguồn','source')
card(248,704,1156,145,'Một thay đổi cần đọc thêm');lines(270,765,['Năm 2024, LNST tăng từ 6.000 lên 9.000 tỷ; CFO giảm từ 8.000 còn 7.000 tỷ.','Đọc các dòng điều chỉnh và vốn lưu động để hiểu sự khác biệt.'],14)
button(248,877,253,'Đọc cầu nối LNTT → CFO','bridge',True);button(519,877,218,'So sánh doanh nghiệp','uc3');button(1120,877,284,'Lưu nhận xét và bằng chứng','saved')
text(248,965,'Thiếu kỳ hoặc mẫu số không hợp lệ: hiện lý do và chặn phép tính liên quan.',13,'muted')
screens.append(finish('uc2','UC-2 · Phân tích tài chính',2,['F02.1','F02.4','F02.5','F02.8']))

shell('uc3',3,'So sánh doanh nghiệp','Đối chiếu nhóm doanh nghiệp bạn tự chọn trên cùng kỳ và phạm vi báo cáo.');filterbar('HPG  +  VNM  +  FPT','Năm 2025')
rect(248,290,1156,58,'amberbg',10);text(270,325,'Ba doanh nghiệp khác ngành. Kết quả là đối chiếu nhóm tự chọn, không phải chuẩn so sánh ngành.',13,'amber')
card(248,369,1156,347,'Số liệu và tỷ số trên cùng cơ sở')
table(268,423,1116,['Chỉ tiêu','HPG · Hòa Phát','VNM · Vinamilk','FPT'],[
 ['Tổng LNST · tỷ đồng','12.000','10.000','9.000'],['CFO · tỷ đồng','16.000','12.500','10.000'],['CFO / LNST · lần','1,33','1,25','1,11'],['Tiền / Tài sản','10,0%','18,2%','15,0%'],['Nợ phải trả / Tài sản','40,0%','32,7%','50,0%']],
 [354,254,254,254],rowheight=43,links={(1,1):'source',(2,1):'source'})
card(248,736,748,266,'CFO / LNST năm 2025 · cùng công thức')
for i,(n,v,c) in enumerate([('HPG',1.333,'brand'),('VNM',1.25,'blue'),('FPT',1.111,'#81949A')]):
 yy=804+i*56;text(270,yy+19,n,13,weight=600);rect(334,yy,v*390,28,c,5);text(353+v*390,yy+19,f'{v:.2f}'.replace('.',','),13)
card(1016,736,388,266,'Giữ bối cảnh so sánh');lines(1038,802,['Năm 2025 · BCTC hợp nhất','Đơn vị đã chuẩn hóa','Có thể mở nguồn từng doanh nghiệp','Khác ngành cần diễn giải thận trọng'],13,step=29)
button(1038,938,344,'Lưu nhóm và nhận xét','saved',True)
screens.append(finish('uc3','UC-3 · So sánh doanh nghiệp',3,['F03.1','F03.2']))

shell('uc4',4,'Theo dõi doanh nghiệp','Tiếp tục đọc công bố và thay đổi dữ liệu của những doanh nghiệp bạn quan tâm.');filterbar('Danh sách: HPG / VNM / FPT','Công bố đã ghi nhận','Theo thời điểm nguồn')
tag(248,284,'Thiết kế giai đoạn sau các UC ưu tiên','amberbg',330)
card(248,332,338,654,'Danh sách tự chọn')
for i,(ticker,name) in enumerate([('HPG','Hòa Phát'),('VNM','Vinamilk'),('FPT','FPT')]):
 y=396+i*126;rect(270,y,294,105,'pale' if i==0 else 'bg',8);text(288,y+33,ticker,21,weight=600);text(288,y+60,name,14,'muted');text(288,y+84,'Xem dữ liệu  →',12,'brand')
button(270,842,294,'Chỉnh danh sách theo dõi');text(270,947,'Chỉ doanh nghiệp đã tự chọn.',12,'muted')
card(606,332,798,393,'Công bố và phiên bản dữ liệu')
for yy,t,d,state in [(396,'HPG · BCTC năm 2025','Mở bộ số đã duyệt để tiếp tục phân tích.','uc1'),(505,'VNM · Thông báo cổ tức','Có lịch thanh toán; chưa xác nhận thực trả.','uc5'),(614,'FPT · Bản trình bày lại số so sánh','CFO 2024: 9.800 → 10.000 tỷ · chờ duyệt bản mới.','source')]:
 group('update-'+str(yy),state);text(628,yy+15,t,16,weight=600);text(628,yy+43,d,13,'muted');text(628,yy+72,'Xem công bố và nguồn  ↗',12,'brand');end();line(628,yy+89,1382,yy+89)
card(606,745,798,241,'Lịch sự kiện · các ngày giả định')
tag(628,797,'15/06/2026',w=110);text(758,815,'VNM · Lịch thanh toán cổ tức · chưa xác nhận trả',13)
tag(628,849,'20/06/2026',w=110);text(758,867,'FPT · Ngày đăng ký cuối cùng · xem thông báo gốc',13)
button(628,926,280,'Mở hồ sơ cổ tức','uc5',True);button(926,926,456,'Xem lần phân tích đã lưu','saved')
screens.append(finish('uc4','UC-4 · Theo dõi doanh nghiệp',4,['F04.1','F04.2','F04.3','F04.4','F04.5']))

shell('uc5',5,'Phân tích cổ tức tiền mặt','Đọc năm lợi nhuận, các đợt cấu thành và bối cảnh dòng tiền cùng nguồn.');filterbar()
card(248,290,680,311,'Lịch sử DPS theo năm lợi nhuận · đồng/cổ phiếu')
for i,(year,v) in enumerate([(2023,1200),(2024,1500),(2025,1800)]):
 x=352+i*180;rect(x,530-v/12,66,v/12,'brand' if i<2 else '#B6CFC6',5);text(x+33,515-v/12,f'{v:,}'.replace(',','.'),17,weight=600,anchor='middle');text(x+33,559,year,12,'muted',anchor='middle')
text(270,585,'DPS gốc; 2025 là mức quan sát, chưa xác nhận đầy đủ.',12,'amber')
card(948,290,456,311,'Độ đầy đủ và cơ sở so sánh');tag(970,353,'2025: còn thiếu nguồn','amberbg',210)
lines(970,412,['Còn cần kiểm các đợt thuộc lợi nhuận 2025.','Có sự kiện cổ phiếu cần xác minh hiệu lực.','Chưa tính tăng trưởng DPS hoặc payout.'],13,step=30)
button(970,527,412,'Kiểm cơ sở cổ phiếu và DPS','basis',True)
card(248,621,1156,183,'Các đợt cổ tức và trạng thái')
table(268,674,1116,['Năm lợi nhuận','Đợt / loại','DPS quan sát','Lịch thanh toán','Trạng thái'],[['2025','Đợt 1 · tiền mặt','1.000 đ/cp','Lịch theo thông báo','Chưa xác nhận trả'],['2025','Đợt 2 · tiền mặt','800 đ/cp','Cần kiểm bản sửa','Còn thiếu nguồn']], [172,252,170,235,287],rowheight=38)
card(248,824,746,179,'Bối cảnh dòng tiền năm 2025 · tỷ đồng')
lines(270,879,['CFO 16.000 − CAPEX 8.000 = 8.000','Trừ khoản phân phối đã chi 10.000 → còn −2.000','Khoản chi trên BCLCTT khác DPS trong thông báo.'],14,step=30)
button(1030,835,374,'Xem nguồn khoản chi và công thức','source');button(1030,891,374,'Đọc cầu nối CFO','bridge');button(1030,947,374,'Lưu hồ sơ nhận xét cổ tức','saved',True)
screens.append(finish('uc5','UC-5 · Phân tích cổ tức',5,['F05.1','F05.2','F05.3','F05.4','F05.5','F05.6']))

def document_panel(x,y,w,h):
    card(x,y,w,h,'BCLCTT · trang nguồn minh họa')
    rect(x+24,y+64,w-48,h-98,'bg',2);text(x+48,y+111,'BÁO CÁO LƯU CHUYỂN TIỀN TỆ',18,weight=600)
    lines(x+48,y+144,['Bố cục dựng để minh họa truy xuất nguồn','Năm 2025 · Hợp nhất · Đơn vị: triệu đồng'],12)
    rect(x+44,y+384,w-88,66,'pale',4)
    table(x+44,y+210,w-88,['Khoản mục','Mã','Năm 2025'],[['Lợi nhuận trước thuế','01','15.000.000'],['Điều chỉnh và vốn lưu động','…','1.000.000'],['Lưu chuyển tiền thuần HĐKD','20','16.000.000']],[(w-88)*.60,(w-88)*.12,(w-88)*.28],rowheight=66)
    text(x+48,y+h-67,'Chưa phải PDF hoặc số liệu nguồn đã xác minh.',12,'amber')

shell('source',1,'Bằng chứng của một số liệu','Từ ô số trên bảng, kiểm lại nhãn, cột, đơn vị và phiên bản tài liệu.',True);filterbar(period='Năm 2025')
document_panel(248,290,710,700);card(978,290,426,700,'CFO · lưu chuyển tiền thuần HĐKD')
text(1000,379,'16.000 tỷ đồng',29,'brand',600);lines(1000,422,['Giá trị chuẩn: 16.000.000.000.000 VND','Số gốc: 16.000.000 triệu đồng','Khoảng kỳ: 01/01–31/12/2025','Phạm vi: Hợp nhất','Dòng 20 · Cột năm hiện tại','Phiên bản: v1 · đã duyệt (minh họa)'],13,step=34)
line(1000,645,1382,645);lines(1000,682,['Định nghĩa','Tiền thuần từ hoạt động kinh doanh.','Giữ dấu âm nếu nguồn báo dùng tiền.','Không thay bằng tiền trước vốn lưu động.'],13,step=29)
button(1000,835,382,'Xem lịch sử duyệt','review');button(1000,901,382,'Quay lại bảng dữ liệu','uc1',True)
screens.append(finish('source','Chi tiết · Nguồn và định nghĩa',1,['F01.4','F01.5']))

shell('review',1,'Duyệt và tra soát số liệu','Vai trò vận hành: đối chiếu ứng viên với nguồn, giữ lý do và lịch sử sửa.',True);filterbar(period='Năm 2025',extra='Đang xem: ô 1 / 2')
card(248,290,1156,127,'Hàng đợi cần xử lý');table(268,340,1116,['Doanh nghiệp','Chỉ tiêu','Vấn đề','Thao tác'],[['HPG · 2025','CFO','Cần xác nhận cột và đơn vị','Đang mở']], [210,260,440,206],rowheight=34)
document_panel(248,437,710,563);card(978,437,426,563,'Ứng viên và quyết định')
lines(1000,504,['Số máy trích: 16.000.000','Đơn vị nguồn: triệu đồng','Chuẩn hóa: 16.000.000.000.000 VND','Cột: năm 2025 · Phạm vi: hợp nhất'],13,step=29)
text(1000,647,'Lý do duyệt / sửa',13,weight=600);rect(1000,665,382,95,'bg',8);lines(1014,694,['Đã đối chiếu nhãn dòng, cột và đơn vị.','Mẫu thao tác minh họa; chưa lưu thật.'],12)
tag(1000,783,'Trước → sau và người duyệt được lưu',w=335)
button(1000,837,382,'Duyệt và lưu lịch sử','source',True);button(1000,893,183,'Sửa ứng viên');button(1200,893,182,'Từ chối')
text(1000,970,'Bản đã thay đổi: tải lại trước khi duyệt.',11,'amber')
screens.append(finish('review','Chi tiết · Duyệt và tra soát',1,['F01.6']))

shell('bridge',2,'Cầu nối lợi nhuận trước thuế → CFO','Đọc các dòng đóng góp, phần còn lệch và nguồn; không ép số khớp bằng dòng bù.',True);filterbar(period='Năm 2025')
card(248,290,1156,352,'Các khoản cấu thành · tỷ đồng')
items=[('LNTT',15,0,'brand'),('Phi tiền',4,15,'blue'),('Vốn lưu động',-2,19,'red'),('Khoản khác',-1,17,'red'),('CFO',16,0,'brand')]
for i,(name,value,start,c) in enumerate(items):
 x=350+i*206;base=577;scale=10;bottom=min(start,start+value);height=abs(value)*scale
 rect(x,base-(bottom+abs(value))*scale,66,height,c,4)
 label=f'{abs(value)*1000:,}'.replace(',','.')
 if i not in [0,4]:label=('+' if value>0 else '−')+label
 text(x+33,base-(bottom+abs(value))*scale-15,label,16,weight=600,anchor='middle');text(x+33,609,name,12,'muted',anchor='middle')
 if i<4:line(x+66,base-(start+value)*scale,x+206,base-(start+value)*scale,'muted')
tag(1162,311,'Residual: 0','pale',215)
card(248,662,748,340,'Dòng nguồn và vai trò trong cầu nối');table(268,718,708,['Nhóm','Tác động','Vai trò'],[['Điểm đầu LNTT','15.000','Điểm đầu'],['Điều chỉnh phi tiền','+4.000','Dòng cấu thành'],['Thay đổi vốn lưu động','−2.000','Dòng cấu thành'],['Các khoản khác','−1.000','Dòng cấu thành'],['CFO cuối','16.000','Điểm cuối']], [350,150,208],rowheight=44,links={(3,1):'source'})
card(1016,662,388,340,'Diễn giải và bằng chứng');lines(1038,727,['15.000 + 4.000 − 2.000 − 1.000','= 16.000 tỷ đồng CFO.','Tổng trung gian chỉ dùng đối chiếu.','Ví dụ gộp nhóm để xem trước bố cục;','khi thực hiện cần từng dòng có nguồn.'],13,step=30)
button(1038,907,344,'Mở nguồn dòng cấu thành','source');button(1038,956,344,'Lưu cầu nối cùng nhận xét','saved',True)
screens.append(finish('bridge','Chi tiết · Cầu nối CFO',2,['F02.5']))

shell('basis',5,'Cơ sở cổ phiếu và tính so sánh DPS','Giữ DPS gốc; chỉ điều chỉnh chuỗi khi có sự kiện và ngày hiệu lực được xác minh.',True);filterbar()
rect(248,290,1156,65,'amberbg',10);text(270,329,'Chưa đủ cơ sở điều chỉnh. Hệ thống hiển thị lý do và giữ nguyên số DPS gốc.',14,'amber',600)
card(248,378,1156,293,'Sự kiện cần xác minh');table(268,435,1116,['Sự kiện','Tỷ lệ','Ngày hiệu lực','Nguồn / trạng thái'],[['Cổ tức bằng cổ phiếu','Cần đối chiếu','Chưa xác định','Cần tài liệu xác nhận'],['Phát hành làm thay đổi số cổ phiếu','Chưa đủ dữ liệu','Không dùng ngày chốt thay thế','Chưa đủ cơ sở điều chỉnh']], [295,165,305,351],rowheight=74)
card(248,691,748,312,'DPS gốc và DPS tham chiếu');table(268,749,708,['Năm lợi nhuận','DPS quan sát · đ/cp','DPS tham chiếu'],[['2023','1.200','Chưa tính'],['2024','1.500','Chưa tính'],['2025','1.800 · chưa đầy đủ','Chưa tính']], [220,235,253],rowheight=53)
card(1016,691,388,312,'Thông tin cần bổ sung');lines(1038,755,['Loại sự kiện và đối tượng cổ phiếu','Tỷ lệ, cơ sở quyền, quy tắc làm tròn','Ngày hiệu lực có tài liệu xác nhận','Không coi mọi phát hành là chia tách','Không cộng cổ phiếu vào tiền mặt'],13,step=30)
button(1038,941,344,'Quay lại lịch sử cổ tức','uc5',True)
screens.append(finish('basis','Chi tiết · Cơ sở DPS',5,['F05.4','F05.5']))

shell('saved',2,'Phân tích đã lưu và nhận xét','Mở lại đúng bộ số, nguồn và bối cảnh đã dùng; tiếp tục nghiên cứu từ câu hỏi đã ghi.',True);filterbar(period='2023 — 2025',extra='Hồ sơ minh họa')
card(248,290,410,707,'Hồ sơ đã lưu')
for i,(a,b) in enumerate([('HPG · Lợi nhuận và CFO','2023–2025 · hợp nhất'),('HPG / VNM / FPT · So sánh','Năm 2025 · nhóm tự chọn'),('HPG · Cổ tức và dòng tiền','Dữ liệu còn thiếu cơ sở DPS')]):
 y=363+i*133;rect(270,y,366,112,'pale' if i==0 else 'bg',8);text(287,y+34,a,13,weight=600);text(287,y+63,b,12,'muted');text(287,y+88,'Bản lưu mẫu · chưa ghi vào hệ thống',11,'muted')
card(678,290,726,707,'Nhận xét: lợi nhuận tăng có đi cùng tiền?');tag(700,350,'Giữ bản dữ liệu đã dùng',w=226)
text(700,411,'Nhận xét của người dùng',15,weight=600);rect(700,432,682,118,'bg',8);lines(716,461,['Năm 2024 LNST tăng, CFO giảm. Cần đọc thay đổi vốn lưu động','và các khoản điều chỉnh để hiểu nguyên nhân. Đây là ví dụ nhận xét,','không phải kết luận về doanh nghiệp thật.'],14,step=29)
text(700,599,'Bằng chứng gắn với nhận xét',15,weight=600);lines(700,636,['LNST/CFO 2023–2025 và phiên bản số đã chọn','Nguồn từng ô và công thức có điều kiện','Cầu nối theo ca, phần thiếu và giới hạn diễn giải'],13,step=31)
text(700,778,'Câu hỏi cần nghiên cứu tiếp',15,weight=600);lines(700,815,['Khoản vốn lưu động nào làm CFO thay đổi?','CAPEX và phân phối đã chi tác động thế nào?'],14)
button(700,921,218,'Xem nguồn','source');button(936,921,216,'Mở phân tích','uc2');button(1170,921,212,'Xuất hồ sơ')
screens.append(finish('saved','Chi tiết · Hồ sơ phân tích',2,['F02.8','F05.6']))

manifest={'version':1,'created':'2026-10-11','status':'local_design_complete_figma_canvas_blocked_by_starter_tool_limit',
 'figma_file_url':'https://www.figma.com/design/GbpKDOPNhXuCYC2X2Yt7sa','figma_canvas_status':'blank; import run not committed',
 'data_status':'All financial values and document layouts are synthetic illustrations, not company evidence.',
 'font':'Be Vietnam Pro','tokens':TOKENS,'screens':[{k:v for k,v in s.items() if k!='svg'} for s in screens]}
(OUT/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
links=''.join(f'<button class="screen-button" data-target="{s["id"]}">{escape(s["title"])}</button>' for s in screens)
views=''.join(f'<section id="view-{s["id"]}" class="screen" hidden>{s["svg"]}</section>' for s in screens)
html='''<!doctype html><html lang="vi"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Thiết kế 5 UC · Nền tảng tài chính</title><style>
*{box-sizing:border-box}body{margin:0;background:#e8edef;font:14px/1.6 "Segoe UI",Arial,sans-serif;color:#182f39}header{background:#fff;padding:20px 28px;border-bottom:1px solid #dce5e8}h1{margin:0;font-size:24px}header p{margin:6px 0;color:#64767e}.note{padding:10px 16px;background:#fff3da;border-radius:8px;margin-top:10px}nav{display:flex;gap:8px;flex-wrap:wrap;padding:16px 28px}button{font:inherit;cursor:pointer;background:white;border:1px solid #c7d5d9;border-radius:7px;padding:8px 12px;color:#182f39}button.active{background:#126b59;color:white;border-color:#126b59}button:focus-visible,[data-screen]:focus-visible{outline:3px solid #4168c8;outline-offset:3px}.canvas{padding:0 28px 24px;overflow:auto}.screen{min-width:950px;max-width:1440px;margin:auto;box-shadow:0 8px 32px #182f3914}.screen svg{display:block;width:100%;height:auto}.summary{padding:0 28px 18px}a{color:#126b59}.legend{display:flex;gap:20px;flex-wrap:wrap}.badge{background:#e6f4ee;border-radius:20px;padding:4px 10px}footer{padding:20px 28px;background:white} [hidden]{display:none!important}@media(max-width:700px){header,nav,footer{padding:16px}.canvas{padding:0 12px 16px}.summary{padding:0 16px 18px}.screen{min-width:950px}h1{font-size:21px}}
</style><header><h1>Thiết kế tổng quan 5 UC</h1><p>Web React + FastAPI + PostgreSQL · HPG / VNM / FPT · Chọn màn hình hoặc bấm điều hướng trong bản thiết kế.</p><div class="note">Figma đã tạo tệp nhưng hết lượt công cụ Starter; canvas chưa có màn hình. Bản xem và 10 SVG bên dưới đã được dựng để nhập vào Figma. Mọi số liệu là minh họa.</div></header><nav>__LINKS__</nav><div class="summary"><div class="legend"><span class="badge">5 màn hình chính + 5 màn hình chi tiết</span><span>Ưu tiên UC-1/2/3/5; UC-4 triển khai sau</span><span>Điều hướng mô phỏng, chưa kết nối backend</span></div></div><main class="canvas">__VIEWS__</main><footer><a href="man-hinh-5-uc-svg.zip" download>Tải 10 màn hình SVG để nhập Figma</a> · <a href="README.md">Danh mục màn hình và hướng dẫn</a> · <a href="https://www.figma.com/design/GbpKDOPNhXuCYC2X2Yt7sa">Tệp Figma đã tạo (chưa có màn hình)</a><p>SVG gồm text và vector chỉnh sửa được. Sau nhập cần tổ chức lại auto-layout và components; không phải một design system Figma đã hoàn thiện.</p></footer><script>
function show(id){if(!document.getElementById('view-'+id))id='uc1';document.querySelectorAll('.screen').forEach(n=>n.hidden=n.id!=='view-'+id);document.querySelectorAll('[data-target]').forEach(n=>n.classList.toggle('active',n.dataset.target===id));location.hash=id;}
document.addEventListener('click',e=>{const t=e.target.closest('[data-target],[data-screen]');if(t)show(t.dataset.target||t.dataset.screen)});document.addEventListener('keydown',e=>{if((e.key==='Enter'||e.key===' ')&&e.target.dataset.screen){e.preventDefault();show(e.target.dataset.screen)}});window.addEventListener('hashchange',()=>show(location.hash.slice(1)));show(location.hash.slice(1)||'uc1');
</script></html>'''.replace('__LINKS__',links).replace('__VIEWS__',views)
(OUT/'index.html').write_text(html,encoding='utf-8')
readme='''# Thiết kế tổng quan 5 UC

Ngày 11/10/2026. [Bản xem tương tác](index.html), [bộ 10 SVG](man-hinh-5-uc-svg.zip), [manifest](manifest.json).

**Trạng thái:** đã hoàn thành bản thiết kế local. Tệp Figma `GbpKDOPNhXuCYC2X2Yt7sa` đã được tạo nhưng công cụ báo hết hạn mức Starter trước khi ghi màn hình; canvas vẫn trống. Không coi tệp trống là thiết kế đã hoàn tất trong Figma.

## Cách xem và nhập Figma

Mở index.html, chọn một trong 10 màn hình hoặc bấm mục bên trái/các nút dẫn tới chi tiết. Đây là prototype điều hướng; bộ chọn, duyệt, lưu và xuất chưa xử lý dữ liệu thật. Bảng tiền dùng tỷ đồng; DPS dùng đồng/cổ phiếu. **Tất cả số liệu, lịch công bố và bố cục tài liệu đều là giả định minh họa**, không là số tài chính doanh nghiệp đã đối chiếu.

Giải nén bộ SVG, kéo các tệp vào Figma Design. Các màn hình chứa text/shape/path chỉnh sửa được, không là ảnh chụp toàn giao diện. Dùng font Be Vietnam Pro đã được xác nhận có trong Figma. SVG nhập vào không tự thành auto-layout/components; bước tiếp theo là tổ chức các lớp, liên kết prototype và chuyển phần dùng chung sang components/tokens. Không import ảnh PNG của toàn màn hình để thay lớp chỉnh sửa.

## Danh mục màn hình

| Màn hình | Vai trò | UC nhỏ |
|---|---|---|
'''
for s in screens:readme+=f'| [{s["title"]}]({s["file"]}) | '+({'uc1':'Bảng nhiều kỳ, bộ chọn, độ đầy đủ, nguồn và xuất','uc2':'Biểu đồ LNST–CFO, tỷ số có điều kiện và nhận xét','uc3':'So nhóm tự chọn; giải thích khác ngành','uc4':'Danh sách quan tâm, công bố, phiên bản và lịch sự kiện','uc5':'DPS/năm lợi nhuận, coverage, lịch trả và bối cảnh tiền','source':'Một ô về định nghĩa và đúng dòng/cột/trang nguồn','review':'Vai trò vận hành: đối chiếu, duyệt/sửa và giữ audit','bridge':'Cầu nối CFO, khoản đóng góp và residual','basis':'Giữ DPS gốc, chặn điều chỉnh khi thiếu cơ sở','saved':'Giữ bối cảnh, bằng chứng, nhận xét/câu hỏi'}[s['id']])+f' | {", ".join(s["functions"])} |\n'
readme+='''
## Những quyết định thể hiện trên giao diện

- Năm, hợp nhất/riêng lẻ, unit và tình trạng dữ liệu hiện rõ; thiếu khác 0.
- UC-1 phục vụ khai thác dữ liệu; duyệt/trích là màn hình hỗ trợ vận hành.
- Biểu đồ thuộc UC-2/3/5, không thành một UC độc lập. Chưa đưa DuPont/quý/định giá vào lát cắt đầu.
- So sánh HPG/VNM/FPT là nhóm tự chọn khác ngành; không xếp hạng, sàng lọc hoặc cảnh báo tiêu chí.
- Lịch thanh toán chưa là xác nhận thực trả; năm lợi nhuận khác năm công bố.
- DPS gốc/điều chỉnh và tiền thực chi trên BCLCTT tách riêng. Thiếu basis/coverage chặn tăng trưởng/payout.
- Hồ sơ lưu giữ số nguồn và version đã dùng; dữ liệu mới không tự sửa nhận xét cũ.
- UC-4 được vẽ để thấy sản phẩm tổng thể, vẫn triển khai sau UC-1/2/3/5.

Thiết kế này không bổ sung nghĩa vụ SRS chỉ vì có màn hình. Các mục F04, giao diện hồ sơ và tương tác biểu đồ là đề xuất/lát cắt đã ghi ở danh mục; chưa triển khai hoặc nghiệm thu. Đối chiếu với [yêu cầu chức năng](../research-platform/27-yeu-cau-chuc-nang-va-vi-du.md), [stack](../research-platform/31-chot-pham-vi-va-stack-paddleocr.md) và [kế hoạch](../research-platform/32-ke-hoach-10-tuan-tiep-theo.md).
'''
(OUT/'README.md').write_text(readme,encoding='utf-8')
with zipfile.ZipFile(OUT/'man-hinh-5-uc-svg.zip','w',zipfile.ZIP_DEFLATED) as z:
    for s in screens:z.write(OUT/s['file'],s['file'])
    for name in ['README.md','manifest.json']:z.write(OUT/name,name)
print(json.dumps({'screens':len(screens),'editable_svg_count':len(screens),'output':str(OUT),'figma_canvas':'blank; rate limited'},ensure_ascii=True))
