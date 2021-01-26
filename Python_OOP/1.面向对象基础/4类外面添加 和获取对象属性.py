# 1.一个类创多个对象
class Washer():
    def wash(self):
        print('洗衣服')


haier1 = Washer()
haier1.height = 800
haier1.width =600

# 获取对象的属性
print(f'洗衣机的宽度{haier1.width}')
print(f'洗衣机的高度{haier1.height}')