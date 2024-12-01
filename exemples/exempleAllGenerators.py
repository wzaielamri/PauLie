import sys
sys.path.append('..')

from time import perf_counter
from common.extKlocal import *

def loopAllGeneratorsNodes(n, name):
    i = 0
    for node in genKlocalAlgebraGenerators(n, name):
        i += 1
if __name__ == '__main__':
    for i in range(10, 21):
        start_time = perf_counter()
        loopAllGeneratorsNodes(100*i, "b4")
        end_time = perf_counter()
        print(f"size = {100*i} time {end_time - start_time: 0.6f}")