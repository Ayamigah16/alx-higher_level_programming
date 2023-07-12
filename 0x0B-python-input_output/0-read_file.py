#!/usr/bin/python3
"""
Contains the read_file function
"""

def read_file(filename=""):
    with open(filename, encoding='utf-8') as file:
        for line in file:
            print(line, end='')
