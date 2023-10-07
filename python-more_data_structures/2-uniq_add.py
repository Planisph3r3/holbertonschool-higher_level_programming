#!/usr/bin/python3
def uniq_add(my_list=[]):
    from functools import reduce

    k = set(my_list)
    return reduce(lambda x, y: x + y, list(k))
