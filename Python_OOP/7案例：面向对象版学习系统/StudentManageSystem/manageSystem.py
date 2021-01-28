"""
@Time : 2021/1/28 10:43 
@Author : Steven Chen
@File : manageSystem.py 
@Software: PyCharm
"""


# 目标：添加学员函数内部需要创建学员对象，故先导入student模块
# 方法：
from student import *

class StudentManager(object):
    def __init__(self):
        # 存储数据所用的列表
        self.student_list = []

    def run(self):
        # 1.加载学员信息
        self.load_student()

        while True:
            # 2.显示菜单功能
            self.show_menu()
            # 3.输入功能序号
            menu_num = int(input('请输⼊入您需要的功能序号：'))
            # 4.根据用户输入的序号执行不同的功能
            if menu_num == 1:
                # 添加学员
                self.add_student()
            elif menu_num == 2:
                # 删除学员
                self.del_student()
            elif menu_num == 3:
                # 修改学员
                self.modify_student()
            elif menu_num == 4:
                # 查询学员
                self.search_student()
            elif menu_num == 5:
                # 显示所有学员信息
                self.show_student()
            elif menu_num == 6:
                # 保存学员信息
                self.save_student()
            else:
                # 退出系统
                break


    # 二、系统功能函数
    # 2.1显示功能函数 打印序号的功能对应关系-静态
    @staticmethod
    def show_menu():
        print('请选择如下功能：')
        print('1:添加学员')
        print('2:删除学员')
        print('3:修改学员')
        print('4:查询学员')
        print('5:显示所有学员信息')
        print('6:保存学员信息')
        print('7:退出系统')


    # 2.2添加学员
    def add_student(self):
        # 1.用户输入姓名、性别、手机号
        name = input('请输入您的姓名：')
        gender = input('请输入您的性别：')
        tel = input('请输入您的手机号：')
        # 2.创建学员对象
        student = Student(name,gender,tel)
        # 3.将该对象添加到学员列表
        self.student_list.append(student)

        print(self.student_list)
        print(student)


    # 2.3删除学员
    def del_student(self):
        # 1.用户输入目标学员姓名
        del_name = input('请输入要删除的学员的姓名：')
        # 2.如果用户输入的目标学员存在则删除，否则提示学员不存在
        for i in self.student_list:
            if del_name == i.name:
                #删除该列表对象
                self.student_list.remove(i)
                break
            else:
                print('查无此人！')
        # 3.打印学员列表，验证删除功能
        print(self.student_list)

    # 2.4修改学员信息
    def modify_student(self):
        print('修改学员')
        # 1.用户输入目标学员姓名
        modify_name = input('请输入要修改的学员的姓名：')
        # 2.如果用户输入的目标学员存在则修改姓名、性别、手机号等数据，否则提示学员不存在
        for i in self.student_list:
            if modify_name == i.name:
                i.name = input('姓名：')
                i.gender = input('性别：')
                i.tel = input('电话号码：')
                print(f'修改的学员信息成功，姓名{i.name},性别{i.gender},电话号码{i.tel}')
                break
            else:
                print('查无此人！')
        # 3.打印修改结果


    # 2.5查询学员信息
    def search_student(self):
        print('查询学员')
        # 1.用户输入目标学员姓名
        search_name = input('请输入要查询的学员的姓名：')
        # 2.如果该学员不存在，则打印学员信息，否则提示学员不存在
        for i in self.student_list:
            if search_name == i.name:
                print(f'修改的学员信息成功，姓名{i.name},性别{i.gender},电话号码{i.tel}')
                break
        else:
            print('查无此人！')


        # 3.打印显示


    # 2.6显示所有学员信息
    def show_student(self):
        print('姓名\t性别\t电话')
        for i in self.student_list:
            print(f'{i.name}\t{i.gender}\t{i.tel}')


    # 2.7保存学员信息
    def save_student(self):
        print('保存学员信息')
        # 1.打开文件
        f = open('student.data','w')
        # 2.文件写入学员数据
        # 2.1 学员对象转换成字典
        new_list = [i.__dict__ for i in self.student_list]
        # 2.2 文件写入字符串
        f.write(str(new_list))
        # 3.关闭文件
        f.close()


    # 2.8加载学员信息
    def load_student(self):
        # 尝试以r模式打开数据文件，文件不存在则提示用户，如果有异常则以w模型打开
        #1.打开文件
        try:
            f = open('student.data','r')
        except:
            f = open('student.data','w')
        else:
        #2.读取数据 还原列表对象 [{}]转换为[学员对象]
            data = f.read()
            new_list = eval(data)
            self.student_list = [Student(i['name'],i['gender'],i['tel']) for i in new_list]
        #3.关闭文件
        finally:
            f.close()
