#!/usr/bin/python3
for box in range(0, 8):
    for toy in range(box + 1, 10):
        print("{:d}{:d}".format(box, toy), end=', ')
    print("{:d}{:d}".format(box + 1, toy))
