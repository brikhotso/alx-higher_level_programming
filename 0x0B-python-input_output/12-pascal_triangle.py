#!/usr/bin/python3
"""contains a functions that represent the pascals triangle"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.

    Parameters:
    - n (int): The number of rows to generate.

    Returns:
    list of lists: Pascal's triangle as a list of lists of integers.
    """
    if n <= 0:
        return []

    triangle = []

    for _ in range(n):
        row = ([1] if not triangle else [1] +
               [triangle[-1][i - 1] + triangle[-1][i]
                for i in range(1, len(triangle[-1]))] + [1])
        triangle.append(row)

    return triangle
