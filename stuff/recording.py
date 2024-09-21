from graphs.graphView import *
from common.pauli import *

class FrameGraph:
      ### constructor 
      def __init__(self, vertices, edges, edge_labels = None):
          self.vertices = vertices
          self.edges = edges
          self.edge_labels = edge_labels

      ### 
      def getGraph(self):
          return self.vertices, self.edges, self.edge_labels

class RecordGraph: 
     def __init__(self):
         self.frames: FrameGraph = []

     def appendFrame(self, frame: FrameGraph):
         self.frames.append(frame)

     def append(self, vertices, edges, edge_labels = None):
         self.appendFrame(FrameGraph(vertices, edges, edge_labels))

     def getFrame(self, index):
         if index > len(self.frames) - 1:
            return FrameGraph(["None"], None)
         return self.frames[index]

     def clear(self):
         self.frames = []

     def getSize(self):
         return len(self.frames)

def recordingGraph(record:RecordGraph, nodes):
    if record is None:
        return
    vertices, edges, edge_labels = getGraphView(nodes)
    record.append(vertices, edges, edge_labels)


def recordingGraphString(record:RecordGraph, nodes):
    if record is None:
        return
    vertices, edges, edge_labels = getGraphView(getArrayPauliArrays(nodes))
    record.append(vertices, edges, edge_labels)
