from PauLie import getAlgebra

if __name__ == '__main__':
    #1
    print("Example III.1")
    alg = getAlgebra(["XY", "XZ"])
    print(f'alg {"XY", "XZ"} = {alg}')
    alg = getAlgebra(["IX", "XY"])
    print(f'alg {"IX", "XY"} = {alg}')
    #2
    print("Example III.2")
    alg = getAlgebra(["XY", "XI", "IX"])
    print(f'alg {"XY", "XI", "IX"} = {alg}')
    alg = getAlgebra(["XY", "XZ"])
    print(f'alg {"XY", "XZ"} = {alg}')
    #3
    print("Example III.3")
    alg = getAlgebra(["XX", "YY"])
    print(f'alg {"XX", "YY"} = {alg}')
    alg = getAlgebra(["XX", "YX"])
    print(f'alg {"XX", "YX"} = {alg}')

    print("Example III.4")
    alg = getAlgebra(["XX", "YZ"])
    print(f'alg {"XX", "YZ"} = {alg}')
    alg = getAlgebra(["YY", "ZX"])
    print(f'alg {"YY", "ZX"} = {alg}')
    alg = getAlgebra(["XX", "YY"])
    print(f'alg {"XX", "YY"} = {alg}')

    print("Example III.5")
    alg = getAlgebra(["ZZ", "YX", "XY"])
    print(f'alg {"ZZ", "YX", "XY"} = {alg}')
    alg = getAlgebra(["XX", "YZ", "ZY"])
    print(f'alg {"XX", "YZ", "ZY"} = {alg}')
    alg = getAlgebra(["YY", "ZX", "XZ"])
    print(f'alg {"YY", "ZX", "XZ"} = {alg}')

    print("Example III.6")
    alg = getAlgebra(["XX", "XZ", "IY"])
    print(f'alg {"XX", "XZ", "IY"} = {alg}')
    alg = getAlgebra(["XY", "XZ", "IX"])
    print(f'alg {"XY", "XZ", "IX"} = {alg}')

    print("Example III.7")
    alg = getAlgebra(["XY", "YX"])
    print(f'alg {"XY", "YX"} = {alg}')
    alg = getAlgebra(["XY", "YZ"])
    print(f'alg {"XY", "YZ"} = {alg}')

    print("Example III.8")
    alg = getAlgebra(["XX", "YY", "ZZ", "ZY"])
    print(f'alg {"XX", "YY", "ZZ", "ZY"} = {alg}')
