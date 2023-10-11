#!/usr/bin/python3
"""Define a Rectangle."""


class Rectangle:
    """The Rectangle itself"""

    def __init__(self, width=0, height=0):
        """Instantiation with optional width and height

        Args:
                width (int): width of the rectangle
                height (int): height of the rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def height(self):
        """Getter & Setter for the attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Getter & Setter for the attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Getter & Setter for the attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Getter & Setter for the attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__height * self.__width

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return ((self.__height * 2) + (self.__width * 2))
