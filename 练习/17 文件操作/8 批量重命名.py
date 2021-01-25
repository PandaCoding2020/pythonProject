# 需求：把当前文件夹所有文件重命名 Python

import os
# 1.找到所有文件
flag = 2
file_list = os.listdir()
print(file_list)

# 2.构造名字
for i in file_list:

    if flag == 1:
        new_name = 'Python-'+ i
    elif flag == 2:
        num = len('Python-')
        new_name = i[num:]

# 3.重命名
    os.rename(i,new_name)
