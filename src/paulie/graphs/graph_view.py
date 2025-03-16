from paulie.common.pauli_string_generators import PauliStringGenerators


def get_graph_view(vertices: PauliStringGenerators, commutators:list[PauliStringGenerators]=[]):
    vertices = []
    edge_labels = {}
    edges = []
    for a in vertices:
        vertices.append(str(a))
        for b in nodes:
            if a < b:
                if a.commutes_with(b) is False:
                    c = nodeA.adjoint_map(b)
                    if len(commutators) == 0 or c in commutators:
                        edges.append((str(a), str(b)))
                        edge_labels[(str(a), str(b))] = str(c)
    return vertices, edges, edge_labels


