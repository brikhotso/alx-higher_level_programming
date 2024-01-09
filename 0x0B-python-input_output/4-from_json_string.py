#!/usr/bin/python3
"""contain function that return object represented by JSON string"""
import json


def from_json_string(my_str):
    """ define function that return object represented by JSON string"""
    return json.loads(my_str)
