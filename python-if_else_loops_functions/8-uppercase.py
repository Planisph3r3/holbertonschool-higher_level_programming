#!/usr/bin/python3
def uppercase(str):
    for i in str:
        k = (ord(i) - 32)
        l = chr(k)
        if "A" <= i <= "Z" or i == " " or "0" <= i <= "9":
            print("{:s}".format(i), end = "")
        else:
            print("{:s}".format(l), end = "")
    print()
