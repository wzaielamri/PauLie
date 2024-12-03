from paulie_classify.common.algebras import *
from paulie_classify.stuff.drawing import *
from paulie_classify.common.extKlocal import *


if __name__ == '__main__':
    generators = getKlocalAlgebraGenerators(4, "a6")
    plotGraphByNodes(generators)

