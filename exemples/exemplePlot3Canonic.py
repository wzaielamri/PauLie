import sys
sys.path.append('..')

from common.extKlocal import *
from classifier.transform import *
from graphs.graphView import *
from stuff.drawing import *


def buildAndPlot(nodes):
    canonics = transformToCanonics(nodes)
    nodes = mergeCanonics(canonics)
    vertices, edges, edge_labels =  getGraphView(nodes)
    plotGraph(vertices, edges, edge_labels)


if __name__ == '__main__':
    generators = getKlocalGenerators(5, ["XYI", "IXY", "YIX"])
    buildAndPlot(generators)






