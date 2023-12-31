#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """The square itself.

        Args:
            size (int): The size of the new square.
            position (tuple): Coordenates where the square is about to be placed.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

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
    
    @property
    def position(self):
        """Getter & Setter for the position value of the square."""
        return self.__position
        
    @position.setter
    def position(self, value):
        """Getter & Setter for the position value of the square."""
        if type(value) is not tuple or len(value) != 2 or not all(type(element) is int for element in value) or not all(element >= 0 for element in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
    
    def area(self):
        """Returns the area of the square"""
        return self.__size**2

    def my_print(self):
        """Printing a square with "#" depending the value: (size) and the value: (position)"""
        if self.size == 0:
            print("")
        for i in range(self.position[1]):
            print("")
        for rows in range(self.size):
            for spaces in range(self.position[0]):
                print(" ", end = "")
            for hashtag in range(1):
                print("#" * self.size)

