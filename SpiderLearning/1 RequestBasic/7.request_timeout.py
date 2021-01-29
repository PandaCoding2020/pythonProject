"""
@Time : 2021/1/29 15:07 
@Author : Steven Chen
@File : 7.request_timeout.py 
@Software: PyCharm
"""
# 目标：
# 方法：
import requests

url = 'https://twitter.com'
response = requests.get(url, timeout=3)
