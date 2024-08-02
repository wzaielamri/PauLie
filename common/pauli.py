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
#    print(f"nest {nest} {getPauliString(p)}")
    for aString in list(nest):
        a = getPauliArray(aString)
        if isCommutate(a, p) is False:
            c = multiPauliArrays(a, p)
            cString = getPauliString(c)
#            print(f"{aString} * {getPauliString(p)} = {cString}")
            if cString not in nest:
                nest.add(cString)
                nest_commutator(nest, c)
    return nest

def generateCommutator(aString, b):
    return nest_commutator({aString}, b)


def generatorIBase(n, pauliString):
    np = n - len(pauliString)
    k = 0
    aGates = getPauliArray(pauliString)
    while(k <= np):
       left = setIString(k)
       left.extend(aGates)
       right = setIString(np-k)
       left.extend(right)
       k = k + 1
       yield left

def generatorAllCommutators(n, arrayGeneratorString):
    for pauliString in arrayGeneratorString:
        yield from generatorIBase(n, pauliString)

def generatorAllPauliStrings(n):
    pauliArray = setIString(n)
    yield pauliArray
    lastPauliArray = getAllOne(n)
    while True:
        pauliArray = IncPauliArray(pauliArray)
        yield pauliArray
        if pauliArray == lastPauliArray:
            break


def isIZString(a):
    i = 0
    size = len(a)
    while(i < size):
        if a[i] != 0:
            return False
        i += 2
    return True

def generatorAllIZPauliString(n):
    pauliArray = setIString(n)
    yield pauliArray
    lastPauliArray = getAllZ(n)
    while True:
        pauliArray = IncIZPauliArray(pauliArray)
        yield pauliArray
        if pauliArray == lastPauliArray:
            break
 

def getAllCommutators(n, arrayGeneratorString):
    commutators = []
    for commutator in generatorAllCommutators(n, arrayGeneratorString):
         commutators.append(commutator)
    return commutators

def generatorSecondAllCommutators(n, arrayGeneratorString):
    for pauliString in arrayGeneratorString:
        yield from generatorIBase(n, pauliString)

def generatorAllBase(n, pauliString):
    np = n - len(pauliString)
    k = 0
    aGates = getPauliArray(pauliString)
    while(k <= np):
        left = setIString(k)
        left_one = getAllOne(k)
        full_left = left == left_one
        right = setIString(np-k)
        right_one = getAllOne(np-k)
        isFinish = False  
        while isFinish is False:
             gen = setIString(0)
             gen.extend(left)
             gen.extend(aGates)
             gen.extend(right)
             if right == right_one:
                 if left == left_one:
                     isFinish = True
                 else:  
                     left = IncPauliArray(left)
             else:
                right = IncPauliArray(right)

             yield gen, k
             
        k = k + 1

def replaceGetes(pos, pauliArray, pauliString):
    pArray = pauliArray.copy()
    aGates = getPauliArray(pauliString)
    pos *= 2
    for bit in aGates:
        pArray[pos] = bit
        pos += 1
    return pArray

def isInArray(a, b, position=0):

    pos = a.find(b, position)
    # print(f" pos {pos}")
    if pos > -1:
        if pos % 2 == 0:
            return True
        else:    
            return isInArray(a, b, position=pos+1)
    return False

def getEdgesInArray(a, arrayEdges):
    #if index >= len(arrayEdges):
    #    return []
    edges = []
    for edge_index in range(0, len(arrayEdges)):
        edge = list(arrayEdges[edge_index])
        #print(f"condidat {edge}")
        # b1 = replaceGetes(pos, a, edge[0])
        b1 = getPauliArray(edge[0])
        if isInArray(a, b1):
            #print(f"condidat 1 {edge[0]}")
            #if isIncluded(b1, arrayEdges, index) is False:
            edges.append([edge[0], edge[1]])
        else:
            #b2 = replaceGetes(pos, a, edge[1])
            b2 = getPauliArray(edge[1])
            if isInArray(a, b2):
                #print(f"condidat 2 {edge[1]}")
                # if isIncluded(b2, arrayEdges, index) is False:
                edges.append([edge[1], edge[0]])

    return edges



