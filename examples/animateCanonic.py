"""
aut.
"""

from paulie_classify.common.pauli import *
#from common.generator import *
from paulie_classify.classifier.transform import *
from paulie_classify.stuff.drawing import *
from paulie_classify.stuff.recording import *



def buildAndAnimate(nodes):
    record = RecordGraph()
    canonics = transformToCanonics(nodes, record = record, debug=False)
    animationGraph(record)

if __name__ == '__main__':
    generators = getAllCommutators(8, getAlgebra("a6"))
    buildAndAnimate(generators)






