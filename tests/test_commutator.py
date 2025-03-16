from paulie.common.pauli_string_factory import get_pauli_string as p 




def test_commmutator():
    I = p("I")   # noqa
    X = p("X")
    Y = p("Y")
    Z = p("Z")
    assert I.commutes_with(I)
    assert I.commutes_with(X)
    assert I.commutes_with(Y)
    assert I.commutes_with(Z)
    assert X.commutes_with(I)
    assert X.commutes_with(X)
    assert not X.commutes_with(Y)
    assert not X.commutes_with(Z)
    assert Y.commutes_with(I)
    assert not Y.commutes_with(X)
    assert Y.commutes_with(Y)
    assert not Y.commutes_with(Z)
    assert Z.commutes_with(I)
    assert not Z.commutes_with(X)
    assert not Z.commutes_with(Y)
    assert Z.commutes_with(Z)
    assert I.multiply(I) == I
    assert I.multiply(X) == X
    assert I.multiply(Y) == Y
    assert I.multiply(Z) == Z
    assert X.multiply(I) == X
    assert X.multiply(X) == I
    assert X.multiply(Y) == Z
    assert X.multiply(Z) == Y
    assert Y.multiply(I) == Y
    assert Y.multiply(X) == Z
    assert Y.multiply(Y) == I
    assert Y.multiply(Z) == X
    assert Z.multiply(I) == Z
    assert Z.multiply(X) == Y
    assert Z.multiply(Y) == X
    assert Z.multiply(Z) == I
    assert Z.adjoint_map(Y) == X
    assert X.multiply(Y.multiply(Z)) == I

    XI = p("XI")
    IX = p("IX")
    assert XI.commutes_with(XI)

    XY = p("XY")
    YX = p("YX")
    assert XY.commutes_with(YX)

    XIIII = p("XIIII")
    ZIIII = p("ZIIII")
    assert not XIIII.commutes_with(ZIIII)


    IYXII = p("IYXII")
    IXIXI = p("IXIXI")
    IIIZI = p("IIIZI")
    IZIXZ = p("IZIXZ")
    IIIIX = p("IIIIX")

    assert XIIII.commutes_with(IYXII)
    assert XIIII.commutes_with(IXIXI)
    assert XIIII.commutes_with(IIIZI)
    assert XIIII.commutes_with(IZIXZ)
    assert XIIII.commutes_with(IIIIX)

    assert ZIIII.commutes_with(IYXII)
    assert ZIIII.commutes_with(IXIXI)
    assert ZIIII.commutes_with(IIIZI)
    assert ZIIII.commutes_with(IZIXZ)
    assert ZIIII.commutes_with(IIIIX)

    assert IYXII.commutes_with(IYXII)
    assert not IYXII.commutes_with(IXIXI)
    assert IYXII.commutes_with(IIIZI)
    assert not IYXII.commutes_with(IZIXZ)
    assert IYXII.commutes_with(IIIIX)

    assert not IXIXI.commutes_with(IYXII)
    assert IXIXI.commutes_with(IXIXI)
    assert not IXIXI.commutes_with(IIIZI)
    assert not IXIXI.commutes_with(IZIXZ)
    assert IXIXI.commutes_with(IIIIX)

    assert IIIZI.commutes_with(IYXII)
    assert not IIIZI.commutes_with(IXIXI)
    assert IIIZI.commutes_with(IIIZI)
    assert not IIIZI.commutes_with(IZIXZ)
    assert IIIZI.commutes_with(IIIIX)

    assert not IZIXZ.commutes_with(IYXII)
    assert not IZIXZ.commutes_with(IXIXI)
    assert not IZIXZ.commutes_with(IIIZI)
    assert IZIXZ.commutes_with(IZIXZ)
    assert not IZIXZ.commutes_with(IIIIX)

    assert IIIIX.commutes_with(IYXII)
    assert IIIIX.commutes_with(IXIXI)
    assert IIIIX.commutes_with(IIIZI)
    assert not IIIIX.commutes_with(IZIXZ)
    assert IIIIX.commutes_with(IIIIX)

    IZXXI = p("IZXXI")
    assert IXIXI.adjoint_map(IYXII) == IZXXI
