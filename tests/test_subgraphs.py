from PauLie.common.extKlocal import *
from PauLie.graphs.subgraphs import *


def test_subgraphs():
    generators = getKlocalGenerators(5, ["XIIII", "ZIIII", "IYXII", "IXIXI", "IIIZI", "IZIXZ", "IIIIX"])
    subgraphs = getSubgraphs(generators)
    assert len(subgraphs) == 2