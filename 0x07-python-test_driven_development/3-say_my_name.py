#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first name> <last name>".

    Parameters:
    first_name (str): The first name.
    last_name (str, optional): The last name. Default is an empty string.

    Raises:
    TypeError: If first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {}".format(first_name))

# Uncomment the following lines to run the provided test cases
# say_my_name("John", "Smith")
# say_my_name("Walter", "White")
# say_my_name("Bob")
# try:
#     say_my_name(12, "White")
# except Exception as e:
#     print(e)
