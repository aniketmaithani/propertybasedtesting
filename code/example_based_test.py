def welcome_to_pydelhi():
    print_output = "PyDehli Conf 2017"
    return print_output

c = welcome_to_pydelhi()
print c


def test_welcome_to_pydelhi():
    output = welcome_to_pydelhi()
    print output
    assert output == "PyDehli Conf 2017"