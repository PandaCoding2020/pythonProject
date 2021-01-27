"""
@Time : 2021/1/27 17:59 
@Author : Steven Chen
@File : 5捕获异常描述信息.py 
@Software: PyCharm
"""
# 目标：
# 方法：
try:
    print(1 / 0)
except (NameError, ZeroDivisionError) as result:
    print(result)
