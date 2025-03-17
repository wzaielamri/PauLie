from paulie.common.pauli_string_factory import (
    get_pauli_string as p, 
    PauliStringType, 
    set_factory,
)
from paulie.common.algebras import get_lie_algebra
from time import perf_counter


def debug_classification(n, name):
    print(f"Debugging classification for algebra {name} size {n}")
    print("--------------------------------------------------")

    generators = p(get_lie_algebra(name), n = n)
    print("--------------------------------------------------")
    print(f"algebra = {generators.get_class().get_algebra()}")


if __name__ == '__main__':
    start_time = perf_counter()
    debug_classification(100, "a22")
    end_time = perf_counter()
    print(f"np time {end_time - start_time: 0.4f} sec.")

    set_factory(PauliStringType.BITARRAY)
    start_time = perf_counter()
    debug_classification(100, "a22")
    end_time = perf_counter()
    print(f"bitarray time {end_time - start_time: 0.4f} sec.")
