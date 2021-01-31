"""
@Time : 2021/1/30 11:32 
@Author : Steven Chen
@File : 1.jsonpath_test.py 
@Software: PyCharm
"""
# 目标：
# 方法：
from jsonpath import jsonpath

data = {'key1':{'key2':{'key3':{'key4':{'key5':{'key6':{'key7':'Python'}}}}}}}

# print(data['key1']['key2']['key3']['key4']['key5']['key6']['key7'])
# jsonpath的结果为列表，获取数据需要索引
print(jsonpath(data,'$.key1.key2.key3.key4.key5.key6.key7')[0])
print(jsonpath(data,'$..key7')[0])