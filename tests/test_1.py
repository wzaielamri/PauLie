# content of test_sample.py

import sys                      
sys.path.append('..')

from paulie_classify.classifier.transform import *
from paulie_classify.common.extKlocal import *

def classifySizeGenerators(size, generators):
    nodes = getKlocalGenerators(size, generators)
    canonics = transformToCanonics(nodes)
    algebras = [];
    for canonic in canonics:
        algebras.append(canonic["shape"].getAlgebra())
    return " + ".join(algebras)


def test_1():
    assert classifySizeGenerators(2, ["XY", "XZ"]) == classifySizeGenerators(2, ["IX", "XY"])