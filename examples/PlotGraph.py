import sys
sys.path.append('..')

from common.algebras import *
from stuff.drawing import *
from common.extKlocal import *


if __name__ == '__main__':
    generators = getKlocalAlgebraGenerators(4, "a6")
    plotGraphByNodes(generators)

