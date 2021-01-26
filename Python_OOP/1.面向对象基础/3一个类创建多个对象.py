# 1.一个类创多个对象
class Washer():
    def wash(self):
        print('洗衣服')


haier1 = Washer()
haier1.height = 800
haier1.width =600

haier2 = Washer()
haier2.wash()


