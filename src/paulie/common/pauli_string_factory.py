import enum
from paulie.common.np_pauli_string import NPPauliString
from paulie.common.bitarray_pauli_string import BitArrayPauliString
from paulie.common.pauli_string import PauliString
from paulie.common.pauli_string_generators import PauliStringGenerators
from typing import Generator
from paulie.common.algebras import get_lie_algebra

class PauliStringType(enum.Enum):
      NP = 0
      BITARRAY = 1
      PAULIARRAY = 2

class PauliStringFactory:
    def __init__(self, type_string: PauliStringType = PauliStringType.NP):
          self.type_string = type_string


    def set_type(self, type_string: PauliStringType):
        self.type_string = type_string

    def build(self, n: int=None, pauli_str: str=None):
        """
        Initialize a Pauli string
        """
        if self.type_string == PauliStringType.NP:
            return NPPauliString(pauli_str=pauli_str, n=n)
        elif self.type_string == PauliStringType.BITARRAY:
            return BitArrayPauliString(pauli_str=pauli_str,n=n)
        return None


_factory = PauliStringFactory()
def get_factory() -> PauliStringFactory:
    return _factory

def set_factory(type_string: PauliStringType):
    _factory.set_type(type_string)

def get_identity(n: int):
    return _factory.build(n=n)

def get_pauli_string(o, n:int = None):
    if isinstance(o, str):
        return _factory.build(pauli_str=o, n=n)
    if isinstance(o, PauliString):
        return _factory.build(pauli_str=str(o), n=n)
    generators = PauliStringGenerators([_factory.build(pauli_str=p) if isinstance(p, str) else _factory.build(pauli_str=str(p)) for p in o])
    if n is not None:
        return PauliStringGenerators(list(gen_k_local_generators(n, generators.get())))
    return generators



class Used:
    def __init__(self):
        self.clear()

    def clear(self):
        self.used = set()

    def append(self, p: PauliString):
         self.used.add(p)

    def is_used(self, p: PauliString) -> bool:
        return p in self.used

def gen_k_local(n: int, p: PauliString, used:Used=None) -> Generator[list[int], None, None]:
    """Generates k-local Pauli operators."""
    if n < len(p):
        raise ValueError(f"Size must be greater than {len(p)}")

    used = used or Used()
    np = n - len(p)
    for k in range(np + 1):
        left = get_identity(k) + p + get_identity(np - k)
        if used.is_used(left):
            continue

        used.append(left)
        yield left

def gen_k_local_generators(n: int, generators: list[str], used: Used = None) -> Generator[list[int], None, None]:
    """Generates k-local operators for a set of generators."""
    used = used or Used()
    longest = max(generators, key=len)
    for g in generators:
        if isinstance(g, str):
            g = get_pauli_string(pauli_str=g, n = len(longest))
        
        yield from gen_k_local(n, g, used=used)

def commutant(generators: PauliStringGenerators) -> PauliStringGenerators:
    """Returns the commutant of a set of Pauli generators."""
    return PauliStringGenerators([g.copy() for g in gen_all_pauli_strings(generators.get_size()) if all(g.commutes_with(gen)) for gen in generators])



