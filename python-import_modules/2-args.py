#!/usr/bin/python3
import sys
def main()
    if len(sys.argv) == 2:
        print("1 argument:") 
    elif len(sys.argv) == 1:
        print("{} arguments.".format(len(sys.argv)-1)) 
    else:
        print("{} arguments:".format(len(sys.argv)-1))

    for i in range(1, len(sys.argv)):
        k = sys.argv[i]
        print(f"{i}: {k}")
if __name__ == "__main__":
    main()
