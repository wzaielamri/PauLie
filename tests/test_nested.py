from paulie.common.pauli_string_factory import get_pauli_string as p 


nesteds = {
"IX": [["ZY", "ZZ"], ["XY", "XZ"], ["YZ", "YY"], ["IZ", "IY"]],
"IY": [["IX", "IZ"], ["XX", "XZ"], ["YX", "YZ"], ["ZX", "ZZ"]],
"IZ": [["IX", "IY"], ["XX", "XY"], ["ZX", "ZY"], ["YX", "YY"]],
"XI": [["ZY", "YY"], ["ZX", "YX"], ["ZZ", "YZ"], ["ZI", "YI"]],
"XX": [["XZ", "IY"], ["IZ", "XY"], ["ZI", "YX"], ["YI", "ZX"]],
"XY": [["IX", "XZ"], ["IZ", "XX"], ["YI", "ZY"], ["YY", "ZI"]],
"XZ": [["IX", "XY"], ["IY", "XX"], ["YI", "ZZ"], ["YZ", "ZI"]],
"YI": [["XX", "ZX"], ["XY", "ZY"], ["XZ", "ZZ"], ["ZI", "XI"]],
"YX": [["IY","YZ"],["IZ","YY"],["ZI","XX"],["ZX","XI"]],
"YY": [["YX","IZ"],["ZI","XY"],["ZY","XI"],["IX","YZ"]],
"YZ": [["IY","YX"],["ZZ","XI"],["ZI","XZ"],["YY","IX"]],
"ZX": [["ZY","IZ"],["YI","XX"],["IY","ZZ"],["YX","XI"]],
"ZY": [["ZX","IZ"],["YI","XY"],["XI","YY"],["IX","ZZ"]],
"ZZ": [["XZ","YI"],["IY","ZX"],["ZY","IX"],["XI","YZ"]]}


def check_nested(node):
    nested = node.get_nested()
    nested_source = nesteds[str(node)]
    if len(nested) != len(nested_source):
        return False

    for pair in nested:
        found = False
        for source_pair in nested_source:
            if str(pair[0]) in source_pair and str(pair[1]) in source_pair:
                found = True
                break
        if found is False:
            return False
    for source_pair in nested_source:
        found = False
        for pair in nested:
            if source_pair[0] in pair and source_pair[1] in pair:
                found = True
                break
        if found is False:
            return False

    return True


def test_nested():
    assert check_nested(p("IX"))
    assert check_nested(p("IY"))
    assert check_nested(p("IZ"))
    assert check_nested(p("XI"))
    assert check_nested(p("XX"))
    assert check_nested(p("XY"))
    assert check_nested(p("XZ"))
    assert check_nested(p("YI"))
    assert check_nested(p("YX"))
    assert check_nested(p("YY"))
    assert check_nested(p("YZ"))
    assert check_nested(p("ZX"))
    assert check_nested(p("ZY"))
    assert check_nested(p("ZZ"))

