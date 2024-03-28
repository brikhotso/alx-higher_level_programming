#!/usr/bin/python3
""" Sends a request to a given URL and displays the response body """
import sys
import urllib.error
import urllib.request

if __name__ == "__main__":
    request = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
