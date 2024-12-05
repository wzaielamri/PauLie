# content of test_sample.py

from PauLie.classifier.transform import *
from PauLie.common.extKlocal import *

def classifySizeGenerators(size, generators):
    nodes = getKlocalGenerators(size, generators)
    canonics = transformToCanonics(nodes)
    algebras = [];
    for canonic in canonics:
        algebras.append(canonic["shape"].getAlgebra())
    return " + ".join(algebras)


def test_1():
    assert classifySizeGenerators(2, ["XY", "XZ"]) == classifySizeGenerators(2, ["IX", "XY"])