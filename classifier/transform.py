from common.pauli import *
import queue
from graphs.subgraphs import *
from classifier.shape import *
from stuff.printing import *
from stuff.recording import *
import random

### Return highlighted vertices (connected to the selected vertex)
def getLits(lighting, nodes):
    lits = []
    for node in nodes:
        if node != lighting:
           if isCommutate(lighting, node) is False:
               lits.append(node)
    return lits

### Find a center with maximum connections. And bring back these connections
def findCenterAndLits(nodes):
    center = nodes[0]
    center_lits = []
    for node in nodes:
        lits = getLits(node, nodes)
        if len(lits) > len(center_lits):
            center = node
            center_lits = lits
    return center, center_lits

### Adding the next node according to the principle of having a connection with the previous one. 
### If there are several connected ones, then we insert them after the first one. (To reduce the risk of graph reassembly)
def appendNextNodes(preparedNodes, nodes):
    for node in nodes:
        if node in preparedNodes:
            nodes.remove(node)
            continue

        lits = getLits(node, preparedNodes)
        if len(lits) == 0:
            continue
        if len(lits) > 1:
           min_index = len(preparedNodes)
           for lit in lits:
               index = preparedNodes.index(lit)
               if index < min_index:
                   min_index = index
           preparedNodes.insert(min_index + 1, node)
        else:
            preparedNodes.append(node)
        nodes.remove(node)
        return

### Sorting nodes in order from the center and then by connections.
def prepareNodes(nodes, debug=False):
    nodes = sorted(nodes)
    preparedNodes = []
    center, lits =  findCenterAndLits(nodes)
    printNode(debug, center,"center")
    printNodes(debug, lits, "lits")
    nodes.remove(center)
    preparedNodes.append(center)

    for lit in lits:
        nodes.remove(lit)
        if lit not in preparedNodes:
            preparedNodes.append(lit)

    while len(nodes) > 0:
         appendNextNodes(preparedNodes, nodes)

    return preparedNodes


### Get lits nodes and if possible then append
def getLitsOrAppend(shape, center, lighting, canonic, debug):
    lits = getLits(lighting, canonic)
    if len(lits) != 1:
        return canonic, False, lits

    if lits[0] == center:
        return canonic, shape.appendIsCanonical(lighting, center), lits
    else:
        if shape.isEnd(lits[0]):
            return canonic, shape.appendIsCanonical(lighting, lits[0]), lits
    return canonic, False, lits

### reconstruct cononic graph if there are no connections
def reconstructIfNotConnection(shape, lighting, canonic, debug):
    lits = getLits(lighting, canonic)
    isAttachable = len(lits) > 0

    while isAttachable is False:
        v, lit = shape.popVertix()
        if v is None:
            shape.clearProhibitedsForPop()
            return canonic, False

        canonic.remove(v)
        nodes, isAppended = appendNode(shape, v, canonic, debug)

        if isAppended:
            last = canonic[len(canonic)]
            if isCommutate(lighting, last) is False:
                shape.clearProhibitedsForPop()
                return  canonic, isAttachable
            else:
                self.appendProhibitedsForPop(v)
        else:
            self.appendProhibitedsForPop(v)
        shape.resetProhibited()
        shape.appendIsCanonical(v, lit)

    shape.clearProhibitedsForPop()
    return canonic, isAttachable

### Append to cononic graph
def appendToCanonic(shape, lighting, canonic, debug):

    if len(canonic) == 0:
        canonic.append(lighting)
        return canonic, True

    center = canonic[0]
    if len(canonic) < 2:
        shape.appendIsCanonical(lighting, center)
        canonic.append(lighting)
        return canonic, True

    canonic, isAttachable = reconstructIfNotConnection(shape, lighting, canonic, debug)
    if isAttachable is False:
        return canonic, False

    used = []
    q = queue.Queue()
    q.put(lighting)

    while q.empty() is False:
        lighting = q.get()
        canonic, isAppended, lits = getLitsOrAppend(shape, center, lighting, canonic, debug)
        if isAppended:
            canonic.append(lighting)
            return canonic, True
        for lit in lits:
             contractor = multiPauliArrays(lighting, lit)
             if contractor in canonic:
                 return canonic, True

             if contractor not in used:
                 used.append(contractor)
                 q.put(contractor)

    return canonic, False

### Find untoggleable nodes in lits
def getUnToggleables(lighting, lits, debug):
    if len(lits) == 1:
        return None, None
    for litA in lits:
        contractor = multiPauliArrays(lighting, litA)
        for litB in lits:
             if litB != litA:
                 if isCommutate(contractor, litB) is False:
                     return litA, litB
    return None, None

##@ Deconstruct the canonical graph up to the first connection
def deconstructCanonicUntilConnect(shape, canonic, untoggleableA, untoggleableB, debug=False):
    route = shape.getRouteToEnd(untoggleableA)
    printNodes(debug, route, "route A")
    if len(route) > 1 or len(route) == 0:
        routeB = shape.getRouteToEnd(untoggleableB)
        printNodes(debug, routeB, "route B")
        if len(routeB) != 0 and len(routeB) < len(route) or len(route) == 0:
            route = routeB
    reverseNodes = route[::-1]
    while len(route) > 0:
        v = route[0]
        route.remove(v)
        shape.removeVertix(v)
        canonic.remove(v)
    return reverseNodes


