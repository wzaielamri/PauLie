import sys
sys.path.append('..')

from common.algebras import *
from stuff.drawing import *
from common.ext2local import *


generators = get2localAlgebraGenerators(4, "a6")
plotGraphByNodes(generators)

