# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(str: str) -> bool:
    """Check if a given string is palindrome."""
    for i in range(len(str) // 2):
        if str[i] != str[-i - 1]:
            break
    else:
        return True
    return False


if __name__ == '__main__':
    palindromes = [i * j for i in range(999, 100, -1) for j in range(999, 100, -1) if is_palindrome(str(i * j))]
    result = max(palindromes)
    print(result)
