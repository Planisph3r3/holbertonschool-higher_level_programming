#!/usr/bin/python3
def roman_to_int(roman_string):
    di_rom = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    k = 0
    if type(roman_string) != str or roman_string is None:
        return 0
    for i in roman_string:
        if len(roman_string) > 1:
            if i == "I" and roman_string[-1] != "I":
                k += -1
                continue
        k += di_rom[i]

    return k
