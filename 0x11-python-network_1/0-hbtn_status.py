#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""

import urllib.request


def fetch_status(url):
    with urllib.request.urlopen(url) as response:
        content = response.read()
        utf8_content = content.decode('utf-8')
    return content, utf8_content


def display_response_info(content, utf8_content):
    print("Body response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}")
    print(f"\t- utf8 content: {utf8_content}")


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    content, utf8_content = fetch_status(url)
    display_response_info(content, utf8_content)
