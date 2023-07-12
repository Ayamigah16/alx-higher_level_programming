import json
"""
Contains the "to_json_string" fundtion
"""


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object.

    Args:
        my_obj: The object to be converted to JSON.

    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)

if __name__ == '__main__':
    my_list = [1, 2, 3]
    s_my_list = to_json_string(my_list)
    print(s_my_list)
    print(type(s_my_list))

    my_dict = {
        'id': 12,
        'name': "John",
        'places': ["San Francisco", "Tokyo"],
        'is_active': True,
        'info': {
            'age': 36,
            'average': 3.14
        }
    }
    s_my_dict = to_json_string(my_dict)
    print(s_my_dict)
    print(type(s_my_dict))

    try:
        my_set = {132, 3}
        s_my_set = to_json_string(my_set)
        print(s_my_set)
        print(type(s_my_set))
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
