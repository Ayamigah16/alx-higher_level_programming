#!/usr/bin/python3
"""Lists 10 commits (from most recent to oldest) of
a GitHub repository"""

import requests
import sys


if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = f'https://api.github.com/repos/{owner_name}/{repo_name}/commits'

    try:
        response = requests.get(url)
        commits = response.json()[:10]

        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f'{sha}: {author_name}')

    except ValueError:
        print("Error: Unable to fetch data from GitHub API")
