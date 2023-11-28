#!/usr/bin/python3
def fizzbuzz():
    # Print numbers from 1 to 100
    for n in range(1, 101):
        if n % 3 == 0 and n % 5 == 0:
            print("FizzBuzz", end='')
        elif n % 3 == 0:
            print("Fizz", end='')
        elif n % 5 == 0:
            print("Buzz", end='')
        else:
            print(n, end='')

        if n < 101:
            print(" ", end='')
