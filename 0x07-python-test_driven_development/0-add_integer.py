#!/usr/bin/python3

def add_integer(a, b=98):
    """ Integer addition module
    Args:
        a: first integer
        b: secodn integer

    Raise:
        TypeError: if a or b are not int or float

    Returns:
        sum of a and b
    """
    if not type(a) is (int, float):
        raise TypeError('a must be an integer')
    if not type(b) is (int, float):
        raise TypeError('b must be an integer')

    return a + b


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
