"""
@Time : 2021/1/28 10:43 
@Author : Steven Chen
@File : student.py 
@Software: PyCharm
"""
# 目标：1.学员的信息：姓名，性别，手机号 2.添加__str__魔法方法，方便查看学员对象信息
# 方法：
class Student(object):
    def __init__(self,name,gender,tel):
        self.name = name
        self.gender = gender
        self.tel = tel

    def __str__(self):
        return f'学生姓名是{self.name}, 性别是{self.gender}, 电话号码是{self.tel}。'

# a = Student('aa','女',123)
# print(a)