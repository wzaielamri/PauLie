import sys
sys.path.append('..')

from common.algebras import *
from graphs.graphView import *


generators = getAlgebra("b4")
v, e, l = getGraphViewByString(generators)
print(f"vertices {v}")
print(f"edges {e}")
print(f"lables edge {l}")

