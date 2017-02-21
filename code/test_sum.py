def sum_of_number(a,b):
    c = a + b
    return c


d = sum_of_number(4,9)
print d 


def test_sum_of_number():
    assert sum_of_number(9,1) == 10