#!/usr/bin/python3
"""Defines the Square class."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle.

    Attributes:
        size (int): Private instance attribute
    representing the size of the square.
        x (int): Private instance attribute
    representing the x-coordinate of the square.
        y (int): Private instance attribute
    representing the y-coordinate of the square.
        id (int): Public instance attribute
    representing the object's ID.

    Methods:
        __init__(self, size, x=0, y=0, id=None):
    Initializes a new instance of the Square class.
        __str__(self): Returns a string representation
    of the square.
        size(self): Getter method for the size attribute.
        size(self, value): Setter method for the size
    attribute.

    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new instance of the Square class.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate of
        the square. Defaults to 0.
            y (int, optional): The y-coordinate of
        the square. Defaults to 0.
            id (int, optional): The object's ID.
        Defaults to None.

        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter method for the size attribute."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter method for the size attribute.

        Args:
            value (int): The value to set the size.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.

        """
        self.width = value
        self.height = value

    def __str__(self):
        """Return the string representation of the square.

        Returns:
            str: The string representation of the square.

        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
