from PauLie.common.extKlocal import *
from PauLie.graphs.subgraphs import *
from PauLie.common.pauli import *

if __name__ == '__main__':
    generators = getKlocalAlgebraGenerators(4, "a2")
    for nodes in getSubgraphs(generators):
        print(f"{getArrayPauliStrings(nodes)}")
