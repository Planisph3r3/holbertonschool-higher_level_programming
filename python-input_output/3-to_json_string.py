#!/usr/bin/python3
"""Defining a function that converts an object into JSON"""
import json


def to_json_string(my_obj):
    """Serializing an object"""
    json_str = json.dumps(my_obj)
    return json_str
