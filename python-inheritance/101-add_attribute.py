#!/usr/bin/python3
"""
This module defines a function that adds an attribute to an object
if the object allows it.
"""


def add_attribute(obj, name, value):
    """
    Adds a new attribute to the object if possible.

    Args:
        obj: The object to modify.
        name (str): The name of the new attribute.
        value: The value of the new attribute.

    Raises:
        TypeError: If the object doesn't support new attributes.
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
