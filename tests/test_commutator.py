from PauLie.common.pauli import *


def test_commmutator():
    I = getPauliArray("I")
    X = getPauliArray("X")
    Y = getPauliArray("Y")
    Z = getPauliArray("Z")
    assert isCommutate(I, I)
    assert isCommutate(I, X)
    assert isCommutate(I, Y)
    assert isCommutate(I, Z)
    assert isCommutate(X, I)
    assert isCommutate(X, X)
    assert isCommutate(X, Y) is False
    assert isCommutate(X, Z) is False
    assert isCommutate(Y, I)
    assert isCommutate(Y, X) is False
    assert isCommutate(Y, Y)
    assert isCommutate(Y, Z) is False
    assert isCommutate(Z, I)
    assert isCommutate(Z, X) is False
    assert isCommutate(Z, Y) is False
    assert isCommutate(Z, Z)
    assert multiPauliArrays(I, I) == I
    assert multiPauliArrays(I, X) == X
    assert multiPauliArrays(I, Y) == Y
    assert multiPauliArrays(I, Z) == Z
    assert commutator(X, Y) == Z
    assert commutator(X, Z) == Y
    assert commutator(Y, X) == Z
    assert commutator(Y, Z) == X
    assert commutator(Z, X) == Y
    assert commutator(Z, Y) == X
    assert(commutator(X, commutator(Y, Z))) == I

    XI = getPauliArray("XI")
    IX = getPauliArray("IX")
    assert isCommutate(XI, XI)

    XY = getPauliArray("XY")
    YX = getPauliArray("YX")
    assert isCommutate(XY, YX)
    XIIII = getPauliArray("XIIII")
    ZIIII = getPauliArray("ZIIII")
    assert isCommutate(XIIII, ZIIII) is False

    IYXII = getPauliArray("IYXII")
    IXIXI = getPauliArray("IXIXI")
    IIIZI = getPauliArray("IIIZI")
    IZIXZ = getPauliArray("IZIXZ")
    IIIIX = getPauliArray("IIIIX")

    assert isCommutate(XIIII, IYXII)
    assert isCommutate(XIIII, IXIXI)
    assert isCommutate(XIIII, IIIZI)
    assert isCommutate(XIIII, IZIXZ)
    assert isCommutate(XIIII, IIIIX)

    assert isCommutate(ZIIII, IYXII)
    assert isCommutate(ZIIII, IXIXI)
    assert isCommutate(ZIIII, IIIZI)
    assert isCommutate(ZIIII, IZIXZ)
    assert isCommutate(ZIIII, IIIIX)

    assert isCommutate(IYXII, IYXII)
    assert isCommutate(IYXII, IXIXI) is False
    assert isCommutate(IYXII, IIIZI)
    assert isCommutate(IYXII, IZIXZ) is False
    assert isCommutate(IYXII, IIIIX)

    assert isCommutate(IXIXI, IYXII) is False
    assert isCommutate(IXIXI, IXIXI)
    assert isCommutate(IXIXI, IIIZI) is False
    assert isCommutate(IXIXI, IZIXZ) is False
    assert isCommutate(IXIXI, IIIIX)

    assert isCommutate(IIIZI, IYXII)
    assert isCommutate(IIIZI, IXIXI) is False
    assert isCommutate(IIIZI, IIIZI)
    assert isCommutate(IIIZI, IZIXZ) is False
    assert isCommutate(IIIZI, IIIIX)

    assert isCommutate(IZIXZ, IYXII) is False
    assert isCommutate(IZIXZ, IXIXI) is False
    assert isCommutate(IZIXZ, IIIZI) is False
    assert isCommutate(IZIXZ, IZIXZ)
    assert isCommutate(IZIXZ, IIIIX) is False

    assert isCommutate(IIIIX, IYXII)
    assert isCommutate(IIIIX, IXIXI)
    assert isCommutate(IIIIX, IIIZI)
    assert isCommutate(IIIIX, IZIXZ) is False
    assert isCommutate(IIIIX, IIIIX)

    IZXXI = getPauliArray("IZXXI")
    assert commutator(IXIXI, IYXII) == IZXXI

