#!/usr/bin/python3
"""Defining a function that reads and prints a whole text file"""


def read_file(filename="", encoding="utf-8"):
    """Printing the content of a file to stout"""
    with open(filename) as f:
        print(f.read(), end="")
