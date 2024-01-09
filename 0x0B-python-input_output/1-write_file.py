#!/usr/bin/python3
""" contains function that writes a string to a file"""


def write_file(filename="", text=""):
    """define write_file """
    with open(filename, "w") as file:
        characters = file.write(text)
        return characters
