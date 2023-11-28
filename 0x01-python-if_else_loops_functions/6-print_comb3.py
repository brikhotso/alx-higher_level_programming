#!/usr/bin/python3
for box in range(0, 10):
    for toy in range(box + 1, 10):
        if box == 8 and toy == 9:
            print("{}{}".format(box, toy))
        else:
            print("{}{}".format(box, toy), end=", ")
