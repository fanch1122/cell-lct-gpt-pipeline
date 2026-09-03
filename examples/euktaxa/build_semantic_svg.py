from pathlib import Path
import math

OUT=Path(__file__).with_name('shibielujing6-gpt-master.svg'); P=[]; n=0
def add(s):
 global n; n+=1; P.append(s.replace('ID',f'gpt6-{n:04d}'))
def rect(x,y,w,h,fill='#fff',stroke='#222',rx=7,sw=2): add(f'<rect id="ID" x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')
def line(x1,y1,x2,y2,c='#222',sw=2): add(f'<line id="ID" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c}" stroke-width="{sw}"/>')
def arrow(x1,y1,x2,y2,c='#222',sw=2):
 line(x1,y1,x2,y2,c,sw); a=math.atan2(y2-y1,x2-x1); z=9
 p1=(x2-z*math.cos(a-.48),y2-z*math.sin(a-.48)); p2=(x2-z*math.cos(a+.48),y2-z*math.sin(a+.48))
 add(f'<polygon id="ID" points="{x2},{y2} {p1[0]:.2f},{p1[1]:.2f} {p2[0]:.2f},{p2[1]:.2f}" fill="{c}"/>')
def text(x,y,s,size=17,w='normal',fill='#111',anchor='middle'):
 s=s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
 add(f'<text id="ID" x="{x}" y="{y}" font-family="Microsoft YaHei, Arial, sans-serif" font-size="{size}" font-weight="{w}" fill="{fill}" text-anchor="{anchor}">{s}</text>')
def multi(x,y,ss,size=16,w='normal',fill='#111',anchor='middle',dy=24):
 for i,s in enumerate(ss): text(x,y+i*dy,s,size,w,fill,anchor)
def chart(cx,y):
 hs=[17,31,49,27,13]; xs=[cx-34,cx-18,cx-2,cx+14,cx+30]
 line(cx-43,y+51,cx+48,y+51,'#6840a1',1.3)
 for x,h in zip(xs,hs): rect(x,y+51-h,10,h,'#d6bfef','#7042aa',0,1.4)
def dashed(x,y,w,h):
 for xx in range(x,x+w,18): line(xx,y,min(xx+11,x+w),y,'#6c3caf',1.8); line(xx,y+h,min(xx+11,x+w),y+h,'#6c3caf',1.8)
 for yy in range(y,y+h,18): line(x,yy,x,min(yy+11,y+h),'#6c3caf',1.8); line(x+w,yy,x+w,min(yy+11,y+h),'#6c3caf',1.8)

