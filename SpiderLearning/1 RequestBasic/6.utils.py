"""
@Time : 2021/1/29 11:08 
@Author : Steven Chen
@File : 6.utils.py 
@Software: PyCharm
"""
# 目标：
# 方法：
import requests

url = 'https://www.baidu.com'

response = requests.get(url)
print(response.cookies)

dict_cookies = requests.utils.dict_from_cookiejar(response.cookies)
print(dict_cookies)

jar_cookies = requests.utils.cookiejar_from_dict(dict_cookies)
print(jar_cookies)