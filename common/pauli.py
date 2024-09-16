from bitarray import bitarray

# Object for handling Pauli strings that relies on the binary symplectic form
#See section 2 of https://quantum-journal.org/papers/q-2020-06-04-278/
#The binary symplectic form works as follows. For N = 1 we have
#I = (00)
#X = (10)
#Y = (11)
#Z = (01)
#This extends obviously for N>1, for example XYZ = (1,1,0|0,1,1)
#By performing modular arithmetic on this array we can implement the Pauli algebra.
I = bitarray([0,0])
X = bitarray([1,0])
Y = bitarray([1,1])
Z = bitarray([0,1])

codec = {'I':I, 'X':X, 'Y':Y, 'Z':Z}

def setIString(n):
    if n == 0:
        return bitarray()
    return bitarray(2*n)

def getAllOne(n):
    if n == 0:
        return bitarray()
    onePauliArray = setIString(n)
    onePauliArray.setall(1)
    return onePauliArray

def getAllZ(n):
    if n == 0:
        return bitarray()
    zetPauliArray = setIString(n)
    i = 1
    while(i < 2*n):
        zetPauliArray[i] = 1
        i += 2
    return zetPauliArray

def getPauliString(bitString):
    return ''.join(bitString.decode(codec))

def getPauliArray(pauliString):

    pauliArray = bitarray()
    pauliArray.encode(codec, pauliString)
    return pauliArray


def IncPauliArray(pauliArray):
    n = len(pauliArray) - 1
    stop = False
    while stop is not True:
        if pauliArray[n] == 0:
           pauliArray[n] = 1
           break
        if pauliArray[n] == 1:
           pauliArray[n] = 0
           n = n - 1
    return pauliArray

def IncIZPauliArray(pauliArray):
    n = len(pauliArray) - 1
    stop = False
    while stop is not True:
        if pauliArray[n] == 0:
           pauliArray[n] = 1
           break
        if pauliArray[n] == 1:
           pauliArray[n] = 0
           n = n - 2
    return pauliArray



def isCommutate(a, b):
    if len(a) != len(b):
        raise ValueError("gates must have the same length")
    i = 0
    lenString = len(a)
    a_dot_b = 0
    b_dot_a = 0

    while i < lenString:
       bitOneA = a[i]
       bitTwoA = a[i + 1]
       bitOneB = b[i]
       bitTwoB = b[i + 1]
       a_dot_b += 1 if bitOneA and bitTwoB else 0
       b_dot_a += 1 if bitTwoA and bitOneB else 0
       i = i + 2

    a_dot_b %= 2
    b_dot_a %= 2
    return a_dot_b == b_dot_a

def multiPauliArrays(a, b):
    c = bitarray(len(a))
    lenString = len(c)
    i = 0
    while i < lenString:
       c[i] = (a[i] + b[i]) % 2
       i = i + 1
    return c

def multiPauliStringToArray(a, b):
    aArray = getPauliArray(a)
    bArray = getPauliArray(b)
    cArray = multiPauliArrays(aArray, bArray)
    return cArray

def multiPauliString(a, b):
    return getPauliString(multiPauliStringToArray(a, b))

def commutator(a, b):
    if isCommutate(a, b):
        return bitarray(len(a))
    return multiPauliArrays(a, b)

def commutatorPauliString(a, b):
    aArray = getPauliArray(a)
    bArray = getPauliArray(b)
    cArray = commutator(aArray, bArray)
    return getPauliString(cArray)


def isIZString(a):
    i = 0
    size = len(a)
    while(i < size):
        if a[i] != 0:
            return False
        i += 2
    return True

def isIm(a):
    lenString = len(a)
    i = 0
    numbY = 0
    while i < lenString:
        if a[i] == 1 and a[i + 1] == 1:
           numbY += 1
        i += 2
    return numbY%2 == 1

def selectPauliString(a, b):
    if isCommutate(a, b):
       return b

    c = commutator(a, b)
    imA = isIm(a)
    imB = isIm(b)
    imC = isIm(c)
    if imA and imB and imC:
        return c
    if imA and not imB and not imC:
        return c
    if not imA and imB and not imC:
        return c
    if not imA and not imB and imC:
        return c
    return b


