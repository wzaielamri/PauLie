import sys
sys.path.append('..')

from common.extKlocal import *

for g in genKlocalString(4, "XY"):
    print(f"{g}")

generators = getKlocalStringAlgebraGenerators(4, "b0")
print(f"{generators}")
