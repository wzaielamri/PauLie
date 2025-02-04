
#a_8, a_9 posses non-commuting charges for all n
size= 10
generators = get_algebra_generators("a8")
assert len(non_commuting_charges(generators, size)) != 0
generators = get_algebra_generators("a9")
assert len(non_commuting_charges(generators, size)) != 0