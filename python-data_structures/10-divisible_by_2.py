#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    neww = []
    for i in my_list:
        if i % 2 == 0:
            i = True
            neww.append(i)
        else:
            i = False
            neww.append(i)
    return neww
