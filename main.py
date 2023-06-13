import random

import numpy as np
import graph
import time

import matplotlib.pyplot as plt


def generate(vertices,edges):
    with open("a.txt","w") as f:
        f.writelines(f"{vertices}\n")
        f.writelines(f"{edges}\n")
        for i in range(edges):
            f.writelines(f"{random.randint(0,vertices-1)} {random.randint(0,vertices-1)}\n")


if __name__ == "__main__":
    before_table = []
    after_table = []
    for i in range(100,1000,300):
        lis1 = []
        lis2 = []
        for j in range(100,300,50):
            print(f"{i} {j}")
            generate(i,j)
            x = graph.Board("a.txt")
            x1 = time.time()
            x.check_bridge_new()
            lis1.append(time.time()-x1)
            x2 = time.time()
            x.check_bridge()
            lis2.append(time.time() - x2)
        before_table.append(lis2)
        after_table.append(lis1)
    print(before_table)
    print(after_table)
    # x = graph.Board("mediumDG.txt")
    # x1 = time.time()
    # x.check_bridge_new()
    # print(time.time() - x1)
    # x2 = time.time()
    # x.check_bridge()
    # print(time.time() - x2)
