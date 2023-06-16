#!/usr/bin/python3

def common_elements(set_1, set_2):
    # Create an empty set to store the common elements
    common_set = set()

    # Iterate over each element in set_1
    for item in set_1:
        # Check if the element exists in set_2
        if item in set_2:
            # If it does, add it to the common_set
            common_set.add(item)

    # Return the set of common elements
    return common_set
