#!/bin/python
"""
Project Euler Problem 1.

=======================

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

n = int(raw_input().strip())
a = (n - 1) % 3
a = n - 1 - a
a = a / 3
b = (n - 1) % 5
b = n - 1 - b
b = b / 5
d = (n - 1) % 15
d = n - 1 - d
d = d / 15
c = 3 * a * (a + 1) / 2 + 5 * b * (b + 1) / 2 - 15 * d * (d + 1) / 2

print c
