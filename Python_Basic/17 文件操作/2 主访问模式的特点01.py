"""
测试目标
1.访问模式对文件的影响
2.访问模式对write()的影响
3.访问模式是否可以省略
"""
# r:如果文件不存在报错
# f = open('test1.txt','r')
# f = open('test.txt','r')
# # f.write('a') #不能写入
# f.close()

# w 只写如果执行写入，会覆盖原有内容。
# f = open('1.txt','w')
# f.write('bbb')
# f.close()

# a
# f = open('2.txt','a')
# f.write('Hello')
# f.write('Hello')
# f.close()

# 访问模式是否可以省略:可以省略，如果省略，则为r
f = open('1.txt')
f.close()