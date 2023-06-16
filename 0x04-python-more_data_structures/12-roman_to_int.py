#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0

    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    length = len(roman_string)

    for i in range(length):
        value = roman_values.get(roman_string[i])
        if i < length - 1 and value < roman_values.get(roman_string[i + 1]):
            total -= value
        else:
            total += value

    return total
