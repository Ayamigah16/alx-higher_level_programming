#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # get the number of command line argument
    count = len(sys.argv) - 1

    # display result
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))
    for index in range(count):
        print("{}: {}".format(index + 1, sys.argv[index + 1]))
