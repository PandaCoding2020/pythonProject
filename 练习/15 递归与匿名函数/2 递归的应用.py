# 3以内的数字做累加和运算 3+2+1 = 6
# 6 = 3+2以内的数字做累加和
# 3 = 2+1以内的数字做累加和
# 1以内的数字做累加和为1

def sum_numbers(num):
    # 出口
    if num == 1:
        return 1
    # 当前数字+当前数字-1的累加和
    return num + sum_numbers(num - 1)


result = sum_numbers(500)
print(result)
