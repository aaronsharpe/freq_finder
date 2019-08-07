"""
Functions for finding prime numbers
"""

import numpy as np


def seive(limit, low_limit=0):
    """
    Returns list of all primes within the search window

    Arguments:
        limit: upper limit of search range
        low_limit: lower limit of search range
    """
    isprime = [True] * limit

    for i in range(2, int(limit**0.5 + 1)):
        if isprime[i]:
            for j in range(i*i, limit, i):
                isprime[j] = False

    primes = []
    for i in range(2, limit):
        if isprime[i] and i >= low_limit:
            primes.append(i)

    return primes


def seive_60(limit, low_limit=0):
    """
    Returns list of tuples of all prime numbers within
    search window and their distance from the nearest
    multiple of 60

    Arguments:
        limit: upper limit of search range
        low_limit: lower limit of search range
    """
    isprime = [True] * limit

    for i in range(2, int(limit**0.5 + 1)):
        if isprime[i]:
            for j in range(i*i, limit, i):
                isprime[j] = False

    primes = []
    for i in range(2, limit):
        if isprime[i] and i >= low_limit:
            diff = np.min((60 - i % 60, i % 60))
            primes.append((i, diff))

    return primes
