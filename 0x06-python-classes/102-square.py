#!/usr/bin/python3
class Square:
    """
    This class represents a square.

    Attributes:
        __size (float or int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance.

        Args:
            size (float or int): The size of the square. Default is 0.

        Raises:
            TypeError: If the size is not a number.
            ValueError: If the size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method for the size attribute.

        Returns:
            float or int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.

        Args:
            value (float or int): The size value to set.

        Raises:
            TypeError: If the provided value is not a number.
            ValueError: If the provided value is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            float or int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Equality comparison for squares based on their areas.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the squares have equal areas, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """
        Inequality comparison for squares based on their areas.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the squares have unequal areas, False otherwise.
        """
        return not self.__eq__(other)

    def __gt__(self, other):
        """
        Greater than comparison for squares based on their areas.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the current square has a greater area, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() > other.area()
        return False

    def __ge__(self, other):
        """
        Greater than or equal comparison for squares based on their areas.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the current square has a greater or equal area, False otherwise.
        """
        return self.__gt__(other) or self.__eq__(other)

    def __lt__(self, other):
        """
        Less than comparison for squares based on their areas.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the current square has a smaller area, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() < other.area()
        return False

    def __le__(self, other):
        """
        Less than or equal comparison for squares based on their areas.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the current square has a smaller or equal area, False otherwise.
        """
        return self.__lt__(other) or self.__eq__(other)