P.append('<svg xmlns="http://www.w3.org/2000/svg" width="1122" height="1402" viewBox="0 0 1122 1402">'); rect(0,0,1122,1402,'#fff','#fff',0,0)
text(445,60,'EukTaxa 模型总体框架',34,'700','#123a79')
rect(265,84,560,87,'#f5f9ff','#1457ae',10,2); text(548,125,'18S 序列输入',25,'700','#123a79'); text(590,153,'A  G  T  C  G  A  T   ...   ...   ...   C  T  A  G  C  T',15)
# DNA icon
for i in range(5): line(318+i*8,104+i*8,344+i*8,130+i*8,'#1457ae',3); line(344+i*8,104+i*8,318+i*8,130+i*8,'#1457ae',3)
line(530,171,530,194); line(201,194,708,194); arrow(201,194,201,225); arrow(708,194,708,225)
rect(52,226,315,132,'#f7fbff','#1457ae',10,2); text(209,264,'局部模式编码器',24,'700','#123a79'); text(209,294,'（单碱基 CNN）',18,'700','#123a79')
for x in [75,104,133,177,206,257,286]: rect(x,315,21,22,'#dbe9fa','#1761bb',0,1.3)
text(163,333,'·',18); text(232,333,'··',18); text(323,333,'···',18)
rect(520,226,369,132,'#f7fcf5','#3d8a2f',10,2); text(705,264,'上下文编码器',24,'700','#236b27'); text(705,294,'(overlapping k-mer transformer)',17)
for x,s in [(542,'AGTC'),(632,'GTCG'),(722,'TCGA')]: rect(x,311,77,37,'#eef7ea','#3d8a2f',7,1.4); text(x+38.5,337,s,16)
text(838,337,'···',20)
arrow(202,358,202,393); arrow(701,358,701,393)
rect(62,394,276,49,'#f7fbff','#1457ae',7,1.8); text(200,426,'局部 motif 特征',20,'700','#123a79')
rect(544,394,315,49,'#f7fcf5','#3d8a2f',7,1.8); text(701,426,'长距离 / 上下文特征',20,'700','#236b27')
line(202,443,202,462); line(701,443,701,462); line(202,462,452,462); line(701,462,452,462); arrow(452,462,452,490)
rect(294,490,319,76,'#fff8e8','#ee9800',9,2); text(453,524,'特征融合主干',23,'700','#b95b00'); text(453,552,'（融合与投影）',17,'700','#b95b00'); arrow(453,566,453,596)
rect(54,596,752,137,'#fff','#6840a1',10,2); text(430,632,'分层预测头（自顶向下）',24,'700','#3f207f')
heads=[(75,'Domain','头 1'),(207,'Supergroup','头 2'),(355,'Division','头 3'),(562,'Genus','头 8'),(691,'Species','头 9')]
for x,a,b in heads: rect(x,646,110,75,'#f4effb','#7042aa',6,1.6); multi(x+55,676,[a,b],16,'normal','#22134c',dy=25); arrow(x+55,721,x+55,753); chart(x+55,753)
text(505,683,'···',21); text(505,787,'···',21); multi(14,765,['每层','logits'],17,'normal','#111','start',25)
line(130,804,742,804); arrow(446,804,446,847)
rect(200,847,485,82,'#fff1f1','#e22a25',9,2); text(443,882,'ConstrainedDecoder',24,'700','#b1110e'); text(443,913,'（利用分类树 + Beam Search + 拒绝预测）',17,'700','#b1110e'); arrow(445,929,445,964)
rect(124,965,663,302,'#fbfff9','#4a9d39',18,2); text(455,1001,'分类树（部分）',23,'700','#23751d')
rect(399,1011,116,31,'#eff8ec','#4a9d39',6,1.5); text(457,1033,'Domain',15)
line(457,1042,457,1050); line(308,1050,608,1050); arrow(308,1050,308,1061); arrow(457,1050,457,1061); arrow(608,1050,608,1061)
for x,s in [(249,'Eukarya'),(411,'Bacteria'),(554,'Archaea')]: rect(x,1061,117,31,'#eff8ec','#4a9d39',6,1.5); text(x+58,1083,s,15)
text(695,1084,'···',19); line(308,1092,308,1102); line(207,1102,468,1102); arrow(207,1102,207,1112); arrow(375,1102,375,1112)
for x,s in [(147,'Supergroup A'),(311,'Supergroup B')]: rect(x,1112,136,31,'#eff8ec','#4a9d39',6,1.5); text(x+68,1134,s,14)
text(505,1135,'···',19); line(207,1143,207,1153); line(178,1153,292,1153); arrow(178,1153,178,1163); arrow(292,1153,292,1163)
for x,s in [(132,'Division A1'),(247,'Division A2')]: rect(x,1163,105,31,'#eff8ec','#4a9d39',6,1.5); text(x+52,1185,s,13)
text(400,1186,'···',19); arrow(181,1194,181,1215); arrow(300,1194,300,1215)
for x,s in [(132,'Genus ...'),(257,'Species ...')]: rect(x,1215,100,31,'#eff8ec','#4a9d39',6,1.5); text(x+50,1237,s,13)
text(400,1238,'···',19); arrow(458,1267,458,1297)
rect(302,1298,311,83,'#f7fbff','#1457ae',10,2); text(457,1352,'最终合法谱系',25,'700','#123a79')
# clipboard icon
rect(331,1317,48,52,'#fff','#1457ae',3,3); rect(342,1310,26,12,'#fff','#1457ae',4,3); line(341,1337,348,1344,'#1457ae',3); line(348,1344,360,1330,'#1457ae',3); rect(365,1344,31,31,'#24a85a','#24a85a',16,0); line(374,1360,381,1366,'#fff',3); line(381,1366,391,1353,'#fff',3)
# right explanation column
items=[(628,'双分支编码',['CNN 捕获局部 motif，','Transformer 捕获长距离 /','上下文信息']),(785,'特征融合',['融合两类特征，形成','统一表示']),(914,'分层预测',['9 个自顶向下的分类头','逐层输出 logits']),(1040,'约束解码',['结合分类树，采用','Beam Search 与','拒绝机制，保证结果合法']),(1205,'输出结果',['输出最终的合法分类谱系'])]
for idx,(y,title,body) in enumerate(items,1):
 add(f'<circle id="ID" cx="881" cy="{y}" r="18" fill="#12479b"/>'); text(881,y+7,str(idx),20,'700','#fff'); text(912,y+7,title,20,'700','#12479b','start'); multi(912,y+42,body,15,'normal','#222','start',31)
P.append('</svg>'); OUT.write_text('\n'.join(P),encoding='utf-8'); print(OUT)
