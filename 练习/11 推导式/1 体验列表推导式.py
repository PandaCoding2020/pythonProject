# 创建列表1-10
# 1、循环实现 2.列表推导式

# 1. while实现
# list1 = []
# i = 0
# while i < 10:
#     list1.append(i)
#     i += 1
#
# print(list1)

# 2. for实现
# list1 = []
# for i in range(10):
#     list1.append(i)
#
# print(list1)

# 3.推导式实现
list1 = [i+1 for i in range(10)]

print(list1)

