#!/usr/bin/python3
""" Script that computes a minimum operations
needed in a CopyAll - Paste task
"""


def minOperations(n):
    """
    Method for compute the minimum number
    of operations for task Copy All and Paste
    Args:
        n: input value
        factors: List to save the operations
    Return: the sum of the operations
    """
    if n < 2:
        return 0
    factors = []
    num = 1
    while n != 1:
        num += 1
        if n % num == 0:
            while n % num == 0:
                n /= num
                factors.append(num)
    return sum(factors)
