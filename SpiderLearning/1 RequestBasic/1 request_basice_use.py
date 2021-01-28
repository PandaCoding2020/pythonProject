"""
@Time : 2021/1/28 22:31 
@Author : Steven Chen
@File : 1 request_basice_use.py 
@Software: PyCharm
"""
# 目标：
# 方法：
import requests
url = 'https://www.baidu.com'
response = requests.get(url)
# response.encoding = 'utf-8'
# # print(response.text)
# print(response.content.decode())
# # print(response.encoding)

# 常见的响应对象和方法
# 响应url
print(response.url)
# 状态码
print(response.status_code)
# 响应对应的请求头
print(response.request.headers)
# cookie
print(response.cookies)