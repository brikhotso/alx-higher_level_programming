#!/usr/bin/python3
""" contains function that appends a string at the end of a file"""


def append_write(filename="", text=""):
    """define append_write"""
    with open(filename, "a") as file:
        characters = file.write(text)
        return characters
