import numpy as np


def solution(height: int, egg: int) -> int:
    matrix = np.zeros((height+1, egg+1), dtype='float')
    # 初始化边值条件
    for i in range(height+1):
        matrix[i][1] = i
    for i in range(1, egg+1):
        matrix[1][i] = 1
        matrix[0][i] = 0
    # 将除去边界外的所有其他情况设为无穷大
    for i in range(2, height+1):
        for j in range(2, egg+1):
            matrix[i][j] = np.inf

    for i in range(2, egg+1):
        for j in range(2, height+1):
            # 逐层搜索，若该层鸡蛋碎了返回上一层和鸡蛋数减少一个的搜索次数，若没碎返回x层往上i个鸡蛋的搜索次数
            for x in range(1, j+1):
                broke = matrix[x - 1][i - 1]
                not_broke = matrix[j - x][i]
                res = 1 + max(broke, not_broke)
                matrix[j][i] = min(matrix[j][i], res)
    return matrix[height, egg]


def solution_devide(height: int, egg: int) -> int:
    matrix = np.zeros((height+1, egg+1), dtype='float')
    # 初始化边值条件
    for i in range(height+1):
        matrix[i][1] = i
    for i in range(1, egg+1):
        matrix[1][i] = 1
        matrix[0][i] = 0
    # 将除去边界外的所有其他情况设为无穷大
    for i in range(2, height+1):
        for j in range(2, egg+1):
            matrix[i][j] = np.inf

    for i in range(2, egg+1):
        for j in range(2, height+1):
            # 二分搜索
            start = 0
            end = j
            while start is not end:
                x = (start + end) // 2
                broke = matrix[x - 1][i - 1]
                not_broke = matrix[j - x][i]
                res = 1 + max(broke, not_broke)
                if res == broke + 1:
                    # 碎了就往下二分搜索
                    end = x
                else:
                    # 否则往上
                    start = x + 1
                matrix[j][i] = min(matrix[j][i], res)
    return matrix[height, egg]
