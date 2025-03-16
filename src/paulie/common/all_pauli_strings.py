from bitarray import bitarray
from typing import Generator

CODEC = {
    "I": bitarray([0, 0]), 
    "X": bitarray([1, 0]), 
    "Y": bitarray([1, 1]), 
    "Z": bitarray([0, 1]),
}


def inc_pauli(pauli_array: bitarray) -> bitarray:
    """Increments the binary representation of a Pauli array."""
    for i in reversed(range(len(pauli_array))):
        if pauli_array[i] == 0:
            pauli_array[i] = 1
            break
        pauli_array[i] = 0
    return pauli_array

def gen_all_pauli_strings(n: int) -> Generator[list[int], None, None]:
    pauli_string = bitarray(2 * n)
    last = bitarray([1] * (2 * n))

    while pauli_string !=last:
        yield "".join(pauli_string.decode(CODEC))
        inc_pauli(pauli_string)
    yield "".join(pauli_string.decode(CODEC))

def get_all_pauli_strings(n: int):
    return [p for p in  gen_all_pauli_strings(n)]
