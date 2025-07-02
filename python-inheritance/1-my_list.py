#!/usr/bin/python3
"""MyList class that inherits from list"""

class MyList(list):
    """Inherits from built-in list and adds print_sorted method"""

    def print_sorted(self):
        """Prints the list sorted (ascending) without modifying the original list"""
        print(sorted(self))
