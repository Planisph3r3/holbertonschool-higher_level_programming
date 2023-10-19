#!/usr/bin/python3
"""Defining a function that decodes a JSON into an object"""
import json


def from_json_string(my_str):
    """Deserializing an object"""
    json_str = json.loads(my_str)
    return json_str
