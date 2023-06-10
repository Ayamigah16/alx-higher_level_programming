#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """ 
    Change a list value a particular index
    """
    if idx >= 0 and idx < len(my_list):
        my_list[idx] = element
    return my_list
