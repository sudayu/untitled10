#引入相关模块
import requests

#从百度上爬取数据
url = 'http://www.baidu.com/'
r_obj = requests.get(url)
r_obj.encoding = 'utf-8'
print(r_obj.text)
print(r_obj.content)


