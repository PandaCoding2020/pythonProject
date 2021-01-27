"""
@Time : 2021/1/27 18:14 
@Author : Steven Chen
@File : 8异常的finally.py 
@Software: PyCharm
"""
# 目标：
# 方法：
try:
    f = open('text.txt','r')
except Exception as result:
    print('text.txt','w')
else:
    print('没有异常，真开心')
finally:
    f.close()