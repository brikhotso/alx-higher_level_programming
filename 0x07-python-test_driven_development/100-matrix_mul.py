#!/usr/bin/python3
"""
contains method for multiplying 2 matrices
"""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices.

    Parameters:
    - m_a (list): First matrix.
    - m_b (list): Second matrix.

    Raises:
    - TypeError: If m_a or m_b is not a list, not a list of lists,
        or contains non-numeric elements.
    - ValueError: If m_a or m_b is empty, not a rectangle,
        or can't be multiplied.

    Returns:
    - list: Result of the matrix multiplication.
    """
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')

    if False in [isinstance(listx, list) for listx in m_a]:
        raise TypeError("m_a must be a list of lists")

    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')

    if False in [isinstance(listx, list) for listx in m_b]:
        raise TypeError("m_b must be a list of lists")

    if not len(m_a) or 0 in [len(listx) for listx in m_a]:
        raise ValueError("m_a can't be empty")

    if not len(m_b) or 0 in [len(listx) for listx in m_b]:
        raise ValueError("m_b can't be empty")

    if any(False in x for x in [[isinstance(ele, (int, float))
                                 for ele in listx] for listx in m_a]):
        raise TypeError('m_a should contain only integers or floats')

    if any(False in x for x in [[isinstance(ele, (int, float))
                                 for ele in listx] for listx in m_b]):
        raise TypeError('m_b should contain only integers or floats')

    if len(set(len(listx) for listx in m_a)) > 1:
        raise TypeError('each row of m_a must should be of the same size')

    if len(set(len(listx) for listx in m_b)) > 1:
        raise TypeError('each row of m_b must should be of the same size')

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []

    for i in range(len(m_a)):
        new_row = []
        for j in range(len(m_b[0])):
            element_sum = 0
            for k in range(len(m_a[0])):
                element_sum += m_a[i][k] * m_b[k][j]
            new_row.append(element_sum)
        result.append(new_row)

    return result
