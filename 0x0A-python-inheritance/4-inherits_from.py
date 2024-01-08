#!/usr/bin/python3
"""Define function that checks if object is inherited"""


def inherits_from(obj, a_class):
    """
    function that returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class ;
    otherwise False
    """
    return type(obj) != a_class and isinstance(obj, a_class)
