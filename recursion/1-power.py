#!/usr/bin/python3
""" a function used to calculate the power of
    number using recurtion
"""


def power(x: int, y: int) -> float:
    """
        finding x**5 using rectution
    """
    if y == 1:
        return x
    return x * power(x, y-1)
