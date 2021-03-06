# 两个数字比较大小
# 1.带判断的lambda
fn1 = lambda a, b: a if a > b else b
print(fn1(1000, 500))
# 2.列表数据按字典key的值排序
students = [
    {'name': 'Tom', 'age': 20},
    {'name': 'Rose', 'age': 19},
    {'name': 'Jack', 'age': 22}
]

# 按name值升序排列
students.sort(key=lambda x: x['name'])
print(students)
# 按name值降序排列
students.sort(key=lambda x: x['name'], reverse=True)
print(students)
