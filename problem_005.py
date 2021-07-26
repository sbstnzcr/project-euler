# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import math
from typing import List

def get_primes(n: int) -> List[int]:
    """Get all prime numbers up to integer `n`."""
    primes = []
    for i in range(2, n + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes

if __name__ == '__main__':
    n = 20
    mult_primes = []
    for prime in get_primes(n):
        res = prime
        while res * prime < n:
            res *= prime
        mult_primes.append(res)
    result = math.prod(mult_primes)
    print(result)
