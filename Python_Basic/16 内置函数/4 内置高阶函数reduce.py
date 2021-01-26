# reduce函数 reduce(fun,lst)
# 需求：计算list1序列中各个数字的累加和
# 1.准备列表
import functools

list1 = [1, 2, 3, 4, 5]


# 2.定义函数
def func(a, b):
    return a + b


# 3.调用函数
result = functools.reduce(func, list1)
# 4.验收成果
print(result)
