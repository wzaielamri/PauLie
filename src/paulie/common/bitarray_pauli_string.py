from bitarray import bitarray
from paulie.common.pauli_string import PauliString

CODEC = {
    "I": bitarray([0, 0]), 
    "X": bitarray([1, 0]), 
    "Y": bitarray([1, 1]), 
    "Z": bitarray([0, 1]),
}

class BitArrayPauliString(PauliString):
    def __init__(self, n: int = None, pauli_str: str = None, bits: bitarray = None):
        """
        Initialize a Pauli string with X and Z components
        
        Args:
            x_comp: Binary array indicating X/Y positions (1 = present)
            z_comp: Binary array indicating Z/Y positions (1 = present)
        """
        super().__init__()
        self.nextpos = 0
        if bits is not None:
           self.bits = bits.copy()
        elif n is not None:
           self.bits = bitarray(2 * n)
        elif pauli_str is not None:
             self.bits = bitarray()
             self.bits.encode(CODEC, pauli_str)


   
    def __str__(self) -> str:
        """Convert PauliString to readable string (e.g., "XYZI")"""
        return "".join(self.bits.decode(CODEC))
    
    def __eq__(self, other) -> bool:
        if isinstance(other, str):
            other = BitArrayPauliString(pauli_str=other)
        if not isinstance(other, BitArrayPauliString):
            return False
        return self.bits == other.bits

   
    def __hash__(self) -> int:
        """Make PauliString hashable so it can be used in sets"""
        return hash(str(self.bits))
    
    def __len__(self) -> int:
        return len(self.bits) // 2

    def __iter__(self):
        self.nextpos = 0
        return self

    def __next__(self):
        if self.nextpos >= len(self):
            # we are done
            raise StopIteration
        value = BitArrayPauliString(bits=self.bits[2*self.nextpos:2*self.nextpos+2])
        self.nextpos += 1
        return value
    
    def commutes_with(self, other: "BitArrayPauliString") -> bool:
        """
        Check if this Pauli string commutes with another
        Returns True if they commute, False if they anticommute
        """
        # Compute symplectic product mod 2
        # Paulis commute iff the symplectic product is 0
        if len(self) != len(other):
            raise ValueError("Pauli arrays must be of equal length")
        return sum(self.bits[i] & other.bits[i + 1] for i in range(0, len(self.bits), 2)) % 2 == sum(self.bits[i + 1] & other.bits[i] for i in range(0, len(self.bits), 2)) % 2
      
    def get_subsystem(self, start: int, length: int = 1) -> "BitArrayPauliString":
        """Get a subsystem of this Pauli string"""
        return BitArrayPauliString(bits=self.bits[2*start:2*start+2*length])

    def get_list_subsystem(self, start: int = 0, length: int = 1) -> list[PauliString]:
        return [self.get_subsystem(i, length) for i in range(0, len(self), length)]

    def set_subsystem(self, position: int, pauli_string):
        if isinstance(pauli_string, str):
            pauli_string = BitArrayPauliString(pauli_str=pauli_string)

        for i in range(0, len(pauli_string)):
            self.bits[2*position + 2*i] = pauli_string.bits[2*i]
            self.bits[2*position + 2*i + 1] = pauli_string.bits[2*i + 1]

    def is_identity(self) -> bool:
        """Check if this Pauli string is the identity"""
        return bitarray(len(self.bits)) == self.bits
    
    def tensor(self, other: "BitArrayPauliString") -> "BitArrayPauliString":
        """Tensor product of this Pauli string with another"""
        new_bits = bitarray(len(self.bits) + len(other.bits))
        for i in range(len(new_bits)):
            s = self.bits if i < len(self.bits) else other.bits
            j = i if i < len(self.bits) else i - len(self.bits)
            new_bits[i] = s[j]

        return BitArrayPauliString(bits=new_bits)
    
    def adjoint_map(self, other: "BitArrayPauliString") -> "BitArrayPauliString":
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
        if len(self.bits) != len(other.bits):
            raise ValueError("Pauli arrays must have the same length")
        return BitArrayPauliString(bits = self.bits ^ other.bits)  # Bitwise XOR is equivalent to mod-2 addition



