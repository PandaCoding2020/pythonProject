# a = 10
# b = 20

# 1.方法1
"""
1.1 定义中间变量，为了临时存储a 和 b的数据
1.2 把a的数据存储到c
1.3 把b的值赋给a a = 20
1.4 把c的值赋给b b = 10
"""
# c = 0
# c = a
# a = b
# b = c
#
# print(a)
# print(b)

# 2. 方法2
a, b = 1, 2
print(a)
print(b)
a, b = b, a
print(a)
print(b)