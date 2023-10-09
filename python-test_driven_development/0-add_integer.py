#!/usr/bin/python3
# 0-add_integer.py
"""
This module defines a function for adding two integers or floats.

Function:
- add_integer(a, b=98): Adds two integers or floats and returns the result as an integer.
"""

def add_integer(a, b=98):
    """
    Add two integers or floats and return the result as an integer.
    
    Args:
        a (int or float): The first number to be added.
        b (int or float, optional): The second number to be added. Defaults to 98.

    Returns:
        int: The sum of "a" and "b" as an integer.

    Raises:
        TypeError: If "a" or "b" is not an integer or a float.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
