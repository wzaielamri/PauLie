from paulie.common.all_pauli_strings import get_all_pauli_strings
from itertools import combinations


class PauliString:
    def __init__(self, pauli_str: str = ""):
        """
        Initialize a Pauli string
        """
        pass

    def create_instance(self, n: int = None, pauli_str: str = None):
        return None

    @classmethod
    def from_string(cls, pauli_str: str) -> "PauliString":
        """
        Create a PauliString from a string like "IXYZ"
        
        Args:
            pauli_str: String of I, X, Y, Z characters
        """
        return cls()        
    
    def __str__(self) -> str:
        """Convert PauliString to readable string (e.g., "XYZI")"""
        return ""
    
    def __eq__(self, other) -> bool:
        return False

    def __lt__(self, other):
        #<
        return False
    def __le__(self, other):
        #<=
        return False

    def __gt__(self, other):
        #>
        return False
    def __ge__(self, other):
        #>=
        return False
    def __ne__(self, other):
        # != 
        return False

    def __hash__(self) -> int:
        """Make PauliString hashable so it can be used in sets"""
        return hash(0)
    
    def __len__(self) -> int:
        return 0

    def __iter__(self):
        return self

    def __next__(self):
        return self

    def __setitem__(self, position: int, pauli_string):
        self.set_subsystem(position, pauli_string)

    def __getitem__(self, position: int):
        return self.get_subsystem(position)

    def __copy__(self):
        return None

    def copy(self):
        return None

    def __add__(self, val2): 
        return None


    def commutes_with(self, other) -> bool:
        """
        Check if this Pauli string commutes with another
        Returns True if they commute, False if they anticommute
        """
        # Compute symplectic product mod 2
        # Paulis commute iff the symplectic product is 0
        return False
    
    def get_subsystem(self, start: int, length: int = 1) -> "PauliString":
        """Get a subsystem of this Pauli string"""
        return PauliString()
    
    def get_list_subsystem(self, start: int = 0, length: int = 1) -> list["PauliString"]:
        """Get list  subsystem of this Pauli string"""
        return []

    def set_subsystem(self, position: int, pauli_string: "PauliString"):
        pass

    def set_subsystem(self, position: int, pauli_string: str):
        pass

    def is_identity(self) -> bool:
        """Check if this Pauli string is the identity"""
        return False
    
    def tensor(self, other: "PauliString") -> "PauliString":
        """Tensor product of this Pauli string with another"""
        return PauliString()

    def multiply(self, other) -> "NPPauliString":
        return None

    def adjoint_map(self, other) -> "PauliString":
        """
        Compute the adjoint map ad_A(B) = [A,B]
        Returns None if the commutator is zero (i.e., if A and B commute)
        Otherwise returns a PauliString proportional to the commutator
        """
        if self.commutes_with(other):
            return None
        
        # For Pauli strings, if they anticommute, [A,B] = 2AB
        # In the context of generating a Lie algebra, we only care about
        # the result up to a constant factor
        
        # For anticommuting Paulis, the product gives a new Pauli
        # XOR of the bit vectors gives the non-phase part of the product
        
        return PauliString()

    def inc(self):
         pass

    def is_last(self) -> bool:
        for p in self:
            if p != "Y":
                return False
        return True

    def expand(self, n: int):
        pass

    def get_nested(self, generators = None):
        if generators is None:
           generators = get_all_pauli_strings(len(self))
        return [
            (self.create_instance(pauli_str=a), self.create_instance(pauli_str=b))
            for a, b in combinations(generators, 2)
            if a != str(self) and b != str(self) and not self.create_instance(pauli_str=a).commutes_with(b) and self.create_instance(pauli_str=a).adjoint_map(b) == self
        ]
                      
    def get_commutants(self, generators = None):
        if generators is None:
            generators = get_all_pauli_strings(len(self))

        return [self.create_instance(pauli_str=str(g)) for g in generators if self.commutes_with(g)]