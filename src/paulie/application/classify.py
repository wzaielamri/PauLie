from paulie.common.pauli_string_collection import PauliStringCollection


# Get algebra
# generators - list of generators
def get_algebra(generators: PauliStringCollection):
    classification = generators.get_class()
    return classification.get_algebra()



