from PauLie.common.pauli import *
from PauLie.common.algebras import *


def getNested(p):
    nested = []
    for a in genAllNodes(len(p)//2):
        if a != p:
            for b in genAllNodes(len(p)//2):
                if b != p and a < b:
                    if isCommutate(a, b) is False:
                        if multiPauliArrays(a, b) == p:
                            nested.append([a.copy(), b.copy()])
    return nested

def getNestedByString(pauliString):
    return getNested(getPauliArray(pauliString))

def getNestedStrings(pauliString):
    nested = getNestedByString(pauliString)
    return  list(map(getArrayPauliStrings, nested))

def getNestedAlgebra(name):
    generators = getAlgebraGenerators(name)
    nested = []
    for g in generators:
        nested += getNestedByString(g)
    return nested

def getNestedStringAlgebra(name):
    generators = getAlgebraGenerators(name)
    nested = []
    for g in generators:
        nested += getNestedStrings(g)
    return nested

def getNodesInNested(nested):
    nodes = []
    for pair in nested:
        for node in pair:
            if node not in nodes:
                nodes.append(node)
    return nodes

def getNestedNodesInAlgebra(name):
    return getNodesInNested(getNestedAlgebra(name))