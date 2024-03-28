#!/usr/bin/python3
"""Send request to URL and displays the value of the X-Request-Id variable """
import urllib.request
import sys

if __name__ == "__main__":
    request = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
