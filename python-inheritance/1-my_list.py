#!/usr/bin/python3
"""Defines the MyList class that inherits from list."""


class MyList(list):
    """Custom list class with print_sorted and overridden methods."""

    def __init__(self):
        """Initialize the MyList object."""
        list.__init__(self)

    def append(self, item):
        """Append an item to the list."""
        list.append(self, item)

    def __str__(self):
        """Return the string representation of the list."""
        return list.__str__(self)

    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        print(sorted(self))
