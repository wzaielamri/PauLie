"""
Implementation of a Pauli string on numpy
"""

import numpy as np
from paulie.common.pauli_string import PauliString
from paulie.common.pauli_string_parser import pauli_string_parser

class NPPauliString(PauliString):
    """
    Implementation of a Pauli string on numpy
    """

    def __init__(self, x_comp: np.ndarray = None, z_comp: np.ndarray = None, n: int = None, pauli_str: str = None):
        """
        Initialize a Pauli string with X and Z components
        
        Args:
            x_comp: Binary array indicating X/Y positions (1 = present)
            z_comp: Binary array indicating Z/Y positions (1 = present)
            n: Pauli string length
            pauli_str: String representation of a Pauli string
        """
        super().__init__()
        self.nextpos = 0
        if x_comp is not None and z_comp is not None:
            self.x = np.array(x_comp, dtype=np.int8)
            self.z = np.array(z_comp, dtype=np.int8)
            assert len(self.x) == len(self.z), "X and Z components must have the same length"
        elif n is not None and pauli_str is None:
           self.x = np.zeros(n, dtype=np.int8)
           self.z = np.zeros(n, dtype=np.int8)
        elif pauli_str is not None:
           pauli_str = pauli_string_parser(pauli_str) 
           if n is None:
               n = len(pauli_str)

           self.x = np.zeros(n, dtype=np.int8)
           self.z = np.zeros(n, dtype=np.int8)
        
           for i, char in enumerate(pauli_str):
               if char == "X":
                   self.x[i] = 1
               elif char == "Z":
                   self.z[i] = 1
               elif char == "Y":
                   self.x[i] = 1
                   self.z[i] = 1
               elif char == "I":
                   pass  # Both components remain 0
               else:
                   raise ValueError(f"Invalid Pauli character: {char}")


        else:
             raise ValueError(f"Invalid Pauli character: {char}")

    def create_instance(self, n: int = None, pauli_str: str = None):
        """
           Create a Pauli string instance
           Args:
                n: Pauli string length
                pauli_str: String representation of a Pauli string
           Returns the intensity of a Pauli string
        """
        return NPPauliString(n=n, pauli_str=pauli_str)
   
    def __str__(self) -> str:
        """Convert PauliString to readable string (e.g., "XYZI")"""
        result = []
        for x_bit, z_bit in zip(self.x, self.z):
            if x_bit == 0 and z_bit == 0:
                result.append("I")
            elif x_bit == 1 and z_bit == 0:
                result.append("X")
            elif x_bit == 0 and z_bit == 1:
                result.append("Z")
            else:  # x_bit == 1 and z_bit == 1
                result.append("Y")
        return "".join(result)
    
    def __eq__(self, other) -> bool:
        """
        Overloading the equality operator of two Pauli strings
        Args:
             other: Comparable Pauli string
        Returns the result of the comparison
        """
        if isinstance(other, str):
            other = NPPauliString(pauli_str=other)
        if not isinstance(other, NPPauliString):
            return False
        return np.array_equal(self.x, other.x) and np.array_equal(self.z, other.z)

    def __lt__(self, other):
        """
        Overloading < operator of two Pauli strings
        Args:
             other: Comparable Pauli string
        Returns the result of the comparison
        """
        if isinstance(other, str):
            other = NPPauliString(pauli_str=other)
        if not isinstance(other, NPPauliString):
            return False
        if len(self) != len(other):
            return  len(self) < len(other)
        if len(self) == 0:
            return False

        order = ["I", "Z", "X", "Y"]
        for o in zip(self, other):
            i_self = order.index(str(o[0]))  
            i_other = order.index(str(o[1]))
            if i_self != i_other:
                return  i_self < i_other
        return False

    def __le__(self, other):
        """
        Overloading <= operator of two Pauli strings
        Args:
             other: Comparable Pauli string
        Returns the result of the comparison
        """
        if isinstance(other, str):
            other = NPPauliString(pauli_str=other)
        if not isinstance(other, NPPauliString):
            return False
        if len(self) != len(other):
            return  len(self) < len(other)
        if len(self) == 0:
            return True

        order = ["I", "Z", "X", "Y"]
        for o in zip(self, other):
            i_self = order.index(str(o[0]))  
            i_other = order.index(str(o[1]))
            if i_self != i_other:
                return  i_self < i_other
        return True

    def __gt__(self, other):
        """
        Overloading > operator of two Pauli strings
        Args:
             other: Comparable Pauli string
        Returns the result of the comparison
        """
        return not self <= other

    def __ge__(self, other):
        """
        Overloading >= operator of two Pauli strings
        Args:
             other: Comparable Pauli string
        Returns the result of the comparison
        """
        return not self < other

    def __ne__(self, other):
        """
        Overloading != operator of two Pauli strings
        Args:
             other: Comparable Pauli string
        Returns the result of the comparison
        """
        return not self == other

   
    def __hash__(self) -> int:
        """Make PauliString hashable so it can be used in sets"""
        x_tuple = tuple(self.x)
        z_tuple = tuple(self.z)
        return hash((x_tuple, z_tuple))
    
    def __len__(self) -> int:
        """
        Pauli string length
        """
        return len(self.x)

    def __iter__(self):
        """
        Pauli String Iterator
        """
        self.nextpos = 0
        return self

    def __next__(self):
        """
        The value of the next position of the Pauli string
        """
        if self.nextpos >= len(self):
            # we are done
            raise StopIteration
        value = NPPauliString(x_comp=self.x[self.nextpos:self.nextpos+1], z_comp=self.z[self.nextpos:self.nextpos+1])
        self.nextpos += 1
        return value

    def __copy__(self):
        """
        Pauli string copy operator
        """
        return NPPauliString(x_comp=self.x, z_comp=self.z)

    def copy(self):
        """
        Copy Pauli string
        """
        return NPPauliString(x_comp=self.x, z_comp=self.z)
    
    def __add__(self, other): 
        """
        Pauli string addition operator
        """
        if isinstance(other, str):
            other = NPPauliString(pauli_str=other)
        return self.tensor(other)


    def commutes_with(self, other) -> bool:
        """
        Check if this Pauli string commutes with another
        Returns True if they commute, False if they anticommute
        """
        # Compute symplectic product mod 2
        # Paulis commute iff the symplectic product is 0
        if isinstance(other, str):
            other = NPPauliString(pauli_str=other)

        dot1 = np.sum(self.x * other.z) % 2
        dot2 = np.sum(self.z * other.x) % 2

        return True if (dot1 + dot2) % 2 == 0 else False
    
    def get_subsystem(self, start: int, length: int = 1) -> "NPPauliString":
        """Get a subsystem of this Pauli string"""
        return NPPauliString(x_comp=self.x[start:start+length], z_comp=self.z[start:start+length])

    def get_list_subsystem(self, start: int = 0, length: int = 1) -> list[PauliString]:
        """Get a list of Pauli string subsystems"""
        return [self.get_subsystem(i, length) for i in range(0, len(self), length)]

    def set_subsystem(self, position: int, pauli_string):
        """
        Set subsystem value
        """
        if isinstance(pauli_string, str):
            pauli_string = NPPauliString(pauli_str=pauli_string)

        for i in range(0, len(pauli_string)):
            self.x[position + i] = pauli_string.x[i]
            self.z[position + i] = pauli_string.z[i]

    def is_identity(self) -> bool:
        """Check if this Pauli string is the identity"""
        return np.all(self.x == 0) and np.all(self.z == 0)
    
    def tensor(self, other: "NPPauliString") -> "NPPauliString":
        """Tensor product of this Pauli string with another"""
        x_new = np.concatenate((self.x, other.x))
        z_new = np.concatenate((self.z, other.z))
        return NPPauliString(x_comp=x_new, z_comp=z_new)

    def multiply(self, other) -> "NPPauliString":
        """
        Proportional multiplication operator of two Pauli strings
        Returns a PauliString proportional to the multiplication 
        """
        if isinstance(other, str):
            other = NPPauliString(pauli_str=other)

        result_x = (self.x + other.x) % 2
        result_z = (self.z + other.z) % 2
        
        return NPPauliString(x_comp=result_x, z_comp=result_z)

    def adjoint_map(self, other) -> "NPPauliString":
        """
        Compute the adjoint map ad_A(B) = [A,B]
        Returns None if the commutator is zero (i.e., if A and B commute)
        Otherwise returns a PauliString proportional to the commutator
        """
        if isinstance(other, str):
            other = NPPauliString(pauli_str=other)

        if self.commutes_with(other):
            return None
        
        # For Pauli strings, if they anticommute, [A,B] = 2AB
        # In the context of generating a Lie algebra, we only care about
        # the result up to a constant factor
        
        # For anticommuting Paulis, the product gives a new Pauli
        # XOR of the bit vectors gives the non-phase part of the product
        result_x = (self.x + other.x) % 2
        result_z = (self.z + other.z) % 2
        
        return NPPauliString(x_comp=result_x, z_comp=result_z)

    def inc(self):
        """
        Pauli string increment operator
        """
        for i in reversed(range(len(self))):
            if self.z[i] == 0:
                self.z[i] = 1
                break
            else:
                self.z[i] = 0

            if self.x[i] == 0:
                self.x[i] = 1
                break
            else:
                self.x[i] = 0

    def expand(self, n: int):
        """
        Increasing the size of the Pauli string
        Args:
            n (int): New Pauli string length
        Returns the Pauli string extension
        """
        return self + NPPauliString(n = n - len(self))

