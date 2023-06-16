#!/usr/bin/python3

def search_replace(my_list, search, replace):
    # Create a new list to store the modified elements
    new_list = []

    # Iterate over each element in the input list
    for item in my_list:
        # Check if the element matches the search element
        if item == search:
            # If it matches, add the replace element to the new list
            new_list.append(replace)
        else:
            # If it doesn't match, add the original element to the new list
            new_list.append(item)

    # Return the new list
    return new_list
