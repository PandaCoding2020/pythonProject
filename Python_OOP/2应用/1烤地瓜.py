"""
@Time : 2021/1/26 15:25 
@Author : Steven Chen
@File : 1烤地瓜.py 
@Software: PyCharm
"""


# 目标：
# 方法：1.定义类：初始化属性、被烤和添加调料的方法
class SweetPotato():
    def __init__(self):
        # 被时间
        self.cook_time = 0
        # 烤的状态
        self.cook_state = '生的'
        # 调料列表
        self.condiments = []

    def cook(self, time):
        """烤地瓜"""
        # 1.计算地瓜整体烤过的时间
        # 2.用整体烤过的时间判断地瓜的状态
        self.cook_time += time
        if 0 <= self.cook_time < 3:
            self.cook_state = '生的'
        elif 3 <= self.cook_time < 5:
            self.cook_state = '半生不熟'
        elif 5 <= self.cook_time < 8:
            self.cook_state = '熟了'
        elif self.cook_time >= 8:
            self.cook_state = '烤糊了'

# 2. 创建对象并调用对应的实例方法
    def __str__(self):
        return f'这个地瓜被烤过的时间是{self.cook_time},状态是{self.cook_state},调料有{self.condiments}'

    def add_condiments(self,condiment):
        """添加调料"""
        #用户意愿的调料追加到调料列表
        self.condiments.append(condiment)

# 3. 创建对角，测试实例属性和实例方法
digua1 = SweetPotato()
print(digua1)

digua1.cook(6)
digua1.add_condiments('辣椒面儿')
print(digua1)

digua1.cook(1)
digua1.add_condiments('酱油')
print(digua1)