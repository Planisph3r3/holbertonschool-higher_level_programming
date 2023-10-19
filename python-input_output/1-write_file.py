#!/usr/bin/python3
"""Defining a function that writes a string on a text file"""


def write_file(filename="", text=""):
    """Writing on what is on the text variable to the upcoming (filename)
    and returns the number of characters written"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
