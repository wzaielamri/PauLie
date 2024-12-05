from PauLie.common.pauli import *
#from common.generator import *
from PauLie.classifier.transform import *
from PauLie.graphs.graphView import *
from PauLie.stuff.drawing import *


def buildAndPlot(nodes):
    canonics = transformToCanonics(nodes)
    nodes = mergeCanonics(canonics)
    vertices, edges, edge_labels =  getGraphView(nodes)
    plotGraph(vertices, edges, edge_labels)


if __name__ == '__main__':
    generators = getAllCommutators(6, getAlgebra("a3"))
    buildAndPlot(generators)






