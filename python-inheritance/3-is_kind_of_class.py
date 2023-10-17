#!/usr/bin/python3
"""Define a module for checking the instance of an object"""


def is_kind_of_class(obj, a_class):
    """Returns True or False depending if obj is exactlly the same instance
    as the specified"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
