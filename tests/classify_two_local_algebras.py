from paulie.common.two_local_generators import get_lie_algebras
from paulie.application.classify import get_algebra
from paulie.common.pauli_string_factory import get_pauli_string as p


def classify_all_algebras(size: int):
    print(f"Classification of two local dynamical Lie algebras size = {size}")
    print("--------------------------------------------------")

    for name, generators in get_lie_algebras().items():
        algebra = get_algebra(p(generators, n=size))
        print(f"name={name} algebra={algebra}")

if __name__ == '__main__':
    classify_all_algebras(3)
