# 1.一个类创多个对象
class Washer():
    def wash(self):
        print('洗衣服')

    def print_info(self):
        print(f'洗衣机的宽度{self.width}')
        print(f'洗衣机的高度{self.height}')


haier1 = Washer()

# 2.添加属性值
haier1.height = 800
haier1.width =600

# 3.获取对象的属性
haier1.print_info()