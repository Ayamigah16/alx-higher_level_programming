#!/usr/bin/python3
"""
Contains the "class_to_json" function
"""
def class_to_json(obj):
    """
    Returns the dictionary description with simple data structures for JSON serialization of an object.

    Args:
        obj: The object to be serialized.

    Returns:
        dict: The dictionary representation of the object.
    """
    return obj.__dict__


if __name__ == '__main__':
    m = MyClass("John")
    m.number = 89
    print(type(m))
    print(m)

    mj = class_to_json(m)
    print(type(mj))
    print(mj)
