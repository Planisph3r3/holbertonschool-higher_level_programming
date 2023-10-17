#!/usr/bin/python3
def is_same_class(obj, a_class):
    """Returns True or False depending if obj is exactly
    the same instance
    as the specified"""
    if type(obj) is a_class:
        return True
    else:
        return False
