import numpy as np


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return

        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1


class Board:
    def __init__(self, filename):
        with open(filename) as f:
            self.vertices = int(f.readline())
            self.edge = int(f.readline())
            self.board = np.zeros((self.vertices, self.vertices), dtype=int)
            self.edges = np.zeros((self.edge, 2), dtype=int)
            for i in range(self.edge):
                line = f.readline().split()
                self.edges[i] = [min(int(line[0]), int(line[1])), max(int(line[0]), int(line[1]))]
                self.board[self.edges[i, 0], self.edges[i, 1]] = 1
            self.board = self.board | self.board.T

    def check_bridge(self):
        count = 0
        for edge in self.edges:
            self.board[edge[0], edge[1]] = 0
            self.board[edge[1], edge[0]] = 0
            if self.BFS(edge[0], edge[1]):
                count += 1
            self.board[edge[0], edge[1]] = 1
            self.board[edge[1], edge[0]] = 1
        return count

    def BFS(self, start, end):
        to_be_check = []
        checked = []
        for i in range(self.vertices):
            if self.board[start, i] == 1:
                to_be_check.append(i)
        while to_be_check:
            if end in to_be_check:
                return False
            temp = to_be_check.pop(0)
            checked.append(temp)
            for i in range(self.vertices):
                if (self.board[temp, i] == 1) & (i not in checked):
                    to_be_check.append(i)
        return True

    def check_bridge_new(self):
        UFset = UnionFind(self.vertices)
        default_len = len(set(self.renew_set(UFset).parent))
        count = 0
        for ignore_edge in self.edges:
            UFset = UnionFind(self.vertices)
            temp = set(self.renew_set(UFset, ignore_edge).parent)
            if default_len != len(temp):
                count += 1
        return count

    def renew_set(self, UF, ignore_edge=None):
        if ignore_edge is None:
            ignore_edge = [-1, -1]
        for u, v in self.edges:
            if u == ignore_edge[0] and v == ignore_edge[1]:
                continue
            UF.union(u, v)
        for i in range(self.vertices):
            UF.parent[i] = UF.find(UF.parent[i])
        return UF
