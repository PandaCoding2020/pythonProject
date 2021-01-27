"""
@Time : 2021/1/27 15:49 
@Author : Steven Chen
@File : 4类方法.py 
@Software: PyCharm
"""
# 目标：
# 方法：
# 1.定义类：私有类属性，类方法获取这个私有类属性
class Dog(object):
    __tooth = 10

    @classmethod
    def get_tooth(cls):
        return cls.__tooth
# 2.创建对象，调用类方法
wangcai = Dog()
result = wangcai.get_tooth()
print(result)