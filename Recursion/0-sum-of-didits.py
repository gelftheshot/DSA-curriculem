#!/usr/bin/python3


def sum_of_digit(num: int) -> int:
    """
        a function to find out sum of all
        digits but using recurtion
    """
    if num // 10 == 0:
        return num
    return ((num % 10) + sum_of_digit(num//10))
print(sum_of_digit(2331))
