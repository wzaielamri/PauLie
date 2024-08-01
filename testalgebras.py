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
    print(f"{store}")
    end_time = perf_counter()
    print(f'time excexution {end_time - start_time: 0.4f} sec.')
    print(f"{sizes}")
    # print("commutators")
    # printCommutators(store)
    print("edges")
    printEdges(algebraName, size, store)

    print("****************************************")
    print(" static graph")
    print("****************************************")

    start_time = perf_counter()
    subgraphs = stateGraph(algebraName, size)
    print(f"subgraphs {subgraphs}")
    sorted_list = [len(c) for c in subgraphs]
    print(f"subgraphs sizes {sorted_list}")

    end_time = perf_counter()
    print(f'time excexution graph {end_time - start_time: 0.4f} sec.')
    print("Subgraphs commutators")

testGraph("a0", 2)
testGraph("a1", 2)
testGraph("a2", 2)
testGraph("a3", 2)
testGraph("a4", 2)
testGraph("a5", 2)
testGraph("a6", 2)
testGraph("a7", 2)
testGraph("a8", 2)
testGraph("a9", 2)
testGraph("a10", 2)
testGraph("a11", 2)
testGraph("a12", 2)
testGraph("a13", 2)
testGraph("a14", 2)
testGraph("a15", 2)
testGraph("a16", 2)
testGraph("a17", 2)
testGraph("a18", 2)
testGraph("a19", 2)
testGraph("a20", 2)
testGraph("a21", 2)
testGraph("a22", 2)
testGraph("b0", 2)
testGraph("b1", 2)
testGraph("b2", 2)
testGraph("b3", 2)
testGraph("b4", 2)
