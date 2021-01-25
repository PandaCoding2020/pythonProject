"""
测试目标
1. r+和w+,a+的区别：
2。文件指针对数据读取的影响
"""
# r+:没有文件的时候报错,文件指针在开头，所以能读出所有数据
# f = open('test.txt','r+')
#
# con = f.read()
# print(con)
#
# f.close()

# w+ 没有该文件会新建文件，文件指针也在开头，但是会用新内容覆盖原内容
# f = open('test.txt','w+')
#
# con = f.read()
# print(con)
#
# f.close()

# a+:如果没有文件会新建文件，文件指针在内容的末尾
f = open('test.txt','a+')

con = f.read()
print(con)

f.close()