#!/usr/bin/python3
"""
function that returns True if the object is an instance of, or if the
object is an instance of a class that inherited from
the specified class ; otherwise False
"""


def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of, or if it is an instance of a class
    that inherited from, the specified class.

    Parameters:
        obj (object): The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if the object is an instance of the specified
    class or inherits from it, False otherwise.
    """
    return isinstance(obj, a_class)
