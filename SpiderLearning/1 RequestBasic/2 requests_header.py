"""
@Time : 2021/1/29 9:17 
@Author : Steven Chen
@File : 2 requests_header.py 
@Software: PyCharm
"""
# 目标：
# 方法：
import requests

url = 'https://www.baidu.com'

response = requests.get(url)

print(len(response.content.decode()))
print(response.content.decode())
# 带请求头的请求
header = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.53"}
response1 = requests.get(url,headers = header)

print(len(response1.content.decode()))
print(response1.content.decode())