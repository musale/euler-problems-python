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
import sys, math

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    summed = reduce((lambda x, y: x + y), range(1, n+1))
    squaredSum = reduce((lambda x, y: x + y), map(lambda x: x**2, range(1, n+1)))
    print int(math.pow(summed, 2) - squaredSum)
