import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation
from PauLie.helpers.recording import *
from PauLie.graphs.graphView import *
from PauLie.common.pauli import *

### plotting graph
def plotGraph(vertices, edges, edge_labels = None):
   graph = nx.Graph()
   graph.add_nodes_from(vertices)
   graph.add_edges_from(edges)
   fig, ax = plt.subplots(figsize=(6,4))
   pos = nx.spring_layout(graph)
   if edge_labels is not None:
       nx.draw_networkx_edge_labels(graph, pos=pos, edge_labels=edge_labels,font_color='red')
   nx.draw_networkx(graph, pos=pos)
   plt.show()

def plotGraphByNodes(nodes, commutators=[]):
    v,e,l = getGraphView(nodes, commutators)
    return plotGraph(v,e,l)

def plotGraphByStringNodes(nodes, commutators=[]):
    v,e,l = getGraphView(getArrayPauliArrays(nodes), getArrayPauliArrays(commutators))
    return plotGraph(v,e,l)

### animating graph record
def animationGraph(record: RecordGraph, interval=1000, repeat=False, storage=None):
   graph = nx.Graph()
   fig, ax = plt.subplots(figsize=(6,4))
   def clear():
       ax.clear()
       graph.remove_nodes_from(list(n for n in graph.nodes)) 

   def update(num):
       clear()
       vertices, edges, edge_labels = record.getFrame(num).getGraph()
       graph.add_nodes_from(vertices)
       graph.add_edges_from(edges)
       pos = nx.spring_layout(graph)
       if edge_labels is not None:
           nx.draw_networkx_edge_labels(graph, pos=pos, edge_labels=edge_labels,font_color='red')
       return nx.draw_networkx(graph, pos=pos)


   ani = matplotlib.animation.FuncAnimation(fig, update, frames=record.getSize(), interval=interval, repeat=repeat)
   if storage is not None:
       ani.save(filename=storage["filename"], writer=storage["writer"])
#       ani.save(filename=storage["filename"], writer="pillow")
   plt.show()
   #ani.save(filename="data/example.html", writer="html")

