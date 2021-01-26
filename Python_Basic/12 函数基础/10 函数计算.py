# 1、求任意三个数之和
def sun_num(a, b, c):
    return a + b + c


result1 = sun_num(1, 2, 3)
print(f'这三个数的和是{result1}')


# 2、任意三个数的平均值
def average_num(a, b, c):
    sunResult = sun_num(a, b, c)
    return sunResult / 3


result2 = average_num(1, 2, 3)
print(f'这三个数的平均值是{result2}')
