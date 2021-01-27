"""
@Time : 2021/1/27 18:11 
@Author : Steven Chen
@File : 7异常的else.py 
@Software: PyCharm
"""
# 目标：
# 方法：
try:
    # print(num)
    print(1)
except Exception as result:
    print(result)
else:
    print('我的else,当没有异常的时候才会执行到这里')