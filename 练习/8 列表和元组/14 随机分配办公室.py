# 需求：将8位老师分配到3个办公室
"""
步骤：
1、准备数据
    1.1 8位老师的名字 列表
    1.2 3个办公室 列表
2、分配老师到办公室
    随机分配
    就是把老师的名字写入办公室列表——办公室列表追加老师的名字
3、验证是否成功
    打印每个办公室的人数和名字
"""
import random
teachers = ['A','B','C','D','E','F','G','H']
offiices = [[],[],[]]
# 遍历老师列表的数据
for name in teachers:
    # 列表追加数据
    num = random.randint(0,2)
    offiices[num].append(name)

print(offiices)
# 验证是否分配成功
# 加一个办公室编号
i = 1
for office in offiices:
    print(f'办公室{i}的人数是{len(office)}')
    # 打印老师的名字
    for name in office:
        print(name)
    i += 1