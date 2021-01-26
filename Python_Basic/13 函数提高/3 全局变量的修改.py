# 定义全局变量
a = 100

print(a)

def testA():
    print(a)

def testB():
    # a = 200
    # print(a)
#     修改全局变量
    global a
    a = 200
    print(a)

testA()
testB()

print(a)