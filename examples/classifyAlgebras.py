from PauLie import *
from PauLie.common.algebras import *


def classifyAllAlgebras(size):
    print(f"Classification of dynamic Lia algebras size = {size}")
    print("--------------------------------------------------")
    for name in getAlgebras():
        generators = getAlgebraGenerators(name)
        algebra = getAlgebra(generators, size=size)
        print(f"name={name} algebra={algebra}")

if __name__ == '__main__':
    classifyAllAlgebras(8)






