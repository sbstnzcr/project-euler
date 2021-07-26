# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def get_largest_prime_factor(n: int) -> int:
    """Get largest prime factor of integer `n`."""
    for i in range(2, n + 1):
        while n % i == 0:
            n //= i
        if n == 1:
            return i
    return 0


if __name__ == '__main__':
    result = get_largest_prime_factor(600851475143)
    print(result)
