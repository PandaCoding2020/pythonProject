"""
@Time : 2021/1/27 15:25 
@Author : Steven Chen
@File : 2类属性.py 
@Software: PyCharm
"""
# 目标：
# 方法：
# 1.定义类
class Dog(object):
    tooth = 10
# 2.创建对象
wangcai = Dog()
xiaohei = Dog()
# 3.访问类属性
print(Dog.tooth)
print(wangcai.tooth)
print(xiaohei.tooth)