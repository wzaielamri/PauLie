from common.pauli import *
from common.algebras import *
from common.nested import *


def genKlocal(n, p, converter = None, used = []):
    if n < len(p)//2:
        raise ValueError(f"Size must be greater than {len(p)//2}")

    #if len(p) != 4:
    #    raise ValueError("Pauli string should be equal to 2")

    np = n - len(p)//2
    k = 0
    while(k <= np):
       left = getI(k)
       left.extend(p)
       right = getI(np-k)
       left.extend(right)
       k = k + 1
       if left in used:
           continue
       if converter is None:
           yield left
       else:
           yield converter(left)
       used.append(left)

def genKlocalByString(n, pauliString, used = []):
    yield from genKlocal(n, getPauliArray(pauliString), used=used)

def genKlocalString(n, pauliString, used = []):
    yield from genKlocal(n, getPauliArray(pauliString), getPauliString, used=used)


def genKlocalExt(n, p, converter = None, used = []):

    if n < 2:
        raise ValueError("Size must be greater than 1")

    #if len(p) != 4:
    #    raise ValueError("Pauli string should be equal to 2")

    np = n - len(p)//2
    k = 0
    while(k <= np):
        left = getI(k)
        left_one = getY(k)
        full_left = left == left_one
        right = getI(np-k)
        right_one = getY(np-k)
        isFinish = False  
        while isFinish is False:
             gen = getI(0)
             gen.extend(left)
             gen.extend(p)
             gen.extend(right)
             if right == right_one:
                 if left == left_one:
                     isFinish = True
                 else:  
                     left = IncPauliArray(left)
             else:
                right = IncPauliArray(right)
             if len(used) > 0:
                 isUsed = False
                 for u in used:
                     if isSubInArray(u, gen):
                        isUsed = True
                        break
                 if isUsed:
                     continue
             if converter is None:
                 yield gen
             else:
                 yield converter(gen)
        k = k + 1

def genKlocalExtByString(n, pauliString):
    yield from genKlocalExt(n, getPauliArray(pauliString))

def genKlocalExtString(n, pauliString):
    yield from genKlocalExt(n, getPauliArray(pauliString), getPauliString)


def genKlocalAlgebraGenerators(n, name):
    generators = getAlgebra(name)
    used = []
    for g in generators:
        yield from genKlocalByString(n, g, used=used)

def getKlocalAlgebraGenerators(n, name):
    generators = []
    for g in genKlocalAlgebraGenerators(n, name):
        generators.append(g)
    return generators

def genKlocalStringAlgebraGenerators(n, name):
    generators = getAlgebra(name)
    used = []
    for g in generators:
        yield from genKlocalString(n, g, used=used)

def getKlocalStringAlgebraGenerators(n, name):
    generators = []
    used = []
    for g in genKlocalStringAlgebraGenerators(n, name):
        generators.append(g)
    return generators
####

def genKlocalGenerators(n, generators):
    used = []
    for g in generators:
        yield from genKlocalByString(n, g, used=used)

def getKlocalGenerators(n, generators):
    gens = []
    for g in genKlocalGenerators(n, generators):
        gens.append(g)
    return gens

def genKlocalStringGenerators(n, generators):
    used = []
    for g in generators:
        yield from genKlocalString(n, g, used=used)

def getKlocalStringGenerators(n, generators):
    gens = []
    for g in genKlocalStringGenerators(n, generators):
        gens.append(g)
    return gens

####

def genKlocalNestedNodesInAgebraGenerator(n, name):
    nested = getNestedNodesInAlgebra(name)
    used = []
    for node in nested:
        yield from genKlocalExt(n, node, used = used)
        used.append(node)

def getKlocalNestedNodesInAgebraGenerator(n, name):
    nodes = []
    for node in genKlocalNestedNodesInAgebraGenerator(n, name):
        nodes.append(node)
    return nodes