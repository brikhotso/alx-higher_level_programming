#!/usr/bin/python3
"""contain function that inserts a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """
    Insert a line of text after each line with specific string in a file.

    Parameters:
    - filename (str): The name of the file.
    - search_string (str): The string to search for in each line.
    - new_string (str): The line of text to insert after each matching line.
    """
    with open(filename, "r") as file:
        lines = file.readlines()

    with open(filename, "w") as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
