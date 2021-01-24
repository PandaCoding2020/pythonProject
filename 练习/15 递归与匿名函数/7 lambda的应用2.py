# 列表数据按字典key的值排序
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
# 按age的值进行排序
students.sort(key=lambda x: x['age'])
# students.sort(key=lambda x: x['age'], reverse=True)
print(students)
