#!/usr/bin/python3
def max_integer(my_list=[]):
    last = 0
    if my_list == []:
        return None
    for i in my_list:
        if i > last:
            last = i
            continue
    return last
