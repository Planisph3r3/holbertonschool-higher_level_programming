#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 100):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz ", end="")
        elif i % 3 == 0:
            if i != 99:
                print("Fizz ", end="")
            else:
                print("Fizz", end="")
        elif i % 5 == 0:
            print("Buzz ", end="")
        else:
            print(f"{i} ", end="")
