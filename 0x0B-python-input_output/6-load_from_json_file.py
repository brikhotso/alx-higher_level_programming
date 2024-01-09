#!/usr/bin/python3
"""Contain function that creates an object from a JSON file"""
import json


def load_from_json_file(filename):
    """Define load_from_json_file"""
    with open(filename) as file:
        return json.load(file)
