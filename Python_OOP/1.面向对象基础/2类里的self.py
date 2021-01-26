# 类：洗衣机 功能：洗衣服
class Washer():
    def wash(self):
        print('洗衣服')
        print(self)


haier = Washer()
print(haier)

haier.wash()

# 打印对象和self的内存是一样的，所以self指的是调用该函数的对象
