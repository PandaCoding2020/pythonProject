"""
@Time : 2021/1/27 21:55 
@Author : Steven Chen
@File : 1模块的使用方法.py 
@Software: PyCharm
"""
# 目标：math模块下sqrt()开平方计算
# 方法：1、导入模块 2、测试是否导入成功：调用该模型内的sqrt功能
# 方法一：
# import math
# print(math.sqrt(9))

# 方法二：不需要写模块名，直接使用功能
# from math import sqrt
# print(sqrt(9))

# 方法三：
from math import *
print(sqrt(9))