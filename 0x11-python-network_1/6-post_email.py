#!/usr/bin/python3
"""send POST request to passed URL with email as parameter, display response"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = {"email": email}
    response = requests.post(url, data=data)

    print(response.text)
