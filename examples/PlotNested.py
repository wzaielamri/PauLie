from PauLie.common.extKlocal import *
from PauLie.stuff.drawing import *


if __name__ == '__main__':
    generators = getKlocalAlgebraGenerators(2, "a13")
    nestedNodes = getKlocalNestedNodesInAgebraGenerator(2, "a13")
    plotGraphByNodes(nestedNodes, generators)
