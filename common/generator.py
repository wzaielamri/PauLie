from common.pauli import *
from common.algebras import *
import queue


def mergeGraph(listNest, nest):
    isUnion = False
    for itemNest in listNest:
        for item in nest:
            if item in itemNest:
                itemNest.union(nest)
                isUnion = True
                break
    if isUnion is False:
        listNest.append(nest)

    return listNest

def genarateGroupNodesByPauliString(aString):                                         
    n = len(aString)
    b = getI(n)
    last = getY(n)
    isFinishB = False
    listNest = []
    while isFinishB is False:
#        print(f"b = {getPauliString(b)}")
        if b == last:
            isFinishB = True
        nest = generateCommutator(aString, b)
        nest.remove(aString)
        if len(nest) > 0:
            listNest = mergeGraph(listNest, nest)
#            print(f"generator {aString} {getPauliString(b)} -> {nest}")

        if isFinishB is False:
            b = IncPauliArray(b)
    return listNest


def generateEdge(algebra):
    edges = []
    for a in algebra:
        edges += genarateGroupNodesByPauliString(a)
    return edges

def generateEdgeByAlgebraName(G, algebra):
    if algebra not in G:
        raise ValueError(f"invalid algebra: {algebra}")

    return generateEdge(G[algebra])



def nest_commutator(nest, p):
#    print(f"nest {nest} {getPauliString(p)}")
    for aString in list(nest):
        a = getPauliArray(aString)
        if isCommutate(a, p) is False:
            c = multiPauliArrays(a, p)
            cString = getPauliString(c)
#            print(f"{aString} * {getPauliString(p)} = {cString}")
            if cString not in nest:
                nest.add(cString)
                nest_commutator(nest, c)
    return nest

def generateCommutator(aString, b):
    return nest_commutator({aString}, b)


def generatorIBase(n, pauliString):
    np = n - len(pauliString)
    k = 0
    aGates = getPauliArray(pauliString)
    while(k <= np):
       left = getI(k)
       left.extend(aGates)
       right = getI(np-k)
       left.extend(right)
       k = k + 1
       yield left

def generatorAllCommutators(n, arrayGeneratorString):
    for pauliString in arrayGeneratorString:
        yield from generatorIBase(n, pauliString)

def generatorAllPauliStrings(n):
    pauliArray = getI(n)
    yield pauliArray
    lastPauliArray = getY(n)
    while True:
        pauliArray = IncPauliArray(pauliArray)
        yield pauliArray
        if pauliArray == lastPauliArray:
            break

def generatorAllIZPauliString(n):
    pauliArray = getI(n)
    yield pauliArray
    lastPauliArray = getZ(n)
    while True:
        pauliArray = IncIZPauliArray(pauliArray)
        yield pauliArray
        if pauliArray == lastPauliArray:
            break
 

def getAllCommutators(n, arrayGeneratorString):
    commutators = []
    for commutator in generatorAllCommutators(n, arrayGeneratorString):
         commutators.append(commutator)
    return commutators

def getSetAllCommutators(n, arrayGeneratorString):
    commutators = {}
    for commutator in generatorAllCommutators(n, arrayGeneratorString):
         commutators.add(commutator)
    return commutators

def generatorSecondAllCommutators(n, arrayGeneratorString):
    for pauliString in arrayGeneratorString:
        yield from generatorIBase(n, pauliString)

def generatorAllBase(n, pauliString):
    np = n - len(pauliString)
    k = 0
    aGates = getPauliArray(pauliString)
    while(k <= np):
        left = getI(k)
        left_one = getY(k)
        full_left = left == left_one
        right = getI(np-k)
        right_one = getY(np-k)
        isFinish = False  
        while isFinish is False:
             gen = getI(0)
             gen.extend(left)
             gen.extend(aGates)
             gen.extend(right)
             if right == right_one:
                 if left == left_one:
                     isFinish = True
                 else:  
                     left = IncPauliArray(left)
             else:
                right = IncPauliArray(right)

             yield gen, k
             
        k = k + 1

def geteratorNodeByCommutators(n, pauliArray, commutators):
    I = getI(n)
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
