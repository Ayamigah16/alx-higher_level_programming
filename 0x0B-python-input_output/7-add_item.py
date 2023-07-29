#!/usr/bin/env python3

"""Script to add items to a JSON file.

This script takes command-line arguments and adds them to a list.
The list is then saved to a JSON file named "add_item.json".
If the file already exists, the script loads its contents into the list before adding the new items.
If the file does not exist, it initializes an empty list and then appends the command-line arguments.

Usage:
    ./add_item.py item1 item2 item3 ...

Author: [Your Name]
"""

import sys
import os.path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

def main():
    # The filename to use for the JSON file
    filename = 'add_item.json'

    # Check if the JSON file exists and load its contents
    if os.path.exists(filename):
        my_list = load_from_json_file(filename)
    else:
        my_list = []

    # Extend the list with the command-line arguments provided
    my_list.extend(sys.argv[1:])

    # Save the updated list to the JSON file
    save_to_json_file(my_list, filename)

if __name__ == '__main__':
    main()
