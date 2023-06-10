#!/usr/bin/python3
import sys

if __name__ == "__main__":
    """ Add all command line arguments """
    # initializing sum as zero
    sum = 0
    # get sum
    for i in range(len(sys.argv) - 1):
        sum += int(sys.argv[i + 1])
    # print sum
    print("{}".format(sum))