### Reconstruct the canonical graph if there are untoggleable nodes and append
def reconstructAndAppendToToggleable(shape, lighting, canonic, debug):
    printNode(debug, lighting, "reconstruct and append to toggleable")
    lenNodes = len(canonic)
    lits = getLits(lighting, canonic)

    untoggleableA, untoggleableB = getUnToggleables(lighting, lits, debug)
    if untoggleableA is not None:
        printNode(debug, untoggleableA, "untoggleableA")
        printNode(debug, untoggleableB, "untoggleableB")
        deconstructedNodes = deconstructCanonicUntilConnect(shape, canonic, untoggleableA, untoggleableB, debug)
        printNodes(debug, deconstructedNodes, "deconstucted nodes")
        printNodes(debug, canonic, "remain")
        if len(deconstructedNodes) == 0:
            return canonic, False
        canonic, isAppended = appendNode(shape, lighting, canonic, debug)
        if isAppended is False:
            return canonic, False
        mix = True
        for node in deconstructedNodes:
            canonic, isAppended = appendNode(shape, node, canonic, debug)
            if isAppended is False:
                return canonic, False

    if lenNodes < len(canonic):
        return canonic, True
    return canonic, False

def resortNodes(center, nodes, debug):
    new_nodes = []
    random.shuffle(nodes)
    lits = getLits(center, nodes)
    for node in nodes:
        if node in lits:
           new_nodes.append(node)
           nodes.remove(node)
    while len(nodes) > 0:
        for node in nodes:
            lits = getLits(node, new_nodes)
            if len(lits) > 0:
                new_nodes.append(node)
                nodes.remove(node)
                break
    return new_nodes

### Reconfigure the canonical graph and append a node
def reconfingAndAppend(shape, lighting, canonic, debug, record):
    printNode(debug, lighting, "reconfig")
    canonic, isAppended = reconstructAndAppendToToggleable(shape, lighting, canonic, debug)
    if isAppended:
        return canonic, True


    nodes = shape.decreaseLenLine()
    printNodes(debug, nodes, "decreased")
    if len(nodes) > 1:
        center = shape.getCenter()
        #nodes = canonic.copy()
        #nodes.remove(center)
        #shape.reset()
        shape.setProhibitedLine(True)
#        nodes = resortNodes(center, nodes, debug)
        canonic = [center]
        return canonic, False
    else:
        for node in nodes:
            canonic.remove(node)

    mix = False
    for node in nodes:
        if mix is False:
            lits = getLits(lighting, canonic)
            if len(lits) > 0:
                 canonic, isAppended = appendNode(shape, lighting, canonic, debug)
                 mix = True
        canonic, isAppended = appendNode(shape, node, canonic, debug)
        if isAppended is False:
            return canonic, False

    if mix is False:
        canonic, isAppended = appendNode(shape, lighting, canonic, debug)

    return canonic, isAppended


### appending a node to a cononic graph
def appendNode(shape, lighting, canonic, debug=False, record=None):
    printNode(debug, lighting, "append Node")
    if lighting in canonic:
        return canonic, True

    canonic, isAppended = appendToCanonic(shape, lighting, canonic, debug)
    if isAppended is False:
        canonic, isAppended = reconfingAndAppend(shape, lighting, canonic, debug, record)
    
    return canonic, isAppended


### Transform a connected graph to a cononic type
def transformToCanonic(nodes, debug=False, record=None):

    shape = Shape(debug)
    if len(nodes) == 0:
        return shape, nodes

    canonic = []
    nodes = prepareNodes(nodes, debug)
    center = nodes[0]
    shape.setCenter(nodes[0])
    index = 0
    original = nodes.copy()
    original.remove(center)
    #nodes = resortNodes(center, original, debug)
    #nodes.insert(0, center)
    while len(nodes) > 0:
        lighting = nodes[0]
        nodes.remove(lighting)
        isException = False
        try:
            canonic, isAppended = appendNode(shape, lighting, canonic, debug, record)
            if isAppended is False:
                nodes = resortNodes(center, original, debug)
                shape.reset()
                canonic = [center]
        except Exception as ex:
            printNode(debug, lighting, f"exception {ex}")
            nodes = resortNodes(center, original, debug)
            shape.reset()
            canonic = [center]
            isException = True
        recordingGraph(record, canonic)
        if isException:
            printNodes(debug, nodes, f"nodes after exception")

    return shape, canonic

### Split the original graph into connected subgraphs and transform them to a cononical type
def transformToCanonics(nodes, debug=False, record=None):
    subgraphs = getSubgraphs(nodes)
    shapes = []
    canonics = []

    for subgraph in subgraphs:
        shape, canonic = transformToCanonic(subgraph, debug, record)
        canonics.append({"shape": shape, "canonic": canonic})
  
    return canonics

### Merge cononic graphs
def mergeCanonics(canonics):
    nodes = []
    for canonic in canonics:
        for node in canonic["canonic"]:
            nodes.append(node)
    return nodes