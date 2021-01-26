"""
这部分跟其它的语言不同
"""
str1 = "itheima"
for i in str1:
    if i == 'e':
        print('遇到e不打印')
        break
    print(i)
else:
    print('循环正常结束后执行的代码')
