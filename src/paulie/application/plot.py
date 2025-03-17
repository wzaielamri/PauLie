from paulie.helpers.drawing import plot_graph
from paulie.common.pauli_string_collection import PauliStringCollection


# Plot anti-commutation graph after tranform graph to canonic
# generators - list of generators
def plot_anti_commutation_graph(generators:PauliStringCollection):
    vertices, edges, edge_labels =  generators.get_canonic_graph()
    plot_graph(vertices, edges, edge_labels)
