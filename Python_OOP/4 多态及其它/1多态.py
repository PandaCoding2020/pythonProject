"""
@Time : 2021/1/27 14:56 
@Author : Steven Chen
@File : 1多态.py 
@Software: PyCharm
"""
# 目标：警务人员和功名成就一起工作，功名成就分2种，追击敌人和追查毒品，携带不同的功名成就，执行不同的任务
# 方法：
# 1.定义父类，提供公共方法
class Dog(object):
    def work(self):
        pass
# 2.定义子类，子类重写父类方法 定义两个不同的警犬
class ArmyDog(Dog):
    def work(self):
        print('追击敌人')

class DrugDog(Dog):
    def work(self):
        print('追击毒品')

# 定义人类
class Person(object):
    def work_with_dog(self, dog):
        dog.work()
# 3.创建对象，调用 不同的工轻盈，传入不同 的对象，观察执行的结果
ad = ArmyDog()
dd = DrugDog()
daqiu = Person()
daqiu.work_with_dog(ad)
daqiu.work_with_dog(dd)