"""
@Time : 2021/1/28 15:38 
@Author : Steven Chen
@File : 拓展__dict__.py 
@Software: PyCharm
"""
# 目标：
# 方法：1.定义类 2.创建对象 3.调用__dict__
class A(object):
    a = 0
    def __init__(self):
        self.b = 1

aa = A()
print(A.__dict__)
print(aa.__dict__)