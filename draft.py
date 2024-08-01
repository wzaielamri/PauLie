from common.pauli import *
from common.algebras import *
from common.generator import *
from stateEdge import *
import queue
from time import perf_counter


class EdgeStorage:
    def create(self):
        pass

    def add(self, pauliString):
        pass

    def store(self):
        pass

    def getStorage(self):
        pass

    def printSubgroup(self):
        pass

    def initRoute(self):
        pass

    def addToRoute(self, pauliString):
        pass
    
    def printRoute(self):
        pass

    def initMeetingRoute(self):
        pass

    def addToMeetingRoute(self, pauliString):
        pass

    def printMeetingRoute(self):
        pass


class EdgeStorageArray(EdgeStorage):
    def __init__(self):
        self.subgroups = []
        self.route = []
        self.meetingRoute = []
        self.subroute = []

    def create(self):
        self.subgroup = set()

    def add(self, pauliString):
        if pauliString in self.subgroup:
            print(f"dublicate *******{pauliString}**************")
        self.subgroup.add(pauliString)

    def store(self):
        self.subgroups.append(self.subgroup)

    def getStorage(self):
        return self.subgroups

    def printSubgroup(self):
        print(self.subgroup)

    def initRoute(self):
        self.route = []

    def addToRoute(self, pauliString):
        if pauliString in self.route:
            print(f"dublicate *******{pauliString}**************")
        self.route.append(pauliString)
    
    def printRoute(self):
        print(self.route)

    def initSubRoute(self):
        self.subroute = []

    def addToSubRoute(self, pauliString):
        if pauliString in self.subroute:
            print(f"*******{pauliString}**************")
        self.route.append(pauliString)
    
    def printSubRoute(self):
        print(self.route)

    def initMeetingRoute(self):
        self.meetingRoute = []

    def addToMeetingRoute(self, pauliString):
        self.meetingRoute.append(pauliString)

    def printMeetingRoute(self):
        print(self.meetingRoute)

def removeEdge(edges, ex_edge):
    index = -1
    for i, edge in enumerate(edges):
        if ex_edge[0] in edge and ex_edge[1] in edge:
            index = i
            break
    if index > -1:
       del edges[index]
    return edges

def meeting(start, current, previous, source_previous, edges, index, storage):
    storage.addToMeetingRoute(getPauliString(start))
    pp = "none"
    if previous is not None:
        pp = getPauliString(previous)
    print(f"meeting start: {getPauliString(start)} current: {getPauliString(current)} prev: {pp} source_prev: {getPauliString(source_previous)}")

    if source_previous == start:
        if previous is None:
            return True, True
        else:
            return False, False


    if source_previous == current:
        return False, True

    edgs = edges.copy()
 #   print(f"len edges {len(edgs)}")
    pa = getPauliString(current)
    ex_edges = getEdgesInArray(start, edgs)
    print(f"meeting ex_edges {ex_edges}")
    for ex_edge in ex_edges:
        arrExt = castExtention(start, ex_edge)
        edgs = removeEdge(edgs, ex_edge)
        for item in arrExt:
             bitItem = getPauliArray(item)
             print(f"metting item {item}")
             if start == getPauliArray(item):
                 continue 
             # if source_previous  == bitItem and previous is None:


             if pa == item and previous is not None and previous != source_previous:
#                 print("meet")
                 return False, True
             if pa == item and previous is not None and previous == source_previous:
                 print("cont meet")
                 return True, True
#             print(f"===============")
             isMeeting, isBreak = meeting(bitItem, current, start, source_previous, edgs, index, storage)
             if isBreak:
#                 print("meet")
                 return isMeeting, True
#    print("not meet")
    return False, False

def positionInRoute(start, current, edges, pos, storage):
    print(f"find position start: {getPauliString(start)} current: {getPauliString(current)} pos: {pos}")
    storage.addToMeetingRoute(getPauliString(start))
    if start == current:
        return pos, True
    edgs = edges.copy()
    ex_edges = getEdgesInArray(start, edgs)
    print(f"position ex {ex_edges}")
    for ex_edge in ex_edges:
        arrExt = castExtention(start, ex_edge)
        edgs = removeEdge(edgs, ex_edge)
        for item in arrExt:
            bitItem = getPauliArray(item)
            if bitItem == start:
               continue
            pos += 1
            pos, isFound = positionInRoute(bitItem, current, edgs, pos, storage)
            if isFound:
                return pos, isFound
    return pos, False

