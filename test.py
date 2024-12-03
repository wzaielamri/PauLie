from paulie_classify.common.pauli import *
from paulie_classify import *

if __name__ == '__main__':
    psA = "XXIZYYYZZYYXXZZYYYZZXXIZYYYZZYYXXZZYYY"
    psB = "XZXIZIYZZYYXIXZIYZZYYXIYXXZZYXZXIZIZYZ"

    psC = commutatorPauliString(psA, psB)
    print(f"[{psA}, {psB}] ~ {psC}")



