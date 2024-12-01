import sys
sys.path.append('..')

from common.nested import *


if __name__ == '__main__':
    nested = getNestedStringAlgebra("a3")
    print(f"{nested}")

    nested = getNestedStrings("XYIZ")
    print(f"{nested}")

