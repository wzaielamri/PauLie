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

def getI(n):
    if n == 0:
        return bitarray()
    return bitarray(2*n)

def getY(n):
    if n == 0:
        return bitarray()
    onePauliArray = getI(n)
    onePauliArray.setall(1)
    return onePauliArray

def getZ(n):
    if n == 0:
        return bitarray()
    zetPauliArray = getI(n)
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
    a_dot_b = 0
    b_dot_a = 0
    i = 0

    while i < len(a):
       a_dot_b += 1 if a[i] and  b[i + 1] else 0
       b_dot_a += 1 if a[i + 1] and b[i] else 0
       i = i + 2

    a_dot_b %= 2
    b_dot_a %= 2
    return a_dot_b == b_dot_a

def isCommutateByString(a, b):
     return isCommutate(getPauliArray(a), getPauliArray(b))

def multiPauliArrays(a, b):
    if len(a) != len(b):
        raise ValueError("gates must have the same length")
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

def isSubInArray(sub, a, pos=0):
    index = a.find(sub, pos)
    if index == -1:
        return False
    if index % 2 == 0:
        return True
    return isSubInArray(sub, a, index+1)


def genAllNodes(n):
    a = getI(n)
    yield a
    last = getY(n)
    while True:
        a = IncPauliArray(a)
        yield a
        if a == last:
            break

def genAllIZ(n):
    a = getI(n)
    yield a
    last = getZ(n)
    while True:
        a = IncIZPauliArray(a)
        yield a
        if a == last:
            break

def getArrayPauliStrings(bitArrays):
    #l = bitArrays.copy()
    return list(map(getPauliString, bitArrays))

def getArrayPauliArrays(pauliStrings):
    #l = pauliStrings.copy()
    return list(map(getPauliArray, pauliStrings))

