#!/usr/bin/python3
"""
a class MyList that inherits from list
"""


class MyList(list):
    """
    A class that inherits from list and provides additional functionality.
    """

    def print_sorted(self):
        """
        Print the list in sorted order (ascending).

        Returns:
            None
        """
        print(sorted(self))
