from common.commutatorGrapth import *
from common.storage.impl.EdgeStorageArray  import *
from common.stateGraph import *
from time import perf_counter
from common.pauli import *


def testGraph(algebraName, size):

    start_time = perf_counter()
    sizes = buildIZGraph(algebraName, size)
    end_time = perf_counter()
    s = dict(sorted(sizes.items(), key=lambda item: item[0], reverse=True))
    print(f"for {size} time {end_time - start_time: 0.4f} sec. {s}")


def testAlgebra(algebraName, size):
    print("============================================")
    print(f" algebra {algebraName}")
    print("============================================")
    for n in range(2, size + 1):
        testGraph(algebraName, n)

testAlgebra("a5", 12)

