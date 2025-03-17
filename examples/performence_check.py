from paulie.common.pauli_string_factory import get_pauli_string as p, PauliStringType, set_factory 
from paulie.common.all_pauli_strings import get_random, get_random_list
from time import perf_counter
from itertools import combinations
import numpy as np
from pauliarray import PauliArray
#from pauliarray.pauli.weighted_pauli_array import commutator

def perfomence_mult(g1):
    for a, b in combinations(g1, 2):
        p3 = a@b

def perfomence_check_comm(g1):
    for a, b in combinations(g1, 2):
        p3 = a^b

def perfomence_commutator_pauliarray(g1):
    for a, b in combinations(g1, 2):
        p3 = a.commute_with(b)

if __name__ == "__main__":
#    set_factory(PauliStringType.BITARRAY)
    print(f"{p("XXZ")}")
    print(f"{p("ZZX")}")
    print(f"{p("YZX")}")
#    exit()
    g = get_random_list(100, 1000)
    g1 = p(g)
    start_time = perf_counter()
    perfomence_mult(g1)
    end_time = perf_counter()
    print(f"np @ time {end_time - start_time: 0.4f} sec.")

    start_time = perf_counter()
    perfomence_check_comm(g1)
    end_time = perf_counter()
    print(f"np | time {end_time - start_time: 0.4f} sec.")


    set_factory(PauliStringType.BITARRAY)
    g1 = p(g)
    start_time = perf_counter()
    perfomence_mult(g1)
    end_time = perf_counter()
    print(f"bitarray @ time {end_time - start_time: 0.4f} sec.")

    start_time = perf_counter()
    perfomence_check_comm(g1)
    end_time = perf_counter()
    print(f"bitarray | time {end_time - start_time: 0.4f} sec.")

    paulis = PauliArray.from_labels(g)

    start_time = perf_counter()
    perfomence_commutator_pauliarray(paulis)
    end_time = perf_counter()
    print(f"pauliarray | time {end_time - start_time: 0.4f} sec.")
