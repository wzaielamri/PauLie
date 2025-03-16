from paulie.common.pauli_string_parser import pauli_string_parser

if __name__ == "__main__":
    print(f"X_4s10 = {pauli_string_parser('X_4s10')}")
    print(f"ZYX_4s10 = {pauli_string_parser('ZYX_4s10')}")
    print(f"Z_10 = {pauli_string_parser('Z_10')}")
    print(f"Y_3Z_10 = {pauli_string_parser('Y_3Z_10')}")
    print(f"s3 = {pauli_string_parser('s3')}")
    print(f"Z_1s5 = {pauli_string_parser('Z_1s5')}")
    print(f"Z_3s5 = {pauli_string_parser('Z_3s5')}")
    print(f"YZ_3X_5s6 = {pauli_string_parser('YZ_3X_5s6')}")
    print(f"YZ_15 = {pauli_string_parser('YZ_15')}")
    print(f"Y_2Z_15 = {pauli_string_parser('Y_2Z_15')}")