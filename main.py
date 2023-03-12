import random
import time

import numpy
import matplotlib.pyplot as plt
import Algrithm_sort


def count_avg_time(n):
    time_list = [[] for i in range(5)]
    method = Algrithm_sort.SortMethod()
    for i in range(20):
        x = [random.randint(1, 10000) for i in range(n)]
        t = time.time()
        method.select_sort(x)
        time_list[0].append(time.time() - t)
        t = time.time()
        method.bubble_sort(x)
        time_list[1].append(time.time() - t)
        t = time.time()
        method.merge_sort(x)
        time_list[2].append(time.time() - t)
        t = time.time()
        method.quick_sort(x)
        time_list[3].append(time.time() - t)
        t = time.time()
        method.insert_sort(x)
        time_list[4].append(time.time() - t)
        t = time.time()
    return [sum(time_list[i])/20 for i in range(5)]

# fig, ax = plt.subplots()
# ax.plot([1, 2, 3, 4], [1, 3, 2, 1])
# ax.plot([2, 3, 4, 5], [1, 3, 2, 1])
# plt.show()

# fig, ax = plt.subplots()


li = count_avg_time(10000)
print(li)

# cl = Algrithm_sort.SortMethod()

# x1 = time.time()
# k = cl.merge_sort(x)
# print(time.time()-x1)
#
# x1 = time.time()
# f = cl.quick_sort(x)
# print(time.time()-x1)
#
# x1 = time.time()
# cl.bubble_sort(x)
# print(time.time()-x1)
#
# x1 = time.time()
# cl.insert_sort(x)
# print(time.time()-x1)
#
# x1 = time.time()
# cl.select_sort(x)
# print(time.time()-x1)

# x = [[i] for i in x]
# x1 = time.time()
# while len(x) != 1:
#     n = len(x)
#     for i in range(len(x)//2):
#         if 2*i <= n:
#             x.append(cl.merge(x.pop(0), x.pop(0)))
# print(time.time()-x1)


