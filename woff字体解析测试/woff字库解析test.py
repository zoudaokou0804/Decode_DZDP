from fontTools.ttLib import TTFont

font = TTFont(r'C:\Users\a6540\Desktop\楷体_GB2312.woff')
font.saveXML(r'C:\Users\a6540\Desktop\SH_Life\AnalysisData\woff字体解析\楷体GB2312.xml')  # 将 woff 写为 xml 文件从而就可以对 xml 文件进行操作了

