from paulie.common.pauli_string_generators import PauliStringGenerators


# Get algebra
# generators - list of generators
def get_algebra(generators: PauliStringGenerators):
    classification = generators.get_class()
    return classification.get_algebra()



