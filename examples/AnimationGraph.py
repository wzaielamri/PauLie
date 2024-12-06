from PauLie import *
from PauLie.common.algebras import *

if __name__ == '__main__':
    generators = getAlgebraGenerators("a6")
    animationAntiCommutationGraph(generators, size=5)

