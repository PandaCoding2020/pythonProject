"""
@Time : 2021/1/30 13:56 
@Author : Steven Chen
@File : 3.jsonpath_case.py 
@Software: PyCharm
"""
# 目标：
# 方法：
import requests
import jsonpath
import json
url = 'https://www.lagou.com/lbs/getAllCitySearchLabels.json'
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.53'
}

response = requests.get(url,headers = headers)

dict_data = json.loads(response.content)
print(jsonpath.jsonpath(dict_data,'$..name'))