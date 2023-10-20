#!/usr/bin/python3
"""Defining a function that converts JSON into an object after importing
from another file"""
import json


def load_from_json_file(filename):
    """Deserializing an object"""
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
