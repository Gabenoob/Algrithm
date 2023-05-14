import numpy as np


# 颜色：1，2，3,4
class Board:
    def __init__(self):
        self.vertices: int = 9
        self.matrix: np.ndarray = np.ndarray((0, 0))
        self.coloredMap: list = []
        self.color = 25

    def renew_matrix(self):
        self.coloredMap = [0 for _ in range(self.vertices)]
        self.matrix: np.ndarray = np.zeros((self.vertices, self.vertices), dtype=int)

    def recall(self):
        layers = 0
        while layers < self.vertices:
            self.coloredMap[layers] += 1
            if self.coloredMap[layers] <= self.color:
                Map = np.multiply(self.matrix[layers], self.coloredMap)
                if self.coloredMap[layers] in Map:
                    continue
            else:
                self.coloredMap[layers] = 0
                layers -= 1
                continue
            layers += 1
            if layers == 0:
                return False
        return True
        # can_be_colored = {i for i in range(1, 26)}
        # cannot_be_colored = set()
        # for i in range(self.vertices):
        #     if self.matrix[vertices][i] == 1:
        #         if self.coloredMap[i] != 0:
        #             cannot_be_colored.add(self.coloredMap[i])
        # can_be_colored = can_be_colored-cannot_be_colored
        # for i in can_be_colored:
        #     self.coloredMap[vertices] = i
        #     if 0 not in self.coloredMap:
        #         return
        #     self.recall(vertices+1)
        #     if 0 not in self.coloredMap:
        #         return
        #     self.coloredMap[vertices] = 0

    # def MRV(self):
    #


def createBoard(file_name) -> Board:
    board = Board()
    with open(file_name) as f:
        lines = f.readlines()
        for line in lines:
            temp = line.split()
            if temp[0] == 'c' and len(temp) > 4:
                if temp[1] + temp[2] + temp[3] == 'numberofvertices':
                    board.vertices = int(temp[5])
                    board.renew_matrix()
            if temp[0] == 'e':
                board.matrix[int(temp[1]) - 1][int(temp[2]) - 1] = 1
    board.matrix = board.matrix.T + board.matrix
    return board
