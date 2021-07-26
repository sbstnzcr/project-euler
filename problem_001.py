# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

from typing import List


def find_multiples_of_3_or_5(n: int) -> List[int]:
    """Find all the multiples of 3 or 5 below `n`."""
    return [i for i in range(1, n) if not i % 3 or not i % 5]


if __name__ == '__main__':
    result = sum(find_multiples_of_3_or_5(1000))
    print(result)
