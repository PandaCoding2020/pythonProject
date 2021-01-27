"""
@Time : 2021/1/27 17:55 
@Author : Steven Chen
@File : 4捕获多个指定的异常.py 
@Software: PyCharm
"""
# 目标：
# 方法：
try:
    print(1/0)
except (NameError,ZeroDivisionError):
    print('有错误！')