import random
import time


class SortMethod:
    @staticmethod
    def select_sort(lis):
        tar_list = lis.copy()
        for j in range(len(tar_list)):
            index = 0
            max_element = tar_list[0]
            for i in range(len(tar_list) - j):
                if max_element < tar_list[i]:
                    max_element = tar_list[i]
                    index = i
            tar_list[len(tar_list) - j - 1], tar_list[index] = tar_list[index], tar_list[len(tar_list) - j - 1]
        return tar_list

    @staticmethod
    def bubble_sort(lis):
        tar_list = lis.copy()
        for i in range(len(tar_list) - 1):
            for j in range(len(tar_list) - 1 - i):
                if tar_list[j] > tar_list[j + 1]:
                    tar_list[j], tar_list[j + 1] = tar_list[j + 1], tar_list[j]
        return tar_list

    def merge_sort(self, lis):
        tar_list = lis.copy()
        if len(tar_list) == 1:
            return tar_list
        left_list = tar_list[0:len(tar_list) // 2]
        right_list = tar_list[len(tar_list) // 2:len(tar_list)]
        left_list = self.merge_sort(left_list)
        right_list = self.merge_sort(right_list)
        return self.merge(left_list, right_list)

    @staticmethod
    def merge(left_list, right_list):
        tar_list = []
        while left_list or right_list:
            if not left_list:
                tar_list.extend(right_list)
                right_list.clear()
                break
            elif not right_list:
                tar_list.extend(left_list)
                left_list.clear()
                break
            if left_list[0] < right_list[0]:
                tar_list.append(left_list.pop(0))
            else:
                tar_list.append(right_list.pop(0))
        return tar_list

    @staticmethod
    def insert_sort(lis):
        tar_list = lis.copy()
        for i in range(1, len(tar_list)):
            for j in range(i):
                if tar_list[j] > tar_list[i]:
                    tar_list.insert(j, tar_list.pop(i))
        return tar_list

    def quick_sort(self, lis):
        tar_lis = lis.copy()
        p = 0
        if len(lis) == 0 or len(lis) == 1:
            return lis
        q = len(lis)-1
        while True:
            while tar_lis[q] >= tar_lis[p]:
                if p == q:
                    break
                q -= 1
            if p == q:
                break
            tar_lis[p], tar_lis[q] = tar_lis[q], tar_lis[p]
            while tar_lis[p] < tar_lis[q]:
                if p == q:
                    break
                p += 1
            if p == q:
                break
            tar_lis[p], tar_lis[q] = tar_lis[q], tar_lis[p]
        tar_lis[:p] = self.quick_sort(tar_lis[:p])
        tar_lis[p+1:] = self.quick_sort(tar_lis[p+1:])
        return tar_lis


def count_avg_time(n):
    time_list = [[] for i in range(5)]
    method = SortMethod()
    for i in range(1):
        x = list(range(n))
        random.shuffle(x)
        # t = time.time()
        # method.select_sort(x)
        # time_list[0].append(time.time() - t)
        # t = time.time()
        # method.bubble_sort(x)
        # time_list[1].append(time.time() - t)
        t = time.time()
        method.merge_sort(x)
        time_list[2].append(time.time() - t)
        # t = time.time()
        # method.quick_sort(x)
        # time_list[3].append(time.time() - t)
        # t = time.time()
        # method.insert_sort(x)
        # time_list[4].append(time.time() - t)
    return [sum(time_list[i])/1 for i in range(5)]


def Algrithm_Test():
    tic = time.time()
    li = count_avg_time(200000)
    print(li)
    toc = time.time()
    print(toc - tic)
