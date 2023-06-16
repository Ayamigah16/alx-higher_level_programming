#!/usr/bin/python3

def uniq_add(my_list=[]):
    # Create a set to store unique integers
    unique_set = set()

    # Iterate over each element in the input list
    for item in my_list:
        # Add the element to the set (sets only store unique values)
        unique_set.add(item)

    # Sum up all the elements in the set and return the result
    return sum(unique_set)
