from common.pauli import *
from common.generator import *
from classifier.transform import *


def classifyAlgebra(name, size):
    nodes = getAllCommutators(size, getAlgebra(name))
    canonics = transformToCanonics(nodes)
    return canonics, nodes

def printAlgebra(name, canonics, nodes):
    print(f"algebra {name} size of generators = {len(nodes)}")

    for canonic in canonics:
        typeCanonic, nl, nc, n2 = canonic["shape"].getType()
        print(f"size = {len(canonic['canonic'])} type = {typeCanonic} nl = {nl} nc = {nc} n2 = {n2}")

    print("--------------------------------------------------")

def printHead(size):
    print(f"Classification of dynamic Lia algebras size = {size}")
    print("--------------------------------------------------")


def classifyAllAlgebras(size):
    printHead(size)
    for name in getAlgebras():
        canonics, nodes = classifyAlgebra(name, size)
        printAlgebra(name, canonics, nodes)


classifyAllAlgebras(8)






