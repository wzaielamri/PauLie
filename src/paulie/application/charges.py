from paulie.common.pauli import commutant


def non_commuting_charges(generators):
    non_q = []
    comm = commutant(generators)
    for c,q in combinations(comm,2):
        if is_commutate(c, q) is False:
            non_q.append(c)
            non_q.append(q)
    return non_q
