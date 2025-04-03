from paulie.application.classify import get_algebra
from paulie.common.pauli_string_factory import get_pauli_string as p

n_qubits = 4
generators = p(["XY", "XZ"], n=n_qubits)
algebra = get_algebra(generators)
print(f"algebra = {algebra}")