#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys


def output(a, b, operator, operation):
    print("{a} {operator} {b} = {operation}".format(a=a,
                                                    operator=operator,
                                                    b=b,
                                                    operation=operation))


if __name__ == "__main__":
    """ Build my own calculator """
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    if operator == '+':
        output(a, b, operator, add(a, b))
    elif operator == '-':
        output(a, b, operator, sub(a, b))
    elif operator == '*':
        output(a, b, operator, mul(a, b))
    elif operator == '/':
        output(a, b, operator, div(a, b))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
