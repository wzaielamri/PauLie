LOWCASE = "_"
SIZE = "s"
GATES = {"I", "X", "Y", "Z"}
TOKENS = GATES.copy()
TOKENS.add(LOWCASE)
TOKENS.add(SIZE)

def _is_token(char: str)->bool:
    return char in TOKENS

def _is_number(char: str)->bool:
    try:
        i = int(char)
        return True
    except Exception:
        if char not in TOKENS:
            raise Exception("Invalid pauli string")
        return False

def _to_int(position: str)->int:
    try:
        return int(position)
    except Exception:
        raise Exception("Invalid pauli string")


def pauli_string_parser(pauli_string:str)->str:
    new_pauli_string = ""
    i = 0
    is_last = False
    size = None
    try:
       index = pauli_string.find("s")
       if index == len(pauli_string) - 1:
            raise Exception("Invalid pauli string")
       size_string = pauli_string[index+1:]
       size = _to_int(size_string)
       pauli_string = pauli_string[0:index]
    except Exception:
       pass
    while i < len(pauli_string):
        if pauli_string[i] not in GATES or is_last:
            raise Exception("Invalid pauli string")

        token = pauli_string[i]
        if i < len(pauli_string) - 2 and pauli_string[i+1] == LOWCASE:
            m = i
            i += 2
            p = ""
            while i < len(pauli_string):
                if _is_token(pauli_string[i]):
                   break
                if _is_number(pauli_string[i]):
                   p += pauli_string[i]
                   i += 1
            position = _to_int(p)
            if position - len(new_pauli_string) - 1 < 0: 
                raise Exception("Invalid pauli string")
            token = "" + "".join(["I" for i in range(position - len(new_pauli_string) - 1)]) + pauli_string[m]
        else:
            i += 1
        new_pauli_string += token
    if size is not None:
        if size < len(new_pauli_string):
            raise Exception("Invalid pauli string")
        size -= len(new_pauli_string)
        new_pauli_string += "".join(["I" for i in range(size)])
    return new_pauli_string 
