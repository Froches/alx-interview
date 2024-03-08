#!/usr/bin/python3
"""
Implementing the pascals triangle
"""


def pascal_triangle(n):
    """
    The pascals triangle, which is a maths concept is a code that
    return a list of intergents
    """

    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        triangle.append([])
        triangle[i].append(1)
        if (i > 0):
            for j in range(1, i):
                triangle[i].append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            triangle[i].append(1)

    return triangle