def getEdgesIn(n, start, a, edges, full_edges, index, storage, numb, state, node, b, routelen):
    #if node in state:
    #    return numb, False
    storage.addToRoute(getPauliString(a))
    edgs = edges.copy()
    #print(f"{edges}")
    # del edgs[index]
    isInc = False
    ex_edges = getEdgesInArray(a, edgs)
    print(f"build {getPauliString(a)}")
    print(f"parent ex_edges {ex_edges}")
    #print(f"a = {getPauliString(a)} {index}")
    #print(f"ex_edges {ex_edges}")
    for ex_edge in ex_edges:
        arrExt = castExtention(a, ex_edge)
        print(f"items {arrExt}")
        for item in arrExt:
            print(f"item {item}")
            bitItem = getPauliArray(item)
            if bitItem == start or bitItem == a:
               continue
            if isNodeIncluded(n, ex_edge[1], full_edges, index, node, start, bitItem, b):
                isInc = True
                break
            # print(f"is meeting {isMeeting}")
            # if isMeeting is False:
            #    continue


#            print(f"before len edges {len(edges)}")
            edgs = removeEdge(edgs, ex_edge)
#            print(f"after len edges {len(edges)}")
            #svnumb = numb + 1
            storage.initSubRoute()
            routelen += 1
            numb, isInc, routelen = getEdgesIn(n, start, bitItem, edgs, full_edges, index, storage, numb, state, ex_edge[1], b, routelen)
            print(f"numb {numb} routelen {routelen} is inc {isInc}")
            if isInc:
                break
            storage.initMeetingRoute()
            pos, isFound = positionInRoute(start, bitItem, full_edges, 0, storage)
            print("--subroute---")
            storage.printSubRoute()

            print(f"position {pos} numb {numb} is found {isFound}")
            # isMeeting, isBreak = meeting(start, bitItem, None, a, full_edges, index, storage)
            storage.printMeetingRoute()

            storage.add(item)
            storage.addToSubRoute(item)
            state.add(item)
            numb += 1
    #print(f"f numb = {numb}")
    return numb, isInc, routelen



def buildSubgraph(pauliArray, edges, index, storage):
    number = 1
    current = pauliArray
    isBuild = False
    while isBuild is False:
        isBuild = True

    return number

def generatorLevelEdges(current, edges, level):
    print(f"generator {getPauliString(current)}")
    currentLevel = 0
    ex_edges = getEdgesInArray(current, edges)
    for ex_edge in ex_edges:
        ext_pauliStrings = castExtention(current, ex_edge)
        for pauliString in ext_pauliStrings:
            pauliArray = getPauliArray(pauliString)
            print(f"generator level {level} {getPauliString(pauliArray)}")

            if level == 0:
                yield pauliArray
            else: 
                yield from generatorLevelEdges(pauliArray, edges, level-1)
    yield None


def createPairString(pos, pauliArray, pauliNodeArray):
    pArray = pauliArray.copy()
    #pos *= 2
    for bit in pauliNodeArray:
        pArray[pos] = bit
        pos += 1
    return pArray

def generatorPauliString (a, node, pair_node):
    pos = findInArray(a, node)
    while(pos >= 0):
        svpos = pos
        pos = findInArray(a, node, position = pos+1)
        yield createPairString(svpos, a, pair_node)

def generatorPauliStringFromEdges (a, edges):
    for edge in edges:
        yield from generatorPauliString(a, edge[0], edge[1])

######################################################################
## Depth
######################################################################

def generatorEdges(a, arrayEdges):
    for edge_index in range(0, len(arrayEdges)):
        edge = list(arrayEdges[edge_index])
        b1 = getPauliArray(edge[0])
        if isInArray(a, b1):
            #print(f"condidat 1 {edge[0]}")
            #if isIncluded(b1, arrayEdges, index) is False:
            yield from generatorPauliString (a, b1, getPauliArray(edge[1])) 
        else:
            b2 = getPauliArray(edge[1])
            if isInArray(a, b2):
                yield from generatorPauliString (a, b2, getPauliArray(edge[0])) 

