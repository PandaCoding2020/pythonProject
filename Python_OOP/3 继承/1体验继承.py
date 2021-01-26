"""
@Time : 2021/1/26 17:39 
@Author : Steven Chen
@File : 1体验继承.py 
@Software: PyCharm
"""
# 目标：体验继承
# 方法：
# 1.定义父类 2.定义子类并继承父类 3.创建对象，验证结论
# 父类A
class A(object):
    def __init__(self):
        self.num = 1

    def info_print(self):
        print(self.num)

# 子类B
class B(A):
    pass

# 测试
result = B()
result.info_print()