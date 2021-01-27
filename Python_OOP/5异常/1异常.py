"""
@Time : 2021/1/27 17:31 
@Author : Steven Chen
@File : 1异常.py 
@Software: PyCharm
"""
# 目标：
# 方法：
"""
try:
    可能发生错误的代码
exception:
    发生错误的时候执行的代码
"""
try:
    f = open('text.txt','r')
except:
    f = open('text.txt','w')