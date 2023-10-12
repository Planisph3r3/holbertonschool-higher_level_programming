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
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """Getter & Setter for the attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Getter & Setter for the attribute height"""
        if not isinstance(value, int):
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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
