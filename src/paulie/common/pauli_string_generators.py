from paulie.common.pauli_string import PauliString
from paulie.common.all_pauli_strings import get_all_pauli_strings
import networkx as nx
from itertools import combinations
from paulie.classifier.classification import Classification
from paulie.classifier.morph_factory import MorphFactory

class PauliStringGenerators:
    def __init__(self, generators:list[PauliString]=[]):
        self.nextpos = 0
        self.generators = []
        self.classification = None
        if len(generators) == 0:
            return

        longest = len(max(generators, key=len))

        for g in generators:
            if len(g) < longest:
                g = g.expand(longest)
            self.generators.append(g)

    def get(self)->list[PauliString]:
        return self.generators

    def __str__(self) -> str:
        """Convert PauliStringGenerator to readable string (e.g., "XYZI, YYYS")"""
        return ",".join([str(g) for g in self.generators])
    
    def __len__(self) -> int:
        return len(self.generators)

    def __iter__(self):
        self.nextpos = 0
        return self

    def __next__(self):
        if self.nextpos >= len(self):
            # we are done
            raise StopIteration
        value = self.generators[self.nextpos].copy()
        self.nextpos += 1
        return value

    def __delitem__(self, key):
        self.classification = None
        del self.generators[key]

    def __copy__(self):
        return PauliStringGenerators(self.generators)

    def copy(self):
        return PauliStringGenerators(self.generators)
    
    def __add__(self, p: PauliString): 
        self.classification = None
        new_generators = []
        for g in self.generators:
            new_generators.append(g + p)
        return PauliStringGenerators(new_generators)

    def mul(self, a, b):
        self.classification = None
        new_generators = []
        for ga in a.generators:
            for gb in b.generators:
                new_generators.append(ga + gb)
        return PauliStringGenerators(new_generators)

    def __mul__(self, other):
        #self*p
        return self.mul(self, other)

    def __rmul__(self, other):
        #p*self
        return self.mul(other, self)

    def expand(self, n: int):
        self.classification = None
        new_generators = []
        for g in enumerate(self.generators):
            g = g.expand(n)
        self.generators = new_generators

    def _processing(self, p: PauliString):
        if len(self.generators) == 0:
            return p
        longest = len(max(self.generators, key=len))
        if len(p) < longest:
            p = p.expand(longest)
        elif len(p) > longest:
            self.expand(len(p))
        return p

    def append(self, p: PauliString):
        self.classification = None
        p = self._processing(p)
        if p not in self.generators:
            self.generators.append(p)

    def insert(self, i: int, p: PauliString):
        self.classification = None
        p = self._processing(p)
        if p not in self.generators:
            self.generators.insert(i, p)

    def remove(self, p: PauliString):
        self.classification = None
        if p in self.generators:
            self.generators.remove(p)

    def index(self, p: PauliString):
        return self.generators.index(p)
    
    def get_size(self):
        return 0 if len(self.generators) == 0 else len(self.generators[0])

    def create_instance(self, n: int = None, pauli_str: str = None):
        if len(self.generators) == 0:
            raise Exception("Empty generator")
        return self.generators[0].create_instance(n=n, pauli_str=pauli_str)
 
    def sort(self):
        self.generators.sort()

    def get_commutants(self, generators=None):
        if generators is None:
            generators = get_all_pauli_strings(self.get_size())
#        return PauliStringGenerators([g for g, gen in combinations (generators, self.generators) if all(gen.commutes_with(g))])
        return PauliStringGenerators([self.create_instance(pauli_str=g) for g in generators if all(gen.commutes_with(g) for gen in self.generators)])

    def get_graph(self, generators: list["PauliStringGenerators"]=[]):
        vertices = []
        edge_labels = {}
        edges = []
        for a in self.generators:
            vertices.append(str(a))
            for b in self.generators:
                if a < b:
                    if not a.commutes_with(b):
                        c = a.adjoint_map(b)
                        if len(generators) == 0 or c in generators:
                            edges.append((str(a), str(b)))
                            edge_labels[(str(a), str(b))] = str(c)
        return vertices, edges, edge_labels

    def _convert(self, generators: list[str])->"PauliStringGenerators":
        return PauliStringGenerators([self.create_instance(pauli_str=g) for g in generators])

    def get_subgraphs(self):
        vertices, edges, _ = self.get_graph()

        g = nx.Graph()
        g.add_nodes_from(vertices)
        g.add_edges_from(edges)
        return [self._convert(subgaph) for subgaph in sorted(nx.connected_components(g), key=len, reverse=True)]

    def classify(self):
        subgraphs = self.get_subgraphs()
        self.classification = Classification()
        for subgraph in subgraphs:
            morph_factory = MorphFactory()
            self.classification.add(morph_factory.build(subgraph).get_morph())
        return self.classification

    def get_class(self):
        if self.classification is None:
            self.classification = self.classify()
        return self.classification

    def get_dependents(self):
        self.get_class().get_dependents()

    def get_canonic_graph(self):
        classification = self.get_class()
        generators = PauliStringGenerators(classification.get_vertices())
        return generators.get_graph()

    def get_anti_commutates(self, pauli_string, generators = None):
        if generators is None:
            generators = self.generators
        return PauliStringGenerators([g for g in generators if g != pauli_string and not pauli_string.commutes_with(g)])

    def get_commutates(self, pauli_string, generators = None):
        if generators is None:
            generators = self.generators
        return PauliStringGenerators([g for g in generators if g != pauli_string and g.commutes_with(pauli_string)])
 
    def get_max_connected(self):
        if len(self) == 0:
            return None, None
        pauli_string = self.generators[0]
        anti_commutates = self.get_anti_commutates(pauli_string)
        for p in self.generators:
            _anti_commutates = self.get_anti_commutates(p)
            if len(_anti_commutates) > len(anti_commutates):
                pauli_string = p
                anti_commutates = _anti_commutates
        return pauli_string, anti_commutates

 

    def _append_to_queue(self, queue_pauli_strings, pauli_strings):
        for p in pauli_strings:
            if p in queue_pauli_strings:
               pauli_strings.remove(v)
               continue
            anti_commutates = self.get_anti_commutates(p, generators = queue_pauli_strings)
            if len(anti_commutates) == 0:
                continue
            if len(anti_commutates) > 1:
                min_index = len(queue_pauli_strings)
                for anti_commutate in anti_commutates:
                    index = queue_pauli_strings.index(anti_commutate)
                    if index < min_index:
                        min_index = index
                        queue_pauli_strings.insert(min_index + 1, p)
            else:
                queue_pauli_strings.append(p)
            pauli_strings.remove(p)
            return

    def get_queue(self):
        new_generators = self.copy()
        new_generators.sort()
        queue_pauli_strings = PauliStringGenerators()
        pauli_string, anti_commutates = self.get_max_connected()

        new_generators.remove(pauli_string)
        queue_pauli_strings.append(pauli_string)

        for anti_commutate in anti_commutates:
            new_generators.remove(anti_commutate)
            if anti_commutate not in queue_pauli_strings:
                queue_pauli_strings.append(anti_commutate)

        while len(new_generators) > 0:
            self._append_to_queue(queue_pauli_strings, new_generators)
        return queue_pauli_strings





