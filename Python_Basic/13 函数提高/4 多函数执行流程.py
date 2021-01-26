# 1.声明全局变量 2. 定义两个函数 3.函数修改两个变量
glo_num = 0

def test1():
    global glo_num
    glo_num = 100

def test2():
    print(glo_num)

print(glo_num)
test2() #test1()还没有执行，所以变量并没有改变
test1()
test2()
print(glo_num)