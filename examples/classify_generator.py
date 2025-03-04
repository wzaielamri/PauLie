from paulie.common.algebras import get_lie_algebra
from paulie.application.classify import get_algebra


def classify_generator(generators):
    algebra = get_algebra(generators)
    print(f"algebra={algebra}")

if __name__ == '__main__':
    classify_generator(["XYZXZZ", "IZZYZY"])
