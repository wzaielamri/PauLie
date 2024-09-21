import sys
sys.path.append('..')

from common.ext2local import *
from graphs.subgraphs import *
from common.pauli import *

generators = get2localAlgebraGenerators(4, "a2")
for nodes in getSubgraphs(generators):
    print(f"{getArrayPauliStrings(nodes)}")
