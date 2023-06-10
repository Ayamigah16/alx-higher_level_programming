#!/usr/bin/python3
from calculator_1 import add, sub, div, mul

if __name__ == "__main__":
    # code will execute when 1-calculation is run
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
