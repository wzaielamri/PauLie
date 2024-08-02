from common.pauli import *
from common.algebras import *
from common.generator import *
from common.storage.EdgeStorage import *
import queue

######################################
###  Graph by commutator
#####################################
def geteratorNodeByCommutators(n, pauliArray, commutators):
    I = setIString(n)
    q = queue.Queue()
    q.put(pauliArray)
    ql = queue.Queue()
    store = {getPauliString(pauliArray)}
    while q.empty() is False:
        current = q.get()
        # print(f"current {getPauliString(current)}")
        for commutator in commutators:
            if isCommutate(commutator, current):
                continue
            next = multiPauliArrays(commutator, current)
            if next != I and getPauliString(next) not in store: # and next not in comutators:
               # print(f"{getPauliString(current)} * {getPauliString(comutator)} next {getPauliString(next)}")
               store.add(getPauliString(next))
               q.put(next)
               yield next

def isIncludedInOther(n, current, pos, edges, index, commutators):

    for pauliArray in geteratorNodeByCommutators(n, current, commutators):
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

def buildCommutatorTree(algebraName, n, storage = EdgeStorage()):
    edges = generateEdgeByAlgebraName(getAlgebras(), algebraName)
    commutators = getAllCommutators(n, getAlgebra(algebraName))
    print("commutators")
    for com in commutators:
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

            # if isIncluded(current, edges, index):
            #    continue
            pair = replaceGetes(pos, current, b)
            # if isIncluded(pair, edges, index):
            #    continue

            # if isIncludedInOther(n, current, pos, edges, index, comutators):
            #     continue
 
            if testInStorage(storage, getPauliString(current)):
                continue
#            print(f"build nodes by {getPauliString(current)}")
            numb = 1
            level = 0
            maxLevel = 2
            storage.create()
            storage.initRoute()
            storage.add(getPauliString(current))

#            print("*****commutators********")

            for pa in geteratorNodeByCommutators(n, current, commutators):
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


def generatorLinearBasis(algebraName, n):
    commutators = getAllCommutators(n, getAlgebra(algebraName))
    for current in generatorAllPauliStrings(n):
        isNotCommutate = False

        for commutator in commutators:
            if isCommutate(commutator, current) is False:
                isNotCommutate = True
                break
        if isNotCommutate is False:
            yield current


def printLinearBasis(algebraName, n):
    for current in generatorLinearBasis(algebraName, n):
        print(f"{getPauliString(current)}")
         
def generatorIZConnectedVertex(algebraName, n):
    commutators = getAllCommutators(n, getAlgebra(algebraName))
    for current in generatorAllIZPauliString(n):
        isIZCommutate = False
        for commutator in commutators:
            if isCommutate(commutator, current) is False:
                for linear in generatorLinearBasis(algebraName, n):
                    c = multiPauliArrays(linear, current)
                    # print(f"ALL {getPauliString(current)} - linear - {getPauliString(linear)} = {getPauliString(c)}")
                    if isIZString(c):
                        isIZCommutate = True
                        # print(f"{getPauliString(current)} - linear - {getPauliString(linear)} = {getPauliString(c)}")
                        break
            if isIZCommutate:
                break
        if isIZCommutate:
            yield current

def printAllIZ(algebraName, n):
    for current in generatorIZConnectedVertex(algebraName, n):
        print(f"{getPauliString(current)}")
    




def printCommutators(subgraphs):
    for subgraph in subgraphs:
        print(f"subgraph {subgraph}")
        for a in subgraph:
            for b in subgraph:
                if a != b:
                    c = multiPauliString(a, b) 
                    print(f"[{a}, {b}] = {c}")

def printEdges(algebraName, n, subgraphs):
    commutators = getAllCommutators(n, getAlgebra(algebraName))

    for subgraph in subgraphs:
        print(f"subgraph {subgraph}")
        for a in subgraph:
            for b in subgraph:
                if a != b:
                    c = multiPauliString(a, b)
                    if getPauliArray(c) in commutators:
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


def isIncludedInGraph(n, current, commutators):
    for pauliArray in geteratorNodeByCommutators(n, current, commutators):
        if isIZString(pauliArray):
           if pauliArray < current:
               return True
    return False      


def buildIZGraph(algebraName, n, storage = EdgeStorage()):
    commutators = getAllCommutators(n, getAlgebra(algebraName))
    sizesOfSubgraph = {}

    for current in generatorIZConnectedVertex(algebraName, n):
        if isIncludedInGraph(n, current, commutators):
            continue

        storage.create()
        storage.add(getPauliString(current))
        numb = 1
        for pa in geteratorNodeByCommutators(n, current, commutators):
            numb += 1
            storage.add(getPauliString(pa))

        storage.store()
        if numb in sizesOfSubgraph.keys():
           sizesOfSubgraph[numb] += 1
        else:
           sizesOfSubgraph[numb] = 1

    sizesOfSubgraph[1] = 0
    for current in generatorLinearBasis(algebraName, n):
        if isIZString(current):
            storage.create()
            storage.add(getPauliString(current))
            sizesOfSubgraph[1] += 1
            storage.store()

    return sizesOfSubgraph
