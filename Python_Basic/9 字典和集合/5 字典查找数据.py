dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}

# 1. [key]
# print(dict1['name'])
# print(dict1['names'])
# 2. 函数 get(),keys(),,item()
# 2.1 get()
# print(dict1.get('name'))
# print(dict1.get('names'))
# print(dict1.get('names','Lily'))
# 2.2 keys() 返回可迭代的对象
# print(dict1.keys())
# 2.3 values()
# print(dict1.values())
# 2.4 items() 返回可迭代对象
print(dict1.items())
