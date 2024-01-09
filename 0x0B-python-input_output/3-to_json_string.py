#!/usr/bin/python3
"""contain function that return JSON representation of an object"""
import json


def to_json_string(my_obj):
    """ define function that return JSON representation of an oject string"""
    return json.dumps(my_obj)
