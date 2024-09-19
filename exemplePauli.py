from common.pauli import *

psA = "XXIZYYYZZYYXXZZYYYZZXXIZYYYZZYYXXZZYYY"
psB = "XZXIZIYZZYYXIXZIYZZYYXIYXXZZYXZXIZIZYZ"


psC = commutatorPauliString(psA, psB)

print(f"[{psA}, {psB}] ~ {psC}")