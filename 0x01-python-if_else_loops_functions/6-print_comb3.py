#!/usr/bin/python3
for box in range(10):
    for toy in range(box + 1, 10):
        print(f"{box}{toy}", end=', ' if (box != 8 or toy != 9) else '')
print()
