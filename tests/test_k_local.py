

from paulie.common.ext_k_local import get_k_local_string_generators


def test_k_local():
    generators = get_k_local_string_generators(5, ["XY", "XZ"])
    assert len(generators) == 8
    assert "XYIII" in generators
    assert "IXYII" in generators
    assert "IIXYI" in generators
    assert "IIIXY" in generators
    assert "XZIII" in generators
    assert "IXZII" in generators
    assert "IIXZI" in generators
    assert "IIIXZ" in generators