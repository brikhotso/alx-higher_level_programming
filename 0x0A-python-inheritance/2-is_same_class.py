#!/usr/bin/python3
"""Define a class check function"""


def is_same_class(obj, a_class):
    """Check if the object is exactly an instance of the specified class."""
    return type(obj) is a_class
