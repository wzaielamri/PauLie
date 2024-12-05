from PauLie.common.algebras import *
from PauLie.stuff.recording import *
from PauLie.stuff.drawing import *
from PauLie.common.extKlocal import *

if __name__ == '__main__':
    record = RecordGraph()
    nodes = []
    for node in genKlocalAlgebraGenerators(4, "a6"):
        nodes.append(node)
        recordingGraph(record, nodes)

    animationGraph(record)

