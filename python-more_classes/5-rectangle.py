#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """Represents a rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width with validation"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height with validation"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Returns a string representation with '#'"""
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(["#" * self.width for _ in range(self.height)])

    def __repr__(self):
        """Returns a string that can recreate the instance via eval()"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Called when an instance is deleted"""
        print("Bye rectangle...")
