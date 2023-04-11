
import math
import time
import random
import matplotlib.pyplot as plt
import numpy as np

class Solution:
    def find_nearest_direction(self, p: list):
        start_time = time.time()
        n = len(p)
        min_dir = float('inf')
        min_p = []
        for i in range(n):
            for j in range(n):
                if j == i:
                    break
                dir = math.sqrt(math.pow(p[i][0]-p[j][0], 2) + math.pow(p[i][1]-p[j][1], 2))
                if dir < min_dir:
                    min_dir = dir
                    min_p = [[p[i]], [p[j]]]
        return min_dir, min_p, time.time() - start_time

def plot_analysis(historty_time: list):
    plt.plot(list(range(len(history_time))), history_time)
    plt.xlabel('times')
    plt.ylabel('signle cost time/s')
    plt.show()

if __name__ == '__main__':
    # single instance
    ins = Solution()
    # p = [[0, 0], [1, 1], [3, 4], [0, 3], [3.2, 4.2], [0, -1], [-2, -2], [-1, -2], [0, 0.4], [-1, 2], [0, 2], [0.5, 2]]
    # min_dir, min_p, cost_time = ins.find_nearest_direction(p)
    # print('距离最小两个点为:', min_p[0][0], min_p[1][0])
    # print('距离为:', min_dir)

    # 100 times simulation
    all_cost_time = 0
    history_time = []
    for i in range(1):
        p = [[random.randint(1, 1000000), random.randint(1, 10000)] for _ in range(10000)]
        history_time.append(ins.find_nearest_direction(p)[2])
        all_cost_time += history_time[i]
    print('100次模拟的总时间花费:', all_cost_time,'s')

    # stability analysis
    # plot_analysis(history_time)
