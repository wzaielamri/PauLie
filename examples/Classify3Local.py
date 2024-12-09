from PauLie import getAlgebra

def classifySizeGenerators(generators):
    for size in range(3, 4):
        algebra = getAlgebra(generators, size=size)
        print(f"size = {size} algebra = {algebra}")

if __name__ == '__main__':
    classifySizeGenerators(["XYI", "IXY", "YIX"])
    classifySizeGenerators(["XYI", "IXY"])





