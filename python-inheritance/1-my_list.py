#!/usr/bin/python3
"""
This module defines a class MyList that inherits from list,
with a method to print the sorted list.
"""


class MyList(list):
    """
    MyList extends the built-in list with a method to print
    the list elements in sorted (ascending) order.
    """

    def print_sorted(self):
        """
        Prints a sorted (ascending) version of the list
        without modifying the original list.
        """
        print(sorted(self))
