s1 = {10,20,30,40,50}
# 1。remove() 不存在则报错
# s1.remove(10)
# print(s1)
#
# s1.remove(10)
# print(s1)
# 2。discard() 不存在不报错
s1.discard(10)
print(s1)

s1.discard(10)
print(s1)
# 3。pop() 随机删除某个数据并返回
s1.pop()