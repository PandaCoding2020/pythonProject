"""
@Time : 2021/1/27 10:01 
@Author : Steven Chen
@File : 5子类调用父类的同名方法和属性.py 
@Software: PyCharm
"""
# 目标：
# 方法：
# 1.师傅类
class Master(object):
    def __init__(self):
        self.kongfu = "[古法煎饼果子配方]"

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


# 2.创建学校类
class School(object):
    def __init__(self):
        self.kongfu = '[黑马煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


# 3.徒弟类继承school和Master两个父类的 优先继承第一个父类的属性和方法
class Prentice(School, Master):
    def __init__(self):
        self.kongfu = '[独创煎饼果子配方]'

    def make_cake(self):
        # 不调用则会使用上一次调用的属性值
        self.__init__()
        print(f'运用{self.kongfu}制作煎饼果子')

    def make_master_cake(self):
        # 父亲类名，函数（）
        # 再次调用初始化的原因，是要先初始化之后再能调用父亲的属性和方法
        Master.__init__(self)
        Master.make_cake(self)

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)


# 4.用徒弟类创建对象，调用 实例属性和方法
daqiu = Prentice()
# print(daqiu.kongfu)
daqiu.make_cake()
daqiu.make_master_cake()
daqiu.make_school_cake()
