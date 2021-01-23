# 打印[(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
list1 = []
for i in range(1,3):
    for j in range(3):
        list1.append((i,j))

print(list1)

# 用列表推导式实现
list2 = [(i,j) for i in range(1,3) for j in range(3)]
print(list2)