def isIncluded(a, arrayEdges, index):
    for edge_index in range(0, index):
        edge = list(arrayEdges[edge_index])
        b1 = getPauliArray(edge[0])
        if isInArray(a, b1):
            return True
        else:
            b2 = getPauliArray(edge[1])
            if isInArray(a, b2):
                return True
    return False

def isNodeIncluded(n, pauliString, arrayEdges, index, node, start, item, pair):
    # 
    if start == item:
        return True
    if pauliString == node:
        if start > item:
            return True
        else:
            return False
    if pauliString in arrayEdges[index]:
        if pair > item:
            return True
        else:
            return False
    if n > 3:
        return True
    if n == 2:
        for edge_index in range(0, index):
            edge = list(arrayEdges[edge_index])
            if pauliString == edge[0] or pauliString == edge[1]:
                return True
    if n == 3:
        for edge_index in range(0, index):
            edge = list(arrayEdges[edge_index])
            if edge[0].find(pauliString[1]) == 0 or edge[1].find(pauliString[1]) == 0:
                return True
            if edge[0].find(pauliString[0]) == 1 or edge[1].find(pauliString[0]) == 1:
                return True
       
    return False    

def findInArray(a, b, position = 0):
    pos = a.find(b, position)
    if pos == -1:
        return -1
    if pos % 2 == 0:
        return pos
    return  findInArray(a, b, position = pos+1)

def castExtention(a, edge):
    ext = []
    l_edge = list(edge)
    b1 = getPauliArray(l_edge[0])
    #b2 = getPauliArray(l_edge[1])
    pos = findInArray(a, b1)
    #print(f"pos = {pos//2} of {l_edge[0]} in {getPauliString(a)}")
    while(pos >= 0):
        
        b2 = replaceGetes(pos//2, a, l_edge[1])
        ext.append(getPauliString(b2))
        pos = findInArray(a, b1, position = pos+1)
    return ext

def cmpPauliArrays(pos, current, pauliArray, node):
    if current == pauliArray:
        return 0
    posInArra = findInArray(pauliArray, node)
    if posInArra < pos:
        return -1
    if posInArra > pos:
        return 1
    II = setIString(2)
    c = replaceGetes(pos, current, "II")
    p = replaceGetes(pos, pauliArray, "II")
    if  p < c:
        return -1
    return 1



class CoordinationInTree:
    def __init__(self):
        self.level = bitarray(1)
        self.position = bitarray(1)
    
    def incBitArray(self, bitarr):
        size = len(bitarr)
        bitOne = bitarray(size)
        bitOne.setall(1)
        if bitOne == bitarr:
            bitarr = bitarray(size + 1)
            bitarr[0] = 1
            return bitarr

        n = size - 1
        stop = False
        while stop is not True:
           if bitarr[n] == 0:
               bitarr[n] = 1
               break
           if bitarr[n] == 1:
               bitarr[n] = 0
               n = n - 1
        return bitarr
 

    def incLevel(self):
        self.level = incBitArray(self.level)
        self.position = bitarray(1)

    def incPosition(self):
        self.position = incBitArray(self.position)

    def getLevel(self):
        return self.level

    def getPosition(self):
        return self.position

    def cmpWidth(self, coord):
        if coord.getLevel() == self.getLevel() and coord.getPosition() == self.getPosition():
            return 0
        if coord.getLevel() == self.getLevel():
           if coord.getPosition() > self.getPosition():
               return 1
           else: 
              return -1
        if coord.getLevel() > self.getLevel():
            return 1
        else:
            return -1

#    def cmpDepth(self, coord):
#        if coord.getLevel() == self.getLevel() and coord.getPosition() == self.getPosition():
#            return 0
#        if coord.getPosition() == self.getPosition():
#           if coord.getLevel() < self.getLevel():
#               return 1
#           else:
#               return -1

#        if coord.getPosition() > self.getPosition():
#            return 1
#        else:
#            return -1





