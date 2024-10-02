#!/usr/bin/python3

"""
A pascal_triangle module.
"""


def pascal_triangle(n):
    """
    The function takes an integer parameter and
    returns an array of rows of a pascal triangle
    if integer is greater than 0, otherwise, returns an empty list.
    """
    matrix = []
    if n <= 0:
        return(matrix)

    prev_row = [1]
    matrix.append(prev_row)

    for idx in range(n):
        if idx > 0:
            next_row = []

            for i in range(len(prev_row)):

                if i == 0 and i == len(prev_row) - 1:
                    next_row.append(1)
                    next_row.append(prev_row[i])

                if i != len(prev_row) - 1:
                    if i == 0:
                        next_row.append(1)
                    if i > 0:
                        next_row.append(prev_row[i] + prev_row[i-1])

                if i > 0 and i == len(prev_row) - 1:
                    next_row.append(prev_row[i] + prev_row[i-1])
                    next_row.append(1)

            prev_row = next_row
            matrix.append(next_row)
    return matrix
