"""
@Time : 2021/1/27 22:25 
@Author : Steven Chen
@File : 2别名.py 
@Software: PyCharm
"""
# 目标：运行后暂停2秒打印hello
# 方法：1、导入time模块或导入time模块的sleep功能 2.调用功能 3、打印hello
# 1.模块定义别名
# import time as tt
# tt.sleep(2)
# print('Hello Python!')

# 2.功能别名
from time  import sleep as sl
sl(2)
print('Hello Python!')

