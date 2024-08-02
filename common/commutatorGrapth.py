from common.pauli import *
from common.algebras import *
from common.generator import *
from common.storage.EdgeStorage import *


######################################
###  Graph by commutator
#####################################

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



def printLinearBasis(algebraName, n):
    for current in generatorLinearBasis(algebraName, n):
        print(f"{getPauliString(current)}")
         

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

def replaceGetes(pos, pauliArray, pauliString):
    pArray = pauliArray.copy()
    aGates = getPauliArray(pauliString)
    pos *= 2
    for bit in aGates:
        pArray[pos] = bit
        pos += 1
    return pArray

def isInArray(a, b, position=0):

    pos = a.find(b, position)
    # print(f" pos {pos}")
    if pos > -1:
        if pos % 2 == 0:
            return True
        else:    
            return isInArray(a, b, position=pos+1)
    return False

def getEdgesInArray(a, arrayEdges):
    #if index >= len(arrayEdges):
    #    return []
    edges = []
    for edge_index in range(0, len(arrayEdges)):
        edge = list(arrayEdges[edge_index])
        #print(f"condidat {edge}")
        # b1 = replaceGetes(pos, a, edge[0])
        b1 = getPauliArray(edge[0])
        if isInArray(a, b1):
            #print(f"condidat 1 {edge[0]}")
            #if isIncluded(b1, arrayEdges, index) is False:
            edges.append([edge[0], edge[1]])
        else:
            #b2 = replaceGetes(pos, a, edge[1])
            b2 = getPauliArray(edge[1])
            if isInArray(a, b2):
                #print(f"condidat 2 {edge[1]}")
                # if isIncluded(b2, arrayEdges, index) is False:
                edges.append([edge[1], edge[0]])

    return edges



def isIncluded(a, arrayEdges, index):
    for edge_index in range(0, index):
        edge = list(arrayEdges[edge_index])
        b1 = getPauliArray(edge[0])
        if isInArray(a, b1):
            return True
        else:
            b2 = getPauliArray(edge[1])
            if isInArray(a, b2):
                return True
    return False

def isNodeIncluded(n, pauliString, arrayEdges, index, node, start, item, pair):
    # 
    if start == item:
        return True
    if pauliString == node:
        if start > item:
            return True
        else:
            return False
    if pauliString in arrayEdges[index]:
        if pair > item:
            return True
        else:
            return False
    if n > 3:
        return True
    if n == 2:
        for edge_index in range(0, index):
            edge = list(arrayEdges[edge_index])
            if pauliString == edge[0] or pauliString == edge[1]:
                return True
    if n == 3:
        for edge_index in range(0, index):
            edge = list(arrayEdges[edge_index])
            if edge[0].find(pauliString[1]) == 0 or edge[1].find(pauliString[1]) == 0:
                return True
            if edge[0].find(pauliString[0]) == 1 or edge[1].find(pauliString[0]) == 1:
                return True
       
    return False    

def findInArray(a, b, position = 0):
    pos = a.find(b, position)
    if pos == -1:
        return -1
    if pos % 2 == 0:
        return pos
    return  findInArray(a, b, position = pos+1)

def castExtention(a, edge):
    ext = []
    l_edge = list(edge)
    b1 = getPauliArray(l_edge[0])
    #b2 = getPauliArray(l_edge[1])
    pos = findInArray(a, b1)
    #print(f"pos = {pos//2} of {l_edge[0]} in {getPauliString(a)}")
    while(pos >= 0):
        
        b2 = replaceGetes(pos//2, a, l_edge[1])
        ext.append(getPauliString(b2))
        pos = findInArray(a, b1, position = pos+1)
    return ext

def cmpPauliArrays(pos, current, pauliArray, node):
    if current == pauliArray:
        return 0
    posInArra = findInArray(pauliArray, node)
    if posInArra < pos:
        return -1
    if posInArra > pos:
        return 1
    II = setIString(2)
    c = replaceGetes(pos, current, "II")
    p = replaceGetes(pos, pauliArray, "II")
    if  p < c:
        return -1
    return 1
