#!/usr/bin/python3

def lookup(obj):
    """
    Return a list of available attributes and methods of an object.

    Parameters:
        obj (object): The object to look up attributes and methods for.

    Returns:
        list: A list of attribute and method names.
    """
    return dir(obj)
