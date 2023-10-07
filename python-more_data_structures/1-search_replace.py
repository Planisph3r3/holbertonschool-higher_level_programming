#!/usr/bin/python3
def search_replace(my_list, search, replace):
    k = []
    for i in my_list:
        if i == search:
            k.append(replace)
        else:
            k.append(i)
    return k
