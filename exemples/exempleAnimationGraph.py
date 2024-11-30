import sys
sys.path.append('..')

from common.algebras import *
from stuff.recording import *
from stuff.drawing import *
from common.extKlocal import *

record = RecordGraph()
nodes = []
for node in genKlocalAlgebraGenerators(4, "a6"):
    nodes.append(node)
    recordingGraph(record, nodes)

animationGraph(record)

