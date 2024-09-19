from common.pauli import *

def getGraphView(nodes):
    vertices = []
    edge_labels = {}
    edges = [];
    for nodeA in nodes:
        vertices.append(getPauliString(nodeA))
        for nodeB in nodes:
            if nodeA < nodeB:
                if isCommutate(nodeA, nodeB) is False:
                    edges.append((getPauliString(nodeA), getPauliString(nodeB)))
                    nodeC = multiPauliArrays(nodeA, nodeB)
                    edge_labels[(getPauliString(nodeA), getPauliString(nodeB))] = getPauliString(nodeC)
    return vertices, edges, edge_labels
