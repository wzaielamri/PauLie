from paulie.common.algebras import get_algebra


def test_classification():
    assert get_algebra(["XY", "XZ"]) == get_algebra(["IX", "XY"])