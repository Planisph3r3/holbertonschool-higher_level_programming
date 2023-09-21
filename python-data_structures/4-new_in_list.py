#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    neww = []
    if idx < 0:
        return my_list
    elif idx > len(my_list):
        return my_list
    else:
        pass
    for i in my_list:
        neww.append(i)
        if i == idx:
            neww[idx - 1] = new_element

    return neww
