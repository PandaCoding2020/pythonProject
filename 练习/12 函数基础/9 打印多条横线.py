# 打印多条横线
def print_line():
    print('_' * 20)


def print_lines(num):
    i = 0
    while i < num:
        print_line()
        i += 1


print_lines(10)