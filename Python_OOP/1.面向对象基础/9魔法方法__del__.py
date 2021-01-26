"""
@Time : 2021/1/26 15:11 
@Author : Steven Chen
@File : 9魔法方法__del__.py 
@Software: PyCharm
"""
# 目标：
# 方法：
class Washer():
    def __init__(self):
        self.width = 300

    def __del__(self):
        print('对象已经删除')

haier = Washer()

