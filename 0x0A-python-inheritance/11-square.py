#!/usr/bin/python3
"""
a class Square that inherits from Rectangle
(9-rectangle.py). (task based on 10-square.py).
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square with a side length."""

    def __init__(self, size):
        """Initialize a Square instance.

        Args:
            size (int): The side length of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Return a string representation of the square.

        Returns:
            str: The string representation of the square.
        """
        return "[Square] {}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = Square(13)
    print(s)
    print(s.area())
