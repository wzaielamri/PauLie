from common.pauli import *
from common.symmetries import Symmetries


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
    b = setIString(n)
    last = getAllOne(n)
    isFinishB = False
    listNest = []
    while isFinishB is False:
        if b == last:
            isFinishB = True
        nest = generateCommutator(aString, b)
        nest.remove(aString)
        if len(nest) > 0:
            listNest = mergeGraph(listNest, nest)
           #print(f"algebra {aString} {getPauliString(b)} -> {nest}")

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




def getSubGroupsOfAlgebra(algebra):
    subgroups = Symmetries()
    for a in algebra:
        edges = genarateGroupNodesByPauliString(a)
        subgroups.add(edges)
    return subgroups

def getSubGroupsOfAlgebraByName(G, algebra):
    if algebra not in G:
        raise ValueError(f"invalid algebra: {algebra}")

    return getSubGroupsOfAlgebra(G[algebra])