def generatorNodeEdges(a, arrayEdges):
    for edge_index in range(0, len(arrayEdges)):
        edge = list(arrayEdges[edge_index])
        b1 = getPauliArray(edge[0])
        if isInArray(a, b1):
            #print(f"condidat 1 {edge[0]}")
            #if isIncluded(b1, arrayEdges, index) is False:
            yield b1, getPauliArray(edge[1]) 
        else:
            b2 = getPauliArray(edge[1])
            if isInArray(a, b2):
                yield b2, getPauliArray(edge[0]) 

class ACCIndex:
    def __init__(self):
        self.index = 0
    def inc(self):
        self.index += 1
    def getIndex(self):
        return self.index

def generatorNodesEdge(current, edges, level, parent, start, index: ACCIndex):
    if level > -1:
       # print(f"current {getPauliString(current)} level {level + 1}")
       for pauliArray in generatorEdges(current, edges):
           if pauliArray == current or pauliArray == start or pauliArray == parent:
              continue
           position = findNode(start, edges, pauliArray, level)
           if position < index.getIndex():
               continue
           # print(f"{getPauliString(pauliArray)} position {position} index {index.getIndex()}")
           index.inc()
           yield pauliArray
           yield from generatorNodesEdge(pauliArray, edges, level - 1, current, start, index)

def generatorFindNodesEdge(current, edges, level, parent, start):
    if level > -1:
       for pauliArray in generatorEdges(current, edges):
           if pauliArray == current or pauliArray == start or pauliArray == parent:
              continue
           yield pauliArray
           yield from generatorFindNodesEdge(pauliArray, edges, level - 1, current, start)

def findNode(current, edges, necessary, level):
    position = 0
    for pauliArray in generatorFindNodesEdge(current, edges, level, current, current):
        #print(f"find {getPauliString(pauliArray)} position {position}")
        if pauliArray == necessary:
            return position
        position += 1
    return -1




###################################################################################
########    
###################################################################################




############################################################################################
def isIncludedInOtherSubgraph(n, current, pos, edges, level, index):
    print(f"*****************************************")

    print(f"test include {getPauliString(current)}")

    for pauliArray in generatorNodesEdge(current, edges, level, current, current, ACCIndex()):
        print(f"{getPauliString(pauliArray)}")

        if isIncluded(pauliArray, edges, index):
            return True


#        for i in range(0, index): 
#            l_edge = list(edges[i])
#            a = getPauliArray(l_edge[0])
#            b = getPauliArray(l_edge[1])
            # print(f"find < index a {getPauliString(a)} {} {getPauliString(b)}")

#            if findInArray(pauliArray, a) > -1 or findInArray(pauliArray, b) > -1:
#                return True

        l_edge = list(edges[index])
        a = getPauliArray(l_edge[0])
        if findInArray(pauliArray, a) > -1:
            if cmpPauliArrays(pos, current, pauliArray, a) < 0:
            #if pauliArray < current:
                print(f"current {getPauliString(pauliArray)} < {getPauliString(current)}")
                return True
        b = getPauliArray(l_edge[1])
        pair = replaceGetes(pos, current, l_edge[1])
        if findInArray(pauliArray, b) > -1:
            if cmpPauliArrays(pos, pair, pauliArray, b) < 0:
#            if pauliArray < pair:
                print(f"pair {getPauliString(pauliArray)} < {getPauliString(pair)}")
                print(f"pair {pauliArray}")
                print(f"current {pair}")

                return True


    return False      

def buildTree(nameAlgebra, n, storage = EdgeStorage()):
    edges = generateEdgeByAlgebraName(getAlgebras(), nameAlgebra)
    print(f"edges algebra = {edges}")
    print(f"len edges algebra = {len(edges)}")
    sizesOfSubgraph = {}
    for index, edge in enumerate(edges):
        # if index != 1:
        #     continue
        l_edge = list(edge)
        a = l_edge[0]
        b = l_edge[1]
        # a = "XZ"
        for current, pos in generatorAllBase(n, a):

            if isIncluded(current, edges, index):
               continue
            pair = replaceGetes(pos, current, b)
            if isIncluded(pair, edges, index):
               continue

            if isIncludedInOtherSubgraph(n, current, pos, edges, 4**n, index):
                continue
            numb = 1
            level = 0
            maxLevel = 2
            storage.create()
            storage.initRoute()
            storage.add(getPauliString(current))

            for pa in generatorNodesEdge(current, edges, 4**n, current, current, ACCIndex()):
                numb += 1
                print(f"{getPauliString(pa)}")
                storage.add(getPauliString(pa))

            storage.printRoute()
            storage.store()
            if numb in sizesOfSubgraph.keys():
                sizesOfSubgraph[numb] += 1
            else:
                sizesOfSubgraph[numb] = 1


