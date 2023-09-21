#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    neww = my_list.copy()
    if idx < 0:
        return neww
    elif idx > len(my_list):
        return neww
    else:
        pass

    neww[idx] = element
    return neww
