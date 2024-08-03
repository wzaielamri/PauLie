from common.commutatorGrapth import *
from common.storage.impl.EdgeStorageArray  import *
from common.stateGraph import *
from time import perf_counter
from common.pauli import *


def testGraph(algebraName, size):

    #store = EdgeStorageArray()
    start_time = perf_counter()
    sizes = buildIZGraph(algebraName, size)
    end_time = perf_counter()
    EZ = 0
    for k, v in sizes.items():
        EZ += float(v/k)

    d = 2**size
    EZ = float(EZ/d)

    s = dict(sorted(sizes.items(), key=lambda item: item[0], reverse=True))
    EZ46 = float((1 + 3/(d + 1))/d)
    print(f"EZ = {EZ} EZ(46) = {EZ46} for {size} d = {d} time {end_time - start_time: 0.4f} sec. {s}")
    #store = sorted(store.getStorage(), key=len, reverse=True)
    #print(f"{store}")
    #print(f"{sizes}")
    #print(f'time excexution {end_time - start_time: 0.4f} sec.')


def testAlgebra(algebraName, size):
    print("============================================")
    print(f" algebra {algebraName}")
    print("============================================")
    for n in range(2, size + 1):
        testGraph(algebraName, n)

def testAllAlgebra(size):
    for algebraName in getAlgebras():
        testAlgebra(algebraName, size)

testAllAlgebra(5)
testAlgebra("a0", 8)
testGraph("a0", 10)

