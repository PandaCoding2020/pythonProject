# 需求：函数定义3个参数：name, age, gender
def user_info(name,age,gender):
    print(f'您的姓名是{name},年龄是{age},性别是{gender}.')

user_info('Tom',20,'男')
user_info('Tom','男') # 个数不一致会报错
user_info(20,'Tom','男') # 顺序，不会报错

