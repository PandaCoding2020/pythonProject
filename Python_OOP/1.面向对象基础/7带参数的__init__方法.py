"""
@Time : 2021/1/26 14:53 
@Author : Steven Chen
@File : 7带参数的__init__方法.py 
@Software: PyCharm
"""
# 1.定义类：带参数的init,设高宽
class Washer():
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def print_info(self):
        print(f'洗衣机的宽度{self.width}')
        print(f'洗衣机的高度{self.height}')

# 2.创建对象并调用实例方法
haier1 = Washer(10,20)
haier1.print_info()

haier2 = Washer(30,40)
haier2.print_info()