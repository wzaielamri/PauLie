import sys
sys.path.append('..')

from time import perf_counter
from common.pauli import *

def loopAllNodes(n):
    i = 0
    for node in genAllNodes(n):
        i += 1
if __name__ == '__main__':
    for i in range(4, 16):
        start_time = perf_counter()
        loopAllNodes(i)
        end_time = perf_counter()
        print(f"size = {i} time {end_time - start_time: 0.6f}")