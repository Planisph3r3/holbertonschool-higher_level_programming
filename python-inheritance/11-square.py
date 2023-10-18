#!/usr/bin/python3
"""Define a class"""


class BaseGeometry:
    """An empty class no more"""

    def area(self):
        """Not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Checks if value is valid"""
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")


"""Defining a class Rectangle"""


class Rectangle(BaseGeometry):
    """A class that uses another one as template"""

    def __init__(self, width, height):
        """Instantiation of width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def integer_validator(self, name, value):
        """Checks if value is valid"""
        super().integer_validator(name, value)

    def area(self):
        """Returns the area"""
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"


"""Defining a class Square"""


class Square(Rectangle):
    """A class that uses another one as template"""
    def __init__(self, size):
        """Instantiation of size"""
        self.__size = size
        self.integer_validator("size", size)

    def integer_validator(self, name, value):
        """Checks if value is valid"""
        super().integer_validator(name, value)

    def area(self):
        """Returns the area"""
        return self.__size ** 2

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
