# reduce函数 reduce(fun,lst)
# 需求：筛选序列中的偶数
# 1.准备列表

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# 2.定义函数
def func(x):
    return x % 2 == 0


# 3.调用函数
result = filter(func, list1)
# 4.验收成果
print(list(result))
