import numpy as np
import graph
import time

import matplotlib.pyplot as plt

if __name__ == "__main__":
    x = graph.Board("largeG.txt")
    x1 = time.time()
    print(x.check_bridge_new())
    print(time.time()-x1)
    x2 = time.time()
    print(x.check_bridge())
    print(time.time()-x2)
