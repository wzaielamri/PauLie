from paulie_classify.common.algebras import *
from paulie_classify.stuff.recording import *
from paulie_classify.stuff.drawing import *
from paulie_classify.common.extKlocal import *

if __name__ == '__main__':
    record = RecordGraph()
    nodes = []
    for node in genKlocalAlgebraGenerators(4, "a6"):
        nodes.append(node)
        recordingGraph(record, nodes)

    animationGraph(record)

