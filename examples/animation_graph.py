from paulie.common.algebras import get_algebra_generators
from paulie.helpers.drawing import animation_anti_commutation_graph


if __name__ == "__main__":
    generators = get_algebra_generators("a6")
    animation_anti_commutation_graph(generators, size=5)

