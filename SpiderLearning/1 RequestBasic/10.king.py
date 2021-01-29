"""
@Time : 2021/1/29 16:37 
@Author : Steven Chen
@File : 10.king.py 
@Software: PyCharm
"""
# 目标：
# 方法：
import requests
import json
class King(object):
    def __init__(self):
        self.url = 'http://www.iciba.com/fy'
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.53"
        }
        self.data = {

        }
    def get_data(self):
        response = requests.get(self.url, data = self.data, headers = self.header)
        return response.content

    def parse_data(self,data):
        dict_data  = json.loads(data)

    def run(self):
        #缩写爬虫
        pass
        # url
        # header
        # data字典
        # 发送请求获取响应
        response = self.get_data()
        print(response)
        # 数据解析
        self.parse_data(response)
if __name__ == '__main__':
    king = King()
    king.run()