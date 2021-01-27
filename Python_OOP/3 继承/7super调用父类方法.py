"""
@Time : 2021/1/27 11:17 
@Author : Steven Chen
@File : 7super调用父类方法.py 
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
class School(Master):
    def __init__(self):
        self.kongfu = '[黑马煎饼果子配方]'

    def make_cake(self):
        # 2.1 带参数的super()
        print(f'运用{self.kongfu}制作煎饼果子')
        # super(School, self).__init__()
        # super(School, self).make_cake()


        # 2.2 无参数super()
        super().__init__()
        super().make_cake()


# 3.徒弟类继承school和Master两个父类的 优先继承第一个父类的属性和方法
class Prentice(School):
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
# 需求：一次性调用父类的同名属性和方法
    def make_old_cake(self):
        # 方法1：如果定义的类名修改，这里也要修改，代码量大，冗余
        # School.__init__(self)
        # School.make_cake(self)
        # Master.__init__(self)
        # Master.make_cake(self)

        # 方法2：super(当前类名，self)
        # super(Prentice,self).__init__()
        # super(Prentice, self).make_cake()

        super().__init__()
        super().make_cake()


daqiu = Prentice()
daqiu.make_old_cake()
