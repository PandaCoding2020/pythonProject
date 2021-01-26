# 1. 不可变 int类型
# a = 1
# b = a
#
# print(b)
# # a和b的id值都是相同的
# print(id(a))
# print(id(b))
#
# a = 2
# print(b)
# # 因为修改了a的数值，所以需要另外开辟一块存地址
# print(id(a))
# print(id(b))

# 2. 可变 列表类型
aa = [10,20]
bb = aa

print(id(aa))
print(id(bb))

