"""
@Time : 2021/1/29 9:30 
@Author : Steven Chen
@File : 3 request_parents.py 
@Software: PyCharm
"""
# 目标：如何发送带参数的请求
# 方法：1. url中直接带参数 2.
# import requests
# url = 'https://www.baidu.com/s?wd=gitbook'
# header = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.53"}
# response = requests.get(url, headers = header)
# with open('baidu.com','wb') as f:
#     f.write(response.content)

import requests
url = 'https://www.baidu.com/s?'
header = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.53"}
# 构建参数字典
data = {
    'wd':'python'
}
response = requests.get(url, headers = header, params=data)
print(response.url)
with open('baidu.com','wb') as f:
    f.write(response.content)