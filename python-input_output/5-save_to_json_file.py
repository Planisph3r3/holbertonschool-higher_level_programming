#!/usr/bin/python3
"""Defining a function that converts an object into JSON then
exports it to another file"""
import json


def save_to_json_file(my_obj, filename):
    """Serializing an object"""
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
