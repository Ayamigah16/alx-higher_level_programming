#!/usr/bin/python3


class LockedClass:
    """
    Class that prevents dynamically creating new instance attributes,
    except if the attribute is named 'first_name'.

    """

    __slots__ = ['first_name']
