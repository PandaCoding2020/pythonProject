"""
@Time : 2021/1/28 9:38 
@Author : Steven Chen
@File : 4模块的定位顺序.py 
@Software: PyCharm
"""
# 目标：
# 方法：
# 1.自己的文件名不能和已有的模块名重复，如果重复则会导致模块无法使用
import random
num =random.randint(1,5)
print(num)

# 2.当使用from xx import 功能 ，导入模块的功能的时候，如果功能名字重复，导入的时候后定义或后导入的这个同名功能
from time import sleep
# 定义函数sleep
def sleep():
    print('自己定义的sleep')

sleep(2)