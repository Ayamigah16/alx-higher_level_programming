#!/usr/bin/python3
"""a class MyInt that inherits from int:"""


class MyInt(int):
    """Class that inherits from int and inverts == and != operators."""

    def __eq__(self, other):
        """Invert the == operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Invert the != operator."""
        return super().__eq__(other)


if __name__ == "__main__":
    my_i = MyInt(3)
    print(my_i)
    print(my_i == 3)
    print(my_i != 3)
