def info_print():
    print('请选择功能-----------')
    print('1.添加学员')
    print('2.删除学员')
    print('3.修改学员')
    print('4.查询学员')
    print('5.显示学员')
    print('6.退出系统')
    print('-' * 20)


# 准备一个空的列表，等待存储所有学员的信息
info = []


# 添加学员的函数
def add_info():
    """添加学员"""
    # 1. 用户输入：学号、姓名、手机号
    new_id = input('请输入学号：')
    new_name = input('请输入姓名：')
    new_tel = input('请输入手机号：')
    # 2、判断这具用户名是否存在
    global info
    # 2.1 不允许姓名重复
    for i in info:
        if new_name == i['name']:
            print('用户名已经存在！')
            # return退出函数，那么后面的添加代码就不会执行
            return
    # 2.2 如果姓名不存在，添加数据：准备空字典，字典新增数据，列表追加字典
    info_dict = {}
    # 字典新增数据
    info_dict['id'] = new_id
    info_dict['name'] = new_name
    info_dict['Tel'] = new_tel
    # print(info_dict)

    # 列表追加字典
    info.append(info_dict)
    print(info)


def del_info():
    """删除学员"""
    # 1.用户输入要删除的学员的姓名
    del_name = input('请输入要删除的学员姓名：')

    global info
    # 2.判断学员是否存在：存在则删除，不存在则报错
    # 2.1 声明info是个全局变量
    # 2.2 遍历列表
    # 2.3 判断学员是否存在，break退出这个循环
    for i in info:
        if del_name == i['name']:
            info.remove(i)
            break
    else:
        print('该学员不存在！')

    print(info)


# 修改函数
def modify_info():
    """修改学员信息"""
    # 1.用户输入要修改的用户名
    mofify_name = input('请输入要修改的学员的姓名：')
    # 2. 判断学员是否存在：如果存在则修改，不存在则报错
    # 2.1 声明为全局变量
    global info
    # 2.2 遍历列表，判断是否存在
    for i in info:
        if mofify_name == i['name']:
            # 将tel这个key的值进行更新，并终止此循环
            i['Tel'] = input('请输入新的手机号')
            break
    else:
        # 学员不存在
        print('该学员不存在！')
    # 3. 打印
    print(info)


# 查询学员
def search_info():
    """查询学员信息"""
    # 1.输入学员的姓名
    search_name = input('请输入要查询的学员姓名：')
    global info
    # 2. 判断学员是否存在：存在则显示，否则报错
    for i in info:
        if search_name == i['name']:
            # 学员存在，打印信息并终止循环
            print('查询到的学员的信息如下--------------')
            print(f"学员的学号为{i[id]},姓名为{i['name']},手机号为{i['Tel']}")
            break
    else:
        print('查无此人')


# 查询所有学员信息
def print_all():
    """显示所有学员信息"""
    # 打印提示信息
    print('学号\t姓名\t手机号')
    # 打印所有学员信息
    for i in info:
        print(f'{i["id"]}\t{i["name"]}\t{i["Tel"]}')


# 系统功能要循环使用，直到用户输入6才退出
while True:
    # 1.显示功能界面
    info_print()

    # 2. 用户输入功能
    user_num = int(input('请输入功能序号：'))

    # 3. 按照用户输入的功能序号，执行不同的功能
    if user_num == 1:
        # print('添加')
        add_info()
    elif user_num == 2:
        # print('删除')
        del_info()
    elif user_num == 3:
        # print('修改')
        modify_info()
    elif user_num == 4:
        # print('查询')
        search_info()
    elif user_num == 5:
        # print('显示')
        print_all()
    elif user_num == 6:
        # print('退出')
        # 程序想结束，退出while即可
        exit_flag = input('确定要退出吗？Yes or No?')
        if exit_flag == 'Yes' or 'yes':
            break
    else:
        print('输入的功能序号有误！')
