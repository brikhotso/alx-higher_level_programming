#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    result = 0

    if len(sys.argv) < 2:
        print(result)
        sys.exit(0)

    for arg in range(1, len(sys.argv)):
        result += int(sys.argv[arg])

    print(result)
