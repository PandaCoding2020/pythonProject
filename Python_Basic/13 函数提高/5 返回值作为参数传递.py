# 1.定交两个函数 2、函数1有返回值50作为函数2的输入值

def test1():
    return 50


def test2(num):
    print(num)


# 先得到函数1的返回值
result = test1()
print(result)

test2(result)
