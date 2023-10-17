#!/usr/bin/python3
"""Define a module for checking the instance of an object that
inherited directly from the specified class"""


def inherits_from(obj, a_class):
    """Returns True or False depending if obj is exactly the same instance
    as the specified"""
    if issubclass(obj, a_class):
        return True
    else:
        return False
