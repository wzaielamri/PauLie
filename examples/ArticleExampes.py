import sys                      
sys.path.append('..')

from classifier.transform import *
from common.extKlocal import *
from common.pauli import *


def classifySizeGenerators(size, generators):
    nodes = getKlocalGenerators(size, generators)
    canonics = transformToCanonics(nodes)
    algebras = [];
    for canonic in canonics:
        algebras.append(canonic["shape"].getAlgebra())
    return " + ".join(algebras)

if __name__ == '__main__':
    #1
    print("Example III.1")
    alg = classifySizeGenerators(2, ["XY", "XZ"])
    print(f'alg {"XY", "XZ"} = {alg}')
    alg = classifySizeGenerators(2, ["IX", "XY"])
    print(f'alg {"IX", "XY"} = {alg}')
    #2
    print("Example III.2")
    alg = classifySizeGenerators(2, ["XY", "XI", "IX"])
    print(f'alg {"XY", "XI", "IX"} = {alg}')
    alg = classifySizeGenerators(2, ["XY", "XZ"])
    print(f'alg {"XY", "XZ"} = {alg}')
    #3
    print("Example III.3")
    alg = classifySizeGenerators(2, ["XX", "YY"])
    print(f'alg {"XX", "YY"} = {alg}')
    alg = classifySizeGenerators(2, ["XX", "YX"])
    print(f'alg {"XX", "YX"} = {alg}')

    print("Example III.4")
    alg = classifySizeGenerators(2, ["XX", "YZ"])
    print(f'alg {"XX", "YZ"} = {alg} isCommutate = {isCommutateByString("XX", "YZ")}')
    alg = classifySizeGenerators(2, ["YY", "ZX"])
    print(f'alg {"YY", "ZX"} = {alg} isCommutate = {isCommutateByString("YY", "ZX")}')
    alg = classifySizeGenerators(2, ["XX", "YY"])
    print(f'alg {"XX", "YY"} = {alg} isCommutate = {isCommutateByString("XX", "YY")}')

    print("Example III.5")
    alg = classifySizeGenerators(2, ["ZZ", "YX", "XY"])
    print(f'alg {"ZZ", "YX", "XY"} = {alg}')
    alg = classifySizeGenerators(2, ["XX", "YZ", "ZY"])
    print(f'alg {"XX", "YZ", "ZY"} = {alg}')
    alg = classifySizeGenerators(2, ["YY", "ZX", "XZ"])
    print(f'alg {"YY", "ZX", "XZ"} = {alg}')

    print("Example III.6")
    alg = classifySizeGenerators(2, ["XX", "XZ", "IY"])
    print(f'alg {"XX", "XZ", "IY"} = {alg}')
    alg = classifySizeGenerators(2, ["XY", "XZ", "IX"])
    print(f'alg {"XY", "XZ", "IX"} = {alg}')

    print("Example III.7")
    alg = classifySizeGenerators(2, ["XY", "YX"])
    print(f'alg {"XY", "YX"} = {alg} isCommutate = {isCommutateByString("XY", "YX")}')
    alg = classifySizeGenerators(2, ["XY", "YZ"])
    print(f'alg {"XY", "YZ"} = {alg} isCommutate = {isCommutateByString("XY", "YZ")}')

    print("Example III.8")
    alg = classifySizeGenerators(2, ["XX", "YY", "ZZ", "ZY"])
    print(f'alg {"XX", "YY", "ZZ", "ZY"} = {alg}')
