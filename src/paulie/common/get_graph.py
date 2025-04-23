from itertools import combinations

def get_graph(generators, commutators=[]):
    """
    Get graph
    Args:
        generators: Array of PauliString
        commutators: The area of Pauli strings over which to build a graph. If not specified, then that's it
    Returns the vertices, edges, and labels of edges
    """
    vertices = [str(g) for g in generators]
    edge_labels = {}
    edges = []
    for a, b in combinations(generators, 2):
        c = a^b
        if c and (len(commutators) == 0 or c in commutators):
            edges.append((str(a), str(b)))
            edge_labels[(str(a), str(b))] = str(c)
    return vertices, edges, edge_labels

