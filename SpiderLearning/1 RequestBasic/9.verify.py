"""
@Time : 2021/1/29 16:26 
@Author : Steven Chen
@File : 9.verify.py 
@Software: PyCharm
"""
# 目标：
# 方法：
import requests

import requests
url = "https://sam.huat.edu.cn:8443/selfservice/"
response = requests.get(url, verify = False)
print(response.content)