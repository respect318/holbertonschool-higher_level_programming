#!/usr/bin/python3
"""Check if an object is instance of a subclass of a class."""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a subclass of a_class."""
    return type(obj) != a_class and isinstance(obj, a_class)
