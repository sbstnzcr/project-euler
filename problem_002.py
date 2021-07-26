# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

def fibonacci(n: int) -> int:
    """Find the nth fibonacci number."""
    sequence = [1, 2]
    for i in range(2, n+1):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence[n]


if __name__ == '__main__':
    even_terms = []
    i = 0
    while True:
        element = fibonacci(i)
        i += 1
        if element > 4_000_000:
            break
        elif not element % 2:
            even_terms.append(element)
    result = sum(even_terms)
    print(result)
