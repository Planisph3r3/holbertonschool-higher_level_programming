#!/usr/bin/python3
def uppercase(str):
    fuli = ""
    for i in str:
        k = (ord(i) - 32)
        upper = chr(k)
        if "A" <= i <= "Z" or i == " " or "0" <= i <= "9" or i == ",":
            fuli += i
        else:
            fuli += upper
    print("{:s}".format(fuli))
