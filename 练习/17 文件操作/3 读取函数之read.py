# f = open('test.txt','r')
# # 1.read()方法
# # 不写参数表示读出所有的
# # print(f.read())
# # 如果有换行\t则会有字符的占位,没有换行则没有
# print(f.read(10))
# f.close()

# 2. readlines()方法
# f = open('test.txt', 'r')
# con = f.readlines()
# print(con)
# f.close()

# 3.readline()方法
f = open('test.txt', 'r')
con = f.readline()
print(con)
con = f.readline()
print(con)
f.close()
