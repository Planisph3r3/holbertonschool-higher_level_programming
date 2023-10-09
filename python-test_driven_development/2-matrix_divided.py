#!/usr/bin/python3

# 2-matrix_divided.py

"""
This module defines a function for dividing all elements
of a matrix by a specified number.

Function:
- matrix_divided(matrix, div): Divides all elements in the matrix
by `div` and returns a new matrix.
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a specified
    number and return a new matrix.

    Args:
        matrix (list of lists): The matrix to be divided.
        div (int or float): The number by which to divide
        each element in the matrix.

    Returns:
        list of lists: A new matrix where each element is the result
        of dividing the corresponding
        element in the input matrix
        by 'div', rounded to 2 decimal places.

    Raises:
        TypeError: If 'matrix' is not a matrix of integers or floats,
                   if rows in the matrix have different sizes, or
                   if 'div' is not a number.
        ZeroDivisionError: If 'div' is 0.
    """

    if type(matrix) is not list and all(type(elements) not in (int, float) for elements in rows for rows in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(rows) == len(matrix[0]) for rows in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []

    for rows in matrix:
        for elements in rows:
            new_matrix.append(round(elements / div, 2))

    return new_matrix
