#!/usr/bin/python3
"""Send request to URL and displays the value of the X-Request-Id variable """
import requests
import sys


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(response.headers.get("X-Request-Id"))
