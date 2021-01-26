# 接收一个关键字参数，返回一个字典
def user_info(**kwargs):
    print(kwargs)


user_info(name ='Tom')
user_info(name = 'Rose', age = 20, gender ='女')
user_info()
