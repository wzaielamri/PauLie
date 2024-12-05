from PauLie.common.algebras import *
from PauLie.stuff.drawing import *
from PauLie.common.extKlocal import *


if __name__ == '__main__':
    generators = getKlocalAlgebraGenerators(4, "a6")
    plotGraphByNodes(generators)

