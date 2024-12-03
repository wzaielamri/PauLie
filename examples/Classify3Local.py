import sys
sys.path.append('..')

from common.extKlocal import *
from classifier.transform import *
#from graphs.graphView import *
#from stuff.drawing import *


#["XYI", "IXY", "YIX"]
def classifyGenerators(size, generators):
    nodes = getKlocalGenerators(size, generators)
    canonics = transformToCanonics(nodes)
    return canonics, nodes

def printClassify(size, generators, canonics, nodes):
    print(f"genetators {generators} size of {size}")

    for canonic in canonics:
        typeCanonic, nl, nc, n2 = canonic["shape"].getType()
        print(f"type = {typeCanonic} nl = {nl} nc = {nc} n2 = {n2}")

    print("--------------------------------------------------")

def printHead(size):
    print(f"Classification of dynamic Lia algebras size = {size}")
    print("--------------------------------------------------")


def classifySizeGenerators(generators):
    for size in range(3, 11):
        canonics, nodes = classifyGenerators(size, generators)
        printClassify(size, generators, canonics, nodes)

if __name__ == '__main__':
    classifySizeGenerators(["XYI", "IXY", "YIX"])






