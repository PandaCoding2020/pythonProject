s1 = {10,20,30,40,50}
# add()
# s1.add(100)
# print(s1)
# s1.add(100)
# print(s1) #追加的是集合中已有的数据，则什么也不做
# s1.add([200,300,400])
# print(s1)

# 2.update()
s1.update([10,20,100,200,300])
print(s1)
#如果增加单一数据会出错
s1.update(10)