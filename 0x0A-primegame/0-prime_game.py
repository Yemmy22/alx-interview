#!/usr/bin/python3
"""
Prime Game Module
"""


def sieve_of_eratosthenes(n):
    """
    Generate a list of prime numbers up to n
    using the Sieve of Eratosthenes.
    """
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return is_prime


def count_primes_upto(n, primes):
    """
    Count the number of prime numbers up to
    n using a precomputed prime list.
    """
    return sum(primes[:n + 1])


def isWinner(x, nums):
    """
    Determines the winner of the Prime Game.
    """
    if not nums or x < 1:
        return None

    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = count_primes_upto(n, primes)
        if prime_count % 2 == 0:  # Ben wins if the count is even
            ben_wins += 1
        else:  # Maria wins if the count is odd
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
