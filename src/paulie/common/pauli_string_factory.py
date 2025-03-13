import enum
from paulie.common.np_pauli_string import NPPauliString
from paulie.common.bitarray_pauli_string import BitArrayPauliString

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
            if n is not None:
                return NPPauliString(n=n)
            elif pauli_str is not None:
                return NPPauliString(pauli_str=pauli_str)
        elif self.type_string == PauliStringType.BITARRAY:
            if n is not None:
                return BitArrayPauliString(n=n)
            elif pauli_str is not None:
                return BitArrayPauliString(pauli_str=pauli_str)
        return None


_factory = PauliStringFactory()
def get_factory() -> PauliStringFactory:
    return _factory

def set_factory(type_string: PauliStringType):
    _factory.set_type(type_string)

def get_identity(n: int):
    return _factory.build(n=n)

def get_pauli_string(pauli_str: str):
    return _factory.build(pauli_str=pauli_str)