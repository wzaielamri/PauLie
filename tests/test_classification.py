from paulie.application.classify import get_algebra
from paulie.common.pauli_string_factory import get_pauli_string as p 


def test_classification():
    assert get_algebra(p(["XY", "XZ"])) == get_algebra(p(["IX", "XY"]))