#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Extract the first two elements from each tuple
    a = tuple_a[:2]
    b = tuple_b[:2]

    # Pad the tuples with zeros if they are smaller than 2
    a += (0,) * (2 - len(a))
    b += (0,) * (2 - len(b))

    # Perform element-wise addition of the tuples
    result = (a[0] + b[0], a[1] + b[1])

    return result
