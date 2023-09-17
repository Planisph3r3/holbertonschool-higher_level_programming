#!/usr/bin/python3
for i in range(10):
    for k in range(10):
        if i == 9 and k == 9:
            print("{:d}{:d}".format(i, k))
        else:
            print("{:d}{:d}".format(i, k), end=", ")
