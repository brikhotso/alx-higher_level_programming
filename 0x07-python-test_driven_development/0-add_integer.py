#!/usr/bin/python3
"""
0-add_integer module

This module provides a function to add two integers or floats.

The module contains the following function:
- add_integer(a, b=98)
"""


def add_integer(a, b=98):
    """
    Adds two numbers, 'a' and 'b', and returns the result.

    Parameters:
    - a (int or float): The first number to add
    - b (int or float): The second number to add (default is 98)

    Raises:
    - TypeError: If 'a' or 'b' is not an integer or float.
    """
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")

    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
