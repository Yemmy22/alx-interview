#!/usr/bin/python3
"""
A minOperations function module.
"""


def minOperations(n):
    """
    Returns the fewest number of operations needed
    to result in exactly n H characters
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        # While n is divisible by the current factor
        while n % factor == 0:
            operations += factor  # Add the factor to the count
            n //= factor  # Divide n by the factor
        factor += 1  # Move to the next factor

    return operations
