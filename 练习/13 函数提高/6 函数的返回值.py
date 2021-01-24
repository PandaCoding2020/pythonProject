# 要求：一个函数有两个返回值
# def return_num():
#     return 1
#     return 2 #不执行
#
# result = return_num()
# print(result)

# 一个函数多个返回值的写法
def return_num():
    # return 1,2 #返回一个元组

    # return后面可以直接返回元组列表字典
    # return (10,20)
    # return [1,2]
    return {1,2}

result = return_num()
print(result)