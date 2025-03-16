from paulie.application.classify import get_algebra
from paulie.common.pauli_string_factory import get_pauli_string as p 



def classify_size_generators(generators):
    for size in range(3, 4):
        algebra = get_algebra(p(generators, n=size))
        print(f"size = {size} algebra = {algebra}")


if __name__ == "__main__":
    classify_size_generators(p(["XYI", "IXY", "YIX"]))
    classify_size_generators(p(["XYI", "IXY"]))





