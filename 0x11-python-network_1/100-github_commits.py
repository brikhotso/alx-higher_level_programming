#!/usr/bin/python3
"""List 10 commits from the most recent to oldest from a github repository"""
import requests
import sys


if __name__ == "__main__":
    repository = sys.argv[1]
    owner = sys.argv[2]

    url = "https://api.github.com/repos/{}/{}/commits".format(
        owner, repository)
    response = requests.get(url)

    commits = response.json()[:10]

    for commit in commits:
        sha = commit.get('sha')
        author_name = commit.get('commit', {}).get(
            'author', {}).get('name', {})
        print("{}: {}".format(sha, author_name))
