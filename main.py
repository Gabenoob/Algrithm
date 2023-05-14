import dynamicProgram as dp
import time

if __name__ == "__main__":
    height, egg = 200, 1000
    x1 = time.time()
    dp.solution(height, egg)
    x2 = time.time()
    print(x2-x1)
    x1 = time.time()
    dp.solution_devide(height, egg)
    x2 = time.time()
    print(x2-x1)
