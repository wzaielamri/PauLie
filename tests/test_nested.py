from PauLie.common.nested import *
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


def checkNested(node):
    nested = getNestedStrings(node)
    nested_source = nesteds[node]
    if len(nested) != len(nested_source):
        return False

    for pair in nested:
        found = False
        for source_pair in nested_source:
            if pair[0] in source_pair and pair[1] in source_pair:
                found = True
                break;
        if found is False:
            return False
    for source_pair in nested_source:
        found = False
        for pair in nested:
            if source_pair[0] in pair and source_pair[1] in pair:
                found = True
                break;
        if found is False:
            return False

    return True


def test_nested():
    assert checkNested("IX")
    assert checkNested("IY")
    assert checkNested("IZ")
    assert checkNested("XI")
    assert checkNested("XX")
    assert checkNested("XY")
    assert checkNested("XZ")
    assert checkNested("YI")
    assert checkNested("YX")
    assert checkNested("YY")
    assert checkNested("YZ")
    assert checkNested("ZX")
    assert checkNested("ZY")
    assert checkNested("ZZ")

