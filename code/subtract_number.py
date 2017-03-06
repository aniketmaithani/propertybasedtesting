def subtract_number(a,b):
    c = a - b
    return c


d = subtract_number(5,4)
print d

def test_subtract_number():
    output = subtract_number(10,1)
    assert output == 9