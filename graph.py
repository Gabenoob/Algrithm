import numpy as np


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        temp = x
        while self.parent[temp] != temp:
            temp = self.parent[temp]
        return temp

    def union(self, x, y,depth):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return
        elif depth[rootX] < depth[rootY]:
            self.parent[y] = rootX
        else:
            self.parent[x] = rootY

    def renew(self):
        for i in range(len(self.parent)):
            self.parent[i] = self.find(i)


class Board:
    def __init__(self, filename):
        with open(filename) as f:
            self.vertices = int(f.readline())
            self.edge = int(f.readline())
            # board 空间过大
            self.board = np.zeros((self.vertices, self.vertices), dtype=int)
            self.edges = np.zeros((self.edge, 2), dtype=int)
            self.lingjie_table = [set()] * self.vertices
            for i in range(self.edge):
                line = f.readline().split()
                self.edges[i] = [min(int(line[0]), int(line[1])), max(int(line[0]), int(line[1]))]
                self.lingjie_table[self.edges[i, 0]] = set.union(self.lingjie_table[self.edges[i, 0]],
                                                                 {self.edges[i, 1]})
                self.lingjie_table[self.edges[i, 1]] = set.union(self.lingjie_table[self.edges[i, 1]],
                                                                 {self.edges[i, 0]})
                self.board[self.edges[i, 0], self.edges[i, 1]] = 1
            self.board = self.board | self.board.T
            # board空间过大

    # 旧版找桥，即暴力法用的是邻接矩阵
    # 使用暴力法将__init__方法中的三行注释解开即可
    def check_bridge(self):
        count = 0
        for edge in self.edges:
            self.board[edge[0], edge[1]] = 0
            self.board[edge[1], edge[0]] = 0
            if (edge[0] != edge[1]) & self.BFS(edge[0], edge[1]):
                count += 1
            self.board[edge[0], edge[1]] = 1
            self.board[edge[1], edge[0]] = 1
        return count

    # BFS用的是邻接矩阵
    def BFS(self, start, end):
        to_be_check = []
        checked = []
        for i in range(self.vertices):
            if self.board[start, i] != 0:
                to_be_check.append(i)
        while to_be_check:
            if end in to_be_check:
                return False
            temp = to_be_check.pop(0)
            checked.append(temp)
            for i in range(self.vertices):
                if (self.board[temp, i] != 0) & (i not in checked):
                    to_be_check.append(i)
        return True

    def check_bridge_new(self):
        ori_UF = UnionFind(self.vertices)
        # BFS建树
        Tree = list(range(self.vertices))
        depth = [0]*self.vertices
        track = set()
        untrack = set(range(self.vertices))
        queue = []
        k = 0
        while untrack:
            if queue:
                temp = queue.pop(0)
                untrack.discard(temp)
            else:
                temp = untrack.pop()
                k = 0
            track.add(temp)
            depth[temp] = k
            for i in self.lingjie_table[temp]:
                if (i not in track) & (i != temp):
                    queue.append(i)
                    Tree[i] = temp
                    ori_UF.union(i, temp,depth)
            k += 1
        ori_UF.renew()
        new_UF = UnionFind(self.vertices)
        for i in range(self.edge):
            u, v = self.edges[i][0], self.edges[i][1]
            if Tree[v] == u or Tree[u] == v:
                continue
            if new_UF.find(u) == new_UF.find(v):
                continue
            self.LCA(Tree, u, v, new_UF,depth)
            new_UF.renew()
        count = 0
        for u, v in self.edges:
            if new_UF.find(u) != new_UF.find(v):
                count += 1
        return count

    def LCA(self, Tree, u, v, UF,depth):
        while True:
            if depth[u]>depth[v]:
                UF.union(u,Tree[u],depth)
                u = Tree[u]
            elif depth[u]<depth[v]:
                UF.union(v, Tree[v],depth)
                v = Tree[v]
            else:
                UF.union(u,v,depth)
                break
