#!/usr/bin/python3
"""Send request to URL and displays the value of the X-Request-Id variable """
import urllib.request
import sys


with urllib.request.urlopen(sys.argv[1]) as response:
    print(dict(response.headers).get("X-Request-Id"))
