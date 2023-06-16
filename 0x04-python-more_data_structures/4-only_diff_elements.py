#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    # Create an empty set to store the elements present in only one set
    different_set = set()

    # Iterate over each element in set_1
    for item in set_1:
        # Check if the element is not present in set_2
        if item not in set_2:
            # If it is not present, add it to the different_set
            different_set.add(item)

    # Iterate over each element in set_2
    for item in set_2:
        # Check if the element is not present in set_1
        if item not in set_1:
            # If it is not present, add it to the different_set
            different_set.add(item)

    # Return the set of elements present in only one set
    return different_set
