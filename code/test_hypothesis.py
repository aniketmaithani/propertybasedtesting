from hypothesis import given
import hypothesis.strategies as st

def sum_and_associativity(a,b):
    c = a + b
    return c

@given(st.integers(), st.integers())
def test_ints_are_commutative(x, y):
    assert x + y == y + x

@given(x=st.integers(), y=st.integers())
def test_ints_cancel(x, y):
    assert (x + y) - y == x


