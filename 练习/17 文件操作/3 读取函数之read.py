f = open('test.txt','r')
# print(f.read())
# 如果有换行\t则会有字符的占位,没有换行则没有
print(f.read(10))
f.close()