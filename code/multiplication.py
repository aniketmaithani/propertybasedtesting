def multiply(a, b):
    c = a * b 
    return c 

output = multiply(5,6)
print output

def test_multiply_function():
    output_check = multiply(10,10)
    assert output_check == 1000 