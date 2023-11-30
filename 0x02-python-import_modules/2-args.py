#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    number_arg = len(sys.argv)

    if number_arg == 1:
        print("0 arguments.")
    else:
        print("{} arguments:".format(number_arg - 1))

    if number_arg > 1:

        for i in range(1, number_arg):
            print("{}: {}".format(i, sys.argv[i]))
