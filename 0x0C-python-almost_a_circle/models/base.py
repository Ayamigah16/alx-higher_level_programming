#!/usr/bin/python3
"""
Defines the Base Class
"""


class Base:
    """Base class for managing id attribute."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new instance of the Base class.

        Args:
            id (int): An integer representing the
        object's id. If None, a new id is assigned
        based on the class attribute __nb_objects.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
