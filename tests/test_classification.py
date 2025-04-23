import pytest
from paulie.application.classify import get_algebra
from paulie.common.pauli_string_factory import get_pauli_string as p
from paulie.common.two_local_generators import G_LIE, two_local_algebras
from operator import itemgetter

@pytest.mark.parametrize("generators_to_compare", [
    ([["XY", "XZ"], ["IX", "XY"]]), #Example III.1 Wie+24
    ([["XX", "YZ"], ["YY", "ZX"]]), #Example III.4
    ([["ZZ", "YX", "XY"],["XX", "YZ", "ZY"],["YY", "ZX", "XZ"]]), #Example III.5
    (itemgetter("a2", "a4")(G_LIE)), #so(n)+so(n)
    (itemgetter("a11", "a16")(G_LIE)), #so(2^n)
    (itemgetter("a6", "a7", "a10")(G_LIE)), #su(2^(n-1))
    (itemgetter("a13", "a20", "a15")(G_LIE)), #su(2^(n-1))+su(2^(n-1))
    (itemgetter("a12", "a17", "a18", "a19", "a21", "a22")(G_LIE)), #su(2^n)

])
def test_multiple_algebra_equivalences(generators_to_compare):
    """Test algebra equivalences"""
    algebra = []
    for generator_set in generators_to_compare:
        algebra.append(get_algebra(p(generator_set)))

    assert all(x==algebra[0] for x in algebra), f"Expected to represent the same algebra"

def test_explicit_algebras():
    assert p(["XX", "YY", "ZZ", "ZY"]).get_class().is_algebra("u(1)+2*so(2)") # Example III.8
    assert p(["XY"]).get_class().is_algebra("u(1)") # Example I.4
    assert p(["XY"], n = 3).get_class().is_algebra("so(3)")
    for n in [3,5,10]:
        algs = two_local_algebras(n)
        for name in algs.keys():
            assert p(G_LIE[name], n = n).get_class().is_algebra(algs[name])









