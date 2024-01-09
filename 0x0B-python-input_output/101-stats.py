#!/usr/bin/python3
"""Reads stdin line by line and computes metrics"""
import sys


def print_status(lines):
    """
    Print statistics based on the accumulated data.

    Parameters:
    - lines (list): List of lines read from stdin.
    """
    counter = 0
    size = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}
    for line in lines:
        parts = line.split()
        try:
            size += int(parts[-1])
            code = parts[-2]
            status_codes[code] += 1
        except(ValueError, IndexError):
            continue
        if counter == 9:
            print("File size: {}".format(size))
            for key, val in sorted(status_codes.items()):
                if (val != 0):
                    print("{}: {}".format(key, val))
            counter = 0
        counter += 1
    if counter < 9:
        print("File size: {}".format(size))
        for key, val in sorted(status_codes.items()):
            if (val != 0):
                print("{}: {}".format(key, val))


if __name__ == "__main__":
    lines = sys.stdin.readlines()
    print_status(lines)
