import sys
sys.path.append('..')

from common.extKlocal import *
from classifier.transform import *

def classifySizeGenerators(size, generators):
    nodes = getKlocalGenerators(size, generators)
    canonics = transformToCanonics(nodes)
    algebras = [];
    for canonic in canonics:
        algebras.append(canonic["shape"].getAlgebra())
    print("algebra = " + " + ".join(algebras))

if __name__ == '__main__':
    classifySizeGenerators(9, ["XYI", "IXY", "YIX"])






