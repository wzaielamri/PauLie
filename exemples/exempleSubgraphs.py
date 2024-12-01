import sys
sys.path.append('..')

from common.extKlocal import *
from graphs.subgraphs import *
from common.pauli import *

if __name__ == '__main__':
    generators = getKlocalAlgebraGenerators(4, "a2")
    for nodes in getSubgraphs(generators):
        print(f"{getArrayPauliStrings(nodes)}")
