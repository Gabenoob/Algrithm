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
    generate(5000,2000)
    x = graph.Board("a.txt")
    x1 = time.time()
    print(x.check_bridge_new())
    print(time.time()-x1)
    x2 = time.time()
    print(x.check_bridge())
    print(time.time()-x2)
