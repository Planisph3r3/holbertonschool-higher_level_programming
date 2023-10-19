#!/usr/bin/python3
def read_file(filename="", encoding="utf-8"):
    """Printing the content of a file to stout"""
    with open(filename) as f:
        print(f.read(), end="")
