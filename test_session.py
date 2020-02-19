#requests.session():维持会话,可以让我们在跨请求时保存某些参数
 
 
import requests
 
#实例化session
session = requests.session()
 
#目标url
url = 'http://www.dianping.com'
 
form_data = {
    'source': 'index_nav',
    'form_email': 'xxx',
    'form_password': 'xxx',
    'captcha-solution': 'stamp',
    'captcha-id': 'b3dssX515MsmNaklBX8uh5Ab:en'
}
 
#设置请求头
req_header = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}
 
#使用session发起请求
response = session.post(url,headers=req_header,data=form_data)
 
if response.status_code == 200:
 
    #访问个人主页：
    url = 'http://www.dianping.com/shanghai/ch10/g1783'
 
    response = session.get(url,headers = req_header)
 
    if response.status_code == 200:
 
        with open('douban3.html','w') as file:
 
            file.write(response.text)