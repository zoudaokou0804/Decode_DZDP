import pandas as pd
import numpy as np
import pymysql
import requests
from lxml import etree
from get_proxy_ip import get_proxyip, getheaders
from fake_useragent import UserAgent
from tqdm import tqdm
import pymysql as pm
import re 
def gethtml(url):
    data = {
        'cityId': '1',
        'cityChName': '上海',
        'cityEnName': 'shanghai',
        'pageType': 'search',
        'userId': '1142709687',
        'userName': 'ZoudaokoU_8412',
        'searchType': 'category',
        'categoryId': '0',
        'seo': 'false'
    }
    user_agent = UserAgent().random
    headers = {
        'User-Agent':
        user_agent,
        'Referer':
        url,
        'Accept':
        'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Connection':
        'keep-alive',
        'Cookie':
        'navCtgScroll=0; _lxsdk_cuid=1701b0d982b7c-001b7e25110448-3a65420e-1fa400-1701b0d982cc8; _lxsdk=1701b0d982b7c-001b7e25110448-3a65420e-1fa400-1701b0d982cc8; _hc.v=563cf142-fbcb-d930-575f-1b7a8e71987a.1581001842; s_ViewType=10; ua=ZoudaokoU_8412; ctu=72ebc9cb42cc57573729b84348eccf3564be61a380fc3b49751f82ac13a1c08f; aburl=1; cy=1; cye=shanghai; Hm_lvt_dbeeb675516927da776beeb1d9802bd4=1581358123,1581402480,1581431820; cityInfo=%7B%22cityId%22%3A1%2C%22cityName%22%3A%22%E4%B8%8A%E6%B5%B7%22%2C%22provinceId%22%3A0%2C%22parentCityId%22%3A0%2C%22cityOrderId%22%3A0%2C%22isActiveCity%22%3Afalse%2C%22cityEnName%22%3A%22shanghai%22%2C%22cityPyName%22%3Anull%2C%22cityAreaCode%22%3Anull%2C%22cityAbbrCode%22%3Anull%2C%22isOverseasCity%22%3Afalse%2C%22isScenery%22%3Afalse%2C%22TuanGouFlag%22%3A0%2C%22cityLevel%22%3A0%2C%22appHotLevel%22%3A0%2C%22gLat%22%3A0%2C%22gLng%22%3A0%2C%22directURL%22%3Anull%2C%22standardEnName%22%3Anull%7D; dplet=c19cde79cace62a3b84ea7fc3b9454c0; dper=a4b4e7fd903b7d0657c3b5fb3d28472c30e24bb340ec9685e34c0817ecdcacb7c0e7ebee2c23a33f4c66c269f130196d87417f9229988fe80655c91e020ee24fb60a07d26486197a2b622256b257bce245743be3fba70a73fa8e67d136d58aa5; ll=7fd06e815b796be3df069dec7836c3df; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_s=17046d5304b-b9d-7cf-324%7C%7C92'
    }
    rsp = requests.get(url, params=data, headers=headers)
    rsp.encoding = 'utf-8'
    html = rsp.text
    if rsp.status_code==200:
        return html
    else:
        gethtml(url)
        
def pa(html):
    pat=re.compile('&#x....;')
    li=pat.findall(html)
    print(li)
if __name__ == "__main__":
    url='http://www.dianping.com/shanghai/ch10/g1338p1'
    # gethtml(url)
    pa(gethtml(url))
