from paulie.application.classify import get_algebra
from paulie.common.pauli_string_factory import get_pauli_string as p 


def classify_generator(generators):
    algebra = get_algebra(p(generators))
    print(f"algebra={algebra}")

if __name__ == '__main__':
    classify_generator(["XYZXZZ", "ZZYZYI"])
