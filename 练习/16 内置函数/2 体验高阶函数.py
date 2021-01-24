# 需求：任意两个数字，先进行数字处理再求和计算
# 写法1
# def add_sum(a,b):
#     return abs(a) + abs(b)
#
# result1 = add_sum(-1.1, 1.9)
# print(result1)
# 写法2 高阶函数 f是用来接收第三个函数  参数
def sum_num(a,b,f):
    return f(a) + f(b)

result2 = sum_num(-1,5,abs)
print(result2)

result3 = sum_num(1.1,1.3,round)
print(result3)
