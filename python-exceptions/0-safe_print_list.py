#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for elem in my_list:
            count += 1
            print(elem, end="")
            if count == x:
                break
        print()
        return count
    except:
        return count
