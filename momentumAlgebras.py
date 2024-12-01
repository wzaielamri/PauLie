from common.commutatorGrapth import *
from common.storage.impl.EdgeStorageArray  import *
from common.stateGraph import *
from common.pauli import *

### Algebra moment calculation
def calcMomentumAlgebra(algebraName, size):

    subgraphs = buildIZGraph(algebraName, size)
    EZ = 0
    for k, v in subgraphs.items():
        EZ += float(v/k)

    d = 2**size
    EZ = float(EZ/d)
    s = dict(sorted(subgraphs.items(), key=lambda item: item[0], reverse=True))
    return s, d, EZ

### Algebra Moment Calculation and Printing
def momentumAlgebra(algebraName, size):
    print("============================================")
    print(f" algebra {algebraName}")
    print("============================================")
    for n in range(2, size + 1):
        s, d, EZ = calcMomentumAlgebra(algebraName, n)
        print(f"EZ = {EZ} for {size} d = {d}")
        print(f"subgraps {s}")
### Calculate and print algebra moments
def momentumAllAlgebras(size):
    for algebraName in getAlgebras():
        momentumAlgebra(algebraName, size)

if __name__ == '__main__':
    momentumAllAlgebras(5)

