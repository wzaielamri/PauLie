from paulie.common.algebras import get_lie_algebra
from paulie.application.animation import animation_anti_commutation_graph
from paulie.common.pauli_string_factory import get_pauli_string as p 


if __name__ == "__main__":
    animation_anti_commutation_graph(
        generators=p(get_lie_algebra("a6"), n=5)
    )
