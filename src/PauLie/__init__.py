from PauLie.common.extKlocal import *
from PauLie.classifier.transform import *
from PauLie.graphs.graphView import *
from PauLie.helpers.drawing import *
from PauLie.helpers.recording import *

#Partial function for constructing a canonical graph
# generators - list of generators
# size - Generator extensions to size size
# debug - debbuging
# record - recording 
def _trasformToCanonics(generators, size = 0, debug=False, record=None):
    bytGenerators = []
    if size == 0:
        bitGenerators = getArrayPauliArrays(generators)
    else:
        bitGenerators = getKlocalGenerators(size, generators)

    return transformToCanonics(bitGenerators, debug, record)

# Get algebra
# generators - list of generators
# size - Generator extensions to size size
def getAlgebra(generators, size=0):
    canonics = _trasformToCanonics(generators, size=size)
    algebras = [];
    for canonic in canonics:
        algebras.append(canonic["shape"].getAlgebra())
    return " + ".join(algebras)

# Plot anti-commutation graph after tranform graph to canonic
# generators - list of generators
# size - Generator extensions to size size
def plotAntiCommutationGraph(generators, size=0):
    canonics = _trasformToCanonics(generators, size=size)
    nodes = mergeCanonics(canonics)
    vertices, edges, edge_labels =  getGraphView(nodes)
    plotGraph(vertices, edges, edge_labels)

# Animation building transformation anti-commutation graph
# generators - list of generators
# size - Generator extensions to size size
def animationAntiCommutationGraph(generators, size=0):
    record = RecordGraph()
    canonics = _trasformToCanonics(generators, size=size, record = record)
    animationGraph(record)

