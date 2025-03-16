from itertools import combinations
from paulie.common.pauli_string_generators import PauliStringGenerators

def non_commuting_charges(generators: PauliStringGenerators)->PauliStringGenerators:
    """
    inputs: generators as strings
    outputs: list of charges as strings
    """
    non_q = PauliStringGenerators()
    comm = generators.get_commutants()
    for c,q in combinations(comm,2):
        if c.commutes_with(q) is False:
            if c not in non_q:
                non_q.append(c)
            if q not in non_q:
                non_q.append(q)
    return non_q
