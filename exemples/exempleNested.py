import sys
sys.path.append('..')

from common.nested import *


nested = getNestedStringAlgebra("a3")
print(f"{nested}")

nested = getNestedStrings("XYIZ")
print(f"{nested}")

