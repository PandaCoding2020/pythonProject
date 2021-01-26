"""
@Time : 2021/1/26 15:05 
@Author : Steven Chen
@File : 8魔法方法__str__.py 
@Software: PyCharm
"""
class Washer():
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def __str__(self):
        return '这是海尔洗衣机的说明书'

haier1 = Washer(10,20)
print(haier1)