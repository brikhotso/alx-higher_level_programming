#!/usr/bin/python3
"""send POST request to passed URL with email as parameter, display response"""
import urllib.parse
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({"email": email}).encode('utf-8')
    request = urllib.request.Request(url, data)

    with urllib.request.urlopen(request) as response:
        body = response.read().decode('utf-8')
        print(body)
