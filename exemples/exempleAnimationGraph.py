import sys
sys.path.append('..')

from common.algebras import *
from stuff.recording import *
from stuff.drawing import *
from common.ext2local import *

record = RecordGraph()
nodes = []
for node in gen2localAlgebraGenerators(4, "a6"):
    nodes.append(node)
    recordingGraph(record, nodes)

animationGraph(record)

