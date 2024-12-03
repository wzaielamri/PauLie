from paulie_classify.common.extKlocal import *
from paulie_classify.stuff.drawing import *

#XYI;IXY; YIX
for g in genKlocalString(6, "XXX"):
    print(f"{g}")

if __name__ == '__main__':
    generators = getKlocalStringGenerators(6, ["XYI", "IXY", "YIX"])
    print(f"{generators}");

    generators = getKlocalGenerators(6, ["XYI", "IXY", "YIX"])
    print(f"{generators}");

    generators = getKlocalGenerators(6, ["XYI", "IXY", "YIX"])
    plotGraphByNodes(generators)