#            while level < maxLevel:
#                for pauliArray in generatorLevelEdges(current, edges, level):
#                    if pauliArray is not None:
#                        print(getPauliString(pauliArray))
#                        if pauliArray == current:
#                            continue
#                        storage.add(getPauliString(pauliArray))
                
#                level += 1
#                storage.store()
#                storage.initRoute()

        print(f"######################################################################")
        print(f"edge {getPauliString(current)}")

    linked = 0
    for tot in sizesOfSubgraph.keys():
        linked += sizesOfSubgraph[tot] * tot
    one = 4**n - linked
    sizesOfSubgraph[1] = one
    return sizesOfSubgraph

#store = EdgeStorageArray()
#sizes = buildTree("a12", 3, store)
#store = sorted(store.getStorage(), key=len, reverse=True)
#print(f"{store}")
#print(f"{sizes}")
#subgraphs = stateGraph("a12", 3)
#print(f"subgraphs {subgraphs}")
######################################
###  Graph by commutator
#####################################


def geteratorNodeByComutators(n, pauliArray, comutators):
    I = setIString(n)
    q = queue.Queue()
    q.put(pauliArray)
    ql = queue.Queue()
    store = {getPauliString(pauliArray)}
    while q.empty() is False:
        current = q.get()
        # print(f"current {getPauliString(current)}")
        for comutator in comutators:
            next = multiPauliArrays(comutator, current)
            if next != I and getPauliString(next) not in store: # and next not in comutators:
               # print(f"{getPauliString(current)} * {getPauliString(comutator)} next {getPauliString(next)}")
               store.add(getPauliString(next))
               q.put(next)
               yield next

def isIncludedInOther(n, current, pos, edges, index, comutators):

    for pauliArray in geteratorNodeByComutators(n, current, comutators):
        if isIncluded(pauliArray, edges, index):
            return True
        l_edge = list(edges[index])
        a = getPauliArray(l_edge[0])
        if findInArray(pauliArray, a) > -1:
            if cmpPauliArrays(pos, current, pauliArray, a) < 0:
            #if pauliArray < current:
                return True
        b = getPauliArray(l_edge[1])
        pair = replaceGetes(pos, current, l_edge[1])
        if findInArray(pauliArray, b) > -1:
            if cmpPauliArrays(pos, pair, pauliArray, b) < 0:
#            if pauliArray < pair:
                return True

    return False      
   
def buildCommutatorTree(nameAlgebra, n, storage = EdgeStorage()):
    edges = generateEdgeByAlgebraName(getAlgebras(), nameAlgebra)
    comutators = getAllComutators(n, getAlgebra(nameAlgebra))
    for com in comutators:
        print(f"{getPauliString(com)}")
    print(f"edges algebra = {edges}")
    print(f"len edges algebra = {len(edges)}")
    sizesOfSubgraph = {}
    for index, edge in enumerate(edges):
        #if index != 0:
        #    continue
        l_edge = list(edge)
        a = l_edge[0]
        b = l_edge[1]
        #a = "XY"
        #b = "IZ"
        for current, pos in generatorAllBase(n, a):

            if isIncluded(current, edges, index):
               continue
            pair = replaceGetes(pos, current, b)
            if isIncluded(pair, edges, index):
               continue

            if isIncludedInOther(n, current, pos, edges, index, comutators):
                continue
 

#            print(f"build nodes by {getPauliString(current)}")
            numb = 1
            level = 0
            maxLevel = 2
            storage.create()
            storage.initRoute()
            storage.add(getPauliString(current))

#            print("*****comutators********")

            for pa in geteratorNodeByComutators(n, current, comutators):
                numb += 1
#                print(f"pa {getPauliString(pa)}")
                storage.add(getPauliString(pa))

