#!/usr/bin/python3
def uppercase(str):
    fuli = ""
    for i in str:
        k = (ord(i) - 32)
        l = chr(k)
        if "A" <= i <= "Z" or i == " " or "0" <= i <= "9":
            fuli += i
        else:
            fuli += l
    print("{:s}".format(fuli))
