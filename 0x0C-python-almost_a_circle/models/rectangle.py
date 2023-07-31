#!/usr/bin/python3
"""
Implements the Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base.

    Attributes:
        __width (int): Private instance attribute
    representing the width of the rectangle.
        __height (int): Private instance attribute
    representing the height of the rectangle.
        __x (int): Private instance attribute
    representing the x-coordinate of the rectangle.
        __y (int): Private instance attribute
    representing the y-coordinate of the rectangle.
        id (int): Public instance attribute
    representing the object's ID.

    Methods:
        __init__(self, width, height, x=0, y=0, id=None):
    Initializes a new instance of the Rectangle class.

    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new instance of the Rectangle class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the
        rectangle. Default is 0.
            y (int, optional): The y-coordinate of the
        rectangle. Default is 0.
            id (int, optional): An integer representing
        the object's id.
       If None, a new id is assigned based on the class
        attribute __nb_objects.

        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        Args:
            value (int): The new width value to set.

        Raises:
            TypeError: If the width is not an integer.
            ValueError: If the width is less than or equal to 0.

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.

        Args:
            value (int): The new height value to set.

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is less than or equal to 0.

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the x-coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x-coordinate of the rectangle.

        Args:
            value (int): The new x-coordinate value to set.

        Raises:
            TypeError: If the x-coordinate is not an integer.
            ValueError: If the x-coordinate is less than 0.

        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the y-coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y-coordinate of the rectangle.

        Args:
            value (int): The new y-coordinate value to set.

        Raises:
            TypeError: If the y-coordinate is not an integer.
            ValueError: If the y-coordinate is less than 0.

        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.

        """
        return self.__width * self.__height

    def display(self):
        """Print the rectangle with the character '#'."""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """Return the string representation of the rectangle.

        Returns:
            str: The string representation of the rectangle.

        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y,
            self.__width, self.__height)