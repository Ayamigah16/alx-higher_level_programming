#!/usr/bin/python3
"""Uses GitHub API to display user id"""

import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    url = 'https://api.github.com/user'
    auth = (username, token)

    response = requests.get(url, auth=auth)

    try:
        user_data = response.json()
        if 'id' in user_data:
            print(user_data['id'])
        else:
            print("None")
    except ValueError:
        print("None")
