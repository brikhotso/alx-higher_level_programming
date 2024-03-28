#!/usr/bin/python3
"""Send request to URL and displays the value of the X-Request-Id variable """
import urllib.request
import sys


with urllib.request.urlopen(sys.argv[1]) as response:
    x_request_id = response.headers.get('X-Request-Id')
    print("{}".format(x_request_id))
