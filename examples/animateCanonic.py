"""
aut.
"""

from PauLie.common.pauli import *
#from common.generator import *
from PauLie.classifier.transform import *
from PauLie.stuff.drawing import *
from PauLie.stuff.recording import *



def buildAndAnimate(nodes):
    record = RecordGraph()
    canonics = transformToCanonics(nodes, record = record, debug=False)
    animationGraph(record)

if __name__ == '__main__':
    generators = getAllCommutators(8, getAlgebra("a6"))
    buildAndAnimate(generators)






