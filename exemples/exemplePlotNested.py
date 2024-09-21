import sys
sys.path.append('..')

from common.ext2local import *
from stuff.drawing import *


generators = get2localAlgebraGenerators(2, "a13")
nestedNodes = get2localNestedNodesInAgebraGenerator(2, "a13")
plotGraphByNodes(nestedNodes, generators)
