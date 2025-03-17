import pytest
from paulie.application.classify import get_algebra
from paulie.common.pauli_string_factory import get_pauli_string as p

def test_classification():
    """Test algebra classification equivalence for different generator sets."""
    # Define the two sets of generators to be compared
    generators_set1 = p(["XY", "XZ"])
    generators_set2 = p(["IX", "XY"])
    
    # Get the algebra classifications
    algebra1 = get_algebra(generators_set1)
    algebra2 = get_algebra(generators_set2)
    
    # Assert that they represent the same algebra
    assert algebra1 == algebra2, f"Expected equal algebras, but got {algebra1} and {algebra2}"

@pytest.mark.parametrize("generators1, generators2, should_equal", [
    (["XY", "XZ"], ["IX", "XY"], True),
    # Add more test cases here as needed
])
def test_multiple_algebra_equivalences(generators1, generators2, should_equal):
    """Test multiple cases of algebra classifications using parametrization."""
    algebra1 = get_algebra(p(generators1))
    algebra2 = get_algebra(p(generators2))
    
    if should_equal:
        assert algebra1 == algebra2, f"Expected {generators1} and {generators2} to represent the same algebra"
    else:
        assert algebra1 != algebra2, f"Expected {generators1} and {generators2} to represent different algebras"