#!/usr/bin/python3
"""Module for converting object to JSON string."""


import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)."""
    return json.dumps(my_obj)
