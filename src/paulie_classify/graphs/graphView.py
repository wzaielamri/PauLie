from paulie_classify.common.pauli import *

def getGraphView(nodes, commutators=[]):
    vertices = []
    edge_labels = {}
    edges = [];
    for nodeA in nodes:
        vertices.append(getPauliString(nodeA))
        for nodeB in nodes:
            if nodeA < nodeB:
                if isCommutate(nodeA, nodeB) is False:
                    nodeC = multiPauliArrays(nodeA, nodeB)
                    if len(commutators) == 0 or nodeC in commutators:
                        edges.append((getPauliString(nodeA), getPauliString(nodeB)))
                        edge_labels[(getPauliString(nodeA), getPauliString(nodeB))] = getPauliString(nodeC)
    return vertices, edges, edge_labels

def getGraphViewByString(nodes, commutators=[]):
    return getGraphView(getArrayPauliArrays(nodes), getArrayPauliArrays(commutators))
