#!/usr/bin/python3
"""This module defines a MyList class that inherits from list."""


class MyList(list):
    """A custom list class that extends the built-in list."""

    def __init__(self):
        """Initialize the list."""
        super().__init__()  # çağırılmasa 'instantiation' testindən keçməyəcək

    def append(self, item):
        """Append an item to the list."""
        super().append(item)

    def __str__(self):
        """Return the string representation of the list."""
        return super().__str__()

    def print_sorted(self):
        """Print the list in ascending sorted order."""
        print(sorted(self))
