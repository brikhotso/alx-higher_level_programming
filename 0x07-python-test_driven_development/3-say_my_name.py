#!/usr/bin/python
"""
contains a function say_my_name which prints out first and last names
"""


def say_my_name(first_name, last_name=""):
    """
    Prints a formatted string with the provided first and last names.

    Parameters:
    - first_name (str): The first name to be included in the output.
    - last_name (str, optional): The last name to be included in the output.

    Raises:
    - TypeError: If either first_name or last_name is not a string.

    Returns:
    - None
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
