#!/usr/bin/python3
"""Define a class"""


class BaseGeometry:
    """An empty class no more"""
    def area(self):
        """Module that raises an exception"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """Checks if value is valid"""
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
