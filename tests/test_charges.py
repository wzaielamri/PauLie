import pytest
from paulie.common.algebras import get_lie_algebra
from paulie.application.charges import non_commuting_charges
from paulie.common.pauli_string_factory import get_pauli_string as p

@pytest.mark.parametrize("algebra_name, should_have_charges", [
    ("a8", True),
    ("a9", True),
    # Add more algebras to test as needed
])
def test_algebras_with_non_commuting_charges(algebra_name, should_have_charges):
    """
    Test that specific algebras possess non-commuting charges.
    
    Args:
        algebra_name: The name of the Lie algebra to test
        should_have_charges: Whether the algebra should have non-commuting charges
    """
    # Get the generators for the specified algebra
    generators = p(get_lie_algebra(algebra_name))
    
    # Find non-commuting charges
    charges = non_commuting_charges(generators)
    
    # Check if non-commuting charges exist as expected
    if should_have_charges:
        assert len(charges) > 0, f"Expected {algebra_name} to have non-commuting charges, but found none"
    else:
        assert len(charges) == 0, f"Expected {algebra_name} to have no non-commuting charges, but found {len(charges)}"

def test_a8_specific_charges():
    """Test specific properties of non-commuting charges in the a8 algebra."""
    generators = p(get_lie_algebra("a8"))
    charges = non_commuting_charges(generators)
    
    # Add more specific assertions about the charges if needed
    assert len(charges) > 0, "a8 should have non-commuting charges"
    
def test_a9_specific_charges():
    """Test specific properties of non-commuting charges in the a9 algebra."""
    generators = p(get_lie_algebra("a9"))
    charges = non_commuting_charges(generators)
    
    assert len(charges) > 0, "a9 should have non-commuting charges"
