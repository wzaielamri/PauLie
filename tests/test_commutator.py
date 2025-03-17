from paulie.common.pauli_string_factory import get_pauli_string as p 




def test_commmutator():
    I = p("I")   # noqa
    X = p("X")
    Y = p("Y")
    Z = p("Z")
    assert I|I
    assert I|X
    assert I|Y
    assert I|Z
    assert X|I
    assert X|X
    assert not X|Y
    assert not X|Z
    assert Y|I
    assert not Y|X
    assert Y|Y
    assert not Y|Z
    assert Z|I
    assert not Z|X
    assert not Z|Y
    assert Z|Z
    assert I@I == I
    assert I@X == X
    assert I@Y == Y
    assert I@Z == Z
    assert X@I == X
    assert X@X == I
    assert X@Y == Z
    assert X@Z == Y
    assert Y@I == Y
    assert Y@X == Z
    assert Y@Y == I
    assert Y@Z == X
    assert Z@I == Z
    assert Z@X == Y
    assert Z@Y == X
    assert Z@Z == I
    assert Z^Y == X
    assert X@(Y@Z) == I
    assert X@Y@Z == I

    XI = p("XI")
    IX = p("IX")
    assert XI|XI

    XY = p("XY")
    YX = p("YX")
    assert XY|YX

    XIIII = p("XIIII")
    ZIIII = p("ZIIII")
    assert not XIIII|ZIIII


    IYXII = p("IYXII")
    IXIXI = p("IXIXI")
    IIIZI = p("IIIZI")
    IZIXZ = p("IZIXZ")
    IIIIX = p("IIIIX")

    assert XIIII|IYXII
    assert XIIII|IXIXI
    assert XIIII|IIIZI
    assert XIIII|IZIXZ
    assert XIIII|IIIIX

    assert ZIIII|IYXII
    assert ZIIII|IXIXI
    assert ZIIII|IIIZI
    assert ZIIII|IZIXZ
    assert ZIIII|IIIIX

    assert IYXII|IYXII
    assert not IYXII|IXIXI
    assert IYXII|IIIZI
    assert not IYXII|IZIXZ
    assert IYXII|IIIIX

    assert not IXIXI|IYXII
    assert IXIXI|IXIXI
    assert not IXIXI|IIIZI
    assert not IXIXI|IZIXZ
    assert IXIXI|IIIIX

    assert IIIZI|IYXII
    assert not IIIZI|IXIXI
    assert IIIZI|IIIZI
    assert not IIIZI|IZIXZ
    assert IIIZI|IIIIX

    assert not IZIXZ|IYXII
    assert not IZIXZ|IXIXI
    assert not IZIXZ|IIIZI
    assert IZIXZ|IZIXZ
    assert not IZIXZ|IIIIX

    assert IIIIX|IYXII
    assert IIIIX|IXIXI
    assert IIIIX|IIIZI
    assert not IIIIX|IZIXZ
    assert IIIIX|IIIIX

    IZXXI = p("IZXXI")
    assert IXIXI^IYXII == IZXXI
