#!/usr/bin/python3
"""
    decimal to binary using a recution
"""
def decimal_to_binary(n: int) -> str:
    """
        a function to change the decimal to binary
    """
    if n == 0 or n == 1:
        return str(n)
    return decimal_to_binary(n // 2) + str(n % 2)
