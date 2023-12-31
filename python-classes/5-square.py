#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """The square itself.

        Args:
            size (int): The size of the new square.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Getter & Setter for the size value of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Getter & Setter for the size value of the square."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square"""
        return self.__size**2
    
    def my_print(self):
        """Printing a square with "#" depending the value: size"""
        if self.__size == 0:
            print("")
        for rows in range(self.__size):
            print("#" * self.__size)
