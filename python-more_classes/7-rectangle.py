#!/usr/bin/python3
"""Define a Rectangle."""


class Rectangle:
    """The Rectangle itself"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Instantiation with optional width and height

        Args:
                width (int): width of the rectangle
                height (int): height of the rectangle
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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
        if self.__height == 0 or self.__width == 0:
            return (0)
        return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        """Define the string representation of the rectangle"""
        str_store = ""
        if self.__height == 0 or self.__width == 0:
            return("")
        for i in range(self.__height):
            if isinstance(self.print_symbol, list):
                str_store += (str(self.print_symbol) * self.__width)
            else:
                str_store += (Rectangle.print_symbol * self.__width)
            if i < self.__height - 1:
                str_store += '\n'
        return str_store

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Warns when an object is about to be deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
