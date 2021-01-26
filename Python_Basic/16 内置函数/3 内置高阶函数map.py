# map函数 map(fun,lst)
# 需求：计算list1序列中各个数字的2次方
# 1.准备列表
list1 = [1, 2, 3, 4, 5]

# 2.定义函数
def func(x):
    return x ** 2

# 3.调用函数
result = map(func, list1)
# 4.验收成果
print(result)
print(list(result))
