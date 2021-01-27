"""
@Time : 2021/1/27 21:14 
@Author : Steven Chen
@File : 10自定义异常.py 
@Software: PyCharm
"""
# 目标：
# 方法：1.自定义异常 2.抛出异常 3.捕获异常
class ShortInputError(Exception):
    def __init__(self,length,min_len):
        self.length = length
        self.min_len = min_len

    def __str__(self):
        return f'您输入的长度是{self.length},不能少于{self.min_len}个字符'
# 如果长度小于3，抛出异常
def main():
    try:
        con = input('请输入密码：')
        if len(con)<3:
            raise ShortInputError(len(con),3)
    except Exception as result:
        print(result)
    else:
        print('密码输入已经完成！')

if __name__ == '__main__':
    main()