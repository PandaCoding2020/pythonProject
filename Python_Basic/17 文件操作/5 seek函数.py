"""
语法：文件对象.seek(偏移量，超始位置) 0开头，1当前 2结尾
目标：
1.r改变读取文件指针：改变读取数据开始位置或把文件指针放结尾(无法读取数据)
2.a改变读取文件指针，做到可以读到数据
"""
# 1.1.改变读取数据开始位置
# f.seek(2, 0)
# 1.2.把文件指针放到结尾（无法读取数据）
# f.seek(0, 2)
# f = open('test.txt', 'r+')
# f.seek(2, 0)
# con = f.read()
# print(con)
#
# f.close()

# 2.把文件指针放到结尾（无法读取数据）
f = open('test.txt', 'a+')
f.seek(0, 0)
con = f.read()
print(con)

f.close()
