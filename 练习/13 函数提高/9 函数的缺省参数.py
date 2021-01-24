#缺省参数
def user_info(name, age, gender='男'):
    print(f'您的姓名是{name},年龄是{age},性别是{gender}.')


user_info('Tom', age=20)
user_info('Rose', age=20, gender='女')
