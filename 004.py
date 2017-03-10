"""
Project Euler Problem 4.

=======================

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
# !/bin/python


def generate_palindromes():
    """Generate all palindromes to nab memory timeout."""
    palindromes = []
    for j in xrange(100, 999):
        for k in xrange(j, 999):
            prod = j*k
            if str(prod) == str(prod)[::-1]:
                palindromes.append(prod)
    return palindromes


palindromes = generate_palindromes()

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    list_palindromes = []
    for palindrome in palindromes:
        if palindrome < n and palindrome >= 101101:
            list_palindromes.append(palindrome)

    print max(list_palindromes)
