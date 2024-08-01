from common.commutatorGrapth import *
from common.storage.impl.EdgeStorageArray  import *
from common.stateGraph import *
from time import perf_counter


def testGraph(algebraName, size):
    store = EdgeStorageArray()
    start_time = perf_counter()
    sizes = buildCommutatorTree(algebraName, size, store)
    store = sorted(store.getStorage(), key=len, reverse=True)
    print(f"{store}")
    end_time = perf_counter()
    print(f'time excexution {end_time - start_time: 0.4f} sec.')
    print(f"{sizes}")

    print("Subgraphs commutators")
    #printSubgraphs(store)
    printCommutators(store)
    #findDublicate(store)

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
    printCommutators(subgraphs)

testGraph("a0", 3)