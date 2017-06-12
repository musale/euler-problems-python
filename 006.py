"""
Project Euler Problem 6
=======================

The sum of the squares of the first ten natural numbers is,
                       1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
                    (1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.
"""
# Reference: https://brilliant.org/wiki/sum-of-n-n2-or-n3/
import sys

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    summed = (n * (n+1))/2
    squared = (n* (n+1) *((2*n) + 1))/6
    print (summed**2) - squaredSum)
