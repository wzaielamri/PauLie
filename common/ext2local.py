from common.pauli import *
from common.algebras import *


def gen2local(n, p, converter = None):
    if n < 3:
        raise ValueError("Size must be greater than 2")

    if len(p) != 4:
        raise ValueError("Pauli string should be equal to 2")

    np = n - len(p)//2
    k = 0
    while(k <= np):
       left = getI(k)
       left.extend(p)
       right = getI(np-k)
       left.extend(right)
       k = k + 1
       if converter is None:
           yield left
       else:
           yield converter(left)

def gen2localByString(n, pauliString):
    yield from gen2local(n, getPauliArray(pauliString))

def gen2localString(n, pauliString):
    yield from gen2local(n, getPauliArray(pauliString), getPauliString)


def gen2localExt(n, p, converter = None):

    if n < 3:
        raise ValueError("Size must be greater than 2")

    if len(p) != 4:
        raise ValueError("Pauli string should be equal to 2")

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

             if converter is None:
                 yield gen
             else:
                 yield converter(gen)
        k = k + 1

def gen2LocalExtByString(n, pauliString):
    yield from gen2localExt(n, getPauliArray(pauliString))

def gen2localExtString(n, pauliString):
    yield from gen2localExt(n, getPauliArray(pauliString), getPauliString)

def gen2localAlgebraGenerators(n, name):
    generators = getAlgebra(name)
    for g in generators:
        yield from gen2localByString(n, g)

def get2localAlgebraGenerators(n, name):
    generators = []
    for g in gen2localAlgebraGenerators(n, name):
        generators.append(g)
    return generators

def gen2localStringAlgebraGenerators(n, name):
    generators = getAlgebra(name)
    for g in generators:
        yield from gen2localString(n, g)

def get2localStringAlgebraGenerators(n, name):
    generators = []
    for g in gen2localStringAlgebraGenerators(n, name):
        generators.append(g)
    return generators

