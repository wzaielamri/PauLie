import sys
sys.path.append('..')

from common.pauli import *

if __name__ == '__main__':
    psA = "XXIZYYYZZYYXXZZYYYZZXXIZYYYZZYYXXZZYYY"
    psB = "XZXIZIYZZYYXIXZIYZZYYXIYXXZZYXZXIZIZYZ"

    psC = commutatorPauliString(psA, psB)
    print(f"[{psA}, {psB}] ~ {psC}")