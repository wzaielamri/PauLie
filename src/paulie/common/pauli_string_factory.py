"""Pauli's String Factory. Responsible for creating instances of Pauli strings of various implementations"""
import enum
from paulie.common.np_pauli_string import NPPauliString
from paulie.common.bitarray_pauli_string import BitArrayPauliString
from paulie.common.pauli_string import PauliString
from paulie.common.pauli_string_collection import PauliStringCollection
from typing import Generator


class PauliStringType(enum.Enum):
      """Pauli string implementation types."""
      NP = 0 # numpy implemebtation
      BITARRAY = 1  # bitarray implementation
      PAULIARRAY = 2  # pauliarray implementation


class PauliStringFactory:
    """Pauli's String Factory. Responsible for creating instances of Pauli strings of various implementations"""

    def __init__(self, type_string: PauliStringType = PauliStringType.NP):
        """
        Factory initialization
        """
        self.type_string = type_string

    def set_type(self, type_string: PauliStringType):
        """
        Set Pauli string implementation type
        """
        self.type_string = type_string

    def build(self, n: int=None, pauli_str: str=None):
        """
        Create an instance of a Pauli string of a given implementation
        Args: n - lenght of Pauli string
              pauli_str - string representation of Pauli string
        """
        if self.type_string == PauliStringType.NP:
            return NPPauliString(pauli_str=pauli_str, n=n)
        elif self.type_string == PauliStringType.BITARRAY:
            return BitArrayPauliString(pauli_str=pauli_str,n=n)


"""
Current factory instance
"""
_factory = PauliStringFactory()

def get_factory() -> PauliStringFactory:
    """
    Get the current instance of the factory
    """
    return _factory

def set_factory(type_string: PauliStringType):
    """
    Set Pauli string implementation type
    Args: type_string - Pauli string implementation types
    """

    _factory.set_type(type_string)

def get_identity(n: int):
    """
    Get an identity of a given length
    Args: n - lenght of Pauli string
    returns identity
    """
    return _factory.build(n=n)

def get_pauli_string(o, n:int = None):
    """
    Get Pauli strings in their current representation
    Args: 
         o - a Pauli string or a collection of Pauli strings.
         n - length of Pauli strings
    Returns If o is a Pauli string, then its current instantiation value n is created
    otherwise PauliStringCollection is created - a collection of Pauli strings.
    Given n, the collection is expanded as k-local. Where k is the maximum length of a Pauli string in a given collection
    """
    if isinstance(o, str):
        return _factory.build(pauli_str=o, n=n)
    if isinstance(o, PauliString):
        return _factory.build(pauli_str=str(o), n=n)
    generators = PauliStringCollection([_factory.build(pauli_str=p) if isinstance(p, str) else _factory.build(pauli_str=str(p)) for p in o])
    if n is not None:
        return PauliStringCollection(list(gen_k_local_generators(n, generators.get())))
    return generators


class Used:
    """
    Helper class for monitoring previously created Pauli strings
    """
    def __init__(self):
        self.clear()

    def clear(self):
        """Clear set"""
        self.used = set()

    def append(self, p: PauliString):
        """Append to set
        Args:
            p - Pauli string
        """
        self.used.add(p)

    def is_used(self, p: PauliString) -> bool:
        """Checking a Pauli string in a set"""
        return p in self.used


def gen_k_local(n: int, p: PauliString, used:Used=None) -> Generator[list[int], None, None]:
    """Generates k-local Pauli strings."""
    if n < len(p):
        raise ValueError(f"Size must be greater than {len(p)}")

    used = used or Used()
    n_p = n - len(p)
    for k in range(n_p + 1):
        left = get_identity(k) + p + get_identity(n_p - k)
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
