
# 1.简单列表推导式
# list1 = [i for i in range(0,10,2)]
# print(list1)

# 2.用for循环创建
list2 =[]
for i in range(10):
    if i%2==0:
        list2.append(i)

print(list2)

# 3.带if的的列表推导式
list3 = [i for i in range(10) if i%2 == 0]
print(list3)