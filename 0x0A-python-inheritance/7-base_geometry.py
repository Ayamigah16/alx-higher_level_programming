#!/usr/bin/python3
"""
a class BaseGeometry (based on 6-base_geometry.py).
"""


class BaseGeometry:
    """An empty class representing BaseGeometry."""

    def area(self):
        """Raises an exception with a message indicating area() is
        not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that the value is an integer and greater than 0.

        Args:
            name (str): The name of the value.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
