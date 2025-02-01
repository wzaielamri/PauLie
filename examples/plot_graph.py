from paulie.common.ext_k_local import get_k_local_string_algebra_generators
from paulie.helpers.drawing import plot_anti_commutation_graph


if __name__ == "__main__":
    generators = get_k_local_string_algebra_generators(6, "a6")
    plot_anti_commutation_graph(generators, size=0)

