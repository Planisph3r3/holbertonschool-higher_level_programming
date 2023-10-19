#!/usr/bin/python3
"""Define a module for checking the instance of an object that
inherited directly from the specified class"""


def inherits_from(obj, a_class):
    """Returns True or False depending if obj is an inherited instance
    of the specified class"""
    return isinstance(obj, a_class)
