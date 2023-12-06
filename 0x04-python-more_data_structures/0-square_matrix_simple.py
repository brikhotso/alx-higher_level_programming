#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

    squared_matrix = []

    for row in matrix:
        squared_row = map(lambda i: i**2, row)

        squared_matrix.append(list(squared_row))

    return (squared_matrix)