#            for pa in generatorNodesEdge(current, edges, 4**n, current, current, ACCIndex()):
#                numb += 1
#                print(f"{getPauliString(pa)}")
#                storage.add(getPauliString(pa))

            storage.printSubgroup()
            storage.store()
            if numb in sizesOfSubgraph.keys():
                sizesOfSubgraph[numb] += 1
            else:
                sizesOfSubgraph[numb] = 1


#            while level < maxLevel:
#                for pauliArray in generatorLevelEdges(current, edges, level):
#                    if pauliArray is not None:
#                        print(getPauliString(pauliArray))
#                        if pauliArray == current:
#                            continue
#                        storage.add(getPauliString(pauliArray))
                
#                level += 1
#                storage.store()
#                storage.initRoute()

#        print(f"######################################################################")
#        print(f"edge {getPauliString(current)}")

    linked = 0
    for tot in sizesOfSubgraph.keys():
        linked += sizesOfSubgraph[tot] * tot
    one = 4**n - linked
    sizesOfSubgraph[1] = one
    return sizesOfSubgraph


def compareStateAndDyn(states, dyns):
    for index, state in enumerate(states):
        if len(dyns) > index:
            for item in state:
                index_dyn = -1
                for dyn in dyns:
                    if item in dyn:
                       index_dyn = 0
                if index_dyn == -1:
                   print(f"lost {item}")


store = EdgeStorageArray()
start_time = perf_counter()
sizes = buildCommutatorTree("a0", 3)
store = sorted(store.getStorage(), key=len, reverse=True)
print(f"{store}")
end_time = perf_counter()
print(f'time excexution {end_time - start_time: 0.4f} sec.')
print(f"{sizes}")
start_time = perf_counter()

subgraphs = stateGraph("a0", 3)
# print(f"subgraphs {subgraphs}")
end_time = perf_counter()
print(f'time excexution graph {end_time - start_time: 0.4f} sec.')

# compareStateAndDyn(subgraphs, store)


#generatorNodesEdge

#store = sorted(store.getStorage(), key=len, reverse=True)
#print(f"connected sizes {sizes}")



def buildSubgraphs(nameAlgebra, n, storage = EdgeStorage()):
    edges = generateEdgeByAlgebraName(getAlgebras(), nameAlgebra)
    print(f"edges algebra = {edges}")
    print(f"len edges algebra = {len(edges)}")
    # subgroups = []
    sizesOfSubgraph = {}
    for index, edge in enumerate(edges):
        print(f"######################################################################")
        print(f"edge {edge}")
        l_edge = list(edge)
        a = l_edge[0]
        b = l_edge[1]
        for gen, pos in generatorAllBase(n, a):
            a_g = gen
            b_g = replaceGetes(pos, a_g, b)
            storage.create()
            numb = 0
            if isIncluded(a_g, edges, index) or isIncluded(b_g, edges, index):
                continue
            storage.add(getPauliString(a_g))
            # storage.add(getPauliString(b_g))
            numb += 1
            state = set()
            print(f"*****************")
            storage.initRoute()
            subnumb, isInc, routelen = getEdgesIn(n, a_g, a_g, edges, edges, index, storage, 0, state, l_edge[0], b_g, 0)
            if isInc:
                continue
            numb +=  subnumb
            print(f"----a nodes ---")
            storage.printRoute()
#            print(f"---------------")
#            storage.initRoute()
#            subnumb, isInc = getEdgesIn(n, b_g, b_g, edges, edges, index, storage, 0, state, l_edge[1])
#            if isInc:
#                continue
#            numb +=  subnumb
#            print(f"----b nodes ---")
#            storage.printRoute()
            #print(f"2 numb = {numb}")
            storage.store()
            if numb in sizesOfSubgraph.keys():
                sizesOfSubgraph[numb] += 1
            else:
                sizesOfSubgraph[numb] = 1
    linked = 0
    for tot in sizesOfSubgraph.keys():
        linked += sizesOfSubgraph[tot] * tot
    one = 4**n - linked
    sizesOfSubgraph[1] = one
    return sizesOfSubgraph

#store = EdgeStorageArray()
#sizes = buildSubgraphs("a12", 2, store)
#store = sorted(store.getStorage(), key=len, reverse=True)
#print(f"{store}")
#print(f"connected sizes {sizes}")

#subgraphs = stateGraph("a12", 2)
#print(f"subgraphs {subgraphs}")