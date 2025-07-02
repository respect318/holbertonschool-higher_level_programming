#!/usr/bin/python3
"""This module defines a MyList class that inherits from list."""


class MyList(list):
    """Custom list class with a print_sorted method."""

    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        print(sorted(self))
