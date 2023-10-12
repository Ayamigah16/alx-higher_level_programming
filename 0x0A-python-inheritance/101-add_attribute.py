#!/usr/bin/python3
"""function that adds a new attribute to an object if it’s possible:"""


def add_attribute(obj, attr, value):
    """Adds a new attribute to an object if possible.

    Args:
        obj: The object to which the attribute will be added.
        attr (str): The name of the attribute.
        value: The value of the attribute.

    Raises:
        TypeError: If it's not possible to add a new attribute.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)


if __name__ == "__main__":
    class MyClass:
        pass

    mc = MyClass()
    add_attribute(mc, "name", "John")
    print(mc.name)

    try:
        a = "My String"
        add_attribute(a, "name", "Bob")
        print(a.name)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
