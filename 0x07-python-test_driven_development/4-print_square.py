#!/usr/bin/python3

def print_square(size):
    """
    Prints a square of '#' characters.

    Parameters:
    size (int): The size length of the square.

    Raises:
    TypeError: If size is not an integer or if size is a float.
    ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()

# Uncomment the following lines to run the provided test cases
# print_square(4)
# print("")
# print_square(10)
# print("")
# print_square(0)
# print("")
# print_square(1)
# print("")
# try:
#     print_square(-1)
# except Exception as e:
#     print(e)
