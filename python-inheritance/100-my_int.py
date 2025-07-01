#!/usr/bin/python3
"""
This module defines a rebel integer class MyInt.
"""


class MyInt(int):
    """
    MyInt class inherits from int but reverses
    the behavior of == and != operators.
    """

    def __eq__(self, other):
        """Override == operator: behave like !=."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override != operator: behave like ==."""
        return super().__eq__(other)
