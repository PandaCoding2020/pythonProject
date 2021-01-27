"""
@Time : 2021/1/27 18:04 
@Author : Steven Chen
@File : 6捕获所有异常.py 
@Software: PyCharm
"""
# 目标：尝试打印num，验证Expection
# 方法：
try:
    # print(num)
    print(1/0)
except Exception as result:
    print(result)