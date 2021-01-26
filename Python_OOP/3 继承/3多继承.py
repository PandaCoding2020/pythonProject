"""
@Time : 2021/1/26 17:58 
@Author : Steven Chen
@File : 2单继承.py 
@Software: PyCharm
"""
# 目标：
# 方法：
# 1.师傅类
class Master(object):
    def __init__(self):
        self.kongfu ="[古法煎饼果子配方]"

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

# 2.徒弟类
class Prentice(Master):
    pass

# 3.用徒弟类创建对象，调用 实例属性和方法
daqiu = Prentice()
print(daqiu.kongfu)
daqiu.make_cake()