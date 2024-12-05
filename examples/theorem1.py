from PauLie.common.pauli import *
from PauLie.graphs.graphView import *
from PauLie.stuff.drawing import *

def append(nodes, vertix):
    nodes.append(getPauliArray(vertix))

def remove(nodes, vertix):
    nodes.remove(getPauliArray(vertix))

def plot(nodes):
    vertices, edges, edge_labels =  getGraphView(nodes)
    plotGraph(vertices, edges, edge_labels)

def contract(nodes, lighting, contractor):
    remove(nodes, lighting)
    append(nodes, contractor)

def contractAndPlot(nodes, ligting, contractor):
    contract(nodes, ligting, contractor)
    plot(nodes)

def appendAndPlot(nodes, vertix):
    append(nodes, vertix)
    plot(nodes)


def theorem1():
    nodes = []
    append(nodes, "IYZI")
    append(nodes, "XXII")
    append(nodes, "IIXX")
    append(nodes, "YZII")
    append(nodes, "IIYZ")
    plot(nodes)
    appendAndPlot(nodes, "IXXI")
    contractAndPlot(nodes, "IXXI", "YYXI")
    contractAndPlot(nodes, "YYXI", "YIYI")
    contractAndPlot(nodes, "YIYI", "ZXYI")
    contractAndPlot(nodes, "ZXYI", "ZXZX")
    contractAndPlot(nodes, "ZXZX", "ZZIX")
    contractAndPlot(nodes, "ZZIX", "ZZYY")
    contractAndPlot(nodes, "ZZYY", "XIYY")
    contractAndPlot(nodes, "XIYY", "XYXY")

if __name__ == '__main__':
    theorem1()






