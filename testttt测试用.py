import re
txt="""
@font-face{font-family: "PingFangSC-Regular-tagName";src:url("//s3plus.meituan.net/v1/mss_73a511b8f91f43d0bdae92584ea6330b/font/abef7b00.eot");src:url("//s3plus.meituan.net/v1/mss_73a511b8f91f43d0bdae92584ea6330b/font/abef7b00.eot?#iefix") format("embedded-opentype"),url("//s3plus.meituan.net/v1/mss_73a511b8f91f43d0bdae92584ea6330b/font/abef7b00.woff");} .tagName{font-family: 'PingFangSC-Regular-tagName';}@font-face{font-family: "PingFangSC-Regular-shopNum";src:url("//s3plus.meituan.net/v1/mss_73a511b8f91f43d0bdae92584ea6330b/font/af3ce6b9.eot");src:url("//s3plus.meituan.net/v1/mss_73a511b8f91f43d0bdae92584ea6330b/font/af3ce6b9.eot?#iefix") format("embedded-opentype"),url("//s3plus.meituan.net/v1/mss_73a511b8f91f43d0bdae92584ea6330b/font/af3ce6b9.woff");} .shopNum{font-family: 'PingFangSC-Regular-shopNum';}@font-face{font-family: "PingFangSC-Regular-reviewTag";src:url("//s3plus.meituan.net/v1/mss_73a511b8f91f43d0bdae92584ea6330b/font/413b3070.eot");src:url("//s3plus.meituan.net/v1/mss_73a511b8f91f43d0bdae92584ea6330b/font/413b3070.eot?#iefix") format("embedded-opentype"),url("//s3plus.meituan.net/v1/mss_73a511b8f91f43d0bdae92584ea6330b/font/413b3070.woff");} .reviewTag{font-family: 'PingFangSC-Regular-reviewTag';}@font-face{font-family: "PingFangSC-Regular-address";src:url("//s3plus.meituan.net/v1/mss_73a511b8f91f43d0bdae92584ea6330b/font/76849753.eot");src:url("//s3plus.meituan.net/v1/mss_73a511b8f91f43d0bdae92584ea6330b/font/76849753.eot?#iefix") format("embedded-opentype"),url("//s3plus.meituan.net/v1/mss_73a511b8f91f43d0bdae92584ea6330b/font/76849753.woff");} .address{font-family: 'PingFangSC-Regular-address';}"""
# print(txt)
pat=re.compile('{(.*?)}', re.S)
li=pat.findall(txt)
a=li[0]
print(a)
print('\n')
print('*'*50)
pat2=re.compile('((.*?))', re.S)
li2=pat.findall(a)
print('*'*50)
b=a.split('("')[1].split('")')[0]
print(b)


# def getfontslink(url):
#     # 方法2 直接调用上面函数返回结果，这里要从txt中地区主要是为了方便调试，免得再跑一圈网上数据，省的ip又被封了
#     li = getcsslink(url)
#     # 下面方法熊txt中读取css链接
#     # li=[]
#     d = []
#     # with open(r'C:\Users\a6540\Desktop\大众点评字体加密库\csslink.txt','r',encoding='utf-8') as f2:
#     #     for line in f2:
#     #         li.append(line.replace('\n', ''))
#     print('\n' + 'css链接集合：')
#     print(li)
#     for css in set(li):
#         txt = requests.get(css).text
#         # print(txt)
#         pattern = re.compile('"//(.*?)"')
#         a = list(set(pattern.findall(txt)))
#         for b in a:
#             if 'iefix' not in b:
#                 d.append('http://' + b)
#     print('\n' + '字体文件链接集合：')
#     print(d)
#     return d