#!/usr/bin/python3
"""Program to save strings from command line arguments to file called
`add_item.json`. File contains a json serialized list of all strings
entered as arguments to the program.
"""
import sys
from os import path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


if __name__ == '__main__':
    """
    Script to add command-line arguments to a Python
    list and save them to a file.
    """

    filename = 'add_item.json'

    if path.exists(filename):
        my_list = load_from_json_file(filename)
    else:
        my_list = []

    my_list.extend(sys.argv[1:])
    save_to_json_file(my_list, filename)
