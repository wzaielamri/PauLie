from paulie.common.pauli_string_factory import get_pauli_string as p 

nested = p("IX").get_nested()
print("nested for IX")
for a,b in nested:
    print(f"({a}, {b})")
