#!/usr/bin/python3
"""
A makeChange function module
"""


def makeChange(coins, total):
    """
    Determine the minimum number of coins needed to
    meet a given total.
    """
    if total <= 0:
        return 0

    # Initialize the DP table with a high value (infinity-like)
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make a total of 0

    # Fill the DP table
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If the value at dp[total] is still inf, total cannot be achieved
    return dp[total] if dp[total] != float('inf') else -1
