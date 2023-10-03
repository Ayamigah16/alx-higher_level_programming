#!/usr/bin/python3
"""
Rectangle Module
"""


class Rectangle:
    """
    Rectangle class
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle object with a given width and height.
        Default values are set to 0.
        Increments the number_of_instances class attribute.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Retrieves the width of the Rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the Rectangle.

        Args:
            value (int): The width value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the height of the Rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the Rectangle.

        Args:
            value (int): The height value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Computes the area of the Rectangle.

        Returns:
            int: The area of the Rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Computes the perimeter of the Rectangle.

        Returns:
            int: The perimeter of the Rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the Rectangle.

        Returns:
            str: The string representation of the Rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        symbol = str(Rectangle.print_symbol)
        return "\n".join([symbol * self.__width] * self.__height)

    def __repr__(self):
        """
        Returns a string representation of the Rectangle for reproduction.

        Returns:
            str: The string representation of the Rectangle.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Prints a message when an instance of Rectangle is deleted.
        Decrements the number_of_instances class attribute.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
