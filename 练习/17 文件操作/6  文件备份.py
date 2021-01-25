# 1.用户输入目标文件
old_name = input('请输入您要备份的文件名：')
# print(old_name)
# print(type(old_name))
# 2. 规划备份文件的名字
# 2.1 提取文件后缀点的下标-找到文件名中的. rfind
index = old_name.rfind('.')

# 4.有效文件才备份
if index > 0:
    postfix = old_name[index:]

# print(index)
# 2.2 组织新文件名 旧文件名+[备份]+后缀
# 原名字的一部分就是字符串的一部分
# print(old_name[:index])
# print(old_name[index:])
# new_name = old_name[:index]+'[备份]'+old_name[index:]
new_name = old_name[:index] + '[备份]' + postfix
# print(new_name)
# 3.备份文件写入数据
# 3.1 原文件要打开和备份也要打开
old_f = open(old_name, 'rb')
new_f = open(new_name, 'wb')
# 3.2 原文件读取，备份文件支持写入
# 如果不确定文件大小，循环读取写入，当读取出来的数据没有，终止循环即可
while True:
    con = old_f.read(1024)
    if len(con) == 0:
        # 读取完成了
        break
    new_f.write(con)
# 3.3 关闭两个文件 先读取先关闭
old_f.close()
new_f.close()
