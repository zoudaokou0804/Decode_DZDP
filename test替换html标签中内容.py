from lxml import etree
import re

with open(r'C:\Users\a6540\Desktop\大众点评字体解密\Decode_DZDP\htmlsourcecode.html', 'r', encoding='utf-8') as f:
    htl = f.read()
# htl2 = etree.HTML(htl)
# kjh = htl2.xpath('//svgmtsi')
# for k in kjh:
#     tn=k.xpath('@class')[0]
#     # te=etree.tostring(k)
#     if tn=='address':
#         print(tn)
#         print(k.xpath('text()'))
#         print(etree.tostring(k))

pat=re.compile('<svgmtsi class="(.*?)">(.*?)</svgmtsi>')
ll=pat.findall(htl)
for i in ll:
    if i[0]=='shopNum':
        t='王超'
        htl=htl.replace('<svgmtsi class="shopNum">{}</svgmtsi>'.format(i[1]), '<svgmtsi class="shopNum">{}</svgmtsi>'.format(t))
with open(r'C:\Users\a6540\Desktop\大众点评字体解密\Decode_DZDP\htmlsourcecode2.html', 'w', encoding='utf-8') as f:
    f.write(htl)