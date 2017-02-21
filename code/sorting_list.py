from collections import Counter
from hypothesis import given, strategies as st


def sort_fn(list_type):
    list_type.sort()
    return list_type

#def test_sorting_strings():
#    list_unsorted = [4,1,0,9,7,5]
#    result = sort_fn(list_unsorted)
#    assert isinstance(result, list)
#    assert result == [0,1,4,5,7,9]

@given(st.lists(st.text()))
def test_sorting_strings(strings):
    result = sort_fn(strings)
    assert isinstance(result, list)
    assert Counter(result) == Counter(strings)
    assert all(x <= y for x, y in zip(result, result[1:]))

