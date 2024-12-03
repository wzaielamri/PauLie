from paulie_classify.common.extKlocal import *
from paulie_classify.classifier.transform import *
from paulie_classify.graphs.graphView import *
from paulie_classify.stuff.drawing import *


def buildAndPlot(nodes):
    canonics = transformToCanonics(nodes)
    nodes = mergeCanonics(canonics)
    vertices, edges, edge_labels =  getGraphView(nodes)
    plotGraph(vertices, edges, edge_labels)


if __name__ == '__main__':
    generators = getKlocalGenerators(5, ["XYI", "IXY", "YIX"])
    buildAndPlot(generators)






