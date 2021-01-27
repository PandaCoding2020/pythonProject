"""
@Time : 2021/1/27 15:58 
@Author : Steven Chen
@File : 5静态方法.py 
@Software: PyCharm
"""
# 目标：
# 方法：
# 1.定义类，定义静态方法
class Dog(object):
    @staticmethod
    def info_print():
        print('这是一个狗类，用于创建狗实例')

# 2.创建对象
wangcei = Dog()
# 3.调用静态方法：类和对象
Dog.info_print()
wangcei.info_print()