#!/usr/bin/python3
"""contain function class_to_json"""


def class_to_json(obj):
    """Convert an object to a dictionary with serializable attributes."""
    return obj.__dict__
