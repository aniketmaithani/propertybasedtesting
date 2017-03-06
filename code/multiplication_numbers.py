def multiply(a,b):
    c = a * b
    return c 


output = multiply(5,5)
print output

def test_multiply():
    test_output = multiply(10,10)
    assert test_output == 1900 