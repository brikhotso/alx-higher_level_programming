#!/usr/bin/python3
""" contains function  that adds a new attribute to an object."""


def add_attribute(obj, name, value):
    """
    Add a new attribute to an object if it's possible.

    Args:
        obj (object): The object to which the attribute should be added.
        name (str): The name of the new attribute.
        value (any): The value of the new attribute.

    Raises:
        TypeError: If the object cannot have new attributes.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
