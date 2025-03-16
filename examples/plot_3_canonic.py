from paulie.application.plot import plot_anti_commutation_graph
from paulie.common.pauli_string_factory import get_pauli_string as p 


if __name__ == "__main__":
    plot_anti_commutation_graph(p(["XYI", "IXY", "XZY", "YIX", "YXZ", "ZYX"]))
    plot_anti_commutation_graph(p(["XYI", "IXY", "XZY"]))




