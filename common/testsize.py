from common.commutatorGrapth import *
from common.storage.impl.EdgeStorageArray  import *
from common.stateGraph import *
from time import perf_counter


def testGraph(algebraName, size):
    print("============================================")
    print(f" algebra {algebraName} size {size}")
    print("============================================")

    store = EdgeStorageArray()
    start_time = perf_counter()
    sizes = buildCommutatorTree(algebraName, size, store)
    store = sorted(store.getStorage(), key=len, reverse=True)
    # print(f"{store}")
    end_time = perf_counter()
    print(f'time excexution {end_time - start_time: 0.4f} sec.')
    # print(f"{sizes}")

    #s = dict(sorted(sizes.items(), key=lambda item: item[1]))
    #s = dict(sorted(sizes.keys()))
    s = dict(sorted(sizes.items(), key=lambda item: item[0], reverse=True))
    print(f"{s}")


for i in range(2,8):
    testGraph("a2", i)
# testGraph("a5", 2)
# testGraph("a12", 2)