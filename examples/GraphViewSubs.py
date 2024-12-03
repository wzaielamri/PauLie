from paulie_classify.common.algebras import *
from paulie_classify.graphs.graphView import *


if __name__ == '__main__':
    generators = getAlgebra("b4")
    v, e, l = getGraphViewByString(generators)
    print(f"vertices {v}")
    print(f"edges {e}")
    print(f"lables edge {l}")

