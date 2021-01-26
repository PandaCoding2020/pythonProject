name_list  = ['Tom','Lily','Rose']
"""
1 用户输入账号
2 判断if...else
"""
name = input('请输入您的用户名：')
if name in name_list:
    print(f'您输入的用户名{name}，此用户名已经存在。')
else:
    print(f'您输入的用户名{name}，可以注册。')