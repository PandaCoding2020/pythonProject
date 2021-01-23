list1 = ['name','age','gender']
list2 = ['Tom',20,'man']

# 1 创建一个字典：keys 1-5 values:key的平方
dict1 = {i:i**2 for i in range(1,5)}
print(dict1)

# 2 将2个表合并为一个字典
dict2 = {list1[i]:list2[i] for i in range(len(list1))}
print(dict2)

