import random
import time


# 生成随机点，个数为n,存入dot_list列表中，x、y为生成随机数的范围，
# 横坐标为0-x，纵坐标为0-y
def createBoard(n, x, y):
    for i in range(n):
        x0 = random.random() * x
        y0 = random.random() * y
        dot_list.append((x0, y0))


# 蛮力法求解，输入为点集dlist，输出为最短距离的两个点的距离和各自的坐标
def direct_count(dlist):
    n = len(dlist)
    startdot_index = 0
    enddot_index = 1
    min_dis = (dlist[0][0] - dlist[1][0]) ** 2 + (dlist[0][1] - dlist[1][1]) ** 2
    for start in range(n):
        for end in range(start + 1, n):
            temp = (dlist[start][0] - dlist[end][0]) ** 2 + (dlist[start][1] - dlist[end][1]) ** 2
            if min_dis > temp:
                min_dis = temp
                startdot_index = start
                enddot_index = end
    return startdot_index, enddot_index, min_dis


if __name__ == '__main__':
    dot_list = []
    createBoard(10000, 10, 10)
    dot_list.sort()
    tic = time.time()
    direct_count(dot_list)
    print(time.time() - tic)
