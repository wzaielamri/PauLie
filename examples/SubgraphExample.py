from paulie_classify.common.extKlocal import *
from paulie_classify.graphs.subgraphs import *
from paulie_classify.common.pauli import *

if __name__ == '__main__':
    generators = getKlocalAlgebraGenerators(4, "a2")
    for nodes in getSubgraphs(generators):
        print(f"{getArrayPauliStrings(nodes)}")
