from paulie.common.algebras import get_lie_algebra
from paulie.application.charges import non_commuting_charges
from paulie.common.pauli_string_factory import get_pauli_string as p 


# a_8, a_9 posses non-commuting charges for all n
generators = p(get_lie_algebra("a8"))
assert len(non_commuting_charges(generators)) != 0
generators = p(get_lie_algebra("a9"))
assert len(non_commuting_charges(generators)) != 0
