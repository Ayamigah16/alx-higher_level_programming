#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    # Update the value of an existing key
    if key in a_dictionary:
        a_dictionary[key] = value
    # Add a new key/value pair
    else:
        a_dictionary[key] = value

    # Return the updated dictionary
    return a_dictionary
