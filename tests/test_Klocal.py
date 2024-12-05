# content of test_sample.py
from PauLie.common.extKlocal import *


def test_Klocal():
    generators = getKlocalStringGenerators(5, ["XY", "XZ"])
    assert len(generators) == 8
    assert "XYIII" in generators
    assert "IXYII" in generators
    assert "IIXYI" in generators
    assert "IIIXY" in generators
    assert "XZIII" in generators
    assert "IXZII" in generators
    assert "IIXZI" in generators
    assert "IIIXZ" in generators