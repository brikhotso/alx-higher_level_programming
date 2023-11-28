#!/usr/bin/python3
output = ""
for box in range(10):
    for toy in range(box + 1, 10):
        output += f"{box}{toy}, " if box != 8 or toy != 9 else f"{box}{toy}\n"

print(output, end="", flush=True)
