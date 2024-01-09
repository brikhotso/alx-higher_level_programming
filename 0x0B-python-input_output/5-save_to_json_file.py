#!/usr/bin/python3
"""
contain function that writes an object to a textfile ,
using JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """Define save_to_json_file"""
    with open(filename, "w") as file:
        json.dump(my_obj, file)
