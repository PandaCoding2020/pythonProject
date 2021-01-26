# 目标：定义__init__，体验魔法方法
"""
1.定义类
init魔法方法：width 和 height
添加方法访问实例
2.创建对象
3.验证成果，调用实例方法
"""
class Washer():
    # 定义__init__，添加实例性
    def __init__(self):
        self.width = 600
        self.height = 800

    def print_info(self):
        # 里面调用实例
        print(f'洗衣机的宽度{self.width},高度是{self.height}')

haier1 = Washer()
haier1.print_info()