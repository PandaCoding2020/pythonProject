"""
@Time : 2021/1/28 10:12 
@Author : Steven Chen
@File : 6导入包.py 
@Software: PyCharm
"""
# 目标：导入mypackage包下的模块1，使用这个模块内的info_print1方法
# 方法一：
# 1.导入 import 包名 2.调用功能
# import mypackage.my_module1
# mypackage.my_module1.info_print1()

# 方法二：1、from 包名 import*
from mypackage import*
my_module1.info_print1()
my_module2.info_print2()