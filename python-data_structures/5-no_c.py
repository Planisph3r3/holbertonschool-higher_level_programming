#!/usr/bin/python3
def no_c(my_string):
    neww = ""
    for i in my_string:
        if i == "c" or i == "C":
            continue
        neww += i
    return neww
