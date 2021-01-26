"""
@Time : 2021/1/26 15:57 
@Author : Steven Chen
@File : 2搬家具.py 
@Software: PyCharm
"""


# 目标：
# 方法：1、定义类

class Furniture():
    def __init__(self, name, area):
        # 家具名字
        self.name = name
        # 家具的占地面积
        self.area = area


class House():
    def __init__(self, address, area):
        # 地理位置
        self.address = address
        # 房屋面积
        self.area = area
        # 空闲面积
        self.free_area = area
        # 家具列表
        self.furniture = []

    def __str__(self):
        return f'房子的地理位置在{self.address},房屋面积是{self.area},剩余面积{self.free_area},家具有{self.furniture}'

    def add_furniture(self, item):
        """容纳家具"""
        if self.free_area >= item.area:
            self.furniture.append(item.name)
            # 家具搬入后
            self.free_area -= item.area
        else:
            print('家具太大，剩余面积不足，无法容纳！')


# 双人床和沙发
bed = Furniture('双人床', 6)
sofa = Furniture('沙发', 10)
ball = Furniture('篮球场',2000)

house1 = House('北京', 1000)
house1.add_furniture(bed)
house1.add_furniture(ball)
print(house1)
