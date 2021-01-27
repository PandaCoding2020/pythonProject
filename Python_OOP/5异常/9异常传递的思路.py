"""
@Time : 2021/1/27 20:56 
@Author : Steven Chen
@File : 9异常传递的思路.py 
@Software: PyCharm
"""
# 目标：1、尝试只读打开text.txt文件存在读取内容，不存在提示用户 2、读取内容，循环读取，当无内容的时候退出循环，如果用户意外终止，
# 提示用户已被意外终止
# 方法：
import time

try:
    f = open('text.txt')
    try:
        while True:
            content = f.readline()
            # 如果读取完成退出循环
            if len(content) == 0:
                break
            time.sleep(2)
            print(content)
    except:
        # 在命令提示符中如果按下ctrl+c结束终止
        print('意外终止了读取数据')

    finally:
        f.close()
        print('关闭文件')
except:
    print('该文件不存在')
