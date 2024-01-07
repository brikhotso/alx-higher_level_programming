#!/usr/bin/python3
"""
matrix_operations module

The module contains the following function:
- matrix_divided(matrix, div)
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    Parameters:
    - matrix (list of lists): Matrix containing integers or floats.
    - div (int or float): Number to divide the matrix elements.

    Returns:
    - New matrix with elements divided by div.

    Raises:
    - TypeError: If the matrix is not a list of lists of integers or floats,
                or if each row of the matrix doesn't have the same size,
                or if div is not a number.
    - ZeroDivisionError: If div is equal to 0.
    """

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of "
                            "integers/floats")

        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of "
                                "integers/floats")

    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result_matrix = list(
        map(
            lambda row: list(
                map(lambda element: round(element / div, 2), row)
            ),
            matrix
        )
    )
    return (result_matrix)
