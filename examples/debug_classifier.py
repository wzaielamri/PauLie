from paulie.helpers.drawing import plot_graph
from paulie.common.pauli_string_factory import get_pauli_string as p, PauliStringType, set_factory 
from paulie.common.algebras import get_lie_algebra
from time import perf_counter


def debug_classification(n, name, debug = True):
    print(f"Debugging classification for algebra {name} size {n}")
    print("--------------------------------------------------")

    generators = p(get_lie_algebra(name), n = n)
    print("--------------------------------------------------")
    print(f"algebra = {generators.get_class().get_algebra()}")

    #vertices, edges, edge_labels =  generators.get_canonic_graph()
    #plot_graph(vertices, edges, edge_labels)


if __name__ == '__main__':
    #debug_transform(600, "a1", True)
    start_time = perf_counter()
    debug_classification(10, "a22", True)
    end_time = perf_counter()
    print(f"np time {end_time - start_time: 0.4f} sec.")

    set_factory(PauliStringType.BITARRAY)
    start_time = perf_counter()
    debug_classification(10, "a22", True)
    end_time = perf_counter()
    print(f"bitarray time {end_time - start_time: 0.4f} sec.")



