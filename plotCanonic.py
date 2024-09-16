from common.pauli import *
from common.generator import *
from classifier.transform import *
from classifier.graphView import *
from classifier.drawing import *
from classifier.recording import *


def buildAndPlot(nodes):
    canonics = transformToCanonics(nodes)
    nodes = mergeCanonics(canonics)
    vertices, edges, edge_labels =  getGraphView(nodes)
    plotGraph(vertices, edges, edge_labels)


generators = getAllCommutators(8, getAlgebra("a6"))
buildAndPlot(generators)






