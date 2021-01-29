"""
@Time : 2021/1/29 15:37 
@Author : Steven Chen
@File : 8.proxies.py 
@Software: PyCharm
"""
# 目标：
# 方法：
import requests

url = 'https://www.baidu.com'

proxies = {
    'https':'https://223.247.164.117:9999'
}

response = requests.get(url, proxies = proxies)
print(response.text)