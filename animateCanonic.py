from common.pauli import *
from common.generator import *
from classifier.transform import *
from classifier.graphView import *
from classifier.drawing import *
from classifier.recording import *



def buildAndAnimate(nodes):
    record = RecordGraph()
    canonics = transformToCanonics(nodes, record = record, debug=True)
    animationGraph(record)

generators = getAllCommutators(8, getAlgebra("a9"))
buildAndAnimate(generators)






