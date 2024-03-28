#!/usr/bin/python3
""" Sends a request to a given URL and displays the response body """
import sys
import requests


if __name__ == "__main__":
    try:
        response = requests.get(sys.argv[1])
        response.raise_for_status()
        print(response.text)
    except requests.exceptions.RequestException as e:
        print("Error:", e)
