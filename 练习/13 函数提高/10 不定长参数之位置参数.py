# 接收一个位置参数，返回一个元组
def user_info(*args):
    print(args)


user_info('Tom')
user_info('Rose', 20, '女')
user_info()
