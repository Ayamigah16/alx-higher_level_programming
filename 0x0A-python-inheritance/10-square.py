#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Represents a square with a side length."""

    def __init__(self, size):
        """Initialize a Square instance.

        Args:
            size (int): The side length of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Return a string representation of the square.

        Returns:
            str: The string representation of the square.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)

if __name__ == "__main__":
    s = Square(13)
    print(s)
    print(s.area())
