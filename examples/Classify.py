from paulie_classify.common.extKlocal import *
from paulie_classify.classifier.transform import *

def classifySizeGenerators(size, generators):
    nodes = getKlocalGenerators(size, generators)
    canonics = transformToCanonics(nodes)
    algebras = [];
    for canonic in canonics:
        algebras.append(canonic["shape"].getAlgebra())
    print("algebra = " + " + ".join(algebras))

if __name__ == '__main__':
    classifySizeGenerators(9, ["XYI", "IXY", "YIX"])






