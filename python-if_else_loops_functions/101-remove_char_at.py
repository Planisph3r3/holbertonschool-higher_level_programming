#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n >= len(str):
        return str
    k = ""
    for i in range(0, len(str)):
        if i != n:
            k += str[i]
    return k
