# # 1.abs()
# print(abs(-10))
# # 2.round()
# print(round(1.2))
# print(round(1.9))

# 需求：任意两个数字，按照指定的要求整理数字后再进行求和计算
# 方法1
def add_num(a,b):
    return abs(a) + abs(b)

result1 = add_num(1,-2)
print(result1)

# 方法2
def sum_num(a,b,f):
    return f(a) + f(b)

result2 = sum_num(1,-2, abs)
print(result2)
