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
    return bitarray(2*n)

def getAllOne(n):
    onePauliArray = setIString(n)
    onePauliArray.setall(1)
    return onePauliArray

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


def countAllPauliString(n):
    pauliArray = setIString(n)
    lastPauliArray = getAllOne(n)
    n = 1
    while True:
        pauliArray = IncPauliArray(pauliArray)
        n = n + 1
        if pauliArray == lastPauliArray:
            break
    return n


def printAllPauliStrings(n):
    pauliArray = setIString(n)
    pauliString = getPauliString(pauliArray)
    print(f"pauliString {pauliString}")
    lastPauliArray = getAllOne(n)

    while True:
        pauliArray = IncPauliArray(pauliArray)
        pauliString = getPauliString(pauliArray)
        print(f"pauliString {pauliString}")
        if pauliArray == lastPauliArray:
            break

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

def nest_commutator(nest, p):
    for aString in list(nest):
        a = getPauliArray(aString)
        if isCommutate(a, p) is False:
            c = multiPauliArrays(a, p)
            cString = getPauliString(c)

            if cString not in nest:
                nest.add(cString)
                nest_commutator(nest, c)
    return nest

def generateCommutator(aString, b):
    return nest_commutator({aString}, b)
