#!/usr/bin/python3
"""Defining a function that appends a string on a text file"""


def append_write(filename="", text=""):
    """Appends on what is on the text variable to the upcoming (filename)
    and returns the number of characters added"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
