

from paulie.graphs.subgraphs import get_subgraphs
from paulie.common.ext_k_local import get_k_local_generators


def test_subgraphs():
    generators = get_k_local_generators(5, ["XIIII", "ZIIII", "IYXII", "IXIXI", "IIIZI", "IZIXZ", "IIIIX"])
    subgraphs = get_subgraphs(generators)
    assert len(subgraphs) == 2