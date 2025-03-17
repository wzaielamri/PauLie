"""
Abstract Pauli String Class
"""
from paulie.common.all_pauli_strings import get_all_pauli_strings
from itertools import combinations


class PauliString:
    """
    Abstract Pauli String Class
    """

    def __init__(self):
        """
        Initialize a Pauli string
        """
        pass

    def create_instance(self, n: int = None, pauli_str: str = None):
        """
           Create a Pauli string instance
           Args:
                n: Pauli string length
                pauli_str: String representation of a Pauli string
           Returns the intensity of a Pauli string
        """

        return None

    
    def __str__(self) -> str:
        """Convert PauliString to readable string (e.g., "XYZI")"""
        return ""
    
    def __eq__(self, other) -> bool:
        """
        Overloading the equality operator of two Pauli strings
        Args:
             other: Comparable Pauli string
        Returns the result of the comparison
        """
        return False

    def __lt__(self, other):
        """
        Overloading < operator of two Pauli strings
        Args:
             other: Comparable Pauli string
        Returns the result of the comparison
        """
        return False
    def __le__(self, other):
        """
        Overloading <= operator of two Pauli strings
        Args:
             other: Comparable Pauli string
        Returns the result of the comparison
        """
        return False

    def __gt__(self, other):
        """
        Overloading > operator of two Pauli strings
        Args:
             other: Comparable Pauli string
        Returns the result of the comparison
        """
        return False
    def __ge__(self, other):
        """
        Overloading >= operator of two Pauli strings
        Args:
             other: Comparable Pauli string
        Returns the result of the comparison
        """
        return False
    def __ne__(self, other):
        """
        Overloading != operator of two Pauli strings
        Args:
             other: Comparable Pauli string
        Returns the result of the comparison
        """
        return False

    def __hash__(self) -> int:
        """Make PauliString hashable so it can be used in sets"""
        return hash(0)
    
    def __len__(self) -> int:
        """
        Pauli string length
        """
        return 0

    def __iter__(self):
        """
        Pauli String Iterator
        """
        return self

    def __next__(self):
        """
        The value of the next position of the Pauli string
        """
        return self

    def __setitem__(self, position: int, pauli_string):
        """
        Set value to position
        """
        self.set_subsystem(position, pauli_string)

    def __getitem__(self, position: int):
        """
        Get values at position
        """
        return self.get_subsystem(position)

    def __copy__(self):
        """
        Pauli string copy operator
        """
        return None

    def copy(self):
        """
        Copy Pauli string
        """
        return None

    def __add__(self, val2): 
        """
        Pauli string addition operator
        """
        return None

    def __or__(self, other)->bool:
        """
        Overloading | operator of two Pauli strings like commutes_with
        """
        return self.commutes_with(other)

    def __xor__(self, other):
        """
        Overloading ^ operator of two Pauli strings like adjoint_map
        """
        return self.adjoint_map(other)

    def __matmul__(self, other):
        """
        Overloading @ operator of two Pauli strings like multiply
        """
        return self.multiply(other)


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

    def set_subsystem(self, position: int, pauli_string):
        """
        Set subsystem value
        """
        pass


    def is_identity(self) -> bool:
        """Check if this Pauli string is the identity"""
        return False
    
    def tensor(self, other: "PauliString") -> "PauliString":
        """Tensor product of this Pauli string with another"""
        return PauliString()

    def multiply(self, other) -> "NPPauliString":
        """
        Proportional multiplication operator of two Pauli strings
        Returns a PauliString proportional to the multiplication 
        """
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
        """
        Pauli string increment operator
        """
        pass


    def expand(self, n: int):
        """
        Increasing the size of the Pauli string
        Args:
            n (int): New Pauli string length
        Returns the Pauli string extension
        """
        pass

    def get_nested(self, generators = None):
        """
        Get nested of Pauli string
        Args:
            generators: Collection of Pauli strings on which nested is searched
                        If not specified, then the search area is all Pauli strings of the same size
        """

        if generators is None:
           generators = get_all_pauli_strings(len(self))
        return [
            (self.create_instance(pauli_str=a), self.create_instance(pauli_str=b))
            for a, b in combinations(generators, 2)
            if a != str(self) and b != str(self) and not self.create_instance(pauli_str=a)|b and self.create_instance(pauli_str=a)^b == self
        ]
                      
    def get_commutants(self, generators = None):
        """
        Get a list of Pauli strings that commute with this string
        Args:
            generators: Collection of Pauli strings on which commutant is searched
                        If not specified, then the search area is all Pauli strings of the same size

        """
        if generators is None:
            generators = get_all_pauli_strings(len(self))

        return [self.create_instance(pauli_str=str(g)) for g in generators if self|g]

    def get_anti_commutants(self, generators = None):
        """
        Get a list of Pauli strings that no-commute with this string
        Args:
            generators: Collection of Pauli strings on which commutant is searched
                        If not specified, then the search area is all Pauli strings of the same size

        """
        if generators is None:
            generators = get_all_pauli_strings(len(self))

        return [self.create_instance(pauli_str=str(g)) for g in generators if not self|g]