#!/usr/bin/python3
"""This module defines the MyList class that inherits from list"""

class MyList(list):
    """Custom list class with a print_sorted method"""

    def print_sorted(self):
        """Prints the list sorted without changing the original"""
        print(sorted(self))

    def __str__(self):
        """String representation"""
        return super().__str__()

    def append(self, item):
        """Appends item to the list"""
        super().append(item)
