from common.pauli import *
from common.generator import *
from classifier.transform import *
from graphs.graphView import *
from stuff.drawing import *


def buildAndPlot(nodes):
    canonics = transformToCanonics(nodes)
    nodes = mergeCanonics(canonics)
    vertices, edges, edge_labels =  getGraphView(nodes)
    plotGraph(vertices, edges, edge_labels)


generators = getAllCommutators(4, getAlgebra("a3"))
buildAndPlot(generators)






