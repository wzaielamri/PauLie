from common.pauli import *
from common.algebras import *
from common.generator import *
from common.storage.EdgeStorage import *
import queue

######################################
###  Graph by commutator
#####################################
def geteratorNodeByComutators(n, pauliArray, comutators):
    I = setIString(n)
    q = queue.Queue()
    q.put(pauliArray)
    ql = queue.Queue()
    store = {getPauliString(pauliArray)}
    while q.empty() is False:
        current = q.get()
        # print(f"current {getPauliString(current)}")
        for comutator in comutators:
            next = multiPauliArrays(comutator, current)
            if next != I and getPauliString(next) not in store: # and next not in comutators:
               # print(f"{getPauliString(current)} * {getPauliString(comutator)} next {getPauliString(next)}")
               store.add(getPauliString(next))
               q.put(next)
               yield next

def isIncludedInOther(n, current, pos, edges, index, comutators):

    for pauliArray in geteratorNodeByComutators(n, current, comutators):
        if isIncluded(pauliArray, edges, index):
            return True
        l_edge = list(edges[index])
        a = getPauliArray(l_edge[0])
        if findInArray(pauliArray, a) > -1:
            if cmpPauliArrays(pos, current, pauliArray, a) < 0:
            #if pauliArray < current:
                return True
        b = getPauliArray(l_edge[1])
        pair = replaceGetes(pos, current, l_edge[1])
        if findInArray(pauliArray, b) > -1:
            if cmpPauliArrays(pos, pair, pauliArray, b) < 0:
#            if pauliArray < pair:
                return True

    return False      

def testInStorage(storage, pauliString):
    subgraphs = storage.getStorage()
    for subgraph in subgraphs:
        if pauliString in subgraph:
            return True
    return False
def buildCommutatorTree(nameAlgebra, n, storage = EdgeStorage()):
    edges = generateEdgeByAlgebraName(getAlgebras(), nameAlgebra)
    comutators = getAllComutators(n, getAlgebra(nameAlgebra))
    print("commutators")
    for com in comutators:
        print(f"{getPauliString(com)}")
    print(f"edges algebra = {edges}")
    # print(f"len edges algebra = {len(edges)}")
    sizesOfSubgraph = {}
    for index, edge in enumerate(edges):
        #if index != 0:
        #    continue
        l_edge = list(edge)
        a = l_edge[0]
        b = l_edge[1]
        #a = "XY"
        #b = "IZ"
        for current, pos in generatorAllBase(n, a):

            if isIncluded(current, edges, index):
               continue
            pair = replaceGetes(pos, current, b)
            if isIncluded(pair, edges, index):
               continue

            if isIncludedInOther(n, current, pos, edges, index, comutators):
                continue
 
            if testInStorage(storage, getPauliString(current)):
                continue
#            print(f"build nodes by {getPauliString(current)}")
            numb = 1
            level = 0
            maxLevel = 2
            storage.create()
            storage.initRoute()
            storage.add(getPauliString(current))

#            print("*****comutators********")

            for pa in geteratorNodeByComutators(n, current, comutators):
                numb += 1
#                print(f"pa {getPauliString(pa)}")
                storage.add(getPauliString(pa))


#            storage.printSubgroup()
            storage.store()
            if numb in sizesOfSubgraph.keys():
                sizesOfSubgraph[numb] += 1
            else:
                sizesOfSubgraph[numb] = 1

    linked = 0
    for tot in sizesOfSubgraph.keys():
        linked += sizesOfSubgraph[tot] * tot
    one = 4**n - linked
    sizesOfSubgraph[1] = one
    return sizesOfSubgraph

def printCommutators(subgraphs):
    for subgraph in subgraphs:
        print(f"subgraph {subgraph}")
        for a in subgraph:
            for b in subgraph:
                if a != b:
                    c = multiPauliString(a, b) 
                    print(f"[{a}, {b}] = {c}")
 
def findDublicate(subgraphs):
    for index, subgraph in enumerate(subgraphs):
        for a in subgraph:
            for index2, subgraph2 in enumerate(subgraphs):
                if index != index2:
                    for b in subgraph2:
                        if b == a:
                           print(f"{a} in {subgraph} ind {index} and {index2} {subgraph2}")

def printSubgraphs(subgraphs):
    for index, subgraph in enumerate(subgraphs):
        print(f" ind {index} {subgraph}")
