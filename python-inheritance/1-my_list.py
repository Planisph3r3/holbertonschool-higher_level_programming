#!/usr/bin/python3
"""Defining a MyList class"""


class MyList(list):
    """A class that that inherits from list"""

    def print_sorted(self):
        """A method that sorts in ascending order
        the elements of the upcoming list,
        stores it on a new list and then print it"""
        new_list = []
        for i in self:
            new_list.append(i)
        new_list.sort()
        print(new_list)
