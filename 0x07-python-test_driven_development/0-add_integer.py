#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Adds two integers.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number (default is 98).

    Returns:
    int: The addition of a and b.
    
    Raises:
    TypeError: If a or b is not an integer or float.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)

# Uncomment the following line to run the provided test cases
# print(add_integer(1, 2))
# print(add_integer(100, -2))
# print(add_integer(2))
# print(add_integer(100.3, -2))
# print(add_integer(4, "School"))
# print(add_integer(None))
