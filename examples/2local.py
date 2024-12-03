from paulie_classify.common.extKlocal import *

for g in genKlocalString(4, "XY"):
    print(f"{g}")

if __name__ == '__main__':
    generators = getKlocalStringAlgebraGenerators(4, "b0")
    print(f"{generators}")
